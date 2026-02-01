# WSL Proxy

Lightweight WSLg GUI to quickly configure system proxy for WSL, solving the lack of transparent proxy on Windows 10/11 WSL.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- One-click proxy configuration for WSL
- Supports shell environment, apt, and Firefox
- Built-in connectivity test
- Clean PyQt5 interface

## Installation

```bash
# Install dependencies
sudo apt install python3-pyqt5

# Clone
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy

# Run (with sudo for system-wide changes)
sudo ./run.sh
```

## What it configures

| File | Purpose |
|------|---------|
| `/etc/profile.d/wsl-proxy.sh` | Shell environment variables |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT proxy |
| `/etc/environment` | System-wide environment |
| `~/.mozilla/firefox/*/user.js` | Firefox proxy (optional) |

## Defaults

- Host: `172.23.0.1` (WSL gateway)
- Port: `7897` (Clash default)
- No Proxy: `localhost,127.0.0.1,::1`

## Why?

WSL on Windows 10/11 lacks transparent proxy support. You can't simply use `127.0.0.1` to reach Windows host proxy. This tool automates the tedious process of configuring multiple files to route traffic through your Windows proxy (e.g., Clash).

## License

MIT
