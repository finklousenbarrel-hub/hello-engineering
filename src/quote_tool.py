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


HELP_TEXT = """\
汇率转换器 —— 使用说明
============================================================

用法:
    python src/quote_tool.py FROM TO [TO2 ...] [AMOUNT]

参数说明:
    FROM        源币种，三个字母的货币代码，如 USD、CNY、EUR
    TO          目标币种，三个字母的货币代码，如 CNY、HKD
    TO2 ...     （一对多查询专用）更多目标币种，用空格分隔
    AMOUNT      可选金额，放在最后的数字；不填时默认按 1 个单位换算

示例:
    一对一，不填金额:
        python src/quote_tool.py USD CNY
        输出示例: 1 USD = 7.1 CNY
    一对一，填写金额:
        python src/quote_tool.py USD CNY 100
        输出示例: 100 USD = 710.0 CNY
    一对多，不填金额:
        python src/quote_tool.py USD CNY EUR
    一对多，填写金额:
        python src/quote_tool.py USD CNY EUR 100

关键说明:
    汇率有时是经过中转计算而来，不一定为真实汇率。这种情况会在输出
    末尾用括号标注，例如:
        python src/quote_tool.py USD EUR
        输出示例: 1 USD = 0.9088 EUR （经CNY中转估算，不一定为真实汇率）
    表示 USD 与 EUR 之间没有直达汇率，结果是经 CNY 中转估算出来的，
    仅供参考，实际成交汇率可能不同。
"""


def print_usage():
    print("用法: python src/quote_tool.py USD CNY [EUR ...] [100]")
    print("查看完整说明: python src/quote_tool.py --help")


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
    if len(sys.argv) >= 2 and sys.argv[1] in ("--help", "-h"):
        print(HELP_TEXT)
        return

    parsed = parse_args(sys.argv)
    if parsed is None:
        print_usage()
        return

    from_cur, to_curs, amount, amount_input = parsed
    quote_multi(RATES, from_cur, to_curs, amount, amount_input)


if __name__ == "__main__":
    main()
