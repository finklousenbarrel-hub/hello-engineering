import sys
from pathlib import Path
from decimal import Decimal
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from multi_rates import resolve_rate, quote_multi, format_amount

SAMPLE = {
    ("USD", "CNY"): 7.10,
    ("CNY", "EUR"): 0.128,
}

def test_resolve_rate_hit():
    assert resolve_rate(SAMPLE, "USD", "CNY") == Decimal("7.1")

def test_resolve_rate_hop():
    assert resolve_rate(SAMPLE, "USD", "EUR") == Decimal("7.1") * Decimal("0.128")

def test_resolve_rate_miss():
    assert resolve_rate(SAMPLE, "USD", "JPY") is None

def test_format_amount_trims_zeros():
    assert format_amount(Decimal("90.8800")) == "90.88"
    assert format_amount(Decimal("710.0")) == "710.0"

def test_quote_multi_mixed(capsys):
    quote_multi(SAMPLE, "USD", ["CNY", "EUR", "JPY"], 100, "100")
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == [
        "100 USD = 710.0 CNY",
        "100 USD = 90.88 EUR （经CNY中转估算，不一定为真实汇率）",
        "暂不支持 USD -> JPY",
    ]

def test_quote_multi_default_amount(capsys):
    quote_multi(SAMPLE, "USD", ["CNY", "EUR"], None, None)
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == [
        "1 USD = 7.1 CNY",
        "1 USD = 0.9088 EUR （经CNY中转估算，不一定为真实汇率）",
    ]
