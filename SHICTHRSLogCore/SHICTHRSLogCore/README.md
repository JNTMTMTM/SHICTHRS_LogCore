# SHRLogCore

SHICTHRS LOG CORE - 一个功能强大的Python日志记录核心模块

## 简介

SHRLogCore是SHICTHRS团队开发的一个高级日志记录核心模块，提供了丰富的日志记录功能，包括彩色控制台输出、自动日志文件管理、配置文件支持等功能。

## 特性

- 🎨 **彩色控制台输出** - 不同级别的日志使用不同颜色显示
- 📁 **自动日志文件管理** - 自动创建日志目录和文件
- ⚙️ **配置文件支持** - 通过INI文件灵活配置日志行为
- 🕐 **时间同步** - 集成系统时间同步功能
- 🔐 **文件哈希** - 使用MD5哈希确保日志文件唯一性
- 🧹 **自动清理** - 可配置自动清理过期日志
- 📊 **函数追踪** - 可选显示调用函数名称

## 安装

### 依赖项

在安装SHRLogCore之前，请确保已安装以下依赖项：

```bash
pip install colorama
```

### 安装方式

1. **使用pip安装（推荐）**

```bash
pip install SHICTHRSLogCore
```

2. **克隆仓库**

```bash
git clone https://github.com/SHICTHRS/SHICTHRS_LogCore.git
cd SHICTHRS_LogCore
```

3. **将模块添加到项目**

将`src`目录复制到您的项目中，或者将项目路径添加到Python路径中。

## 使用方法

### 基本使用

```python
from SHRLogCore import SHRLogCore

# 创建日志核心实例
logger = SHRLogCore()

# 添加不同级别的日志
logger.add_log('INFO', '这是一条信息日志')
logger.add_log('DEBUG', '这是一条调试日志')
logger.add_log('WARNING', '这是一条警告日志')
logger.add_log('ERROR', '这是一条错误日志')
logger.add_log('CRITICAL', '这是一条严重错误日志')
```

### 配置选项

SHRLogCore通过`config/SHRLogCoreConfigSettings.ini`文件进行配置：

```ini
[SHRLogCore]
isOutputLogsInConsole = True
isOutputFunctionLoggerName = True
isAutoClearOutdatedLogs = False
```

- `isOutputLogsInConsole`: 是否在控制台输出日志
- `isOutputFunctionLoggerName`: 是否在日志中显示调用函数名称
- `isAutoClearOutdatedLogs`: 是否自动清理过期日志

### 高级使用

```python
from SHRLogCore import SHRLogCore

# 创建日志核心实例
logger = SHRLogCore()

# 在不同函数中使用
def function_a():
    logger.add_log('INFO', '在函数A中记录日志')

def function_b():
    logger.add_log('WARNING', '在函数B中记录警告')

function_a()
function_b()
```

## 日志级别

SHRLogCore支持以下日志级别：

- `DEBUG` - 调试信息（绿色）
- `INFO` - 一般信息（蓝色）
- `WARNING` - 警告信息（黄色）
- `ERROR` - 错误信息（红色）
- `CRITICAL` - 严重错误（品红色）

## 项目结构

```
SHICTHRS_LogCore/
├── config/
│   └── SHRLogCoreConfigSettings.ini  # 配置文件
├── log/                              # 日志文件目录（自动创建）
├── src/
│   ├── SHRLogCore.py                 # 核心模块
│   └── utils/                        # 工具模块
│       ├── config/
│       │   ├── SHRLogCore_readConfigFile.py
│       │   └── SHRLogCore_writeConfigFile.py
│       ├── time/
│       │   └── SHRLogCore_pytzTimeSynchronizer.py
│       └── hash/
│           └── SHRLogCore_getHashCode.py
└── README.md                         # 本文件
```

## 许可证

本项目采用GPL-3.0许可证。详见[LICENSE](LICENSE)文件。

## 作者

SHICTHRS-JNTMTMTM

## 版权

© 2025-2026 SHICTHRS, Std. All rights reserved.

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 更新日志

### v1.0.0
- 初始版本发布
- 基本日志记录功能
- 配置文件支持
- 彩色控制台输出
- 自动日志文件管理