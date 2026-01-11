# Oh My OpenCode：让 OpenCode 一键进化成“Agent 团队”（以及 Ralph Wiggum 循环开发怎么用）

关键词：opencode, claude-code, ralph-wiggum, ralph-loop, agent loop, automation

这篇文章的主角其实只有一个：**Oh My OpenCode**。

它是一个最近才爆火的项目，但思路非常“工程化”：把 OpenCode 直接升级成“有主力 agent + 分工子 agent + 工具链 + 兼容层”的完整工作台，让你不用从 0 手搓一堆脚本/规则/配置也能立刻开干。

而 **Ralph Wiggum / Ralph Loop**（“不做完别停”的循环开发）只是它开箱即用的王牌能力之一。

参考来源（可引用）：

- Oh My OpenCode（Sisyphus）项目（Ralph Loop、Claude Code compatibility layer、多 agent/工具链等）：[code-yeongyu/oh-my-opencode](https://github.com/code-yeongyu/oh-my-opencode)
- Anthropic 的 Claude Code 官方插件 Ralph Wiggum（说明了 “Ralph is a Bash loop”、Stop hook、`/ralph-loop` 等）：[anthropics/claude-code/plugins/ralph-wiggum](https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum)
- 一个更“工程模板化”的 OpenCode Ralph 插件（Phoenix/React/Expo + TanStack，带 `plan.md`、验证命令、commit 约定等）：[NicholasBarkolias/ralph-opencode-plugin](https://github.com/NicholasBarkolias/ralph-opencode-plugin)

## 1）先把 Oh My OpenCode 讲清楚：它是什么？为什么最近才火？

你如果最近才看到 `oh-my-opencode`，很正常——它属于那种**短时间内在开发者圈子里突然出圈**的项目。

它的定位可以简单粗暴地理解成：

- **OpenCode 的“超级装配包 / agent harness”**：把一套能跑起来、能扩展、能持续演进的默认工作流装进 OpenCode（主 agent + 子 agent + 工具链 + 兼容层）
- **主打“多模型协作 + 并行/后台任务 + 工程化工具链”**：不是换皮聊天框，而是把“像一个小团队一样干活”做成默认体验
- **强调 Claude Code 兼容**：README 里明确强调 Claude Code compatibility（commands/skills/agents/hooks/plugins 等），让很多资产迁移成本更低

为什么它最近火得快？我观察到的原因基本都很“工程现实”：

- **默认配置就能跑**：很多人不想从 0 拼插件/脚本/规则；它把“可用的最佳实践”打包好了
- **把痛点做成系统能力**：比如 Ralph loop（“不做完别停”），在 `oh-my-opencode` 里就是开箱即用的一环
- **赶上了“供应链焦虑”**：当上游模型/接入策略变化时，大家会更愿意把工作流迁移到更可控、更可替换的开源栈（这也是 OpenCode 生态最近整体升温的背景）

## 2）为什么要重点讲它的 Ralph Loop：解决“写一半就停”的硬伤

如果你用过 AI 编程工具，你一定见过这种场景：

- 写了一半，模型“自我感觉良好”就停了
- 测试挂了、lint 挂了、类型错误一堆，但它不继续修
- 你不断复制粘贴错误输出，像在“人肉驱动 CI”

Ralph 的核心思想是：**把“继续迭代”变成系统默认行为，而不是靠你盯着。**

## 3）Oh My OpenCode 的 Ralph Loop：把“循环开发”做成开箱即用（跨语言）

在 `oh-my-opencode` 的 README 里，Ralph Loop 被放在 “Not Just for the Agents” 部分，明确写了：

- 受到 Anthropic Ralph Wiggum 插件启发（Inspired by Anthropic's Ralph Wiggum plugin）
- 支持所有语言
- 通过 `<promise>DONE</promise>` 判断完成
- 默认最大迭代 100 次
- 提供 `/cancel-ralph` 退出
- 可在 `oh-my-opencode.json` 中配置

一句话总结：**你宣传 Oh My OpenCode 的时候，Ralph Loop 是非常好打的“可感知卖点”**——读者不用理解一堆概念，先感受到“它不会半途而废、能自动反复修到做完”就够了。

## 4）从 Claude Code 视角做对照：官方 Ralph Wiggum 插件在讲什么？

在 Anthropic 的官方插件描述里，Ralph 被定义成一种持续循环的方法论（“Ralph is a Bash loop”），但插件把它“内置化”了：通过 **Stop hook** 拦截退出，把同一个 prompt 重新喂回去，让代理继续改文件、跑测试、再修。

典型用法（概念层面）：

- **启动循环**：`/ralph-loop "<prompt>" --completion-promise "<text>" --max-iterations <n>`
- **取消循环**：`/cancel-ralph`

关键点：

- **完成条件**：`--completion-promise` 是“精确字符串匹配”
- **安全刹车**：`--max-iterations`（强烈建议总是设置）
- **优势**：更像“把代理变成一个会反复自我纠错的工人”

## 5）如果你想更“模板化”：ralph-opencode-plugin 把循环升级成工程规约

另一个很有代表性的实现是 `ralph-opencode-plugin`：它不止是“循环”，更像是“把一个团队的工程规约塞进循环里”：

- 强约束技术栈（Phoenix + React/Expo + TanStack 生态）
- 提供 `/ralph-plan` 先产出 `plan.md`，再 `/ralph` 执行
- 提供不同方向的命令：`/ralph-phoenix`、`/ralph-react`、`/ralph-expo`、`/ralph-full`
- 内置验证命令（编译/格式化/lint/test）和 commit 规范

它的价值是：**把“循环”从方法论升级成“可复制的项目模板”。**

## 6）对比：官方 Ralph vs Oh My OpenCode Ralph Loop vs ralph-opencode-plugin

| 维度 | Claude Code 官方 Ralph Wiggum | Oh My OpenCode：Ralph Loop | ralph-opencode-plugin |
|---|---|---|---|
| 目标 | 让 Claude Code 会话内持续迭代 | 给 OpenCode 提供通用循环能力 | 给特定栈提供“带规约的循环” |
| 完成信号 | `--completion-promise` 精确匹配 | `<promise>DONE</promise>` | `RALPH_COMPLETE`（并配合 plan.md/脚本） |
| 安全刹车 | `--max-iterations` | 默认 100，可配 | 迭代次数可控，且有“BLOCKED”处理 |
| 适用范围 | Claude Code 用户 | OpenCode 用户（偏通用） | Phoenix/React/Expo/TanStack 用户 |
| 你要做的事 | 把“验收标准”写清楚 | 把“验收标准”写清楚 + 可配底座 | 直接套工程模板，按命令跑 |

## 7）怎么写 Prompt 才能让 Oh My OpenCode 的 Ralph Loop 真正跑起来？

不管你用哪一种 Ralph，本质都一样：**把“验收标准”写成可判定的 checklist**，并明确“卡住了怎么办”。

建议最少包含：

- 明确的输出承诺（promise）
- 允许跑测试/静态检查并据此修复
- 最大迭代次数
- 卡住后要做的事：记录阻塞点、列出已尝试方案、给出替代路径

## 8）一句结论：宣传 Oh My OpenCode，别只讲“更强”，要讲“更稳、更成体系”

这类 loop 技术最实用的地方在于：它把 AI 代理从“偶尔灵光一现”，变成“可以交给它熬夜干活的流水线”。

如果你的重点是宣传 **Oh My OpenCode**，我的建议是：

- 先把它定义成“OpenCode 的超级装配包 / agent harness”（一条话术就够）
- 再拿 Ralph Loop 做“可感知的卖点”演示（不做完不让停 + `<promise>DONE</promise>` + `/cancel-ralph` + 默认 100 次）
- 最后补一句：它还强调 Claude Code 兼容，迁移资产成本更低


