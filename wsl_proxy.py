#!/usr/bin/env python3
import os
import re
import shutil
import subprocess
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets

CONFIG_PATH = "/etc/profile.d/wsl-proxy.sh"
APT_PATH = "/etc/apt/apt.conf.d/95wsl-proxy"
ENV_PATH = "/etc/environment"
DEFAULT_HOST = "172.23.0.1"
DEFAULT_PORT = "7897"
DEFAULT_NO_PROXY = "localhost,127.0.0.1,::1"


def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def _parse_proxy_text(text):
    if not text:
        return None
    m = re.search(r"http_proxy=([^\n]+)", text)
    proxy = m.group(1).strip() if m else ""
    host = ""
    port = ""
    if proxy.startswith("http://"):
        proxy = proxy[len("http://"):]
    if ":" in proxy:
        host, port = proxy.split(":", 1)
    no_proxy = ""
    m2 = re.search(r"no_proxy=([^\n]+)", text)
    if m2:
        no_proxy = m2.group(1).strip()
    return {
        "host": host,
        "port": port,
        "no_proxy": no_proxy,
    }


def parse_proxy_file():
    text = _read_text(CONFIG_PATH)
    parsed = _parse_proxy_text(text)
    if parsed:
        return parsed
    env_text = _read_text(ENV_PATH)
    return _parse_proxy_text(env_text)


def _update_environment(proxy, no_proxy):
    lines = _read_text(ENV_PATH).splitlines()
    keys = {
        "http_proxy",
        "https_proxy",
        "all_proxy",
        "no_proxy",
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "NO_PROXY",
    }
    filtered = [line for line in lines if not line.split("=", 1)[0] in keys]
    filtered.extend(
        [
            f"http_proxy={proxy}",
            f"https_proxy={proxy}",
            f"all_proxy={proxy}",
            f"no_proxy={no_proxy}",
            f"HTTP_PROXY={proxy}",
            f"HTTPS_PROXY={proxy}",
            f"ALL_PROXY={proxy}",
            f"NO_PROXY={no_proxy}",
        ]
    )
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join([line for line in filtered if line.strip()]) + "\n")


def _remove_environment_proxy():
    lines = _read_text(ENV_PATH).splitlines()
    keys = {
        "http_proxy",
        "https_proxy",
        "all_proxy",
        "no_proxy",
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "NO_PROXY",
    }
    filtered = [line for line in lines if not line.split("=", 1)[0] in keys]
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join([line for line in filtered if line.strip()]) + "\n")


def _firefox_profiles():
    base = os.path.expanduser("~/.mozilla/firefox")
    if not os.path.isdir(base):
        return []
    profiles = []
    for entry in os.listdir(base):
        if entry.endswith(".default") or ".default-" in entry:
            profiles.append(os.path.join(base, entry))
    return profiles


def _write_firefox_user_js(host, port, no_proxy):
    prefs = [
        'user_pref("network.proxy.type", 1);',
        f'user_pref("network.proxy.http", "{host}");',
        f'user_pref("network.proxy.http_port", {int(port)});',
        f'user_pref("network.proxy.ssl", "{host}");',
        f'user_pref("network.proxy.ssl_port", {int(port)});',
        f'user_pref("network.proxy.no_proxies_on", "{no_proxy}");',
        'user_pref("network.proxy.share_proxy_settings", true);',
        'user_pref("network.trr.mode", 5);',
    ]
    for profile in _firefox_profiles():
        user_js = os.path.join(profile, "user.js")
        with open(user_js, "w", encoding="utf-8") as f:
            f.write("\n".join(prefs) + "\n")


def _remove_firefox_user_js():
    for profile in _firefox_profiles():
        user_js = os.path.join(profile, "user.js")
        try:
            os.remove(user_js)
        except FileNotFoundError:
            pass


def write_proxy(host, port, no_proxy):
    proxy = f"http://{host}:{port}"
    lines = [
        "# WSL Proxy managed file",
        f"export http_proxy={proxy}",
        f"export https_proxy={proxy}",
        f"export all_proxy={proxy}",
        f"export no_proxy={no_proxy}",
        f"export HTTP_PROXY={proxy}",
        f"export HTTPS_PROXY={proxy}",
        f"export ALL_PROXY={proxy}",
        f"export NO_PROXY={no_proxy}",
        "",
    ]
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    apt_lines = [
        f'Acquire::http::Proxy "{proxy}";',
        f'Acquire::https::Proxy "{proxy}";',
        "",
    ]
    with open(APT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(apt_lines))
    _update_environment(proxy, no_proxy)


def disable_proxy():
    for path in (CONFIG_PATH, APT_PATH):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
    _remove_environment_proxy()
    _remove_firefox_user_js()


def is_root():
    return os.geteuid() == 0


class TestWorker(QtCore.QThread):
    finished = QtCore.pyqtSignal(bool, str)

    def __init__(self, host, port, parent=None):
        super().__init__(parent)
        self.host = host
        self.port = port

    def run(self):
        if not shutil.which("curl"):
            self.finished.emit(False, "curl not found")
            return
        proxy = f"http://{self.host}:{self.port}"
        cmd = [
            "curl",
            "-I",
            "-m",
            "5",
            "-x",
            proxy,
            "https://www.google.com",
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            ok = result.returncode == 0
            status = "OK" if ok else "FAIL"
            self.finished.emit(ok, f"{status} (curl exit {result.returncode})")
        except Exception as e:
            self.finished.emit(False, f"ERROR: {e}")


class ProxyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WSL Proxy")
        self.setMinimumSize(520, 420)

        self.setStyleSheet(self._style_sheet())

        font = QtGui.QFont("Fira Sans")
        if not font.exactMatch():
            font = QtGui.QFont("Noto Sans")
        self.setFont(font)

        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QVBoxLayout(central)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(14)

        header = QtWidgets.QLabel("WSL Proxy")
        header.setObjectName("Title")
        subtitle = QtWidgets.QLabel(
            "Quickly set system proxy for WSL and connect to Clash LAN"
        )
        subtitle.setObjectName("Subtitle")

        layout.addWidget(header)
        layout.addWidget(subtitle)

        self.banner = QtWidgets.QLabel()
        self.banner.setObjectName("Banner")
        layout.addWidget(self.banner)

        card = QtWidgets.QFrame()
        card.setObjectName("Card")
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(16, 16, 16, 16)
        card_layout.setSpacing(12)

        form = QtWidgets.QFormLayout()
        form.setLabelAlignment(QtCore.Qt.AlignLeft)
        form.setFormAlignment(QtCore.Qt.AlignLeft)

        self.host_edit = QtWidgets.QLineEdit(DEFAULT_HOST)
        self.host_edit.setPlaceholderText("Proxy host")
        self.port_edit = QtWidgets.QLineEdit(DEFAULT_PORT)
        self.port_edit.setValidator(QtGui.QIntValidator(1, 65535))
        self.port_edit.setPlaceholderText("Port")
        self.no_proxy_edit = QtWidgets.QLineEdit(DEFAULT_NO_PROXY)
        self.no_proxy_edit.setPlaceholderText("Bypass list (comma separated)")
        self.firefox_check = QtWidgets.QCheckBox("Apply to Firefox")
        self.firefox_check.setChecked(True)

        form.addRow("Host", self.host_edit)
        form.addRow("Port", self.port_edit)
        form.addRow("No Proxy", self.no_proxy_edit)
        form.addRow("", self.firefox_check)
        card_layout.addLayout(form)

        button_row = QtWidgets.QHBoxLayout()
        self.apply_btn = QtWidgets.QPushButton("Apply")
        self.disable_btn = QtWidgets.QPushButton("Disable")
        self.test_btn = QtWidgets.QPushButton("Test")
        self.clash_btn = QtWidgets.QPushButton("Use Clash LAN")
        self.clash_btn.setObjectName("GhostButton")

        button_row.addWidget(self.apply_btn)
        button_row.addWidget(self.disable_btn)
        button_row.addStretch(1)
        button_row.addWidget(self.test_btn)
        button_row.addWidget(self.clash_btn)

        card_layout.addLayout(button_row)
        layout.addWidget(card)

        self.status = QtWidgets.QLabel()
        self.status.setObjectName("Status")
        layout.addWidget(self.status)

        footer = QtWidgets.QLabel(
            "Note: Run as root (sudo) to apply system-wide changes."
        )
        footer.setObjectName("Footer")
        layout.addWidget(footer)

        self.apply_btn.clicked.connect(self.on_apply)
        self.disable_btn.clicked.connect(self.on_disable)
        self.test_btn.clicked.connect(self.on_test)
        self.clash_btn.clicked.connect(self.on_clash)

        self.test_worker = None
        self.refresh_state()

    def _style_sheet(self):
        return """
        QWidget {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f6f1ea, stop:1 #e7f3f0);
            color: #172554;
        }
        #Title {
            font-size: 28px;
            font-weight: 700;
            letter-spacing: 0.5px;
        }
        #Subtitle {
            font-size: 13px;
            color: #475569;
        }
        #Card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 14px;
        }
        QLineEdit {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 8px 10px;
        }
        QLineEdit:focus {
            border: 1px solid #0f766e;
            background: #ffffff;
        }
        QPushButton {
            background: #0f766e;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 8px 14px;
            font-weight: 600;
        }
        QPushButton:hover {
            background: #0c5f59;
        }
        QPushButton:disabled {
            background: #94a3b8;
        }
        #GhostButton {
            background: transparent;
            color: #0f766e;
            border: 1px solid #0f766e;
        }
        #GhostButton:hover {
            background: #e6fffb;
        }
        #Status {
            font-size: 12px;
            color: #0f172a;
        }
        #Footer {
            font-size: 11px;
            color: #64748b;
        }
        #Banner {
            font-size: 12px;
            color: #7c2d12;
            background: #fff7ed;
            border: 1px solid #fed7aa;
            border-radius: 10px;
            padding: 6px 8px;
        }
        """

    def refresh_state(self):
        info = parse_proxy_file()
        if info and info.get("host") and info.get("port"):
            self.status.setText(
                f"Active: {info['host']}:{info['port']}  |  Updated: {datetime.now().strftime('%H:%M:%S')}"
            )
            self.host_edit.setText(info["host"])
            self.port_edit.setText(info["port"])
            if info.get("no_proxy"):
                self.no_proxy_edit.setText(info["no_proxy"])
        else:
            self.status.setText("Inactive: no system proxy configured")

        if is_root():
            self.banner.hide()
            self.apply_btn.setEnabled(True)
            self.disable_btn.setEnabled(True)
        else:
            self.banner.setText("Run this app with sudo to apply changes.")
            self.banner.show()
            self.apply_btn.setEnabled(False)
            self.disable_btn.setEnabled(False)

    def on_apply(self):
        host = self.host_edit.text().strip()
        port = self.port_edit.text().strip()
        no_proxy = self.no_proxy_edit.text().strip() or DEFAULT_NO_PROXY
        if not host or not port:
            self.status.setText("Host and port are required")
            return
        try:
            write_proxy(host, port, no_proxy)
            if self.firefox_check.isChecked():
                _write_firefox_user_js(host, port, no_proxy)
            self.status.setText(f"Applied: {host}:{port}")
        except Exception as e:
            self.status.setText(f"Apply failed: {e}")
        self.refresh_state()

    def on_disable(self):
        try:
            disable_proxy()
            self.status.setText("Proxy disabled")
        except Exception as e:
            self.status.setText(f"Disable failed: {e}")
        self.refresh_state()

    def on_test(self):
        host = self.host_edit.text().strip()
        port = self.port_edit.text().strip()
        if not host or not port:
            self.status.setText("Host and port are required")
            return
        self.status.setText("Testing...")
        self.test_btn.setEnabled(False)
        self.test_worker = TestWorker(host, port)
        self.test_worker.finished.connect(self.on_test_done)
        self.test_worker.start()

    def on_test_done(self, ok, message):
        self.status.setText(f"Test: {message}")
        self.test_btn.setEnabled(True)

    def on_clash(self):
        self.host_edit.setText(DEFAULT_HOST)
        self.port_edit.setText(DEFAULT_PORT)
        if is_root():
            self.on_apply()


def main():
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    app = QtWidgets.QApplication([])
    app.setApplicationName("WSL Proxy")
    window = ProxyWindow()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
