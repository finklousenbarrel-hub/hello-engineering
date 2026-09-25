import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rates import get_rate

SAMPLE = {("USD", "CNY"): 7.10}

def test_get_rate_hit():
    assert get_rate(SAMPLE, "USD", "CNY") == 7.10

def test_get_rate_miss():
    assert get_rate(SAMPLE, "USD", "JPY") is None