# Findings — Payment MCP Servers Census (October 2026)

All numbers below are computed directly from `census.csv` (49 rows). Re-derive with:
`python3 -c "import csv; r=list(csv.DictReader(open('census.csv'))); print(len(r))"` and the equivalent `sum(1 for x in r if ...)` filters described under each number.

1. **37 of 49 (76%)** payment-adjacent MCP servers we catalogued can actually **move money** — create a payment, transfer, payout, charge, or issue a card — versus **12 of 49 (24%)** that are read-only/reporting/codegen/discovery only (e.g., Mercury, Dwolla, Plaid, Lithic, PayMongo, Brex, Circle's codegen server, and four x402 discovery/oracle tools). *Column: `moves_money`.*

2. Of the 37 that can move money, **4 of 37 (11%)** document a configurable **per-agent/aggregate spending budget**: Marqeta ("spending caps"), Gatewards ("per-agent spend caps"), MCPay ("a hard budget"), and Pink (per-agent "monthly budget"). *Column: `budget_control` = yes.*

3. Of the 37 that can move money, **5 of 37 (14%)** document a **per-payment/per-transaction limit**: Coinbase AgentKit/CDP (value-based policy rules), Crossmint Checkout (`maxCost`), MCPay (fixed per-call price), x402search-mcp (hard-coded $0.01 USDC per search), and Pink (amount rules; payments over the configured amount go to a human hold). *Column: `per_payment_limit` = yes.*

4. Of the 37 that can move money, only **3 of 37 (8%)** document a **payee/merchant allowlist or block mechanism**: Coinbase AgentKit/CDP (address-based policy rules), Marqeta ("merchant restrictions"), and Pink (`pink.list_payees` plus a documented "blocked" decision example). *Column: `payee_allowlist` = yes.*

5. Of the 37 that can move money, **6 of 37 (16%)** document a **human-approval step** before or to unblock a payment: Stripe (confirmation required for refunds/outbound payments), Crossmint (`awaiting_input` status), Ramp ("managing approvals"), GoCardless ("with user confirmation"), SpendNod ("escalating... to humans for approval"), and Pink (`pending_human` status). *Column: `human_approval` = yes.*

6. Only **1 of 37 (3%)** documents a **spend-velocity/rate limit** distinct from a dollar budget: Marqeta ("velocity limits"). *Column: `rate_limits` = yes.* This is the least-covered control in the entire census.

7. **8 of 37 (22%)** money-moving servers document a dedicated **sandbox/test mode**: Stripe, PayPal, Square, Skyfire, Paddle, the community Payman wrapper, MCPay, and Pink. The other 29 either don't mention one in the sources we could load, or (Crossmint) explicitly warn that even the "live demo can place real orders" with no staging mode referenced. *Column: `sandbox_mode` = yes.*

8. **Pink Agentic AI Payments is the only server in the census (1 of 49) that documents all four of the core agent-governance controls at once** — budget, per-payment limit, payee allowlist, and human approval — in addition to a sandbox-only mode. Every other server documents at most two of those four controls (Coinbase AgentKit/CDP, Crossmint Checkout, Marqeta and MCPay among the money-moving servers; Brex among the read-only ones). Caveat: Pink runs as a sandbox with test money only, and this census is published by PinkWallet; Pink was scored from its public docs by the same criteria as every other row.

9. Among the **24 official-vendor rows**, **17 of 24 (71%)** can move money (the rest — Circle's codegen server, Mercury, Dwolla, Plaid, Brex, Mastercard's docs-toolkit, PayMongo — are read-only, codegen, or doc-assistant servers). Among the **25 community/unofficial rows**, **20 of 25 (80%)** can move money — community and hobbyist servers in this space skew slightly *more* toward actual money movement than official vendor servers do, because several large vendors (Mercury, Dwolla, Plaid, Brex) have deliberately shipped MCP servers that are read-only by design.

10. **No server in the census — including Pink — documents a dollar-denominated spend-velocity rate limit as a distinct, separately-configurable control from a budget**, except Marqeta's "velocity limits." This is the single biggest documentation gap across the entire payment-MCP landscape as of this snapshot, and a credible angle for follow-on coverage ("why doesn't anyone rate-limit AI agent spending by time, not just by amount?").

11. **5 of 49 (10%)** listed servers point to a GitHub repo that returned HTTP 404 on 2026-10-08 (Fin-MCP, mcp-ap2, agent-pay, nullpath-labs/mcp-client, agentshield-mcp), even though registries and mirrors still list them. Registry listings in this space go stale fast; check the repo before you build on a server. *Column: `notes` starting with "PRIMARY REPO UNREACHABLE".*

## Where Pink lands (factual, same criteria as everyone else)

- Pink **can move money** (sandbox/test money only — explicitly disclosed, see `notes` column of its row and [METHODOLOGY.md](./METHODOLOGY.md)).
- Pink is one of only **4 of 37** money-moving servers with a documented budget, one of **5 of 37** with a per-payment limit, one of **3 of 37** with a payee allowlist, one of **6 of 37** with human approval, and one of **8 of 37** with a sandbox mode.
- Pink is the only row that is a "yes" on all four governance controls simultaneously.
- Pink does **not** document a rate-limit control distinct from its per-payment/budget caps (same gap as 36 of the other 37 movers) — this is disclosed, not omitted.

## Three title phrasings worth targeting

1. **"best MCP server for payments"** — closely mirrors existing third-party aggregator page titles we found during research (e.g., Glama's `images.glama.ai/mcp/servers/integrations/stripe` "Best Stripe MCP Servers" pattern, and comparison pages on toolradar.com like "razorpay-mcp-vs-modern-treasury" / "mollie-mcp-vs-modern-treasury" that imply users are actively comparing "best X MCP server" within payments). Evidence: these comparison/ranking page URLs surfaced unprompted across multiple independent searches in this session (toolradar.com, glama.ai), suggesting it's a live query pattern aggregators are already optimizing for.
2. **"MCP server for AI agent payments"** — directly reflects how vendors themselves describe these servers in their own docs/press, e.g. Marqeta's own blog title "Bringing Agentic Payments to Life with Marqeta's MCP Server" and Lithic's "Power Agentic Commerce Workflows with the Lithic MCP Server" — vendors are already framing their own servers this way, which signals it's the phrasing being optimized for on the supply side too. Evidence: `www.marqeta.com/blog/bringing-agentic-payments-to-life-with-marqetas-mcp-server`, `www.lithic.com/blog/mcp-server-agentic-payments`.
3. **"spending controls for AI agents" / "AI agent spending limits"** — distinct blog content already exists under this exact framing from third parties unrelated to any single vendor (e.g., `policylayer.com/blog/mcp-server-spending-controls`, `policylayer.com/blog/spending-controls-mcp-agent`, `satgate.io/blog/mcp-budget-enforcement-guide`), which surfaced specifically when we searched for "Payman MCP server spending controls documentation" — i.e., it's an existing content category, not one we're inventing. Evidence: those three URLs returned directly in that search pass.

**Caveat on phrasing evidence**: none of the above is autocomplete or Reddit/HN thread data (we did not have budget to pull Google/Bing Autocomplete or search Reddit/HN directly); it is inferred from which page titles and content categories independently and repeatedly surfaced across our research searches. Treat it as a reasonable signal, not confirmed query-volume data — flagged here rather than overstated.
