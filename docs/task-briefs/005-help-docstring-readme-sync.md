# 任务简报 005：help 精简、docstring 补充与 README 同步
- 目标：
    1. 删掉 quote_tool.py 中 --help 输出的"对应功能函数"整段（内部实现信息不应对终端用户暴露）
    2. 把 rates / multi_rates 函数的参数含义挪到 rates.py / multi_rates.py 的 docstring 里
    3. README.md 的"用法"一节补上 --help 的说明，保持门面（README）与说明书（--help）同步
- 环境：
    Python 版本：3.12+
    代码文件夹：src
- 限制：
    只改 src/quote_tool.py、src/rates.py、src/multi_rates.py 的文档部分和 README.md
    不改任何逻辑、不删 logging 语句、不碰 data/rates.csv
- 验收标准：
    python src/quote_tool.py --help 输出中不再出现"对应功能函数"段
    rates.py / multi_rates.py 中能通过 docstring 查到各参数含义
    README.md "用法"一节包含 --help 的说明
    python -m pytest tests/ -v 全部通过
