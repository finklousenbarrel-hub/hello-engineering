# 任务简报 001：金额换算功能
- 目标：
    输入两个币种与金额，含义是第一个币种的数量，输出左侧币种数量=多少右侧币种数量
- 环境：
    Python 版本：3.12+
    代码文件：src/quote_tool.py
    数据来自哪：data/rates.csv
    现有代码结构：load_rates提取汇率信息，main函数中调用load_rates和get_rate做查询
- 限制：
    只允许修改src/quote_tool.py中的文件
    logging的输出日志不可删除
- 验收标准：
    输入 python src/quote_tool.py USD CNY 100
    输出 100 USD = 710.0 CNY

    输入 python src/quote_tool.py USD CNY
    输出 1 USD = 7.1 CNY

    输入 python src/quote_tool.py USD ABC 100
    输出 暂不支持 USD -> ABC

    金额非数字时打印用法提示