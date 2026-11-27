# makes report.html for the team (open it in the browser every morning)
import sys
from recon import main

m, u = main(sys.argv)
rows = "".join(f"<tr><td>{r['reference']}</td><td>{r['amount']}</td></tr>" for r in u)
html = f"""<html><body style="font-family: Comic Sans MS; background: #fffbe6">
<h1 style="color: purple">Recon report</h1>
<p>matched: {len(m)} / to check: {len(u)}</p>
<table border=1>{rows}</table>
</body></html>"""
open("report.html", "w").write(html)
print("wrote report.html")
