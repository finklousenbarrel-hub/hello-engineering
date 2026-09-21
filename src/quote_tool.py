import csv
import sys
from pathlib import Path

# __file__ = 这个 .py 文件自己的位置
# 下面的写法不管终端站在哪都能找到 data/rates.csv
DATA_FILE = Path(__file__).parent.parent / "data" / "rates.csv"

def load_rates():
    rates = {}
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rates[(row["from"], row["to"])] = float(row["rate"])
    return rates

try:
    RATES = load_rates()
except FileNotFoundError:
    print("错误：找不到数据文件 data/rates.csv")
    sys.exit(1)

# get_rate 和 main 不用动

def get_rate(from_cur, to_cur):
    return RATES.get((from_cur, to_cur))
    

def main():
    if len(sys.argv) != 3:
        print("用法: python src/quote_tool.py USD CNY")
        return
    from_cur = sys.argv[1].upper()
    to_cur = sys.argv[2].upper()

    rate = get_rate(from_cur, to_cur)

    if rate is not None:
        print(f"1 {from_cur} = {rate} {to_cur}")
    else:
        print(f"暂不支持 {from_cur} -> {to_cur}")

if __name__ == "__main__":
    main()