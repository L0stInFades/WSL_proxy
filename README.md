# WSL Proxy

Lightweight WSLg GUI to quickly configure system proxy for WSL, solving the lack of transparent proxy on Windows 10/11 WSL.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

[English](#english) | [中文](#中文) | [日本語](#日本語) | [한국어](#한국어) | [Español](#español) | [Français](#français) | [Deutsch](#deutsch) | [Русский](#русский)

---

## English

### Features
- One-click proxy configuration for WSL
- Supports shell environment, apt, and Firefox
- Built-in connectivity test
- Clean PyQt5 interface

### Installation
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Configuration Files
| File | Purpose |
|------|---------|
| `/etc/profile.d/wsl-proxy.sh` | Shell environment variables |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT proxy |
| `/etc/environment` | System-wide environment |
| `~/.mozilla/firefox/*/user.js` | Firefox proxy (optional) |

### Defaults
- Host: `172.23.0.1` (WSL gateway)
- Port: `7897` (Clash default)

---

## 中文

### 功能
- 一键配置 WSL 系统代理
- 支持 shell 环境、apt 和 Firefox
- 内置连通性测试
- 简洁的 PyQt5 界面

### 安装
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### 配置文件
| 文件 | 用途 |
|------|------|
| `/etc/profile.d/wsl-proxy.sh` | Shell 环境变量 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT 代理 |
| `/etc/environment` | 系统环境变量 |
| `~/.mozilla/firefox/*/user.js` | Firefox 代理（可选）|

### 默认值
- 主机：`172.23.0.1`（WSL 网关）
- 端口：`7897`（Clash 默认端口）

---

## 日本語

### 機能
- WSL システムプロキシのワンクリック設定
- shell 環境、apt、Firefox をサポート
- 接続テスト内蔵
- シンプルな PyQt5 インターフェース

### インストール
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### 設定ファイル
| ファイル | 用途 |
|----------|------|
| `/etc/profile.d/wsl-proxy.sh` | Shell 環境変数 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT プロキシ |
| `/etc/environment` | システム環境変数 |
| `~/.mozilla/firefox/*/user.js` | Firefox プロキシ（任意）|

### デフォルト値
- ホスト：`172.23.0.1`（WSL ゲートウェイ）
- ポート：`7897`（Clash デフォルト）

---

## 한국어

### 기능
- WSL 시스템 프록시 원클릭 설정
- shell 환경, apt, Firefox 지원
- 연결 테스트 내장
- 깔끔한 PyQt5 인터페이스

### 설치
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### 설정 파일
| 파일 | 용도 |
|------|------|
| `/etc/profile.d/wsl-proxy.sh` | Shell 환경 변수 |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT 프록시 |
| `/etc/environment` | 시스템 환경 변수 |
| `~/.mozilla/firefox/*/user.js` | Firefox 프록시 (선택) |

### 기본값
- 호스트: `172.23.0.1` (WSL 게이트웨이)
- 포트: `7897` (Clash 기본값)

---

## Español

### Características
- Configuración de proxy del sistema WSL con un clic
- Soporta entorno shell, apt y Firefox
- Prueba de conectividad integrada
- Interfaz PyQt5 limpia

### Instalación
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Archivos de configuración
| Archivo | Propósito |
|---------|-----------|
| `/etc/profile.d/wsl-proxy.sh` | Variables de entorno shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Proxy APT |
| `/etc/environment` | Entorno del sistema |
| `~/.mozilla/firefox/*/user.js` | Proxy Firefox (opcional) |

### Valores predeterminados
- Host: `172.23.0.1` (puerta de enlace WSL)
- Puerto: `7897` (predeterminado de Clash)

---

## Français

### Fonctionnalités
- Configuration du proxy système WSL en un clic
- Prend en charge l'environnement shell, apt et Firefox
- Test de connectivité intégré
- Interface PyQt5 épurée

### Installation
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Fichiers de configuration
| Fichier | Objectif |
|---------|----------|
| `/etc/profile.d/wsl-proxy.sh` | Variables d'environnement shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Proxy APT |
| `/etc/environment` | Environnement système |
| `~/.mozilla/firefox/*/user.js` | Proxy Firefox (optionnel) |

### Valeurs par défaut
- Hôte : `172.23.0.1` (passerelle WSL)
- Port : `7897` (par défaut Clash)

---

## Deutsch

### Funktionen
- Ein-Klick-Konfiguration des WSL-Systemproxys
- Unterstützt Shell-Umgebung, apt und Firefox
- Integrierter Konnektivitätstest
- Saubere PyQt5-Oberfläche

### Installation
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Konfigurationsdateien
| Datei | Zweck |
|-------|-------|
| `/etc/profile.d/wsl-proxy.sh` | Shell-Umgebungsvariablen |
| `/etc/apt/apt.conf.d/95wsl-proxy` | APT-Proxy |
| `/etc/environment` | Systemweite Umgebung |
| `~/.mozilla/firefox/*/user.js` | Firefox-Proxy (optional) |

### Standardwerte
- Host: `172.23.0.1` (WSL-Gateway)
- Port: `7897` (Clash-Standard)

---

## Русский

### Возможности
- Настройка системного прокси WSL в один клик
- Поддержка shell-окружения, apt и Firefox
- Встроенный тест подключения
- Чистый интерфейс PyQt5

### Установка
```bash
sudo apt install python3-pyqt5
git clone https://github.com/L0stInFades/WSL_proxy.git
cd WSL_proxy
sudo ./run.sh
```

### Файлы конфигурации
| Файл | Назначение |
|------|------------|
| `/etc/profile.d/wsl-proxy.sh` | Переменные окружения shell |
| `/etc/apt/apt.conf.d/95wsl-proxy` | Прокси APT |
| `/etc/environment` | Системное окружение |
| `~/.mozilla/firefox/*/user.js` | Прокси Firefox (опционально) |

### Значения по умолчанию
- Хост: `172.23.0.1` (шлюз WSL)
- Порт: `7897` (по умолчанию Clash)

---

## License

MIT
