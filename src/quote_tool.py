import sys

RATES = {
    ("USD", "CNY"): 7.10,
    ("CNY", "USD"): 0.141,
    ("EUR", "CNY"): 7.80,
    ("CNY", "EUR"): 0.128,
    ("USD", "HKD"): 7.82,
}

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