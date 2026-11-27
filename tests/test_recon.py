"""What the recon does today, on made-up sample data (tests/data)."""
from pathlib import Path

from recon import load, main, reconcile

DATA = Path(__file__).parent / "data"
BANK = str(DATA / "bank_sample.csv")
PAYOUTS = str(DATA / "payouts_sample.csv")


def refs(rows):
    return [r["reference"] for r in rows]


def test_same_reference_and_amount_is_matched():
    matched, _ = reconcile([{"reference": "A", "amount": "10.00"}], [{"reference": "A", "amount": "10.00"}])
    assert refs(matched) == ["A"]


def test_amounts_differing_by_less_than_a_cent_still_match():
    matched, unmatched = reconcile([{"reference": "A", "amount": "10.000"}], [{"reference": "A", "amount": "10.005"}])
    assert refs(matched) == ["A"] and unmatched == []


def test_amounts_differing_by_ten_cents_must_be_checked():
    matched, unmatched = reconcile([{"reference": "A", "amount": "480.05"}], [{"reference": "A", "amount": "480.50"}])
    assert matched == [] and refs(unmatched) == ["A"]


def test_load_reads_rows_by_column_name():
    rows = load(BANK)
    assert rows[0] == {"reference": "T-001", "amount": "100.00"}
    assert len(rows) == 3


def test_main_on_sample_prints_what_to_check(capsys):
    matched, unmatched = main(["recon.py", BANK, PAYOUTS])
    assert refs(matched) == ["T-001"]
    assert refs(unmatched) == ["T-002"]
    out = capsys.readouterr().out
    assert "matched 1, unmatched 1" in out
    assert "CHECK: T-002 250.10" in out
