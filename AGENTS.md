# 项目说明书

## 项目是什么
汇率转换器，可以支持具体到金额的一对一汇率查询与一对多汇率查询。

## 结构地图
（src/负责代码管理，存放主函数和功能函数 data/负责存放汇率数据 tests/负责测试功能函数 docs/负责存放练习笔记、任务简报和外部资料 ；rates.py 是数据层、quote_tool.py 是 CLI 入口、multi_rates.py 是批量逻辑）

## 怎么运行和验证
- 运行：python src/quote_tool.py USD CNY
- 测试：python -m pytest tests/ -v（任何代码改动后必须全绿）

## 铁律（不许碰）
- 不许修改 data/rates.csv
- 中转汇率必须带"估算"标注，不许伪装成真实汇率
- logging 语句不许删
- 改动必须先有 docs/task-briefs/ 里的任务简报