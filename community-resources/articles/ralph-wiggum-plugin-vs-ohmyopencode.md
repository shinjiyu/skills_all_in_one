# Ralph Wiggum：让 AI “一直干到做完”为止（以及它在 Oh My OpenCode 里的打开方式）

关键词：opencode, claude-code, ralph-wiggum, ralph-loop, agent loop, automation

这篇文章聊一个最近在 Agent 圈子里很火的“暴力但有效”的工作法：**Ralph Wiggum**。

一句话解释：把 AI 代理从“一次性回答”升级为“**while true 迭代直到完成**”，并且给它一个**明确的完成信号**和**安全刹车**。

参考来源（可引用）：

- Anthropic 的 Claude Code 官方插件 Ralph Wiggum（说明了 “Ralph is a Bash loop”、Stop hook、`/ralph-loop` 等）：[anthropics/claude-code/plugins/ralph-wiggum](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)
- Oh My OpenCode（Sisyphus）在 README 里内置的 Ralph Loop（明确写了 Inspired by Anthropic’s Ralph Wiggum plugin、`<promise>DONE</promise>`、默认 100 次、`/cancel-ralph`、`oh-my-opencode.json` 配置）：[code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
- 一个更“工程模板化”的 OpenCode Ralph 插件（Phoenix/React/Expo + TanStack，带 `plan.md`、验证命令、commit 约定等）：[NicholasBarkolias/ralph-opencode-plugin](https://github.com/NicholasBarkolias/ralph-opencode-plugin)

## 1）Ralph Wiggum 到底解决什么问题？

如果你用过 AI 编程工具，你一定见过这种场景：

- 写了一半，模型“自我感觉良好”就停了
- 测试挂了、lint 挂了、类型错误一堆，但它不继续修
- 你不断复制粘贴错误输出，像在“人肉驱动 CI”

Ralph 的核心思想是：**把“继续迭代”变成系统默认行为，而不是靠你盯着。**

## 2）Claude Code 官方 Ralph Wiggum：Stop hook 驱动的“会话内循环”

在 Anthropic 的官方插件描述里，Ralph 被定义成一种持续循环的方法论（“Ralph is a Bash loop”），但插件把它“内置化”了：通过 **Stop hook** 拦截退出，把同一个 prompt 重新喂回去，让代理继续改文件、跑测试、再修。

典型用法（概念层面）：

- **启动循环**：`/ralph-loop "<prompt>" --completion-promise "<text>" --max-iterations <n>`
- **取消循环**：`/cancel-ralph`

关键点：

- **完成条件**：`--completion-promise` 是“精确字符串匹配”
- **安全刹车**：`--max-iterations`（强烈建议总是设置）
- **优势**：更像“把代理变成一个会反复自我纠错的工人”

## 3）Oh My OpenCode 的 Ralph Loop：把“循环能力”做成通用底座（跨语言）

Oh My OpenCode（Sisyphus）在 README 的 “Not Just for the Agents” 里，直接把 **Ralph Loop** 做成了内置能力，并且明确写了：

- 受到 Anthropic Ralph Wiggum 插件启发
- 支持所有语言
- 通过 `<promise>DONE</promise>` 判断完成
- 默认最大迭代 100 次
- 也提供 `/cancel-ralph` 退出
- 可以在 `oh-my-opencode.json` 里配置开关和默认次数

你可以把它理解成：**官方插件的“循环思想”被移植到 OpenCode 生态里，并且做成更通用的默认能力。**

## 4）ralph-opencode-plugin：把“循环”进一步固化成工程规约（适合特定技术栈）

另一个很有代表性的实现是 `ralph-opencode-plugin`：它不止是“循环”，更像是“把一个团队的工程规约塞进循环里”：

- 强约束技术栈（Phoenix + React/Expo + TanStack 生态）
- 提供 `/ralph-plan` 先产出 `plan.md`，再 `/ralph` 执行
- 提供不同方向的命令：`/ralph-phoenix`、`/ralph-react`、`/ralph-expo`、`/ralph-full`
- 内置验证命令（编译/格式化/lint/test）和 commit 规范

它的价值是：**把“循环”从方法论升级成“可复制的项目模板”。**

## 5）对比：官方 Ralph vs Oh My OpenCode Ralph Loop vs ralph-opencode-plugin

| 维度 | Claude Code 官方 Ralph Wiggum | Oh My OpenCode：Ralph Loop | ralph-opencode-plugin |
|---|---|---|---|
| 目标 | 让 Claude Code 会话内持续迭代 | 给 OpenCode 提供通用循环能力 | 给特定栈提供“带规约的循环” |
| 完成信号 | `--completion-promise` 精确匹配 | `<promise>DONE</promise>` | `RALPH_COMPLETE`（并配合 plan.md/脚本） |
| 安全刹车 | `--max-iterations` | 默认 100，可配 | 迭代次数可控，且有“BLOCKED”处理 |
| 适用范围 | Claude Code 用户 | OpenCode 用户（偏通用） | Phoenix/React/Expo/TanStack 用户 |
| 你要做的事 | 把“验收标准”写清楚 | 把“验收标准”写清楚 + 可配底座 | 直接套工程模板，按命令跑 |

## 6）怎么写 Prompt 才能让 Ralph 真正跑起来？

不管你用哪一种 Ralph，本质都一样：**把“验收标准”写成可判定的 checklist**，并明确“卡住了怎么办”。

建议最少包含：

- 明确的输出承诺（promise）
- 允许跑测试/静态检查并据此修复
- 最大迭代次数
- 卡住后要做的事：记录阻塞点、列出已尝试方案、给出替代路径

## 7）一句结论：Ralph 不是“更聪明”，是“更不容易半途而废”

这类 loop 技术最实用的地方在于：它把 AI 代理从“偶尔灵光一现”，变成“可以交给它熬夜干活的流水线”。

如果你已经在用 OpenCode，我建议优先从 Oh My OpenCode 的 Ralph Loop 体验“通用循环”，再决定要不要上更强约束的 `ralph-opencode-plugin`；如果你在 Claude Code 生态里，官方 Ralph Wiggum 插件是最直接的切入口。

