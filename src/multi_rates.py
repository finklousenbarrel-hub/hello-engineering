"""一次查询多个目标币种。"""
import logging
from decimal import Decimal

from rates import get_rate


def _as_decimal(value):
    return Decimal(str(value))


def resolve_rate_with_via(rates, from_cur, to_cur):
    """优先直达汇率；没有则尝试一跳中转。返回 (rate, via)，via 为中转币种或 None。"""
    direct = get_rate(rates, from_cur, to_cur)
    if direct is not None:
        return _as_decimal(direct), None
    mids = {dst for src, dst in rates if src == from_cur}
    for mid in mids:
        hop = get_rate(rates, mid, to_cur)
        if hop is not None:
            rate = _as_decimal(get_rate(rates, from_cur, mid)) * _as_decimal(hop)
            return rate, mid
    return None, None


def resolve_rate(rates, from_cur, to_cur):
    rate, _via = resolve_rate_with_via(rates, from_cur, to_cur)
    return rate


def format_amount(value):
    text = format(value, "f")
    if "." in text:
        text = text.rstrip("0")
        if text.endswith("."):
            text += "0"
    return text


def quote_multi(rates, from_cur, to_curs, amount, amount_input):
    """一对多汇率查询，逐个目标币种打印一行结果。

    参数：
        rates: load_rates() 返回的汇率字典
        from_cur: 源币种，三个字母的货币代码，如 "USD"
        to_curs: 目标币种列表，可填多个，如 ["CNY", "EUR"]
        amount: 金额数值，None 表示不填金额、按 1 个源币种单位换算
        amount_input: 金额的原始输入字符串，用于原样回显；amount 为
            None 时也应为 None

    无直达汇率时尝试一跳中转，中转结果以"（经XX中转估算，不一定为
    真实汇率）"标注；查询不到时打印"暂不支持"。
    """
    qty = Decimal("1") if amount is None else Decimal(amount_input)
    left = "1" if amount is None else amount_input
    for to_cur in to_curs:
        logging.info(f"用户查询了{from_cur}和{to_cur}")
        rate, via = resolve_rate_with_via(rates, from_cur, to_cur)
        if rate is not None:
            line = f"{left} {from_cur} = {format_amount(qty * rate)} {to_cur}"
            if via:
                line += f" （经{via}中转估算，不一定为真实汇率）"
            print(line)
        else:
            print(f"暂不支持 {from_cur} -> {to_cur}")
            logging.warning("用户查询未命中")
