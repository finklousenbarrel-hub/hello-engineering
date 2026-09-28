# 任务简报 004：打印说明报告
- 目标：
    输入 python src/quote_tool.py --help
    能自动打印一份说明，告诉用户每个参数是什么、什么格式、具体示例与关键说明
- 环境：
    Python 版本：3.12+
    代码文件夹：src
    数据来自哪：data/rates.csv
    现有代码结构：
        rates为一对一查询汇率函数，
        multi_rates为一对多查询汇率函数，
        quote_tool为主函数。
- 限制：
    只允许修改 src/quote_tool.py 中的文件
- 验收标准：
    输出
        rates和multi_rates函数的各个所需填入参数的含义
        rates和multi_rates函数的示例（包含不填写金额与填写金额）
    标注
        汇率有时是经过中转计算而来，不一定为真实汇率（会用括号表示），并举例说明

    