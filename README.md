# Payment MCP Servers Census (October 2026)

> **Disclosure**: Published by PinkWallet, which builds Pink Agentic AI Payments (row "Pink Agentic AI Payments"). Pink was scored from its public docs by the same criteria as every other row. Pink currently runs as a public sandbox with test money.

A census of 49 payment-adjacent MCP (Model Context Protocol) servers: which ones let an AI agent actually move money, and which document spending controls (budget, per-payment limit, payee allowlist, human approval, rate limit, sandbox mode). Searches and page fetches were performed 2026-10-08/09. Full method in [METHODOLOGY.md](./METHODOLOGY.md), full findings in [FINDINGS.md](./FINDINGS.md), raw data in [census.csv](./census.csv).

## Headline numbers

- **37 of 49 (76%)** payment-adjacent MCP servers catalogued can actually move money (create a payment, transfer, payout, charge, or issue a card); the other 12 of 49 (24%) are read-only, reporting, codegen, or discovery only.
- Of the 37 that move money, **4 of 37 (11%)** document a configurable per-agent/aggregate spending budget.
- Of the 37 that move money, **5 of 37 (14%)** document a per-payment/per-transaction limit.
- Of the 37 that move money, **3 of 37 (8%)** document a payee/merchant allowlist or block mechanism.
- Of the 37 that move money, **6 of 37 (16%)** document a human-approval step before or to unblock a payment.
- Only **1 of 37 (3%)** documents a spend-velocity/rate limit distinct from a dollar budget — the least-covered control in the census.
- **8 of 37 (22%)** money-moving servers document a dedicated sandbox/test mode.
- Among **24 official-vendor rows**, 17 of 24 (71%) move money; among **25 community/unofficial rows**, 20 of 25 (80%) move money — community servers skew slightly more toward real money movement than official vendor servers.
- **5 of 49 (10%)** listed servers point to a GitHub repo that returned HTTP 404 on 2026-10-08, even though registries and mirrors still list them.

See [FINDINGS.md](./FINDINGS.md) for the full numbered list (11 findings) with evidence quotes and source URLs for every count above.

## Servers that can move money and document at least one spending control

Generated directly from `census.csv` by [generate_table.py](./generate_table.py) — run `python3 generate_table.py` to reproduce.

| Server | Maintainer | Budget | Per-payment limit | Payee allowlist | Human approval | Rate limit | Sandbox |
|---|---|---|---|---|---|---|---|
| Stripe Agent Toolkit / Stripe MCP | official | Not documented | Not documented | Not documented | Yes | Not documented | Yes |
| Coinbase AgentKit / CDP MCP | official | Not documented | Yes | Yes | Not documented | Not documented | Not documented |
| Crossmint Checkout MCP | official | Not documented | Yes | Not documented | Yes | Not documented | Not documented |
| Marqeta MCP Server | official | Yes | Not documented | Yes | Not documented | Yes | Not documented |
| Ramp MCP Server | official | Not documented | Not documented | Not documented | Yes | Not documented | Not documented |
| GoCardless MCP Server | official | Not documented | Not documented | Not documented | Yes | Not documented | Not documented |
| Gatewards | community | Yes | Not documented | Not documented | Not documented | Not documented | Not documented |
| MCPay | community | Yes | Yes | Not documented | Not documented | Not documented | Yes |
| SpendNod | community | Not documented | Not documented | Not documented | Yes | Not documented | Not documented |
| x402search-mcp | community | Not documented | Yes | Not documented | Not documented | Not documented | Not documented |
| Pink Agentic AI Payments | official | Yes | Yes | Yes | Yes | Not documented | Yes |

"Not documented" means the control was not mentioned in the sources we could load — it does not mean the control doesn't exist. See `METHODOLOGY.md` for the distinction between "no" and "not documented" used in `census.csv`.

## Where Pink lands

- Pink **can move money** (sandbox/test money only — explicitly disclosed, see the `notes` column of its row and [METHODOLOGY.md](./METHODOLOGY.md)).
- Pink is one of only **4 of 37** money-moving servers with a documented budget, one of **5 of 37** with a per-payment limit, one of **3 of 37** with a payee allowlist, one of **6 of 37** with human approval, and one of **8 of 37** with a sandbox mode.
- Pink is the only row that is a "yes" on all four governance controls simultaneously (budget, per-payment limit, payee allowlist, human approval).
- Pink does **not** document a rate-limit control distinct from its per-payment/budget caps (same gap as 36 of the other 37 movers) — this is disclosed, not omitted.

Pink Agentic AI Payments is an MCP server that checks per-agent budgets, payee rules and human-approval holds before a payment executes; try it in the public sandbox with test money: https://agentic-sandbox.pinkwallet.com

## Biggest gap in the market

No server in the census — including Pink — documents a dollar-denominated spend-velocity rate limit as a distinct, separately-configurable control from a budget, except Marqeta's "velocity limits". This is the single biggest documentation gap across the entire payment-MCP landscape as of this snapshot, and a credible angle for follow-on coverage: why doesn't anyone rate-limit AI agent spending by time, not just by amount?

## Official MCP Registry cross-check

The 49-row census above was built from vendor docs, aggregators and mirrors, not a direct registry query. As a cross-check, we queried `registry.modelcontextprotocol.io` directly for "payment" and "pay" and found **341 distinct server names across 210 distinct publisher namespaces**, with the largest single namespace (`app.wishpool`, 81 names) being one templated server per country. See the "Official MCP Registry cross-check" section of [METHODOLOGY.md](./METHODOLOGY.md) and the raw list in [registry-payment-servers-2026-10-09.csv](./registry-payment-servers-2026-10-09.csv). These 341 names are not scored and are not part of `census.csv`.

## Method

All 49 rows in `census.csv` carry a public evidence URL per cell. Each server is scored on six independent dimensions (moves money, budget control, per-payment limit, payee allowlist, human approval, rate limits, sandbox mode) using the same rubric for every row, including Pink. Full method, definitions, and known limitations are in [METHODOLOGY.md](./METHODOLOGY.md).

## How to cite

See [CITATION.cff](./CITATION.cff). Short form:

> PinkWallet (2026). *Payment MCP Servers Census (October 2026)*. Version 2026.10. CC BY 4.0. https://github.com/Pink-Agentic-Payments/payment-mcp-census

## Correct a row

If you maintain one of these servers and a cell is wrong or out of date, open an issue using the [Correct a row](./.github/ISSUE_TEMPLATE/correct-a-row.yml) template with a public evidence URL. Corrections with a public source are merged within 7 days and noted in [CHANGELOG.md](./CHANGELOG.md).

## License

[CC BY 4.0](./LICENSE). Attribution: PinkWallet, *Payment MCP Servers Census (October 2026)*.

---

Links: [Pink Agentic AI Payments developer docs](https://pinkwallet.com/agentic/developers/) · [Overspend challenge](https://github.com/Pink-Agentic-Payments/overspend-challenge) ($100 bounty for each of the first 3 verified wins) · [Agent spending incidents](https://github.com/Pink-Agentic-Payments/agent-spending-incidents)
