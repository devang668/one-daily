# C Cleaner Plus（C盘强力清理工具）

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
