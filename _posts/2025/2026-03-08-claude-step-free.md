---
layout:     post
title:      "Claude Code 使用 Step-3.5-Flash 免费模型配置指南"
subtitle:   "通过 OpenRouter 实现零成本 AI 编程助手"
date:       2026-03-08 12:00:00
author:     "donpromax"
header-style: text
catalog: true
tags:
    - 人工智能
    - Claude
    - OpenRouter
    - 免费模型
---

# 前言

Claude Code 是 Anthropic 官方推出的命令行 AI 编程助手,但默认配置需要付费的 Claude API。本篇文章分享如何通过 **OpenRouter** 平台,配置使用 **Step-3.5-Flash:free** 免费模型,让你的 Claude Code 实现零成本运行。

## 为什么选择这个方案?

- 💰 **完全免费** - Step 模型通过 OpenRouter 提供免费额度
- ⚡ **响应速度快** - Step-3.5-Flash 是轻量级模型,响应迅速
- 🔧 **配置简单** - 仅需修改几个环境变量
- 🎯 **兼容性好** - 完全兼容 Claude Code 的 API 接口

---

# 核心概念介绍

## 什么是 Claude?

**Claude** 是 Anthropic 公司开发的大语言模型系列,以强大的推理能力、代码理解和生成能力著称。Claude Code 是其官方命令行工具,让你可以在终端中直接与 Claude 对话,获得代码补丁、bug 修复、代码审查等 AI 辅助编程功能。

Claude 模型的特点:
- 超长的 200K 上下文窗口
- 优秀的代码理解和生成能力
- 重视安全性和对齐性训练
- 支持多种编程语言

## 什么是 OpenRouter?

**OpenRouter** ([https://openrouter.ai](https://openrouter.ai)) 是一个 AI 模型聚合平台,它:

- 🌐 统一 API 接口,一次调用可切换到不同 provider 的模型
- 📊 模型对比功能,可以帮助你选择合适的模型
- 💳 集中管理 API keys 和计费
- 🔄 支持 100+ 模型,包括 Claude、GPT、Gemini、Step 等

OpenRouter 就像一个 AI 模型的"应用商店",你无需在每个 provider 单独注册和充值,通过 OpenRouter 一个入口就能使用各种模型。

## 什么是 Step-3.5-Flash:free?

**Step** 是由 **StepFun(阶跃星辰)** 开发的多模态大语言模型,支持文字、图片等多种输入形式。

**Step-3.5-Flash:free** 特性:

| 特性 | 说明 |
|------|------|
| **模型类型** | Step-3.5-Flash 是 Step 系列的轻量版 |
| **上下文长度** | 支持 16K tokens |
| **能力** | 代码生成、数学推理、多轮对话 |
| **多模态** | 支持文本和图像理解 |
| **价格** | **免费** (通过 OpenRouter) |
| **速率限制** | 有一定免费额度限制 |

这个模型虽然名为"Flash"(轻量),但在日常编程任务中表现优秀,足够满足大部分代码辅助需求。

---

# 配置步骤

## 步骤 1: 安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

这会在你的系统全局安装 `claude` 命令。

---

## 步骤 2: 配置环境变量

编辑你的 shell 配置文件(这里是 zsh 的 `.zshrc`),添加以下内容:

```bash
sudo tee -a ~/.zshrc > /dev/null <<'EOF'
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export OPENROUTER_API_KEY="sk-or-v1-你的密钥"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_MODEL="stepfun/step-3.5-flash:free"
EOF
```

**参数说明:**

| 变量名 | 值 | 作用 |
|--------|-----|------|
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` | 将请求发送到 OpenRouter 而非 Anthropic 官方 |
| `OPENROUTER_API_KEY` | `sk-or-v1-xxx` | 你的 OpenRouter API Key |
| `ANTHROPIC_AUTH_TOKEN` | `$OPENROUTER_API_KEY` | 认证令牌(复用 OpenRouter key) |
| `ANTHROPIC_API_KEY` | `""` | 留空,因为我们不使用 Anthropic 官方 |
| `ANTHROPIC_MODEL` | `stepfun/step-3.5-flash:free` | 指定使用 Step 免费模型 |

---

## 步骤 3: 获取 OpenRouter API Key

1. 访问 [OpenRouter.ai](https://openrouter.ai)
2. 注册/登录账号
3. 在右上角点击你的头像 → **Keys**
4. 创建新的 API Key(格式以 `sk-or-v1-` 开头)
5. 复制并替换上面配置中的 `sk-or-v1-你的密钥`

![](/img/2025/claude-step/示例截图.png)

---

## 步骤 4: 重载配置

```bash
source ~/.zshrc
```

---

## 步骤 5: 验证配置

直接运行 `claude` 命令:

```bash
claude "你好,请用中文回答"
```

如果配置正确,你应该看到 Step 模型的回复,而不是 Anthopic Claude 的回复。

---

# 使用示例

## 代码审查

```bash
claude "请审查这个 Python 函数是否有性能优化空间" < your_file.py
```

## Bug 修复

```bash
claude "这段代码有一个 bug,请帮我修复" --file your_file.py
```

## 生成测试

```bash
claude "为这个函数生成单元测试"
```

## 解释代码

```bash
claude "请解释这段代码的逻辑"
```

---

# 注意事项

## ⚠️ 免费模型限制

Step-3.5-Flash:free 虽然是免费的,但 OpenRouter 可能会有以下限制:

- **每日请求次数限制** (具体额度看 OpenRouter 当前政策)
- **速率限制** - 短时间内多次请求可能被限流
- **可用性** - 免费模型可能随时调整或下线

## 模型选择建议

如果需要更强大的性能,可以考虑 OpenRouter 上的付费模型:

| 模型 | 适合场景 | 成本(每 1M tokens) |
|------|---------|-------------------|
| Claude 3.5 Sonnet | 复杂推理、代码生成 | ~$0.1-$0.3 |
| GPT-4o | 多模态任务 | ~$0.05-$0.15 |
| Step-3.5-Turbo | 平衡型 | ~$0.01-$0.05 |

##  Troubleshooting

**问题: 报错 "Invalid API Key"**
- 检查 `OPENROUTER_API_KEY` 是否正确
- 确认 Key 有足够的余额/额度

**问题: 请求超时**
- 免费模型可能排队,稍后再试
- 检查网络连接

**问题: 回复质量不佳**
- Step Flash 是轻量模型,复杂任务可能不如 Claude 3.5
- 可以尝试在 OpenRouter 选择其他模型

---

# 总结

通过 OpenRouter 平台,我们可以:

✅ 零成本使用 Step-3.5-Flash 免费模型
✅ 快速配置 Claude Code 环境
✅ 享受 AI 编程助手的便利

这个配置方案特别适合:
- 学生和个人开发者
- 想体验 Claude Code 功能但不想付费的用户
- 对性能要求不是特别极端的日常编码任务

未来如果 free 额度不足,也可以平滑切换到 OpenRouter 上的其他付费模型,无需改变任何配置,只需更换 `ANTHROPIC_MODEL` 的值即可。

---

# 参考资源

- [OpenRouter 官网](https://openrouter.ai)
- [StepFun 官网](https://stepfun.com)
- [Claude Code 文档](https://docs.anthropic.com/en/docs/claude-code)
- [OpenRouter 模型列表](https://openrouter.ai/models)
