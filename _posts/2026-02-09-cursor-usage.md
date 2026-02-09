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

Cursor 是面向开发的 AI 编辑器。官方文档的核心概念包括 **Tab**、**Agent** 与 **Chat**，并延伸到 **Custom instructions**、**Semantic search**、**MCP**、**Context** 与 **Models** 等能力（下文会逐一说明）。

本文从三个部分展开：**IDE 安装**、**CLI 使用**、**Concepts + Quickstart**，帮助你快速上手。

## 一、Cursor IDE 安装（参考官方文档）

官方文档的 Get started 提供了下载入口，安装步骤很简单：

1. 访问官方文档的 Quickstart：<https://cursor.com/docs/get-started/quickstart>  
2. 点击 **Download Cursor** 下载对应系统的安装包。
3. 按系统提示完成安装并启动 Cursor。

Quickstart 强调从 **Agent** 开始学习：它会帮助你**规划任务、管理上下文并迭代代码**。

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

## 三、核心概念（Concepts，官方文档）

以下内容来自官方概念页：<https://cursor.com/docs/get-started/concepts>。

### 1. Tab

Tab 是**多行代码补全**能力，会基于你当前代码与最近更改给出建议，按 **Tab** 接受。

### 2. Agent

Agent 是能**跨多个文件读取与修改代码**的 AI。你用自然语言描述修改需求，Agent 会执行变更。

### 3. Chat

Chat 是 AI 对话界面，支持**多标签页、对话历史、检查点与导出**功能。

### 4. Custom instructions

自定义指令用于**定义 AI 行为**，包括编码规范、框架偏好与项目约定。

### 5. Semantic search

语义搜索支持**按含义找代码**，可用自然语言检索并获得上下文建议。

### 6. MCP（Model Context Protocol）

MCP 用于**集成外部工具**，可连接数据库、API 与文档源。

### 7. Context

Context 指模型生成时看到的信息，包括**文件、符号与对话历史**。

### 8. Models

用于代码生成的不同模型具有不同的**速度与能力特征**。

## 四、Quickstart 工作流（官方建议）

以下内容来自 Quickstart：<https://cursor.com/docs/get-started/quickstart>。

### 1. Start with Agent（从 Agent 开始）

Quickstart 建议从 Agent 开始：它会帮助你**规划任务、管理上下文并迭代代码**。  
Agent 会探索代码库、读取相关文件并解释架构，这是理解陌生代码的高效方式。

### 2. Plan before building（先规划再编码）

文档强调：**最有影响力的改变是“先规划再编码”**。建议步骤：

1. 先调研代码库，找到相关文件  
2. 对需求提出澄清问题  
3. 制定详细实现计划  
4. 在开始编码前等待确认

### 3. Let Agent find context（让 Agent 自动找上下文）

你不需要在提示里手动标注每个文件。  
Agent 有强大的搜索能力，能按需拉取上下文。比如你问 “authentication flow”，即使提示中没有文件名，Agent 也能通过搜索找到相关文件。

### 4. Write specific prompts（提示要具体）

Agent 的成功率会随着**更具体的指令**显著提升。  
建议明确目标、引用现有模式，并描述期望结果。

### 5. Know when to start fresh（何时重新开对话）

长对话可能让 Agent 失焦。文档给出的建议是：

**Start a new conversation when（建议新开对话）：**
- 任务或功能切换时  
- Agent 变得困惑或重复犯错时  
- 一个逻辑工作单元已完成时

**Continue the conversation when（继续当前对话）：**
- 仍在迭代同一功能  
- Agent 需要之前讨论的上下文  
- 正在调试它刚刚构建的内容

### 6. Review and iterate（审查与迭代）

AI 生成的代码**看起来正确但可能暗含错误**。文档提醒要认真查看 diff，Agent 越快，审查越重要。

### 7. Provide verifiable goals（给出可验证目标）

Agent 在**有清晰可验证目标**时表现更好。  
推荐流程：先让 Agent 写测试并确认失败，再让它实现代码直至通过测试。

## 总结

Cursor 的核心能力围绕 **Tab、Agent、Chat** 等概念展开，并通过 **Quickstart** 给出清晰的工作流建议。  
从 **IDE 安装** 到 **CLI（agent）** 与 **Concepts/Quickstart** 的完整链路打通后，你可以更高效地理解与修改代码。

如果你还没试过，不妨从官方 Quickstart 开始。
