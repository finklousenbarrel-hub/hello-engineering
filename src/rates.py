"""汇率数据层：加载与查询"""
import csv
import logging
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "rates.csv"

def load_rates():
    rates = {}
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rates[(row["from"], row["to"])] = float(row["rate"])
    logging.info(f"已加载 {len(rates)} 条汇率")
    return rates

def get_rate(rates, from_cur, to_cur):
    return rates.get((from_cur, to_cur))