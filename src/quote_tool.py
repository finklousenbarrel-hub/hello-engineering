import csv
import sys
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# __file__ = 这个 .py 文件自己的位置
# 下面的写法不管终端站在哪都能找到 data/rates.csv
DATA_FILE = Path(__file__).parent.parent / "data" / "rates.csv"

def load_rates():
    rates = {}
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rates[(row["from"], row["to"])] = float(row["rate"])
    logging.info(f"已加载 {len(rates)} 条汇率")
    return rates

try:
    RATES = load_rates()
except FileNotFoundError:
    print("错误：找不到数据文件 data/rates.csv")
    sys.exit(1)

def get_rate(from_cur, to_cur):
    return RATES.get((from_cur, to_cur))


def print_usage():
    print("用法: python src/quote_tool.py USD CNY [100]")


def main():
    argc = len(sys.argv)
    if argc not in (3, 4):
        print_usage()
        return
    from_cur = sys.argv[1].upper()
    to_cur = sys.argv[2].upper()

    amount = None
    amount_input = None
    if argc == 4:
        amount_input = sys.argv[3]
        try:
            amount = float(amount_input)
        except ValueError:
            print_usage()
            return

    rate = get_rate(from_cur, to_cur)
    logging.info(f"用户查询了{from_cur}和{to_cur}")

    if rate is not None:
        if amount is None:
            print(f"1 {from_cur} = {rate} {to_cur}")
        else:
            print(f"{amount_input} {from_cur} = {amount * rate} {to_cur}")
    else:
        print(f"暂不支持 {from_cur} -> {to_cur}")
        logging.warning("用户查询未命中")

if __name__ == "__main__":
    main()