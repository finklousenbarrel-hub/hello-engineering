# docs 目录索引

练习笔记、任务简报和外部资料都放在这里。根目录的 `README.md` 讲项目用法；本文件只说明 `docs/` 里各篇在记什么。

| 文件 / 目录 | 内容概要 |
|---|---|
| [agent-failure-log.md](agent-failure-log.md) | Agent 执行失败日志：按日期记录现象、原因、对策（如简报不够精确、单查与批量汇率语义分裂）。 |
| [ai-tools-landscape.md](ai-tools-landscape.md) | AI 工具版图笔记，目前为空，待补。 |
| [cursor-notes.md](cursor-notes.md) | Cursor 使用备忘：迁移后要重验自动化、Keep ALL 前先跑验收|
| [debugging.md](debugging.md) | 断点调试入门：`launch.json` 管谁在哪怎么跑；F5 / F10 / F11 的分工。 |
| [git.md](git.md) | Git 操作手册：账号配置、clone / add / commit / push、分支与合并、从 reflog 找回、克隆别人项目后建 venv。 |
| [jx3-api.md](jx3-api.md) | 剑网 3 第三方 JX3API 调研：鉴权（token / ticket）、相关接口类目、和后续项目计划的衔接与待办。 |
| [new_function_record.md](new_function_record.md) | 新学语法速记，目前主要是 Python `logging` 的配置和 `info` / `warning` 用法。 |
| [python_env.md](python_env.md) | 从零搭 Python 虚拟环境：`.gitignore`、激活 `.venv`、`requirements.txt`、`$PROFILE` 里写 `venv` 快捷命令。 |
| [task-briefs/](task-briefs/) | 给 Agent 的任务简报（编号递增）。覆盖汇率工具的功能增量（金额换算、一次查多币种）和缺陷修复（单查/批量语义不一致）；每份含目标、限制和验收命令，不在此展开细节。 |
