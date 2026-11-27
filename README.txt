recon tool - made over the weekend with ChatGPT
python src/recon.py  -> prints what to check
python src/report.py -> report.html for the ops team (5 people use it every morning)

The exports (bank_statement_*.csv, payouts_export_*.csv) are passed as arguments or saved in the folder
you run from. They contain client data: they are never committed (see .gitignore).
Tests run on made-up data in tests/data:  uv sync && .venv/bin/python -m pytest
