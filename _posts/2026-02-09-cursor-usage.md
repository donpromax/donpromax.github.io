---
layout: post
title: "cursor的使用"
subtitle: "Cursor IDE 安装、CLI 与 IDE 实战"
date: 2026-02-09 10:00:00
author: "donpromax"
header-style: text
catalog: true
tags: [开发工具, Cursor, IDE, CLI]
---

Cursor 是一款基于 VS Code 的 AI IDE，主打“写代码 + 读代码 + 改代码”的一体化体验。它保留了 VS Code 的扩展生态与熟悉的操作方式，同时内置了 AI Chat、自动补全与多文件改写能力，适合日常编码、重构与文档/代码审查场景。

本文从三个部分展开：**IDE 安装**、**CLI 使用**、**IDE 使用技巧**，帮助你快速上手。

## 一、Cursor IDE 安装

### 1. 获取安装包

前往 Cursor 官网下载对应系统的安装包（macOS / Windows / Linux），按提示安装即可。安装后首次启动通常需要登录账号并进行基础配置（例如主题、字体、快捷键方案等）。

### 2. macOS

1. 下载 `.dmg` 安装包并拖拽到 Applications。
2. 首次启动若提示安全限制，在“系统设置 -> 隐私与安全性”中允许打开。

### 3. Windows

1. 运行安装器并完成安装。
2. 建议勾选“添加到 PATH”（或安装后手动添加到 PATH），方便在终端里使用 `cursor` 命令。

### 4. Linux

1. 下载安装包（常见为 `.deb` 或 AppImage）。
2. AppImage 需要赋予执行权限：`chmod +x Cursor.AppImage`。
3. 若希望终端可直接使用 `cursor` 命令，记得把可执行文件加入 PATH。

---

## 二、Cursor CLI 使用（基于官方文档）

Cursor CLI 在终端中以 **`agent` 命令**运行，支持交互式会话、脚本化执行以及会话管理。下面内容参考官方文档：<https://cursor.com/docs/cli/overview>。

### 1. 安装与启动

```bash
# Install (macOS, Linux, WSL)
curl https://cursor.com/install -fsS | bash

# Install (Windows PowerShell)
irm 'https://cursor.com/install?win32=true' | iex

# Run interactive session
agent
```

### 2. 交互模式（Interactive mode）

交互模式适合边聊边改：描述目标、审阅改动、确认执行命令。

```bash
# Start interactive session
agent

# Start with initial prompt
agent "refactor the auth module to use JWT tokens"
```

### 3. 模式（Modes）

CLI 支持与编辑器一致的模式，可通过 **斜杠命令**、**快捷键** 或 `--mode` 切换：

- **Plan**：`Shift+Tab` / `/plan` / `--mode=plan`
- **Ask**：`/ask` / `--mode=ask`

### 4. 非交互模式（Print mode）

用于脚本、CI 或自动化场景，直接输出结果：

```bash
# Run with specific prompt and model
agent -p "find and fix performance issues" --model "gpt-5.2"

# Use with git changes included for review
agent -p "review these changes for security issues" --output-format text
```

### 5. Cloud Agent handoff

将对话转交到 Cloud Agent 后台继续执行，在消息前加 `&`：

```bash
# Send a task to Cloud Agent
& refactor the auth module and add comprehensive tests
```

任务可在 <https://cursor.com/agents> 继续查看与接力。

### 6. Sessions

```bash
# List all previous chats
agent ls

# Resume latest conversation
agent resume

# Resume specific conversation
agent --resume="chat-id-here"
```

### 7. Sandbox controls

交互模式中使用 `/sandbox` 进入设置菜单，可切换沙箱模式、控制网络访问，设置会持久化。

### 8. Max mode

对支持的模型使用 `/max-mode [on|off]` 切换 Max 模式。

### 9. Sudo password prompting

当命令需要 `sudo` 时，CLI 会弹出安全的密码提示，密码经由安全通道直接传给 `sudo`，模型不可见。

---

## 三、Cursor IDE 使用要点

### 1. 打开项目与索引

- **File -> Open Folder** 打开项目目录。
- Cursor 会对项目建立索引，便于后续对代码库进行理解与检索。
- 建议第一次打开项目时耐心等待索引完成，后续 AI 问答更准确。

### 2. AI Chat：阅读与理解代码

常见用法：

- “请解释这个模块的职责和数据流”
- “这段代码有没有潜在的边界情况？”
- “请给出可读性更好的实现方案”

**提示**：问题越具体，回答越准确；需要跨文件时，尽量明确文件名或路径。

### 3. Inline Edit：就地改写

选中一段代码后发起内联编辑（快捷键与 UI 入口以本地设置为准），可以完成：

- 小范围重构
- 命名优化
- 注释补全
- 逻辑合并与拆分

修改完成后务必**审查 diff**，尤其是涉及边界条件与异常处理的部分。

### 4. 多文件修改（适合重构与需求迭代）

当需求涉及多个文件时，可以让 Cursor 一次性给出修改方案，再逐个审查并应用。  
建议指明约束条件，例如：

- “不要改动外部 API”
- “保持现有测试通过”
- “仅重构，不新增依赖”

### 5. 代码补全与生成

在编辑器中输入注释或函数签名时，Cursor 会给出补全建议。  
对于模板化代码（比如 CRUD、接口封装、配置文件）效果尤佳。

---

## 四、实践建议

1. **先问清楚，再让它改**  
   先让 Cursor 解释或给出方案，再执行改动，能显著降低误改风险。

2. **改完一定要跑测试**  
   AI 修改后的代码仍需测试验证，尤其是业务逻辑与边界条件。

3. **把输出当作“草稿”**  
   Cursor 很擅长生成初稿，但最终质量仍需人工审阅与微调。

4. **避免上传敏感信息**  
   与任何云端模型交互时，请不要粘贴密钥、隐私数据或商业机密。

---

## 总结

Cursor 既保留了 VS Code 的高效开发体验，又融合了 AI 辅助能力。  
从 **IDE 安装** 到 **CLI 与 IDE 使用** 的完整链路打通后，你可以更快完成阅读、修改与交付。

如果你还没试过，不妨从 `cursor .` 打开一个项目开始。
