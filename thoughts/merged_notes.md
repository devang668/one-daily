# 合并笔记

---

# 0323 - Claude Code 远程访问通道打通

Claude Code 远程访问通道打通

打通了一个 ycloudflare 通道

打通了claude code的远程访问

使用下面的这个软件
https://github.com/RioArisk/claudecode_api_RemoteControl

还无法解决的事 ，minimax2.7 图像问题

---

# 0324 - 不要怕，大胆去做吧

不要怕，大胆去做吧

---

# 0328 - 非常酷的 Agent Party

非常酷的 Agent Party

https://github.com/heshengtao/super-agent-party?tab=readme-ov-file

<img width="2217" height="1466" alt="image" src="https://github.com/user-attachments/assets/d8ea9876-bcca-4037-969a-66c413889bf1" />

---

# 0329 - 这是一个非常棒的地方

今天我尝试使用github来进行一个简单的博客网站的部署。

我觉得这种方法有助于我更好的沉淀自己的知识。

也有助于我长期的去坚持做好一件事情

目前基因给他改的非常的方便了。


只要新建一个正文，然后呢添加好标题，然后就可以写正文了。

---

# 0329 - 居然还能免费获得编程会员？

在blibli上我发现

开发者，就是仓库有被很多人标记星星收藏的那种会获取到开。深圳，然后还有VS code，编程会员权限。

~
下面和上面没有关。来一点碎碎念就是我发现。腾讯的ima。有看到很多知识库的。

其中包括我买过的dan koe的付费电子书，这个软件甚至还提供了翻译。当时我还是拿着编程去翻译 现在不用了。

哦，对了，养虾户居然还能把这个知识库，接到自己的龙虾里面去。

_

最近还是对量化很感兴趣，计划继续做下去。

其次是学习一门外国的语言，目前来说，就是英语。打算考雅思到7分，在2026.9之前。

---

# 0330 - C Cleaner Plus（C盘强力清理工具）

基于 Python + PySide6 构建的 Windows 全盘清理工具，采用 Fluent 2 设计语言，界面媲美商业级软件。

![版本](https://img.shields.io/github/v/tag/Kiowx/c_cleaner_plus?style=flat-square&color=green)
![平台](https://img.shields.io/badge/Platform-Windows%2010%2F11-blue?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square)
![许可](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 界面预览

UI 采用微软 Fluent 2 设计语言，视觉风格现代精致，支持深色 / 浅色 / 跟随系统三模式：

![界面截图](https://picui.ogmua.cn/s1/2026/03/14/69b5379caafa3.webp)

---

## 功能概览

### 常规清理
- 预置清理目标：临时文件、系统日志、缩略图缓存、浏览器缓存、包管理器缓存等
- 自定义规则支持，拖拽排序
- 清理前预估可释放空间
- 回收站删除 or 永久删除
- 高风险路径保护与警告机制

### 大文件扫描
- 多分区扫描
- 自定义最小文件大小阈值
- 按大小 / 名称 / 路径排序
- 多线程扫描（SSD 自适应 12 线程，HDD 2 线程）

### 应用卸载
- 标准卸载 + 强力卸载（文件 + 注册表 + 服务 + 计划任务）
- 扫描 Windows 注册表获取已安装软件
- 风险分级（颜色标识保护级别）
- 静默卸载命令自动构建（MSI、Inno、NSIS、InstallShield、Squirrel）

### 更多清理
- 重复文件查找（MD5 / SHA256 哈希比对）
- 空文件夹扫描
- 无效快捷方式清理
- 卸载残留注册表清理
- 右键菜单清理

### 定时任务
- 触发类型：每天、每周、每小时、每分钟、登录时
- 支持自定义间隔
- 可执行：常规清理、空文件夹、无效快捷方式、卸载注册表清理
- 开机自启支持

### 规则商店
- 远程规则包下载与导入
- 分类：通用规则、国产软件、开发工具、AI 工具、游戏平台、设计 / 3D / CAD

### 界面设置
- 深色 / 浅色 / 跟随系统主题
- 横向 / 纵向侧边栏布局
- 自动更新检测

---

## 技术架构

### 技术栈

| 层级 | 技术 |
|------|------|
| UI 框架 | PySide6 + PySide6-Fluent-Widgets v1.11.1 |
| 编程语言 | Python 3.9+ |
| 打包工具 | PyInstaller |
| 运行平台 | Windows 10/11（仅支持 Windows） |

### UI 设计模式

应用以 `MSFluentWindow`（多表面 Fluent 窗口）为基底，通过 `NavigationInterface` / `NavigationBar` 实现侧边栏导航：

```
MSFluentWindow
├── NavigationBar（侧边栏）
│   ├── CleanPage         （常规清理）
│   ├── BigFilePage       （大文件扫描）
│   ├── MoreCleanPage     （更多清理）
│   ├── UninstallPage     （应用卸载）
│   ├── SchedulePage      （定时任务）
│   └── RuleStorePage    （规则商店）
└── Settings / About（底部设置）
```

**核心 UI 组件：**
- `ScrollArea` — 所有页面的基础容器
- `TableWidget` + 自定义 `DragSortTableWidget` — 支持拖拽排序的数据表格
- `SearchLineEdit` — 实时搜索过滤
- `SwitchButton` / `ComboBox` / `CheckBox` — 设置控件
- `ProgressBar` — 操作进度展示
- `InfoBar` — 气泡通知
- `MessageBox` / `MessageBoxBase` — 弹窗对话框

**自定义代理：**
- `FluentOnlyCheckDelegate` — 表格自定义复选框渲染
- `SizeTableWidgetItem` — 文件大小的数值排序支持

### 线程模型

- **主线程** — 仅负责 UI 渲染和用户交互
- **工作线程** — 文件扫描、清理操作、哈希计算
- **线程安全通信** — `queue.Queue` 分发任务，`threading.Lock` 保护共享状态
- **可取消操作** — 每个操作通过 `threading.Event` 停止标志实现取消

### Signal / Slot 架构

所有页面共享一个全局 `Sig(QObject)` 信号总线：

```python
class Sig(QObject):
    log = Signal(str)        # 日志消息
    prog = Signal(int, int)  # 进度（当前值，总计值）
    done = Signal(str)       # 操作完成信号
```

### 配置系统

```
configs/
├── cdisk_cleaner_global_settings.json   # 主题、侧边栏、开机自启
├── cdisk_cleaner_custom_rules.json      # 用户自定义规则
├── cdisk_cleaner_config.json            # 规则顺序、启用状态
cdisk_cleaner_bootstrap.json            # 配置目录定位文件
```

---

## 规则格式

清理规则以 JSON 格式存储，结构如下：

```json
[
  ["规则名称", "%路径%", "类型", 是否启用, "描述", 是否自定义, "glob模式"],
  ...
]
```

| 字段 | 类型 | 说明 |
|------|------|------|
| 0 | string | 规则显示名称 |
| 1 | string | 目标路径（支持 `%TEMP%` 等环境变量） |
| 2 | string | 类型：`dir`、`file` 或 `glob` |
| 3 | bool | 是否启用 |
| 4 | string | 人类可读的描述 |
| 5 | bool | 是否为用户自定义规则 |
| 6 | string | （可选）glob 模式，精细化匹配 |

**类型说明：**
- `dir` — 扫描并清理一个目录及其全部内容
- `file` — 清理指定文件
- `glob` — 在目录中按 glob 模式匹配（如 `*.tmp`）

**内置路径变量：**
- `%TEMP%` — 用户临时文件夹
- `%WINDIR%` — Windows 安装目录
- `%LOCALAPPDATA%`、`%APPDATA%` — 应用数据文件夹

---

## 安装运行

### 方式一：从源码运行

```bash
git clone https://github.com/Kiowx/c_cleaner_plus.git
cd c_cleaner_plus
pip install -r requirements.txt
python main.py
```

> **注意：** Python 3.12 + Anaconda 环境可能出现 PySide6 DLL 兼容性问题，推荐使用独立的 Python 3.11 或虚拟环境。

### 方式二：下载预编译 exe（推荐）

前往 [Releases](https://github.com/Kiowx/c_cleaner_plus/releases) 下载最新版，解压后直接运行即可，建议右键以管理员身份运行。

### 方式三：虚拟环境（开发推荐）

```bash
# 创建虚拟环境
python -m venv .venv

# 激活（Windows CMD）
.venv\Scripts\activate.bat

# 或在 Git Bash / WSL 中
source .venv/Scripts/activate

# 安装依赖
pip install -r requirements.txt

# 运行
python main.py
```

### 一键启动脚本

项目根目录提供 `run.bat`，双击即可启动：

```bat
@echo off
cd /d "%~dp0"
if not exist ".venv311\Scripts\python.exe" (
    C:\Python311\Scripts\virtualenv.exe .venv311
)
.venv311\Scripts\python.exe main.py
```

---

## 打包构建

### 前置条件

- Windows 10/11
- Python 3.9+
- `pyinstaller`（`pip install pyinstaller`）

### 构建命令

```bash
pyinstaller c_cleaner_plus.spec
```

构建产物在 `dist/` 目录下。

### 打包配置（.spec 文件）

- 单文件输出
- 启动时自动申请管理员权限（UAC）
- UPX 压缩
- 排除未使用的 Qt 模块（WebEngine、3D、Bluetooth），减小体积
- 自动收集 qfluentwidgets 所有资源文件

---

## 配置说明

### 全局设置

文件：`configs/cdisk_cleaner_global_settings.json`

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

### 主题模式

| 模式 | 值 | 行为 |
|------|------|------|
| 浅色 | `light` | 始终浅色主题 |
| 深色 | `dark` | 始终深色主题 |
| 跟随系统 | `auto` | 与 Windows 系统主题同步 |

### 侧边栏样式

| 样式 | 值 | 行为 |
|------|------|------|
| 纵向 | `vertical` | 仅图标模式（76px 宽度） |
| 横向 | `horizontal` | 完整宽度，带文字标签 |

---

## 风险保护机制

应用内置多级安全保护：

1. **高风险路径检测** — 规则目标为系统目录、磁盘根目录或可执行文件时发出警告
2. **操作确认对话框** — 清理或卸载前始终弹出确认
3. **回收站优先** — 默认将删除文件移入回收站（永久删除需主动选择）
4. **规则保护** — 内置规则无法被意外删除（受开关保护）

---

## 依赖列表

| 包名 | 版本 | 用途 |
|------|------|------|
| PySide6 | 6.10.2 | Qt 绑定 |
| PySide6-Fluent-Widgets | 1.11.1 | Fluent 2 UI 组件库 |
| PySideSix-Frameless-Window | 0.8.0 | 自定义无边框窗口 |
| darkdetect | 0.8.0 | 系统主题检测 |
| pywin32 | 311 | Windows API 访问 |
| pyinstaller | 6.18.0 | 可执行文件打包 |

---

## 项目结构

```
c_cleaner_plus/
├── main.py                         # 全部应用逻辑（单文件架构）
├── requirements.txt                # Python 依赖
├── c_cleaner_plus.spec             # PyInstaller 打包配置
├── run.bat                         # 一键启动脚本
├── icon.ico / app.ico            # 应用图标
├── config/
│   ├── winapp2.json              # 默认清理规则
│   ├── rules_cn_apps.json       # 国产软件清理规则
│   ├── rules_dev_tools.json       # 开发工具清理规则
│   ├── rules_ai_tools.json        # AI 工具清理规则
│   ├── rules_game_platforms.json  # 游戏平台清理规则
│   └── common_custom_rules.json    # 通用软件清理规则
└── .github/workflows/build.yml   # CI/CD 自动发布流程
```

---

## 版本信息

- **当前版本：** v0.4.5-alpha01
- **更新通道：** Stable
- **版本检测地址：** Gitee raw 文件端点

应用启动时自动检测更新，发现新版本会在界面显示提示。

---

## 相关链接

- **GitHub：** https://github.com/Kiowx/c_cleaner_plus
- **Releases：** https://github.com/Kiowx/c_cleaner_plus/releases
- **文档：** https://docs.cus.cc.cd
- **QQ 群：** [点击加入](https://qm.qq.com/q/xE1xw9wP7M)
- **Telegram：** [@kyu649](https://t.me/kyu649)

---

## 许可

MIT License，详见 LICENSE 文件。

---

# 0330 - C Cleaner Plus

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

---

# 0330 - 推广自己的一个项目 Jnote

推广自己的一个项目 Jnote

位置是，在github

devang668/jbook

我最近的一个想法就是希望通过推广，让自己的仓库有更多的人关注他

因为自己想让自己的一些东西让别人知道，嗯，我觉得这样一件事情是很有乐趣的。

此外还有另外一件事情就是浏览器控制上还在学习。


还有一件事情就是要学会直面恐惧，直面恐惧。

总是逃避呢，总是解决不了问题的。

---

今天还发现一个有趣的监控claw的项目

https://github.com/seekcontext/ClawProbe

---

# 0331 - 企业级别的agent是啥样？

九科信息

参考 https://www.36kr.com/p/2072991771769735


九科信息的详细调查报告：
---

## 九科信息 公司调查报告

### 📊 基本信息

| 项目 | 内容 |
|------|------|
| **公司全称** | 九科信息技术（深圳）有限公司 |
| **成立时间** | 2020年7月6日  |
| **孵化背景** | 招商局集团内部创新项目  |
| **创始人/CEO** | 万正勇  |
| **总部** | 深圳福田区 |
| **分公司** | 北京、上海（2021年设立） |
| **注册资本** | 1552.555万人民币  |
| **定位** | 国央企数字化转型专家  |

---

### 💰 融资历程（累计过亿元）

| 时间 | 轮次 | 金额 | 投资方 |
|------|------|------|--------|
| 2020.11 | 种子轮 | 数百万人民币 | -  |
| 2020.12 | 天使轮 | 千万级人民币 | -  |
| 2021.03 | Pre-A轮 | 数千万人民币 | -  |
| 2022.03 | A轮 | 数千万人民币 | -  |
| 2023.02 | A+轮 | - | 引入流程挖掘技术  |
| 2024.07 | B1轮 | 数千万人民币 | 诺辉基金领投，深创投索斯福跟投  |
| 2026.01 | B2轮 | 近亿元 | 特建发（深圳国资）独家领投  |

**最新动态**：2026年1月刚完成B2轮融资，由深圳国资背景的特建发领投，标志着国资对AI Agent赛道的认可 。

---

### 🏆 核心产品与技术创新

**产品矩阵演进**：
- **bit-Worker RPA**：国内唯一全云原生架构RPA产品 
- **bit-Agent**：企业级智能体平台（2024年推出，业内首个完成GUI Agent商业化落地）
- **bit-Crew**：智能组织管控平台（多智能体协同）
- **bit-Miner**：流程挖掘平台 
- **bit-Builder**：低代码开发平台 
- **bit-IDP**：智能文档处理平台 
- **bit-Bot**：智能知识助手 

**技术亮点**：
- ✅ **国内唯一全云原生RPA**：云端部署，不占用本地资源，支持弹性伸缩 
- ✅ **信创全适配**：通过信通院首批3+级信创评测，支持麒麟、统信、达梦、人大金仓等国产生态 
- ✅ **AI+RPA+低代码+流程挖掘**全链路融合 
- ✅ **高密度机器人部署**：单台服务器可部署多个机器人并发运行 

---

### 🎯 市场地位与行业对比

**与影刀RPA的差异定位**：

| 维度 | 九科信息 | 影刀RPA |
|------|----------|---------|
| **核心客群** | 国央企、大型政企  | 中小企业、电商、个人开发者 |
| **技术架构** | 全云原生SaaS  | 传统C/S架构为主 |
| **信创适配** | 深度适配，国产化自主可控  | 相对较弱 |
| **部署方式** | 云端/私有化/混合云  | 本地部署为主 |
| **AI融合** | 企业级智能体bit-Agent  | 正在探索AI能力 |
| **成立时间** | 2020年（晚于影刀） | 2019年 |

**市场数据**：
- 国央企RPA市场份额**第一**，渗透率超30% 
- 被评为**2025种子独角兽企业** 
- 信创工委会成员单位（超级自动化领域唯一）

---

### 🏢 标杆客户与落地案例

**重点行业**：金融、能源、制造、政府、军工、交通 

**典型案例**：
- **上汽集团**：安全巡检模板开发成本从30人天压缩至1人天，效率提升10倍，错误率从15%降至1%以下 
- **招商局集团**：智能问数大模型项目 
- **中国交通建设集团**：大规模RPA部署 
- **统信软件**：AI数字员工项目 
- **某大型航运企业**：财务部门业务流程自动化 

---

### 🔮 战略方向

1. **AI Agent商业化**：2025年被定义为"AI Agent商业化元年"，九科已率先完成GUI Agent商业化落地 
2. **出海业务布局**：B2轮资金将用于海外市场拓展 
3. **信创替代**：金融领域完成国内规模最大的海外RPA产品替换项目 
4. **制造业深耕**：聚焦生产、供应链、质检、设备数据采集等场景 

---

### 💡 总结评价

九科信息确实比影刀RPA起步稍晚（晚约1年），但发展路径非常清晰：
**优势**：
- 央企孵化背景，天然理解国央企需求
- 全云原生架构技术领先
- 信创适配能力行业最强
- AI Agent转型速度快，已商业化落地
- 国资背书（最新一轮深圳国资领投）

**差异化**：如果说影刀RPA是"平民化、易用型"的RPA工具，九科信息则是"企业级、信创型、智能体化"的数字化转型平台，两者客群和场景有明显区隔。在国央企和信创市场，九科信息确实已经建立了很强的壁垒 。

| 序号 | 来源  | 标题/内容                         | 链接                                                 |
| -- | --- | ----------------------------- | -------------------------------------------------- |
| 1  | 36氪 | 九科信息完成数千万B1轮融资，国央企智能自动化赛道迎来爆发 | <https://36kr.com/p/2898572129731207>              |
| 2  | 36氪 | 九科信息完成近亿元B2轮融资，深圳国资独家领投       | <https://36kr.com/p/4043758282686087>              |
| 3  | 企名片 | 九科信息技术（深圳）有限公司 - 融资信息         | <https://www.qimingpian.com/firm/3F3C4D3A7D9E8F5A> |

---

# 0331 - 这里可以发自己的文章

这里可以发自己的文章


https://juejin.cn/user/3335285492167706


---

# 0331 - 哪些软件我都舍不得删除

哪些软件我都舍不得删除

1. 第一个是ES文件管理器，比系统自带的好用多了。
2. 简朴-github0plainAPP
  我发现这个可以很好的管理我的文件，可以让我在PC上管理自己的视频1 图片 甚至还有一些应用
3. slidebox 这是一个安卓上的清理照片的应用。不想要的照片直接往右上角滑动，最后确认一次，免除了必须要删除一张照片就清理一次的麻烦。

---

# 0402 - 为什么会出现claude code 配置失败

为什么会出现claude code 配置失败

如图，这是我的一个ccmmate里面的配置：

<img width="1740" height="963" alt="image" src="https://github.com/user-attachments/assets/276a397e-e642-4426-aef8-41dd23f9265b" />

非常的简单。

我发现，使用minimax就可以通过，但是，使用支持openai样式的就不可以使用，这就好奇了。

所以决定来搞一搞。

先去使用deepseek，他后来兼容了athropic的样式，同时还支持openai样子的调用。

sk-4f654479949b46b688c7****
https://api.deepseek.com/v1
deepseek-chat

--

athropic  https://api.deepseek.com/anthropic

--

```
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)
```
最后得到了回答，那么切换成为普通的openai样式的
<img width="1396" height="1204" alt="image" src="https://github.com/user-attachments/assets/b4917fda-eac1-4ad6-85c7-2e2af8b453e9" />


<img width="1730" height="1092" alt="image" src="https://github.com/user-attachments/assets/cd4c0068-e024-433d-9b3b-bba9b050d40e" />

很显然，这个软件自己不支持那样的修改。



----



补充，我发现国内的大模型，使用ccr的时候会胡乱回答问题
<img width="1225" height="545" alt="image" src="https://github.com/user-attachments/assets/d400d261-baaa-43ed-b0c9-e9bc54cc09ff" />


-- 回答如下，这个和实际的不符合，差得远呢。


```
Now I have a better understanding of the project. Let me create a comprehensive documentation file for the xtrade project   based on what I've discovered.
                                                                                                                              Overview
                                                                                                                              xtrade is a trading framework that provides a unified interface for various trading platforms, with initial support for
  TWS (Interactive Brokers) and placeholder support for other platforms like Binance.

  Project Structure

  The project includes:
  - Core framework files (xtrade/*.py)
  - Configuration files (xtrade/config/*)
  - Test files (xtrade/test/*)
  - Documentation and example files

  Core Components

  XTrade Framework

  The main class XTrade provides a unified interface for:
  - Connecting to different trading platforms
  - Retrieving account information
  - Managing orders and positions
  - Handling market data

  Supported Platforms

  - tws: Interactive Brokers TWS connection
  - binance: Placeholder for Binance integration
  - default: Generic platform interface

  Key Features

  - Unified API across different trading platforms
  - Connection management with automatic configuration
  - Account information retrieval
  - Order management capabilities
  - Position tracking
  - Market data handling

  Configuration

  The project uses a configuration system with:
  - Platform-specific settings
  - Connection parameters
  - API keys and authentication
  - Default settings for various operations

  Files and Modules

  Main Framework Files

  - xtrade/__init__.py: Package initialization
  - xtrade/xtrade.py: Main XTrade class
  - xtrade/tws/tws.py: TWS (Interactive Brokers) integration
  - xtrade/binance/binance.py: Binance placeholder implementation
  - xtrade/default/default.py: Default platform implementation

  Test Files

  - xtrade/test/test.py: Basic test for the framework
  - test_email.py: Email testing functionality

  Configuration Files

  - xtrade/config/__init__.py: Configuration initialization
  - xtrade/config/config.py: Configuration management
  - xtrade/config/config.json: Default configuration
```

不过这个可能是因为模型不支持的原因，他们是为了支持openai样式的，未必支持claude。
--



```
(base) PS C:\Users\25515> ccr

Usage: ccr [command] [preset-name]

Commands:
  start         Start server
  stop          Stop server
  restart       Restart server
  status        Show server status
  statusline    Integrated statusline
  code          Execute claude command
  model         Interactive model selection and configuration
  preset        Manage presets (export, install, list, delete)
  install       Install preset from GitHub marketplace
  activate      Output environment variables for shell integration
  ui            Open the web UI in browser
  -v, version   Show version information
  -h, help      Show help information

Presets:
  Any preset directory in ~/.claude-code-router/presets/

Examples:
  ccr start
  ccr code "Write a Hello World"
  ccr my-preset "Write a Hello World"    # Use preset configuration
  ccr model
  ccr preset export my-config            # Export current config as preset
  ccr preset install /path/to/preset     # Install a preset from directory
  ccr preset list                        # List all presets
  ccr install my-preset                  # Install preset from marketplace
  eval "$(ccr activate)"  # Set environment variables globally
  ccr ui

```

事实是什么样？
--
直接使用支持anthropic的



<img width="686" height="647" alt="image" src="https://github.com/user-attachments/assets/ac9905e2-3ab3-4252-8043-52d1727958a8" />


那么结果很明显，是可以使用的，没有问题的
回答的质量还不错

请看
```

 我查看了你的项目目录，这是一个 AI 创作系统 项目。以下是详细分析：

  📁 项目结构
                                                                                                                              D:\a.Data\MY_GIT_lib\xtrade\01----copy\xtrade\
  ├── 12.py                    # 基础版 Flask AI 聊天系统                                                                     ├── 12_pro.py               # Pro 版（增强功能）
  ├── 12_enhanced.py          # 增强版（可能类似）
  ├── 12_pro.rar              # 压缩备份
  ├── 12_enhanced.zip         # 压缩备份
  ├── test_email.py           # QQ 邮箱测试脚本
  ├── creative_system_pro_v6.db  # SQLite 数据库（V5/V6 版本）
  └── creative_system_pro_v7.db  # SQLite 数据库（Pro 版本）

  🚀 核心功能

  1. 基础版 (12.py)

  - 技术栈: Flask + SQLite + DeepSeek API
  - 功能:
    - AI 对话聊天（支持记忆）
    - 会话管理（新建、切换）
    - 长期记忆摘要（自动更新）
    - 反馈系统（👍/👎）
    - 响应式 Web 界面

  2. Pro 版 (12_pro.py)

  在基础版上增强：
  - 邮件系统:
    - 每日聊天报告（定时发送）
    - 情报抓取报告
    - QQ 邮箱 SMTP 集成
  - 界面升级:
    - 现代化 UI（渐变、动画）
    - 更好的移动端适配
    - Markdown 渲染
  - 额外功能:
    - 定时任务（每天 8:00 发送报告）
    - 情报抓取模拟（可扩展为真实爬虫）
    - 邮件配置界面

  🔧 数据库设计

  - messages 表：存储对话记录
  - sessions 表：存储会话信息和长期记忆摘要
  - settings 表：存储 API 密钥、邮箱配置等
```





---

# 0403 - 一直认为A股很..，直到

一直认为A股很..，直到

<img width="979" height="724" alt="image" src="https://github.com/user-attachments/assets/6257576b-8c37-47f9-88e9-4a8bec03c0d5" />

他用的网站。

<img width="872" height="422" alt="image" src="https://github.com/user-attachments/assets/436cae59-a419-4013-a55b-06d8780b6ec9" />


<img width="1270" height="460" alt="image" src="https://github.com/user-attachments/assets/c4d74a12-c9b1-4ea0-8f98-feeebd37e1db" />


看得出，有人能，准确的说是有个人能从中获利。这种量化的思维也很重要。

https://khsci.com/khQuant/tutorial/ 这是一个很好的向，项目预计会带来很大的帮助。

csdn的课程

<img width="1483" height="1303" alt="image" src="https://github.com/user-attachments/assets/4e581f86-c41a-4870-bd93-0c8e9c5482c6" />

---

# 0407 - 量化的学习

量化的学习


1. Datawhale - whale-quant (最推荐)
仓库地址: datawhalechina/whale-quant

推荐理由: 这是目前国内最火的量化开源课程之一。它不仅在书单中推荐了《征服市场的人》，更重要的是提供了一套从 Python 基础 -> 金融知识 -> 策略回测 -> 实盘的完整链路。

内容: 适合中文语境，有详细的文档和代码示例。

2. Awesome Quant (全球最全)
仓库地址: wilsonfreitas/awesome-quant (或中文翻译版 whataexpert/awesome-quant-zh)

推荐理由: 这是一个"宝库"级别的资源汇总。它按类别罗列了全球最优秀的量化库、书籍和论文。

内容: 在它的 Books 栏目中，你不仅能找到西蒙斯的传记，还能找到如《量化交易》（Ernie Chan 著）等实操性更强的经典。

3. Quant-Books (专项书单)
仓库地址: quantgirluk/Quant-Books

推荐理由: 这个仓库专门收纳了量化金融领域必读的经典书籍列表。

内容: 它将《征服市场的人》列为"必读传记类"，并推荐了配套的硬核技术书（如随机微积分、机器学习金融应用等）。


## 链接


https://deepwiki.com/datawhalechina/whale-quant

https://www.gitlink.org.cn/datawhalechina/whale-quant


https://github.com/datawhalechina/whale-quant 

https://github.com/wilsonfreitas/awesome-quant

https://github.com/quantgirluk/Quant-Books  这是一个书单




## 框架与环境

使用

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

C:\Users\Administrator\.local\bin  这个路径是要跟自己一样的，不是总和我一致的。

# 添加到用户级 PATH（永久生效）
[Environment]::SetEnvironmentVariable("Path", "C:\Users\Administrator\.local\bin;$([Environment]::GetEnvironmentVariable('Path', 'User'))", "User")


``

---

# 0413 - 这个工具很好用

这个工具很好用


https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-archive





【Gemma 4 被越狱了！谷歌最强开源模型，这才是普通人真正需要的本地AI！| 零度解说】 https://www.bilibili.com/video/BV1oSQYBUEur/?share_source=copy_web&vd_source=265396306a9b45c7eb55b0a869216011
https://www.freedidi.com/23720.html

---

# 0415 - provider-BFpCUlM7.js报错解决办法

provider-BFpCUlM7.js报错解决办法


如

npm-global\\node_modules\\openclaw\\dist\\provider-BFpCUlM7.js
    code: 'MODULE_NOT_FOUND',
    requireStack:

OpenClaw 启动时控制台出现以下警告：                                                                                  
  [gateway-http] stage "slack" threw — skipping: Error: Cannot find module '@slack/bolt'

  错误信息：
  Require stack:
  - D:\at-soft\1-sy\node\npm-global\node_modules\openclaw\dist\provider-BFpCUlM7.js

  原因

  OpenClaw 的 Slack 扩展代码引用了 @slack/bolt 模块，但该模块未随 OpenClaw 一起安装。这是 Slack
  功能的一个可选依赖，不影响其他功能正常运行。

  解决方法

  方法一：注释掉引用代码（推荐）

  找到 provider-BFpCUlM7.js 文件：

  文件路径：
  <openclaw安装目录>/dist/provider-BFpCUlM7.js

  找到并注释掉以下两行（第 69-70 行）：
  // import * as SlackBoltNamespace from "@slack/bolt";
  // import SlackBolt from "@slack/bolt";

  方法二：安装缺失的模块

  如果你需要使用 Slack 功能，可以安装 @slack/bolt：

  cd <openclaw安装目录>
  npm install @slack/bolt

  验证

  重启 OpenClaw，检查控制台输出中是否还有 stage "slack" threw 的警告。如果不再出现，说明问题已解决。

  ---
  适用于 OpenClaw 版本 2026.4.2

---

# 0416 - 为了支付大模型的费用，费力好大

为了支付大模型的费用，费力好大


真是难受死我了，给自己用的那个 open router 大模型充点额度。

费在九牛二虎之力。本来想着自己有欧易的账户，还有币安的账户那么直接用里面的加密货币不就 OK 吗？

USDT 转成 USDC 不就能支付了吗，如果真是这样，那就真太好了

不是这样的，他他每一步需要手续费不说，然然后支付的时候呢，必须使用的是 web3 钱包，web3 钱包里面必须有这个，

必须有必须有那个，矿工费，每一步都需要有矿工费，然后，我直接转进去的是 USDT. USDT 呢，要想办法变成 USDC，需要矿工费。

哦，我没有。有一个很稀有的链儿，

要往里面弄那个以太坊，然后，然后还要存到那个钱包里面，再扣一遍。搞完了之后发现了我这个 欧易的钱包啊，这个 欧易的钱包，它的那个交易密码不是手机手机的密码。

晕了晕了，真的把自己搞晕了。然后发现，等于说自己往一个不知道交易密码的账户里面充了钱，然后也没法搞出来，

只能一遍又一遍地试自己到底哪一个密码是可能对的。如果试不出来的话，这这么点儿钱就白搭了，就白扔了。

想了想，我还是觉得，要是那个钱包就是像币安里边的那种，那种可以使用手机密码去进行支付的。
OE 里面的真是垃圾啊。回到必安里面，我真的回到必然里面，想去来做了，又发现一个问题，

币安里面没有那个支持的链的协议。虽然我有 USDC，但是因为没有那个链儿的支持，所以你要调到那个链里边去，

这个又难到我了，然后我以为是需要用一点有$BNB$没想到不是的,  那咋整呢？这加密货币这条路实在走不通啊

哎，直接用自己的银行卡吧。幸亏自己之前开了一张天星银行的卡片，

然后用这个 visa 卡绑到这个 open router 里边，然后再用自己中国银行往这个天星的卡里边充值，
通过它那个中国银行 APP 里面的跨境支付，跨境通道免手续费的，我看了一眼，他貌似是消耗的我人民币的额度，
然后兑成了港元。等于说他是占用了那个我每年 5 万美金的额度，我反正自己也用不到那么大，
没关系，没关系。搞了一圈，10 块钱里面有这个 0.8 美金的手续费，还是避免不了。

也许是我太菜了，哈哈。

---

# 0416 - 我记得的话

我记得的话

> He always fought, that's what I remember. He fought because he knew if he didn't fight, it would make it that much easier not to fight the next time.

我记得，他总是反抗。他反抗是因为他知道如果他不反抗，下次就更不会反抗了.

自我设限是最大的监狱，否定自己的可能性和可塑性，然后放弃寻找出路，放弃努力和抗争，其实就是在精神上画地为牢，给自己判了监禁。


安迪托瑞德买锤子，瑞德刚开始以为是会闹出大动静的那种违禁用品，有点犹豫。因为狱方虽然对黑市交易睁一只眼，闭一只眼，但是存在一条红线，越过红线就会惹麻烦。

结果瑞德拿到锤子时，撇嘴笑了，实在是太小了，他说："用这玩意儿挖地道，估计得挖上600年。"

可是瑞德觉得要花600年才能挖通的地道，安迪花了19年就挖通了。


> 典狱长果然像老布说的那样以预算不足为由拒绝了，安迪从典狱长那里得不到钱，提出写信向州参议院申请资金，典狱长的说法是老布说法的2.0，监狱想申请到资金，只有三件事，加高围墙、增加牢房、增派守卫。
  
  事情果然如典狱长说的那样，安迪的信石沉大海，所有人都觉得安迪是在犯傻，因为他在做一件没可能的事。
  
  但是安迪一直写一直写，州参议院终于不胜其烦，给他拨款200美元以及捐赠一批旧书和杂物。安迪开心地说："只写了六年。从今天开始我要一周写两封。"
  
  最终州参议院被逼得没办法，每年拨款500美元给图书馆。
  
  大家一致觉得零可能申请到的拨款，安迪只花了几年时间。
  
  你看，事情很少会糟糕到完全无能为力的地步，总能找到可以帮助我们达成目的的办法。



"怯懦囚禁人的灵魂，希望可以让你自由"，说的就是这个。心存希望的人，无论什么处境都无法把他钉死。

他们就像落进石头缝里的草籽，只要有一点点机会都要蓬勃生长。他们是那种被关进监狱就开始积蓄力量，筹谋越狱的人。


<img width="866" height="429" alt="image" src="https://github.com/user-attachments/assets/ca1406d4-e5c2-41c7-b00e-c0d9394fc77b" />

rrefer https://www.sohu.com/a/437918716_100010489 


---

# 0417 - 从抄开始

从抄开始

> 目标：利用开源项目快速入门，建立自己的量化交易系统
>

## 一、为什么靠开源项目入门是最高效的

1. **跳过重复造轮子** — CCXT 已经解决了 100+ 交易所 API 归一化问题
2. **真实代码可参考** — 成熟框架的架构设计是经过实盘验证的
3. **圈子资源丰富** — 很多量化工作室会开源部分策略，站在前人肩膀上事半功倍
4. **先跑通再深入** — 先让系统跑起来，再研究底层原理

---

## 二、架构设计：如何让代码从"散乱"变"模块化"

这是很多人自研量化系统的必经之路。代码"散乱"的本质是**把不同职责的代码混在了一起**。

### 四层解耦架构

成熟的量化系统分为四个独立模块，互不依赖：

```
┌─────────────────────────────────────────────────────┐
│                   Data Handler                      │
│  职责：抓取数据、格式化、自动重连                    │
│  特点：只和数据源打交道，不涉及任何交易逻辑          │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│                 Strategy Engine                     │
│  职责：接收数据 → 计算指标 → 输出信号                │
│  特点：纯数学逻辑，单元测试友好                      │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│               Portfolio Manager                     │
│  职责：仓位计算、止损、风控                          │
│  特点：所有"钱相关"的逻辑在这里                       │
└─────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────┐
│               Execution Handler                     │
│  职责：发单、追单、成交回报处理                      │
│  特点：只和交易所 API 打交道                          │
└─────────────────────────────────────────────────────┘
```

### 自检标准

如果你的策略代码里出现了 `ccxt.create_order`，说明架构有问题。正确的做法：

```python
# ❌ 错误：逻辑散乱
class MyStrategy:
    def on_tick(self, ticker):
        if self.compute_signal(ticker) > threshold:
            exchange.create_order(...)  # 策略里直接调用了交易所API

# ✅ 正确：职责分离
class MyStrategy:
    def on_tick(self, ticker) -> Signal:
        return Signal(self.compute_signal(ticker))  # 只返回信号，不下单

# Execution Handler 负责：
class ExecutionHandler:
    def execute(self, signal: Signal, portfolio: Portfolio):
        exchange.create_order(...)  # 只有这里调用交易所API
```

### 日志规范（放弃 print）

```python
import logging

# 创建专用 logger
logger = logging.getLogger('quant.data')
order_logger = logging.getLogger('quant.order')

# 不同信息进不同文件
fh = logging.FileHandler('logs/market_data.log')
fh.setLevel(logging.DEBUG)
order_logger.addHandler(fh)

order_logger.info(f"买单成交 | 价格:{price} | 数量:{amount}")
```

---

## 三、优质开源项目清单

### 3.1 必学基础框架

#### CCXT — 交易所通信层（必学）

所有项目的底层依赖，支持 100+ 交易所统一接口。

```python
import ccxt

binance = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'enableRateLimit': True,
    'options': {'defaultType': 'spot'},  # 现货
})

# 获取 K 线
ohlcv = binance.fetch_ohlcv('BTC/USDT', '1h', limit=100)

# 获取深度图
orderbook = binance.fetch_order_book('BTC/USDT')
```

#### VN.py — 国内量化首选（C++ 核心）

国内最成熟的量化框架，底层 C++ 高性能，深度适配币安 / OKX / Bybit。

- GitHub: https://github.com/vnpy/vnpy
- 特点：国产、社区活跃、文档中文友好

#### Freqtrade — 策略入门首选

最火的 Python 交易机器人，回测 + 优化 + 实盘一条龙。

```bash
git clone https://github.com/freqtrade/freqtrade.git
cd freqtrade
python -m venv venv
pip install -e.

# 下载历史数据
freqtrade download-data --pairs BTC/USDT --timeframe 1h

# 回测
freqtrade backtesting --config config.json --strategy DefaultStrategy

# 实盘
freqtrade trade --config config.json --strategy DefaultStrategy
```

---

### 3.2 C++ 硬核项目（适合构建高性能底座）

#### WonderTrader — 国产 C++ 硬核框架

最适合有 C++ 背景的开发者，高性能、多策略并发。

- GitHub: https://github.com/wondertrader/wondertrader
- 特点：C++ 核心 / Python 调用 / 高频低延迟 / 插件化架构

#### Hikyuu Quant Framework — 金融级架构

代码组织极其严密，适合学习"如何把金融工程思维融入代码架构"。

- GitHub: https://github.com/fanyf2002/hikyuu

#### QuantConnect Lean Engine — 世界级架构

全球最著名的开源量化引擎，架构设计堪称教科书。

- GitHub: https://github.com/QuantConnect/Lean
- 特点：C# 核心 / 支持 Python / 架构极其严谨

---

### 3.3 按需求选择

| 需求场景 | 推荐项目 | 理由 |
|:---|:---|:---|
| **快速跑通一个策略** | Freqtrade | 安装简单，文档完善 |
| **做市 / 套利** | Hummingbot | 专为做市设计 |
| **高频回测** | VectorBT | 向量化回测，速度极快 |
| **机器学习策略** | Freqtrade + FreqAI | 内置 ML 支持 |
| **C++ 高性能底座** | WonderTrader | 国产硬核 |
| **学习架构设计** | QuantConnect Lean | 世界级参考 |
| **国内 + Python** | VN.py | 社区活跃，中文友好 |

---

### 3.4 更多可参考的项目

| 项目 | 链接 | 特点 |
|:---|:---|:---|
| CCXT | https://github.com/ccxt/ccxt | 交易所统一接口 |
| Hummingbot | https://github.com/hummingbot/hummingbot | 做市策略专家 |
| VectorBT | https://github.com/polakowo/vectorbt | 超高速回测 |
| FreqAI | 内置于 Freqtrade | ML 增强策略 |
| Flashbots | https://github.com/flashbots | 以太坊 MEV 套利 |

### GitHub Topics（找项目用）
- https://github.com/topics/crypto-trading-bot
- https://github.com/topics/quantitative-trading
- https://github.com/topics/algorithmic-trading

---

## 四、网络与部署方案

这是你提到的一个关键痛点：本地需要挂着梯子才能访问交易所 API，极其不稳定。

### 方案一：租用海外 VPS（推荐）

把代码部署到海外服务器，服务器本身直连交易所，延迟低且稳定。

```bash
# 推荐配置（最便宜的即可）
# AWS 东京 / 新加坡节点
# 阿里云国际版（香港节点）
# 腾讯云海外版

# 部署结构
# 本地  →  SSH  →  海外 VPS  →  交易所 API
#         (跳板)     (代码运行)
```

**优点：**
- 服务器在海外，直连交易所毫秒级
- 完全不需要梯子
- 断网不影响 VPS 上的运行

**缺点：**
- 有费用（约 20-50 元/月）
- 调试不如本地方便

### 方案二：代码级代理（调试用）

如果必须本地调试，在 CCXT 初始化时注入代理：

```python
import ccxt

binance = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'proxies': {
        'http': 'http://127.0.0.1:7890',      # 你的梯子端口
        'https': 'http://127.0.0.1:7890',
    },
})
```

### 方案三：反向代理（Nginx）

在 VPS 上搭一个 Nginx 反向代理，本地代码访问 VPS IP，由服务器转发到交易所：

```nginx
# /etc/nginx/conf.d/crypto-proxy.conf
server {
    listen 8080;
    location /binance/ {
        proxy_pass https://api.binance.com/;
        proxy_set_header Host api.binance.com;
    }
}
```

---

## 五、自检清单

完成以下事项，说明你的系统已经初步成型：

- [ ] **架构分离** — 策略逻辑和交易所 API 调用不在同一个文件
- [ ] **日志系统** — 行情数据、下单回报、网络错误分别记录到不同文件
- [ ] **单元测试** — 指标计算函数有 `pytest` 测试，输入一致输出必一致
- [ ] **回测验证** — 策略在历史数据上跑通，且做了样本外验证
- [ ] **参数不过拟合** — 用 walk-forward 验证，而非过度优化

---

## 六、快速入门路线图

```
第1周：CCXT 入门
  ├── 学会获取 K 线 / Order Book
  ├── WebSocket 订阅实时行情
  └── 理解限流机制

第2-3周：Freqtrade 实战
  ├── 跑通自带的示例策略
  ├── 修改 MACD / RSI 策略
  └── 学会用 hyperopt 优化参数

第4周：架构重构
  ├── 把散乱的代码按四层架构拆分
  ├── 引入 logging 日志系统
  └── 给核心函数写单元测试

第5周：部署上线
  ├── 选一个海外 VPS 部署
  ├── 配置自动重启（supervisor / systemd）
  └── 接入 Telegram 通知

第6周+：策略深化
  ├── 研究别人的开源策略（Freqtrade Strategies 仓库）
  ├── 学习仓位管理和风控
  └── 逐步加入自己的策略想法
```

---

## 七、避坑指南

1. **不要迷信复杂模型** — 简单的波动率策略 / 趋势跟踪往往比深度学习更健壮
2. **永远设止损** — 币圈波动极大，不设止损可能归零
3. **注意 API Key 安全** — 环境变量读取，不要明文写在代码里
4. **手续费和滑点** — 回测时务必计入，实盘利润可能和回测差很远
5. **过拟合问题** — 样本外测试不通过，策略不要上实盘

---

# 0418 - win上的超级好用的内存清理工具

win上的超级好用的内存清理工具

有的人，是的，只是为了清理自己的内存，就去下载了2G或者更大的电脑管家，是实在是一个很糟糕的打算。

因为软件清理的内存，可能比不上他自己盈利广告所占用的内存，而且吧，太大了。

那就没法子？


点击访问
`https://learn.microsoft.com/zh-cn/sysinternals/downloads/rammap`

有的，win的官网，一般32位的系统就选择 RAMMap.exe 。
<img width="692" height="425" alt="image" src="https://github.com/user-attachments/assets/0d3ddcb7-6bcb-47c7-b9d8-821bcd3319ab" />

点前两个

<img width="603" height="303" alt="image" src="https://github.com/user-attachments/assets/681ac079-de98-4118-a51e-71b30c762f43" />





---

# 0418 - 一行超级命令，看看自己装了啥

一行超级命令，看看自己装了啥

powershell 中使用







Write-Host "`n====== Node.js ======" -F Cyan; if(Get-Command node -EA 0){Write-Host "  Path: $((Get-Command node).Source)"; Write-Host "  Version: $(node -v)"}else{Write-Host "  Not found"}; Write-Host "`n====== npm ======" -F Cyan; if(Get-Command npm -EA 0){Write-Host "  Path: $((Get-Command npm).Source)"; Write-Host "  Version: $(npm -v)"; Write-Host "  Global Dir: $(npm root -g)"; Write-Host "  \[Global Packages]"; npm list -g --depth=0}else{Write-Host "  Not found"}; Write-Host "`n====== Python ======" -F Cyan; if(Get-Command python -EA 0){Write-Host "  Path: $((Get-Command python).Source)"; python --version 2>\&1|ForEach-Object{Write-Host "  $\_"}; if(Get-Command pip -EA 0){Write-Host "  Pip Path: $((Get-Command pip).Source)"}; Write-Host "  Site Packages:"; python -c "import site;\[print('  '+p)for p in site.getsitepackages()]" 2>$null; Write-Host "  \[Pip Packages]"; python -m pip list 2>$null}else{Write-Host "  Not found"}; Write-Host "`n====== Python Virtual Environments ======" -F Cyan; Write-Host "  Scanning..."; $v=@(); @($env:USERPROFILE,"$env:USERPROFILE\\Desktop","$env:USERPROFILE\\Documents","$env:USERPROFILE\\Projects","$env:USERPROFILE\\code","D:\\")|ForEach-Object{if(Test-Path $\_){Get-ChildItem -Path $\_ -Recurse -Filter "pyvenv.cfg" -EA 0 -Depth 5|ForEach-Object{$v+=$\_.DirectoryName}}}; if($v.Count -gt 0){Write-Host "  Found $($v.Count) venv(s):" -F Green; $v|ForEach-Object{Write-Host "    $\_" -F Yellow}}else{Write-Host "  No venvs found"}; Write-Host "`n============================"; Write-Host "Done!" -F Green




---

# 0419 - 有趣的社区

有趣的社区

linuxdo


https://www.csdn.net/opensource?spm=1000.2115.3001.10510


今日不限token

https://gitcode.com/?utm_source=csdn_github_accelerator&from_id=146422346&isLogin=1


教育优惠

https://github.com/settings/education/benefits

---

# 0419 - AI：2028年全球智能危机

AI：2028年全球智能危机



以下是该内容的核心总结及应对策略：

### 1. 核心危机：2028年全球智能危机
老王引用了一篇关于"2028年全球智能危机"的虚构式报告，预测人类股市将在 **2026年10月** 达到历史最高点（标普8,000点，纳指3万点），随后因AI带来的结构性问题导致长达两年的崩盘，到 **2028年6月** 美国失业率可能飙升至 **10.2%**。

### 2. 核心概念：幽灵GDP（Ghost GDP）与死亡螺旋
*   **幽灵GDP：** 即使AI极大提升了企业的利润和GDP数字，但这些增长并不会产生实体产出，也不会转化为人类的消费。
*   **消费归零：** 算力中心可以产生相当于1万名白领的产值，但机器人不买房、不买车、不消费（仅消耗电费）。
*   **死亡螺旋：** 公司为提高利润裁减白领，将省下的钱投入AI算力，导致更多白领失业，进而摧毁了作为经济基石的消费市场。

### 3. 被AI全面取代的高危行业
老王特别点名了以下依赖"中介、撮合、信息差"或"人类习惯摩擦"的行业：
*   **软件开发：** 智能代理（Agent）型编码工具的出现，让初中生也能在几周内复刻中型SaaS公司的产品。
*   **中介服务：** 包括 **房地产中介、保险续保、旅行社**。AI代理可以不间断地比较最优价格和条款，直接瓦解这些行业15%-20%的利润空间。
*   **专业咨询：** 理财顾问、会计师、法律顾问等白领职位将被AI机器人替代。
*   **金融支付：** 稳定币和AI代理将绕过银行和信用卡公司（如Visa、Mastercard）2%-3%的手续费。

### 4. 社会影响：降维打击与基石坍塌
*   **白领蓝领化：** 失业的白领被迫涌入Uber、外卖等零工经济，导致底层工资被进一步压缩。
*   **最后的体面消失：** 即使是开Uber，随着 **自动驾驶技术** 的普及，人类司机也会在2年内被淘汰。
*   **金融地基融化：** 高收入白领失业导致房地产按揭（美国金融市场的地基）大面积违约，引发系统性崩溃。

### 5. 应对策略：你必须做好的"最坏准备"
综合多个来源，建议采取以下行动：
*   **审视资产：** 检查你的投资组合中是否包含那些挺不过这一关、将被AI彻底颠覆的传统中介或SaaS公司股票。
*   **拥抱AI工具：** 利用像 **Ollama** 或 **Llama.cpp** 这样的本地AI引擎来提升个人效率。建立自己的"数字员工"（AI Agent）来处理标准化、流程化的工作。
*   **构建"第二曲线"：** 逃离单一的体制化收入，尝试自媒体或利用AI进行创业，积累属于自己的粉丝、连接和信任。
*   **财务防御：** 学会延迟满足，拒绝盲目升级消费；通过定投（DCA）标普/纳指等长期增长标的来构建被动收入，而不是指望政府养老金。
*   **精神脱敏：** 保持独立思考，不再迷信权威和体制提供的"标准答案"，主动掌握自己的人生方向。

**总结：** 这一轮AI浪潮不仅是技术的迭代，更是人类智力溢价趋向于零的重构过程。在金融危机（金丝雀）尚未完全爆发前，这是你审视职业规划和投资组合最后的窗口期。

这段视频（老王来了：2028年全球失业潮爆发？）深入探讨了人工智能（AI）对未来经济的冲击，并对 **2026年至2028年** 可能爆发的全球性失业潮与金融危机做出了惊人的预测。

---

# 0419 - 视觉控制win系统

视觉控制win系统

豆包手机？


那么豆包电脑呢？

https://github.com/CursorTouch/Windows-Use

还有微软的基于qwen-vl-2.5--7b 的 fara 

https://github.com/microsoft/fara

---

# 03-29 - minimax2.7 ：有点让人失望的绘图能力

基础会员做不了图片


开了之后是这样的

目前来看是这样的



<img width="1577" height="984" alt="image" src="https://github.com/user-attachments/assets/d4c5e279-8c88-406f-9cf0-65a63bd2b62c" />


制图效果不如gpt的精彩。

下图是gpt5.4做的，使用的是codex。直接在word中做。

<img width="1151" height="429" alt="image" src="https://github.com/user-attachments/assets/f7909991-2948-4ec3-9c6c-d81376210844" />

---

# 目录

这个就作为目录吧

0321  想做一个git仓库的 本地检索工具，我发现自己有太多的本地仓库了。

他们是可以合并的。散落到各个地方，占用我的存储空间。

https://github.com/hangwin/mcp-chrome/tree/master  


