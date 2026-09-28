"""汇率数据层：加载与查询"""
import csv
import logging
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "rates.csv"

def load_rates():
    """从 data/rates.csv 加载汇率。

    返回字典 {(from_cur, to_cur): rate}，键为 (源币种, 目标币种) 元组，
    值为浮点汇率。文件缺失时抛出 FileNotFoundError，由调用方处理。
    """
    rates = {}
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rates[(row["from"], row["to"])] = float(row["rate"])
    logging.info(f"已加载 {len(rates)} 条汇率")
    return rates

def get_rate(rates, from_cur, to_cur):
    """一对一汇率查询。

    参数：
        rates: load_rates() 返回的汇率字典
        from_cur: 源币种，三个字母的货币代码，如 "USD"
        to_cur: 目标币种，三个字母的货币代码，如 "CNY"

    命中返回汇率值，未命中返回 None。只查直达汇率，中转逻辑见
    multi_rates.resolve_rate_with_via。金额换算由调用方处理，
    不填金额时按 1 个源币种单位计算。
    """
    return rates.get((from_cur, to_cur))