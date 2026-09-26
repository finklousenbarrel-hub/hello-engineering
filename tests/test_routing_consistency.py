import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from multi_rates import quote_multi, resolve_rate_with_via
import quote_tool

SAMPLE = {
    ("CNY", "USD"): 0.141,
    ("USD", "HKD"): 7.82,
    ("CNY", "EUR"): 0.128,
}

HKD_LINE = "1 CNY = 1.10262 HKD （经USD中转估算，不一定为真实汇率）"
EUR_LINE = "1 CNY = 0.128 EUR"


def test_resolve_rate_records_usd_via():
    rate, via = resolve_rate_with_via(SAMPLE, "CNY", "HKD")
    assert via == "USD"
    assert rate is not None


def test_single_query_uses_hop_annotation(capsys):
    quote_multi(SAMPLE, "CNY", ["HKD"], None, None)
    assert capsys.readouterr().out.strip() == HKD_LINE


def test_batch_query_hkd_line_matches_single(capsys):
    quote_multi(SAMPLE, "CNY", ["HKD"], None, None)
    single = capsys.readouterr().out.strip()

    quote_multi(SAMPLE, "CNY", ["HKD", "EUR"], None, None)
    batch = capsys.readouterr().out.strip().splitlines()

    assert single == HKD_LINE
    assert batch == [HKD_LINE, EUR_LINE]


def test_quote_tool_single_and_batch_agree(capsys, monkeypatch):
    monkeypatch.setattr(quote_tool, "RATES", SAMPLE)

    monkeypatch.setattr(sys, "argv", ["quote_tool.py", "CNY", "HKD"])
    quote_tool.main()
    single = capsys.readouterr().out.strip()

    monkeypatch.setattr(sys, "argv", ["quote_tool.py", "CNY", "HKD", "EUR"])
    quote_tool.main()
    batch = capsys.readouterr().out.strip().splitlines()

    assert single == HKD_LINE
    assert batch[0] == single
    assert batch[1] == EUR_LINE
