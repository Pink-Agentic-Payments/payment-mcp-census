"""Regenerate the README table from census.csv. Run: python3 generate_table.py"""
import csv

rows = list(csv.DictReader(open("census.csv")))
movers_with_control = []
for r in rows:
    if r["moves_money"] != "yes":
        continue
    controls = [r["budget_control"], r["per_payment_limit"], r["payee_allowlist"], r["human_approval"], r["rate_limits"]]
    if any(c == "yes" for c in controls):
        movers_with_control.append(r)


def fmt(v):
    if v == "yes":
        return "Yes"
    elif v == "no":
        return "No"
    return "Not documented"


lines = []
lines.append("| Server | Maintainer | Budget | Per-payment limit | Payee allowlist | Human approval | Rate limit | Sandbox |")
lines.append("|---|---|---|---|---|---|---|---|")
for r in movers_with_control:
    lines.append(
        f"| {r['name']} | {r['maintainer_type']} | {fmt(r['budget_control'])} | {fmt(r['per_payment_limit'])} | "
        f"{fmt(r['payee_allowlist'])} | {fmt(r['human_approval'])} | {fmt(r['rate_limits'])} | {fmt(r['sandbox_mode'])} |"
    )

print("\n".join(lines))
