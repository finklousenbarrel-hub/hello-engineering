import sys
from pathlib import Path
import logging

SRC_DIR = Path(__file__).parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rates import load_rates
from multi_rates import quote_multi

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


try:
    RATES = load_rates()
except FileNotFoundError:
    print("错误：找不到数据文件 data/rates.csv")
    sys.exit(1)


def print_usage():
    print("用法: python src/quote_tool.py USD CNY [EUR ...] [100]")


def parse_args(argv):
    tokens = argv[1:]
    if len(tokens) < 2:
        return None

    last = tokens[-1]
    try:
        amount = float(last)
        amount_input = last
        cur_tokens = tokens[:-1]
    except ValueError:
        amount = None
        amount_input = None
        cur_tokens = tokens

    if len(cur_tokens) < 2:
        return None
    if not all(token.isalpha() for token in cur_tokens):
        return None

    currencies = [token.upper() for token in cur_tokens]
    return currencies[0], currencies[1:], amount, amount_input


def main():
    parsed = parse_args(sys.argv)
    if parsed is None:
        print_usage()
        return

    from_cur, to_curs, amount, amount_input = parsed
    quote_multi(RATES, from_cur, to_curs, amount, amount_input)


if __name__ == "__main__":
    main()
