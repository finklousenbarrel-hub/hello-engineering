# 任务简报 002：单次查询多币种功能
- 目标：
    输入N个字符串和一个浮点数，第一个字符串代表原始币种，后N-1个字符串代表待查询币种，浮点数代表原始币种数量。根据已知汇率换算后，输出待查询币种及其对应金额。
- 环境：
    Python 版本：3.12+
    代码文件夹：src
    数据来自哪：data/rates.csv
    现有代码结构：
        rates为查询汇率函数，quote_tool为主函数。
- 限制：
    将新功能单独打包为一个模块，命名为multi_rates，再接入主函数以实现目标。
    已有功能，即单对单的查询功能保持不变。
- 验收标准：

    原有标准维持不变

        输入 python src/quote_tool.py USD CNY 100
        输出 100 USD = 710.0 CNY

        输入 python src/quote_tool.py USD CNY
        输出 1 USD = 7.1 CNY

        输入 python src/quote_tool.py USD ABC 100
        输出 暂不支持 USD -> ABC

        金额非数字时打印用法提示

    新的标准

        输入 
        python src/quote_tool.py USD CNY EUR  100
        输出 
        100 USD = 710.0 CNY
        100 USD = xxx EUR （此处的xxx是根据rates.csv文件中的汇率自行计算得出的参数）

        输入 
        python src/quote_tool.py USD CNY EUR
        输出 
        1 USD = 7.1 CNY
        1 USD = xxx EUR （此处的xxx是根据rates.csv文件中的汇率自行计算得出的参数）

        输入 
        python src/quote_tool.py USD CNY JPY  100
        输出 
        100 USD = 710.0 CNY
        暂不支持 USD -> JPY
        金额非数字时打印用法提示