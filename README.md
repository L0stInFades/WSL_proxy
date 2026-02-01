# WSL Proxy

Lightweight WSLg GUI to quickly configure system proxy for WSL, solving the lack of transparent proxy on Windows 10/11 WSL.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

[English](#english) | [中文](#中文) | [日本語](#日本語) | [한국어](#한국어) | [Español](#español) | [Français](#français) | [Deutsch](#deutsch) | [Русский](#русский)

---

## English

### The Problem

WSL (Windows Subsystem for Linux) on Windows 10/11 runs in a NAT network mode. This creates a frustrating proxy problem:

1. **127.0.0.1 doesn't work** - Your Windows proxy (Clash, v2ray, etc.) listens on `127.0.0.1`, but WSL can't reach it because WSL has its own network namespace
2. **No transparent proxy** - Unlike a real Linux system, WSL doesn't support system-wide transparent proxy
3. **Multiple config files** - To make proxy work everywhere (shell, apt, curl, wget, git...), you need to edit multiple configuration files manually
4. **Gateway IP changes** - The WSL gateway IP may change after Windows restart

### The Solution

WSL Proxy solves this by:

1. **Auto-detecting WSL gateway** - Uses the correct IP to reach Windows host (default: `172.23.0.1`)
2. **One-click configuration** - Sets proxy in all necessary places at once
3. **GUI interface** - No need to remember config file paths or syntax

### How It Works

When you click "Apply", the tool writes proxy settings to:

| File | What it does |
|------|--------------|
| `/etc/profile.d/wsl-proxy.sh` | Sets `http_proxy`, `https_proxy`, `all_proxy` environment variables for all shell sessions |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Configures APT package manager to use proxy |
| `/etc/environment` | System-wide environment variables (affects GUI apps too) |
| `~/.mozilla/firefox/*/user.js` | Firefox browser proxy settings (optional) |

### Installation

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Defaults
- Host: `172.23.0.1` (WSL gateway to Windows)
- Port: `7897` (Clash Verge default LAN port)
- No Proxy: `localhost,127.0.0.1,::1`

### Requirements
- Windows 10/11 with WSL2
- A proxy client on Windows (Clash, Clash Verge, v2rayN, etc.) with LAN access enabled
- Python 3.8+ and PyQt5

---

## 中文

### 问题背景

Windows 10/11 上的 WSL（Windows Subsystem for Linux）运行在 NAT 网络模式下，这导致了一个令人头疼的代理问题：

1. **127.0.0.1 不可用** - Windows 上的代理软件（Clash、v2ray 等）监听在 `127.0.0.1`，但 WSL 无法访问，因为 WSL 有自己独立的网络命名空间
2. **没有透明代理** - 与真正的 Linux 系统不同，WSL 不支持系统级透明代理
3. **配置文件繁多** - 要让代理在所有地方生效（shell、apt、curl、wget、git...），需要手动编辑多个配置文件
4. **网关 IP 会变** - WSL 的网关 IP 在 Windows 重启后可能会改变

### 解决方案

WSL Proxy 通过以下方式解决这些问题：

1. **自动识别 WSL 网关** - 使用正确的 IP 访问 Windows 主机（默认：`172.23.0.1`）
2. **一键配置** - 同时在所有必要的位置设置代理
3. **图形界面** - 无需记忆配置文件路径和语法

### 工作原理

点击"Apply"后，工具会将代理设置写入：

| 文件 | 作用 |
|------|------|
| `/etc/profile.d/wsl-proxy.sh` | 为所有 shell 会话设置 `http_proxy`、`https_proxy`、`all_proxy` 环境变量 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | 配置 APT 包管理器使用代理 |
| `/etc/environment` | 系统级环境变量（GUI 应用也会生效）|
| `~/.mozilla/firefox/*/user.js` | Firefox 浏览器代理设置（可选）|

### 安装

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### 默认值
- 主机：`172.23.0.1`（WSL 到 Windows 的网关）
- 端口：`7897`（Clash Verge 默认局域网端口）
- 不代理：`localhost,127.0.0.1,::1`

### 环境要求
- Windows 10/11 + WSL2
- Windows 上运行代理客户端（Clash、Clash Verge、v2rayN 等），并开启局域网访问
- Python 3.8+ 和 PyQt5

---

## 日本語

### 問題の背景

Windows 10/11 の WSL（Windows Subsystem for Linux）は NAT ネットワークモードで動作します。これにより厄介なプロキシ問題が発生します：

1. **127.0.0.1 が使えない** - Windows のプロキシソフト（Clash、v2ray など）は `127.0.0.1` でリッスンしていますが、WSL は独自のネットワーク名前空間を持つためアクセスできません
2. **透過プロキシがない** - 本物の Linux システムと異なり、WSL はシステム全体の透過プロキシをサポートしていません
3. **設定ファイルが多い** - プロキシをすべての場所（shell、apt、curl、wget、git...）で機能させるには、複数の設定ファイルを手動で編集する必要があります
4. **ゲートウェイ IP が変わる** - WSL のゲートウェイ IP は Windows 再起動後に変わる可能性があります

### 解決策

WSL Proxy は以下の方法でこれらの問題を解決します：

1. **WSL ゲートウェイの自動検出** - Windows ホストにアクセスするための正しい IP を使用（デフォルト：`172.23.0.1`）
2. **ワンクリック設定** - 必要なすべての場所に一度にプロキシを設定
3. **GUI インターフェース** - 設定ファイルのパスや構文を覚える必要なし

### 動作原理

「Apply」をクリックすると、ツールは以下にプロキシ設定を書き込みます：

| ファイル | 機能 |
|----------|------|
| `/etc/profile.d/wsl-proxy.sh` | すべての shell セッションに `http_proxy`、`https_proxy`、`all_proxy` 環境変数を設定 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT パッケージマネージャーにプロキシを設定 |
| `/etc/environment` | システム全体の環境変数（GUI アプリにも適用）|
| `~/.mozilla/firefox/*/user.js` | Firefox ブラウザのプロキシ設定（オプション）|

### インストール

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### デフォルト値
- ホスト：`172.23.0.1`（WSL から Windows へのゲートウェイ）
- ポート：`7897`（Clash Verge デフォルト LAN ポート）
- プロキシ除外：`localhost,127.0.0.1,::1`

### 必要環境
- Windows 10/11 + WSL2
- Windows でプロキシクライアント（Clash、Clash Verge、v2rayN など）を実行し、LAN アクセスを有効化
- Python 3.8+ と PyQt5

---

## 한국어

### 문제 배경

Windows 10/11의 WSL(Windows Subsystem for Linux)은 NAT 네트워크 모드로 실행됩니다. 이로 인해 골치 아픈 프록시 문제가 발생합니다:

1. **127.0.0.1 사용 불가** - Windows의 프록시 소프트웨어(Clash, v2ray 등)는 `127.0.0.1`에서 수신하지만, WSL은 자체 네트워크 네임스페이스를 가지므로 접근할 수 없습니다
2. **투명 프록시 없음** - 실제 Linux 시스템과 달리 WSL은 시스템 전체 투명 프록시를 지원하지 않습니다
3. **여러 설정 파일** - 프록시를 모든 곳(shell, apt, curl, wget, git...)에서 작동시키려면 여러 설정 파일을 수동으로 편집해야 합니다
4. **게이트웨이 IP 변경** - WSL 게이트웨이 IP는 Windows 재시작 후 변경될 수 있습니다

### 해결책

WSL Proxy는 다음과 같은 방법으로 이러한 문제를 해결합니다:

1. **WSL 게이트웨이 자동 감지** - Windows 호스트에 접근하기 위한 올바른 IP 사용 (기본값: `172.23.0.1`)
2. **원클릭 설정** - 필요한 모든 위치에 한 번에 프록시 설정
3. **GUI 인터페이스** - 설정 파일 경로나 구문을 기억할 필요 없음

### 작동 원리

"Apply"를 클릭하면 도구가 다음 위치에 프록시 설정을 작성합니다:

| 파일 | 기능 |
|------|------|
| `/etc/profile.d/wsl-proxy.sh` | 모든 shell 세션에 `http_proxy`, `https_proxy`, `all_proxy` 환경 변수 설정 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT 패키지 관리자에 프록시 설정 |
| `/etc/environment` | 시스템 전체 환경 변수 (GUI 앱에도 적용) |
| `~/.mozilla/firefox/*/user.js` | Firefox 브라우저 프록시 설정 (선택 사항) |

### 설치

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### 기본값
- 호스트: `172.23.0.1` (WSL에서 Windows로의 게이트웨이)
- 포트: `7897` (Clash Verge 기본 LAN 포트)
- 프록시 제외: `localhost,127.0.0.1,::1`

### 요구 사항
- Windows 10/11 + WSL2
- Windows에서 프록시 클라이언트(Clash, Clash Verge, v2rayN 등) 실행 및 LAN 접근 활성화
- Python 3.8+ 및 PyQt5

---

## Español

### El Problema

WSL (Windows Subsystem for Linux) en Windows 10/11 se ejecuta en modo de red NAT. Esto crea un problema frustrante con el proxy:

1. **127.0.0.1 no funciona** - Tu proxy de Windows (Clash, v2ray, etc.) escucha en `127.0.0.1`, pero WSL no puede alcanzarlo porque tiene su propio espacio de nombres de red
2. **Sin proxy transparente** - A diferencia de un sistema Linux real, WSL no soporta proxy transparente a nivel de sistema
3. **Múltiples archivos de configuración** - Para que el proxy funcione en todas partes (shell, apt, curl, wget, git...), necesitas editar múltiples archivos de configuración manualmente
4. **La IP del gateway cambia** - La IP del gateway de WSL puede cambiar después de reiniciar Windows

### La Solución

WSL Proxy resuelve esto mediante:

1. **Auto-detección del gateway WSL** - Usa la IP correcta para alcanzar el host Windows (por defecto: `172.23.0.1`)
2. **Configuración con un clic** - Establece el proxy en todos los lugares necesarios a la vez
3. **Interfaz GUI** - No necesitas recordar rutas de archivos de configuración ni sintaxis

### Cómo Funciona

Cuando haces clic en "Apply", la herramienta escribe la configuración del proxy en:

| Archivo | Función |
|---------|---------|
| `/etc/profile.d/wsl-proxy.sh` | Establece variables de entorno `http_proxy`, `https_proxy`, `all_proxy` para todas las sesiones shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Configura el gestor de paquetes APT para usar proxy |
| `/etc/environment` | Variables de entorno a nivel de sistema (también afecta apps GUI) |
| `~/.mozilla/firefox/*/user.js` | Configuración de proxy de Firefox (opcional) |

### Instalación

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Valores Predeterminados
- Host: `172.23.0.1` (gateway de WSL a Windows)
- Puerto: `7897` (puerto LAN predeterminado de Clash Verge)
- Sin Proxy: `localhost,127.0.0.1,::1`

### Requisitos
- Windows 10/11 con WSL2
- Un cliente proxy en Windows (Clash, Clash Verge, v2rayN, etc.) con acceso LAN habilitado
- Python 3.8+ y PyQt5

---

## Français

### Le Problème

WSL (Windows Subsystem for Linux) sur Windows 10/11 fonctionne en mode réseau NAT. Cela crée un problème de proxy frustrant :

1. **127.0.0.1 ne fonctionne pas** - Votre proxy Windows (Clash, v2ray, etc.) écoute sur `127.0.0.1`, mais WSL ne peut pas l'atteindre car il a son propre espace de noms réseau
2. **Pas de proxy transparent** - Contrairement à un vrai système Linux, WSL ne supporte pas le proxy transparent au niveau système
3. **Multiples fichiers de configuration** - Pour que le proxy fonctionne partout (shell, apt, curl, wget, git...), vous devez éditer manuellement plusieurs fichiers de configuration
4. **L'IP de la passerelle change** - L'IP de la passerelle WSL peut changer après un redémarrage de Windows

### La Solution

WSL Proxy résout cela en :

1. **Auto-détection de la passerelle WSL** - Utilise la bonne IP pour atteindre l'hôte Windows (par défaut : `172.23.0.1`)
2. **Configuration en un clic** - Configure le proxy dans tous les endroits nécessaires en une fois
3. **Interface GUI** - Pas besoin de mémoriser les chemins des fichiers de configuration ou la syntaxe

### Comment Ça Marche

Quand vous cliquez sur "Apply", l'outil écrit les paramètres proxy dans :

| Fichier | Fonction |
|---------|----------|
| `/etc/profile.d/wsl-proxy.sh` | Définit les variables d'environnement `http_proxy`, `https_proxy`, `all_proxy` pour toutes les sessions shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Configure le gestionnaire de paquets APT pour utiliser le proxy |
| `/etc/environment` | Variables d'environnement système (affecte aussi les apps GUI) |
| `~/.mozilla/firefox/*/user.js` | Paramètres proxy de Firefox (optionnel) |

### Installation

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Valeurs Par Défaut
- Hôte : `172.23.0.1` (passerelle WSL vers Windows)
- Port : `7897` (port LAN par défaut de Clash Verge)
- Sans Proxy : `localhost,127.0.0.1,::1`

### Prérequis
- Windows 10/11 avec WSL2
- Un client proxy sur Windows (Clash, Clash Verge, v2rayN, etc.) avec accès LAN activé
- Python 3.8+ et PyQt5

---

## Deutsch

### Das Problem

WSL (Windows Subsystem for Linux) auf Windows 10/11 läuft im NAT-Netzwerkmodus. Dies verursacht ein frustrierendes Proxy-Problem:

1. **127.0.0.1 funktioniert nicht** - Ihr Windows-Proxy (Clash, v2ray, etc.) lauscht auf `127.0.0.1`, aber WSL kann ihn nicht erreichen, da WSL seinen eigenen Netzwerk-Namespace hat
2. **Kein transparenter Proxy** - Anders als ein echtes Linux-System unterstützt WSL keinen systemweiten transparenten Proxy
3. **Mehrere Konfigurationsdateien** - Damit der Proxy überall funktioniert (Shell, apt, curl, wget, git...), müssen Sie mehrere Konfigurationsdateien manuell bearbeiten
4. **Gateway-IP ändert sich** - Die WSL-Gateway-IP kann sich nach einem Windows-Neustart ändern

### Die Lösung

WSL Proxy löst dies durch:

1. **Auto-Erkennung des WSL-Gateways** - Verwendet die richtige IP, um den Windows-Host zu erreichen (Standard: `172.23.0.1`)
2. **Ein-Klick-Konfiguration** - Setzt den Proxy an allen notwendigen Stellen gleichzeitig
3. **GUI-Oberfläche** - Keine Notwendigkeit, Konfigurationsdateipfade oder Syntax zu merken

### Wie Es Funktioniert

Wenn Sie auf "Apply" klicken, schreibt das Tool die Proxy-Einstellungen in:

| Datei | Funktion |
|-------|----------|
| `/etc/profile.d/wsl-proxy.sh` | Setzt `http_proxy`, `https_proxy`, `all_proxy` Umgebungsvariablen für alle Shell-Sitzungen |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Konfiguriert den APT-Paketmanager zur Proxy-Nutzung |
| `/etc/environment` | Systemweite Umgebungsvariablen (betrifft auch GUI-Apps) |
| `~/.mozilla/firefox/*/user.js` | Firefox-Browser-Proxy-Einstellungen (optional) |

### Installation

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Standardwerte
- Host: `172.23.0.1` (WSL-Gateway zu Windows)
- Port: `7897` (Clash Verge Standard-LAN-Port)
- Kein Proxy: `localhost,127.0.0.1,::1`

### Voraussetzungen
- Windows 10/11 mit WSL2
- Ein Proxy-Client auf Windows (Clash, Clash Verge, v2rayN, etc.) mit aktiviertem LAN-Zugriff
- Python 3.8+ und PyQt5

---

## Русский

### Проблема

WSL (Windows Subsystem for Linux) на Windows 10/11 работает в сетевом режиме NAT. Это создаёт неприятную проблему с прокси:

1. **127.0.0.1 не работает** - Ваш Windows-прокси (Clash, v2ray и т.д.) слушает на `127.0.0.1`, но WSL не может к нему подключиться, так как имеет собственное сетевое пространство имён
2. **Нет прозрачного прокси** - В отличие от настоящей Linux-системы, WSL не поддерживает системный прозрачный прокси
3. **Множество конфигурационных файлов** - Чтобы прокси работал везде (shell, apt, curl, wget, git...), нужно вручную редактировать несколько конфигурационных файлов
4. **IP шлюза меняется** - IP шлюза WSL может измениться после перезагрузки Windows

### Решение

WSL Proxy решает эту проблему следующим образом:

1. **Автоопределение шлюза WSL** - Использует правильный IP для доступа к хосту Windows (по умолчанию: `172.23.0.1`)
2. **Настройка в один клик** - Устанавливает прокси во всех необходимых местах одновременно
3. **GUI интерфейс** - Не нужно запоминать пути к конфигурационным файлам или синтаксис

### Как Это Работает

При нажатии "Apply" инструмент записывает настройки прокси в:

| Файл | Функция |
|------|---------|
| `/etc/profile.d/wsl-proxy.sh` | Устанавливает переменные окружения `http_proxy`, `https_proxy`, `all_proxy` для всех сессий shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Настраивает менеджер пакетов APT на использование прокси |
| `/etc/environment` | Системные переменные окружения (влияет и на GUI-приложения) |
| `~/.mozilla/firefox/*/user.js` | Настройки прокси браузера Firefox (опционально) |

### Установка

```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Значения По Умолчанию
- Хост: `172.23.0.1` (шлюз WSL к Windows)
- Порт: `7897` (стандартный LAN-порт Clash Verge)
- Без прокси: `localhost,127.0.0.1,::1`

### Требования
- Windows 10/11 с WSL2
- Прокси-клиент на Windows (Clash, Clash Verge, v2rayN и т.д.) с включённым доступом по LAN
- Python 3.8+ и PyQt5

---

## License

MIT
