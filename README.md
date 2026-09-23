# hello-engineering

一个简单的命令行汇率查询工具，我的第一个 Python 工程练习

## 功能演示
> python src/quote_tool.py USD CNY
2026-09-23 18:00:02,463 [INFO] 已加载 5 条汇率
2026-09-23 18:00:02,463 [INFO] 用户查询了USD和CNY
1 USD = 7.1 CNY

## 环境
- Python 版本要求：Python 3.12+
- 从零开始的安装步骤
git clone https://github.com/finklousenbarrel-hub/hello-engineering/
cd hello-engineering
python -m venv .venv           
.venv\Scripts\Activate.ps1     
pip install -r requirements.txt

## 用法
- 正常币种
> python src/quote_tool.py USD CNY
2026-09-23 18:00:02,463 [INFO] 已加载 5 条汇率
2026-09-23 18:00:02,463 [INFO] 用户查询了USD和CNY
1 USD = 7.1 CNY
- 未覆盖的币种
> python src/quote_tool.py 币种1 不存在币种2
> python src/quote_tool.py USD CNM
2026-09-23 18:10:27,045 [INFO] 已加载 5 条汇率
2026-09-23 18:10:27,045 [INFO] 用户查询了USD和CNM
暂不支持 USD -> CNM
2026-09-23 18:10:27,045 [WARNING] 用户查询未命中
- 数据文件缺失
错误：找不到数据文件 data/rates.csv


## 限制
汇率是本地 CSV 快照不是实时的；只支持 5 对货币，详情见data/rates.csv

## 验收标准
- 运行 python src/quote_tool.py USD CNY，应输出 1 USD = 7.1 CNY
- 缺少参数时应打印用法提示
- 删除 data/rates.csv 后运行，应输出友好错误提示而非报错堆栈

## 目录结构
src / 主程序
data / 存放汇率数据方便调用
docs / 项目文档与学习笔记
tests / 未使用，待开发