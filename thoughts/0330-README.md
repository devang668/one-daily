# C Cleaner Plus

A full-featured Windows disk cleaner with a modern Fluent 2 design UI, built with Python + PySide6.

![Version](https://img.shields.io/github/v/tag/Kiowx/c_cleaner_plus?style=flat-square&color=green)
![Platform](https://img.shields.io/badge/Platform-Windows%2010%2F11-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Screenshots

The UI adopts Microsoft's Fluent 2 design language with a clean, modern look that rivals commercial software:

| Light Theme | Dark Theme |
|------------|------------|
| ![Light](https://picui.ogmua.cn/s1/2026/03/14/69b5379caafa3.webp) | _Similar layout, auto-switches with system theme_ |

---

## Features

### Regular Cleaning
- Pre-defined cleaning targets: temp files, system logs, thumbnail caches, browser caches, package manager caches
- Custom rule support with drag-and-drop ordering
- Size estimation before cleaning
- Recycle bin or permanent delete
- High-risk path protection with warnings

### Big File Scanner
- Multi-partition scanning
- Custom minimum file size threshold
- Results sorting by size / name / path
- Multi-threaded scanning (adaptive: 12 threads for SSD, 2 for HDD)

### Application Uninstall
- Standard uninstall + forced uninstall
- Scans Windows registry for installed software
- File + registry + service + scheduled task cleanup
- Risk classification (color-coded protection levels)

### More Cleaning
- Duplicate file finder (MD5/SHA256 hash comparison)
- Empty folder scanner
- Invalid shortcut cleaner
- Uninstall registry cleaner
- Context menu cleaner

### Scheduled Tasks
- Trigger types: daily, weekly, hourly, per-minute, on-logon
- Clean, empty folders, shortcuts, uninstall registry operations
- Auto-start on Windows boot support

### Rule Store
- Remote rule package download and import
- Categories: common, Chinese apps, dev tools, AI tools, gaming platforms, design/3D/CAD

### UI Settings
- Light / Dark / Follow System theme
- Horizontal / Vertical sidebar layout
- Automatic update checking

---

## Architecture

### Tech Stack

| Layer | Technology |
|-------|------------|
| UI Framework | PySide6 + PySide6-Fluent-Widgets v1.11.1 |
| Language | Python 3.9+ |
| Build | PyInstaller |
| Platform | Windows 10/11 only |

### UI Design Pattern

The app uses `MSFluentWindow` (Multi-Surface Fluent Window) from qfluentwidgets as the main window, with `NavigationInterface` / `NavigationBar` for sidebar navigation.

```
MSFluentWindow
├── NavigationBar (sidebar)
│   ├── CleanPage         (常规清理)
│   ├── BigFilePage       (大文件扫描)
│   ├── MoreCleanPage     (更多清理)
│   ├── UninstallPage     (应用卸载)
│   ├── SchedulePage      (定时任务)
│   └── RuleStorePage    (规则商店)
└── Settings / About
```

**Key UI Components:**
- `ScrollArea` — base for all pages
- `TableWidget` with custom `DragSortTableWidget` — drag-drop enabled data tables
- `SearchLineEdit` — real-time filtering
- `SwitchButton` / `ComboBox` / `CheckBox` — settings controls
- `ProgressBar` — operation progress
- `InfoBar` — toast notifications
- `MessageBox` / `MessageBoxBase` — dialogs

**Custom Delegates:**
- `FluentOnlyCheckDelegate` — custom checkbox rendering for tables
- `SizeTableWidgetItem` — numeric sorting for file sizes

### Threading Model

- **Main thread** — UI rendering and user interaction only
- **Worker threads** — file scanning, cleaning, hash computation
- **Thread-safe communication** — `queue.Queue` for work distribution, `threading.Lock` for shared state
- **Cancellable operations** — `threading.Event` stop flags per operation

### Signal/Slot Architecture

All pages share a global `Sig(QObject)` signal bus:

```python
class Sig(QObject):
    log = Signal(str)        # logging messages
    prog = Signal(int, int)  # progress (current, total)
    done = Signal(str)       # completion signal with result
```

### Configuration System

```
configs/
├── cdisk_cleaner_global_settings.json   # theme, sidebar, auto-start
├── cdisk_cleaner_custom_rules.json      # user-defined rules
├── cdisk_cleaner_config.json            # rule order, enabled states
cdisk_cleaner_bootstrap.json             # config directory locator
```

---

## Rule Format

Cleaning rules are stored in JSON with this structure:

```json
[
  ["Rule Name", "%PATH%", "type", enabled, "description", is_custom, "glob_pattern"],
  ...
]
```

| Field | Type | Description |
|-------|------|-------------|
| 0 | string | Rule display name |
| 1 | string | Target path (supports environment variables like `%TEMP%`) |
| 2 | string | Type: `dir`, `file`, or `glob` |
| 3 | bool | Whether the rule is enabled |
| 4 | string | Human-readable description |
| 5 | bool | Whether this is a user-defined rule |
| 6 | string | (optional) Glob pattern for fine-grained matching |

**Type Details:**
- `dir` — scan and clean a directory and all its contents
- `file` — clean a specific file
- `glob` — scan a directory with a glob pattern (e.g. `*.tmp`)

**Built-in Path Variables:**
- `%TEMP%` — user temp folder
- `%WINDIR%` — Windows directory
- `%LOCALAPPDATA%`, `%APPDATA%` — app data folders
- Custom paths can be added via `%PATH%` or absolute paths

---

## Installation

### From Source

```bash
# Requires Python 3.9+ with pip
git clone https://github.com/Kiowx/c_cleaner_plus.git
cd c_cleaner_plus
pip install -r requirements.txt
python main.py
```

> **Note:** Python 3.12 with Anaconda may have PySide6 DLL compatibility issues. It is recommended to use a standalone Python 3.11 installation or a virtual environment.

### From Release (Pre-built Executable)

Download the latest `.exe` from [Releases](https://github.com/Kiowx/c_cleaner_plus/releases) and run directly. No installation required.

---

## Running

### Quick Start (from source)

```bash
git clone https://github.com/Kiowx/c_cleaner_plus.git
cd c_cleaner_plus
pip install -r requirements.txt
python main.py
```

It is recommended to **run as Administrator** for full cleaning capabilities.

### Virtual Environment Setup (Recommended)

```bash
# Install Python 3.11 embeddable (if not present)
# Create virtual environment
python -m venv .venv

# Activate
.venv\Scripts\activate.bat    # Windows CMD
# or
source .venv/Scripts/activate  # Git Bash / WSL

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

### Automated Launch Script

A `run.bat` is provided for quick launch:

```bat
@echo off
cd /d "%~dp0"
if not exist ".venv311\Scripts\python.exe" (
    C:\Python311\Scripts\virtualenv.exe .venv311
)
.venv311\Scripts\python.exe main.py
```

---

## Building from Source

### Prerequisites

- Windows 10/11
- Python 3.9+ (or use the embeddable distribution)
- `pyinstaller` (`pip install pyinstaller`)

### Build Command

```bash
pyinstaller c_cleaner_plus.spec
```

The built executable will be in the `dist/` folder.

### Build Configuration

The `.spec` file is configured for:
- Single-file output
- UAC admin elevation on startup
- UPX compression
- Excludes unused Qt modules (WebEngine, 3D, Bluetooth) to reduce size
- Automatic qfluentwidgets resource collection

---

## Configuration Files

### Global Settings

Stored in `configs/cdisk_cleaner_global_settings.json`:

```json
{
    "auto_save": true,
    "auto_start": false,
    "theme_mode": "auto",
    "sidebar_style": "vertical",
    "update_channel": "stable",
    "protect_builtin_rules": true,
    "deleted_builtin_rules": []
}
```

### Theme Modes

| Mode | Value | Behavior |
|------|-------|----------|
| Light | `light` | Always light theme |
| Dark | `dark` | Always dark theme |
| Follow System | `auto` | Syncs with Windows system theme |

### Sidebar Styles

| Style | Value | Behavior |
|-------|-------|----------|
| Vertical | `vertical` | Icon-only compact mode (76px) |
| Horizontal | `horizontal` | Full-width with text labels |

---

## Risk Protection

The application implements multi-level protection for dangerous operations:

1. **High-risk path detection** — warns when rules target system directories, disk roots, or executable files
2. **Confirmation dialogs** — always confirms before cleaning or uninstalling
3. **Recycle bin default** — deleted files go to recycle bin by default (permanent delete is opt-in)
4. **Rule protection** — built-in rules cannot be accidentally deleted (protected by toggle)

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PySide6 | 6.10.2 | Qt bindings |
| PySide6-Fluent-Widgets | 1.11.1 | Fluent 2 UI components |
| PySideSix-Frameless-Window | 0.8.0 | Custom frameless window |
| darkdetect | 0.8.0 | System theme detection |
| pywin32 | 311 | Windows API access |
| pyinstaller | 6.18.0 | Executable packaging |

---

## Project Structure

```
c_cleaner_plus/
├── main.py                      # All application logic (single-file architecture)
├── requirements.txt              # Python dependencies
├── c_cleaner_plus.spec          # PyInstaller configuration
├── icon.ico / app.ico          # Application icons
├── config/
│   ├── winapp2.json            # Default cleaning rules
│   ├── rules_cn_apps.json       # Chinese app cleaning rules
│   ├── rules_dev_tools.json     # Dev tools cleaning rules
│   ├── rules_ai_tools.json      # AI tools cleaning rules
│   ├── rules_game_platforms.json # Gaming platform cleaning rules
│   └── common_custom_rules.json  # Common app cleaning rules
└── .github/workflows/build.yml  # CI/CD release pipeline
```

---

## Version & Update

- **Current Version:** v0.4.5-alpha01
- **Update Channel:** Stable
- **Update Check URL:** Gitee raw file endpoint

The app checks for updates on startup and displays an info bar when a new version is available.

---

## License

MIT License. See LICENSE file for details.

---

## Links

- **GitHub:** https://github.com/Kiowx/c_cleaner_plus
- **Releases:** https://github.com/Kiowx/c_cleaner_plus/releases
- **Documentation:** https://docs.cus.cc.cd
- **QQ Group:** [Join via QQ](https://qm.qq.com/q/xE1xw9wP7M)
- **Telegram:** [@kyu649](https://t.me/kyu649)
