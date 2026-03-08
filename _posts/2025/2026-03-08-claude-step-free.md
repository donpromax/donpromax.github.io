---
layout:     post
title:      "Claude Code 接入 OpenRouter 免费模型 Step-3.5-Flash 配置指南"
subtitle:   "用 Anthropic-compatible 接口低成本体验 AI 编程助手"
date:       2026-03-08 12:00:00
author:     "donpromax"
header-style: text
header-img: "img/2025/claude-step/cover-openrouter-step.svg"
header-mask: 0.38
catalog: true
tags:
    - 人工智能
    - Claude
    - OpenRouter
    - 免费模型
---

# 前言

Claude Code 是 Anthropic 官方推出的命令行 AI 编程助手。默认情况下，它更适合直接连接 Anthropic 官方服务；如果你只是想先低成本体验，也可以通过 **OpenRouter** 接入第三方模型。本文以 **Step-3.5-Flash:free** 为例，演示如何完成基础配置，并说明这种方案的适用场景与限制。

## 为什么选择这个方案？

- 💰 **在免费额度内可零成本体验**：适合先上手 Claude Code 的工作流
- ⚡ **响应速度快**：Step-3.5-Flash 属于偏轻量、偏高吞吐的模型
- 🔧 **配置简单**：只需要补充几项环境变量
- 🎯 **接入门槛低**：可通过 Anthropic-compatible 接口接入 Claude Code

---

# 核心概念介绍

## 什么是 Claude 与 Claude Code？

**Claude** 是 Anthropic 开发的大语言模型系列，以推理、代码理解和生成能力见长。**Claude Code** 则是它的官方命令行工具，让你可以在终端里直接完成代码审查、修改建议、补丁生成、Bug 排查等开发任务。

Claude 系列模型通常具备以下特点：
- 较长的上下文窗口（具体上限因型号而异）
- 较强的代码理解和生成能力
- 重视安全性与对齐训练
- 适合多语言、多文件场景下的开发协作

## 什么是 OpenRouter？

**OpenRouter**（[https://openrouter.ai](https://openrouter.ai)）是一个模型聚合平台，它可以把不同厂商的模型统一到同一套调用方式下。

- 🌐 统一 API 接口：一次接入，可切换不同 provider 的模型
- 📊 模型对比功能：便于比较价格、性能和可用性
- 💳 集中管理 API Key 与计费
- 🔄 支持数百个模型：包括 Claude、GPT、Gemini、Step 等

你可以把 OpenRouter 理解为一个统一网关：不必分别对接多个模型厂商，就能在一个入口里切换不同模型。

## 什么是 Step-3.5-Flash:free？

`stepfun/step-3.5-flash:free` 是 OpenRouter 上的免费模型标识，对应 StepFun（阶跃星辰）的 Step 3.5 Flash 免费变体。

**Step-3.5-Flash:free** 可以先这样理解：

| 项目 | 说明 |
|------|------|
| **模型 ID** | `stepfun/step-3.5-flash:free` |
| **接入平台** | OpenRouter |
| **上下文长度** | 256K（以 OpenRouter 当前模型页为准） |
| **价格** | 免费变体，按 OpenRouter 当前页面显示为 `$0/M` 输入与输出 |
| **架构说明** | OpenRouter 页面显示其为 MoE 架构，总参数约 196B、激活参数约 11B |
| **适用场景** | 日常问答、代码生成、轻量推理、基础编程辅助 |
| **注意事项** | 免费变体的可用性、排队情况与限额可能随时调整 |

Step 系列覆盖文本、推理、代码等多种能力；但具体模态支持、工具调用表现和稳定性仍建议以 OpenRouter 当前模型页与实测效果为准。

---

# 配置步骤

## 步骤 1：安装 Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

这会在你的系统全局安装 `claude` 命令。

---

## 步骤 2：配置环境变量

编辑你的 shell 配置文件（这里以 zsh 的 `.zshrc` 为例），追加以下内容：

```bash
cat <<'EOF' >> ~/.zshrc
export OPENROUTER_API_KEY="sk-or-v1-你的密钥"
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_MODEL="stepfun/step-3.5-flash:free"
EOF
```

**参数说明：**

| 变量名 | 值 | 作用 |
|--------|-----|------|
| `ANTHROPIC_BASE_URL` | `https://openrouter.ai/api` | 将请求发送到 OpenRouter 的 Anthropic-compatible 接口 |
| `OPENROUTER_API_KEY` | `sk-or-v1-xxx` | 你的 OpenRouter API Key |
| `ANTHROPIC_AUTH_TOKEN` | `$OPENROUTER_API_KEY` | 认证令牌，复用 OpenRouter Key |
| `ANTHROPIC_API_KEY` | `""` | 显式留空，避免 Claude Code 优先走官方认证 |
| `ANTHROPIC_MODEL` | `stepfun/step-3.5-flash:free` | 指定默认模型 |

如果你之前已经登录过 Anthropic 官方账号，环境变量通常仍会生效；但如果行为异常，建议进入 `claude` 后先执行一次 `/logout`，再重新打开终端测试。

---

## 步骤 3：获取 OpenRouter API Key

1. 访问 [OpenRouter.ai](https://openrouter.ai)
2. 注册或登录账号
3. 点击右上角头像 → **Keys**
4. 创建新的 API Key（格式以 `sk-or-v1-` 开头）
5. 复制并替换上面配置中的 `sk-or-v1-你的密钥`

![OpenRouter Keys 页面示意图](/img/2025/claude-step/示例截图.png)

---

## 步骤 4：重载配置

```bash
source ~/.zshrc
```

---

## 步骤 5：验证配置

Claude Code 默认会进入交互模式；如果你只是想快速跑一条命令，建议加上 `-p/--print`：

```bash
claude -p "你好，请用中文做一个一句话自我介绍。"
```

如果这条命令能正常返回，说明基础接入大概率已经打通。接着你还可以做两步确认：

1. 运行 `claude` 进入交互界面
2. 执行 `/status` 查看当前模型与账户接入状态

如果你希望进一步确认请求是否真的走到了 OpenRouter，也可以去 OpenRouter 后台查看请求记录和命中模型。

---

# 使用示例

先提醒一句：下面这些一行命令都加了 `-p`，这样 Claude Code 会直接输出结果并退出，更适合脚本化和快速验证。

## 代码审查

```bash
claude -p "请审查标准输入中的 Python 代码，指出潜在性能问题，并给出优化后的版本。" < your_file.py
```

## Bug 修复

```bash
claude -p "请检查当前目录下的 your_file.py，找出 bug，解释原因，并给出修复建议。"
```

## 生成测试

```bash
claude -p "请为当前目录中的函数补一组 pytest 单元测试，覆盖正常输入、边界条件和异常情况。"
```

## 解释代码

```bash
claude -p "请解释标准输入中的这段代码的整体逻辑、关键分支和潜在风险。" < your_file.py
```

---

# 注意事项

## ⚠️ 免费模型限制

`Step-3.5-Flash:free` 虽然是免费变体，但 OpenRouter 对 `:free` 模型有明确限制。**截至 2026-03-08**，官方文档写明：

- **每分钟限制**：最多 20 次请求
- **每日限制**：未购买满 10 美元额度时，通常为每天 50 次 `:free` 请求
- **提升上限**：累计购买至少 10 美元额度后，每日上限可提升到 1000 次
- **可用性波动**：免费模型可能排队、降速，甚至临时下线

这些规则可能随时调整，建议以 OpenRouter 的 Limits 页面为准。

## 常见问题排查

**问题：报错 `Invalid API Key`**
- 检查 `OPENROUTER_API_KEY` 是否粘贴完整，是否误带空格或换行
- 确认你已经执行过 `source ~/.zshrc`
- 用 `echo $ANTHROPIC_BASE_URL` 和 `echo $ANTHROPIC_MODEL` 检查环境变量是否生效
- 如果之前登录过官方账号，进入 `claude` 后执行 `/logout` 再重试

**问题：出现 `402`、余额不足或额度异常**
- 即使是免费模型，如果账户处于负余额，也可能被 OpenRouter 拒绝请求
- 这类问题通常不是 `Invalid API Key`，而是额度状态异常
- 可登录 OpenRouter 后台检查余额，必要时补充少量额度使账户恢复为非负

**问题：请求超时或排队很久**
- 免费模型在高峰期可能排队，稍后再试
- 检查本地网络是否稳定
- 如果频繁遇到超时，可切换到其他免费模型，或改用付费模型

**问题：回复质量不理想**
- Step Flash 更适合轻量任务，复杂工程问题未必稳定
- 可以尝试把提示词写得更具体，例如补充目标、限制条件和输出格式
- 也可以切换到 OpenRouter 上更强的其他模型进行对比

---

# 总结

通过 OpenRouter，我们可以：

✅ 在免费额度内低成本体验 Claude Code  
✅ 快速接入 `stepfun/step-3.5-flash:free`  
✅ 以较低门槛体验终端里的 AI 编程助手工作流

这个方案特别适合：
- 学生和个人开发者
- 想先体验 Claude Code 工作流的用户
- 对极致稳定性和最强模型暂时没有刚需的日常编码场景

如果后续免费额度不够，大多数情况下只需要替换 `ANTHROPIC_MODEL` 的值，就能切换到 OpenRouter 上的其他模型；但如果你改用不同 provider 或更复杂的工具调用场景，仍建议重新验证稳定性和效果。

---

# 参考资源

- [OpenRouter 官网](https://openrouter.ai)
- [StepFun 官网](https://stepfun.com)
- [Claude Code 模型配置文档](https://code.claude.com/docs/en/model-config)
- [OpenRouter Anthropic-compatible 接入说明](https://openrouter.ai/docs/guides/community/anthropic-agent-sdk)
- [OpenRouter Limits 文档](https://openrouter.ai/docs/api/reference/limits)
- [OpenRouter 模型列表](https://openrouter.ai/models)
