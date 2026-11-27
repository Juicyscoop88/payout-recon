# payout recon - matches bank statement vs payouts export
# run: python recon.py   (exports from the admin panel, save next to this file)
import csv
import sys


def load(path):
    with open(path) as f:
        return list(csv.DictReader(f))


def reconcile(bank, payouts):
    by_ref = {p["reference"]: p for p in payouts}
    matched, unmatched = [], []
    for row in bank:
        p = by_ref.get(row["reference"])
        if p and abs(float(p["amount"]) - float(row["amount"])) < 0.01:
            matched.append(row)
        elif p:
            unmatched.append(row)
    return matched, unmatched


def main(argv):
    bank = load(argv[1] if len(argv) > 1 else "bank_statement_2026-11.csv")
    payouts = load(argv[2] if len(argv) > 2 else "payouts_export_2026-11.csv")
    m, u = reconcile(bank, payouts)
    print(f"matched {len(m)}, unmatched {len(u)}")
    for r in u:
        print("CHECK:", r["reference"], r["amount"])
    return m, u


if __name__ == "__main__":
    main(sys.argv)
