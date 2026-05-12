<div align="center">

# 🛠️ DevUtils-CLI

**A lightweight, zero-dependency Python CLI toolbox for developers**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg)]()

[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

</div>

---

<a name="english"></a>
## 🇺🇸 English

### 🎉 Project Introduction

**DevUtils-CLI** is a lightweight, zero-dependency Python CLI toolbox designed specifically for developers. It provides 10+ practical command-line tools covering common development scenarios such as data format conversion, security encryption, text processing, and more.

**Core Value Proposition:**
- ⚡ **Zero Dependencies** - Uses only Python standard library, no installation hassles
- 🔧 **Ready to Use** - Single-file executable, copy and run
- 🚀 **Lightweight & Fast** - Startup in milliseconds, instant response
- 🌐 **Cross-Platform** - Runs on Linux, macOS, and Windows
- 📦 **Rich Features** - 10+ practical tools, continuously updated

**Inspiration Sources:**
Inspired by excellent projects like [it-tools](https://github.com/CorentinTh/it-tools) (33.6k⭐), [sysbox](https://github.com/skx/sysbox), and [LoggiFly](https://github.com/clemcer/loggifly), but completely independently developed with unique differentiation.

### ✨ Core Features

| Tool | Icon | Description |
|------|------|-------------|
| **JSON Formatter** | 🔧 | Format and validate JSON data |
| **Base64 Codec** | 🔐 | Base64 encoding and decoding |
| **Password Generator** | 🔑 | Generate secure random passwords |
| **UUID Generator** | 🆔 | Generate UUID v1/v3/v4/v5 |
| **Hash Generator** | #️⃣ | MD5/SHA1/SHA256/SHA512 hashing |
| **Timestamp Converter** | ⏰ | Unix timestamp and date conversion |
| **URL Codec** | 🔗 | URL encoding and decoding |
| **Case Converter** | 📝 | camelCase/PascalCase/snake_case/kebab-case |
| **Lorem Ipsum** | 📄 | Generate placeholder text |
| **QR Generator** | 📱 | ASCII QR code generation |

### 🚀 Quick Start

#### Requirements
- **Python 3.7** or higher
- No external dependencies required

#### Installation

**Method 1: Direct Download (Recommended)**
```bash
# Download the tool
curl -O https://raw.githubusercontent.com/gitstq/devutils-cli/main/devutils.py

# Make it executable
chmod +x devutils.py

# Run directly
./devutils.py --help
```

**Method 2: Install via pip**
```bash
pip install devutils-cli
```

**Method 3: Clone Repository**
```bash
git clone https://github.com/gitstq/devutils-cli.git
cd devutils-cli
python3 devutils.py --help
```

#### Quick Usage Examples

```bash
# Format JSON
devutils json --input '{"name":"test","version":"1.0.0"}'

# Generate a 20-character password with symbols
devutils password --length 20 --symbols

# Generate 5 UUIDs
devutils uuid --count 5

# Generate all hash types for a string
devutils hash --input "hello world" --all

# View current timestamp
devutils timestamp

# Base64 encode
devutils base64 --input "Hello World"

# Convert to camelCase
devutils case --input "hello world" --camel

# Generate 3 paragraphs of Lorem Ipsum
devutils lorem --paragraphs 3

# Generate ASCII QR code
devutils qr --input "https://example.com"
```

### 📖 Detailed Usage Guide

#### 🔧 JSON Formatter
```bash
# Format JSON
devutils json --input '{"a":1,"b":2}'

# Minify JSON
devutils json --input '{"a": 1, "b": 2}' --minify

# Interactive mode
devutils json
```

#### 🔐 Base64 Codec
```bash
# Encode
devutils base64 --input "Hello World"

# Decode
devutils base64 --input "SGVsbG8gV29ybGQ=" --decode
```

#### 🔑 Password Generator
```bash
# Generate 16-character password (default)
devutils password

# Generate 32-character password with symbols
devutils password --length 32 --symbols

# Generate password without uppercase
devutils password --no-upper
```

#### 🆔 UUID Generator
```bash
# Generate one UUID v4 (default)
devutils uuid

# Generate 10 UUIDs
devutils uuid --count 10

# Generate UUID v1
devutils uuid --version 1

# Output uppercase
devutils uuid --uppercase
```

#### #️⃣ Hash Generator
```bash
# Generate SHA256 hash (default)
devutils hash --input "text"

# Generate specified algorithm
devutils hash --input "text" --algorithm md5

# Generate all hash types
devutils hash --input "text" --all
```

#### ⏰ Timestamp Converter
```bash
# View current time
devutils timestamp

# Timestamp to date
devutils timestamp --input "1700000000" --to-date

# Date to timestamp
devutils timestamp --input "2024-01-01 00:00:00" --to-timestamp
```

### 💡 Design Philosophy & Iteration Plan

**Design Philosophy:**
1. **Simplicity First** - Each tool focuses on a single function
2. **Zero Dependencies** - Uses only Python standard library
3. **Developer-Centric** - Solves real development pain points
4. **Terminal-Native** - Optimized for command-line workflows

**Technology Stack Selection:**
- **Language:** Python 3.7+ (wide compatibility)
- **Architecture:** Modular design, easy to extend
- **Interface:** argparse (standard library, no dependencies)

**Iteration Plan:**
- [ ] Add more encoding/decoding tools (Hex, HTML entities, etc.)
- [ ] Add data conversion tools (CSV/JSON/YAML)
- [ ] Add network tools (IP lookup, port scanner)
- [ ] Add file processing tools (checksum, file search)
- [ ] Support plugin system
- [ ] Add configuration file support

### 📦 Packaging & Deployment Guide

**Local Build:**
```bash
# Build wheel package
python3 setup.py bdist_wheel

# Build source distribution
python3 setup.py sdist
```

**Publish to PyPI:**
```bash
# Install build tools
pip install twine build

# Build
python -m build

# Upload
twine upload dist/*
```

**Create Standalone Executable:**
```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile devutils.py --name devutils

# Output in dist/ directory
```

### 🤝 Contributing Guide

We welcome community contributions! Please follow these guidelines:

1. **Fork** the repository
2. Create a **feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'feat: add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. Open a **Pull Request**

**Commit Message Convention:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `refactor:` Code refactoring
- `test:` Test-related
- `chore:` Build/tooling changes

### 📄 License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

<a name="简体中文"></a>
## 🇨🇳 简体中文

### 🎉 项目介绍

**DevUtils-CLI** 是一个轻量级、零依赖的 Python 命令行工具箱，专为开发者设计。它提供了 10+ 个实用的命令行工具，涵盖数据格式转换、安全加密、文本处理等常见开发场景。

**核心价值主张：**
- ⚡ **零依赖** - 仅使用 Python 标准库，无需安装烦恼
- 🔧 **开箱即用** - 单文件可执行，复制即用
- 🚀 **轻量快速** - 毫秒级启动，即时响应
- 🌐 **跨平台** - 支持 Linux、macOS 和 Windows
- 📦 **功能丰富** - 10+ 实用工具，持续更新

**灵感来源：**
受 [it-tools](https://github.com/CorentinTh/it-tools) (33.6k⭐)、[sysbox](https://github.com/skx/sysbox)、[LoggiFly](https://github.com/clemcer/loggifly) 等优秀项目启发，但完全独立开发，具有独特差异化。

### ✨ 核心特性

| 工具 | 图标 | 描述 |
|------|------|------|
| **JSON 格式化** | 🔧 | 格式化和验证 JSON 数据 |
| **Base64 编解码** | 🔐 | Base64 编码和解码 |
| **密码生成器** | 🔑 | 生成安全的随机密码 |
| **UUID 生成器** | 🆔 | 生成 UUID v1/v3/v4/v5 |
| **哈希生成器** | #️⃣ | MD5/SHA1/SHA256/SHA512 哈希 |
| **时间戳转换器** | ⏰ | Unix 时间戳和日期转换 |
| **URL 编解码** | 🔗 | URL 编码和解码 |
| **大小写转换** | 📝 | camelCase/PascalCase/snake_case/kebab-case |
| **Lorem Ipsum** | 📄 | 生成占位文本 |
| **二维码生成** | 📱 | ASCII 二维码生成 |

### 🚀 快速开始

#### 环境要求
- **Python 3.7** 或更高版本
- 无需外部依赖

#### 安装方法

**方式一：直接下载（推荐）**
```bash
# 下载工具
curl -O https://raw.githubusercontent.com/gitstq/devutils-cli/main/devutils.py

# 添加执行权限
chmod +x devutils.py

# 直接运行
./devutils.py --help
```

**方式二：通过 pip 安装**
```bash
pip install devutils-cli
```

**方式三：克隆仓库**
```bash
git clone https://github.com/gitstq/devutils-cli.git
cd devutils-cli
python3 devutils.py --help
```

#### 快速使用示例

```bash
# 格式化 JSON
devutils json --input '{"name":"test","version":"1.0.0"}'

# 生成 20 位带符号的密码
devutils password --length 20 --symbols

# 生成 5 个 UUID
devutils uuid --count 5

# 为字符串生成所有哈希类型
devutils hash --input "hello world" --all

# 查看当前时间戳
devutils timestamp

# Base64 编码
devutils base64 --input "Hello World"

# 转换为 camelCase
devutils case --input "hello world" --camel

# 生成 3 段 Lorem Ipsum
devutils lorem --paragraphs 3

# 生成 ASCII 二维码
devutils qr --input "https://example.com"
```

### 📖 详细使用指南

#### 🔧 JSON 格式化器
```bash
# 格式化 JSON
devutils json --input '{"a":1,"b":2}'

# 压缩 JSON
devutils json --input '{"a": 1, "b": 2}' --minify

# 交互模式
devutils json
```

#### 🔐 Base64 编解码
```bash
# 编码
devutils base64 --input "Hello World"

# 解码
devutils base64 --input "SGVsbG8gV29ybGQ=" --decode
```

#### 🔑 密码生成器
```bash
# 生成 16 位密码（默认）
devutils password

# 生成 32 位带符号密码
devutils password --length 32 --symbols

# 生成不含大写字母的密码
devutils password --no-upper
```

#### 🆔 UUID 生成器
```bash
# 生成一个 UUID v4（默认）
devutils uuid

# 生成 10 个 UUID
devutils uuid --count 10

# 生成 UUID v1
devutils uuid --version 1

# 输出大写
devutils uuid --uppercase
```

#### #️⃣ 哈希生成器
```bash
# 生成 SHA256 哈希（默认）
devutils hash --input "text"

# 生成指定算法
devutils hash --input "text" --algorithm md5

# 生成所有哈希类型
devutils hash --input "text" --all
```

#### ⏰ 时间戳转换器
```bash
# 查看当前时间
devutils timestamp

# 时间戳转日期
devutils timestamp --input "1700000000" --to-date

# 日期转时间戳
devutils timestamp --input "2024-01-01 00:00:00" --to-timestamp
```

### 💡 设计思路与迭代规划

**设计理念：**
1. **简洁至上** - 每个工具专注单一功能
2. **零依赖** - 仅使用 Python 标准库
3. **开发者优先** - 解决真实开发痛点
4. **终端原生** - 针对命令行工作流优化

**技术选型：**
- **语言：** Python 3.7+（兼容性广）
- **架构：** 模块化设计，易于扩展
- **界面：** argparse（标准库，零依赖）

**迭代计划：**
- [ ] 增加更多编解码工具（Hex、HTML 实体等）
- [ ] 增加数据转换工具（CSV/JSON/YAML）
- [ ] 增加网络工具（IP 查询、端口扫描）
- [ ] 增加文件处理工具（校验和、文件搜索）
- [ ] 支持插件系统
- [ ] 增加配置文件支持

### 📦 打包与部署指南

**本地构建：**
```bash
# 构建 wheel 包
python3 setup.py bdist_wheel

# 构建源码分发
python3 setup.py sdist
```

**发布到 PyPI：**
```bash
# 安装构建工具
pip install twine build

# 构建
python -m build

# 上传
twine upload dist/*
```

**创建独立可执行文件：**
```bash
# 安装 PyInstaller
pip install pyinstaller

# 构建可执行文件
pyinstaller --onefile devutils.py --name devutils

# 输出在 dist/ 目录
```

### 🤝 贡献指南

欢迎社区贡献！请遵循以下规范：

1. **Fork** 本仓库
2. 创建**功能分支** (`git checkout -b feature/amazing-feature`)
3. **提交**更改 (`git commit -m 'feat: add amazing feature'`)
4. **推送**到分支 (`git push origin feature/amazing-feature`)
5. 发起 **Pull Request**

**提交信息规范：**
- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具变更

### 📄 开源协议

本项目采用 **MIT License** 开源协议 - 详见 [LICENSE](LICENSE) 文件。

---

<a name="繁體中文"></a>
## 🇹