# 任务简报 003：修复单查/批量查询语义不一致（缺陷）

- 现象：`CNY HKD` 单查输出"暂不支持"；`CNY HKD EUR` 批量查却输出合成汇率。
  同一问题，两种答案。
- 复现步骤：
    > python src/quote_tool.py CNY HKD EUR
    [INFO] 已加载 5 条汇率
    [INFO] 用户查询了CNY和HKD
    1 CNY = 1.10262 HKD
    [INFO] 用户查询了CNY和EUR
    1 CNY = 0.128 EUR
- 根因：main 的分发逻辑里，单目标走 quote_pair（仅直达），
  多目标走 quote_multi → resolve_rate（含一跳中转），两条路径语义分裂。
- 决策：保留中转但输出标注"经USD中转估算，不一定为真实汇率"
- 限制：不许动 data/rates.csv；既有的全部验收用例不得回归
- 验收标准：
  1. CNY HKD 无论单查还是批量查，输出一致
  2. 旧的全部验收命令行为不变
  3. tests/ 新增用例覆盖这个一致性（防复发）