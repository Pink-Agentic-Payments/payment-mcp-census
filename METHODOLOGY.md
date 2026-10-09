# Methodology — Payment MCP Servers Census (October 2026)

## Search date

All searches and page fetches for this census were performed on **2026-10-08/09**. MCP servers are a fast-moving space (several vendors shipped or changed MCP servers in 2025–2026); treat this as a snapshot, not a permanent ranking.

## Sources enumerated

- **Official MCP Registry** (`registry.modelcontextprotocol.io`) — we did not get a working direct query against its API within the time/budget for this pass. Instead we reached registry-listed servers indirectly through registry mirrors and aggregators that re-publish registry entries: **getdrio.com**, **mcpplaygroundonline.com**, **skillselion.com**, **claudemarketplaces.com**. This is a disclosed limitation — see below.
- **Glama** (`glama.ai/mcp/servers`, `glama.ai/mcp/servers/integrations/*`) — used extensively; many community server READMEs were read through Glama's mirrored blob pages.
- **Smithery** (`smithery.ai/server/*`) — used for several Solana/x402 and BayarCash/Payman listings.
- **PulseMCP** — queried; it did not surface payment-specific listings directly, but its own server (`PulseMCP Server`) and several payment servers appeared in the same search pass via other aggregators.
- **mcp.so** — used; has a `#payment-server` tag that, as of the search date, listed exactly one server (Fin-MCP Payment Server).
- **awesome-mcp-servers / awesome-x402** — reached via a Gitea mirror (`git.cynarski.dev/Awesome/awesome-mcp-servers`) that preserves the Finance & Fintech section's commit history; several x402-ecosystem rows (nullpath-labs/mcp-client, agentshield-mcp, braintree-mcp-server, x402station-mcp) are sourced from this mirror's listing text rather than from the servers' own README pages, which we did not independently fetch.
- **Official vendor documentation** — fetched directly wherever possible: Stripe, PayPal, Marqeta, Skyfire, Crossmint, Modern Treasury, Paddle, Dwolla, Coinbase CDP, Pink (our own product).
- Search terms used across the above: `payment`, `pay`, `invoice`, `wallet`, `card`, `checkout`, `stripe`, `x402`, `crypto transfer`, `billing`, `payout`, plus vendor-specific follow-ups (Stripe, PayPal, Square, Coinbase, Circle, Crossmint, Skyfire, Payman, Ramp, Brex, Mercury, Razorpay, Modern Treasury, GoCardless, Rapyd, Lithic, Marqeta, Highnote, thirdweb, Alchemy, Privy, Paddle, Lemon Squeezy, Polar, Plaid, Dwolla, Increase, Visa, Mastercard, Google AP2).

## Definitions

- **Moves money (`moves_money` = yes)**: the server exposes at least one documented tool/endpoint that creates, captures, transfers, charges, refunds, pays out, or issues a card — i.e., an action that changes a balance or initiates a real-world funds movement (sandbox/test money counts). Tools that only list, search, debug, or analyze existing data are **not** counted as moving money, even if they belong to a payments company (see Mercury, Dwolla, Plaid, Lithic, PayMongo, Brex in the dataset — all classified `no` on this basis, with the exact quote cited).
- **Spending control dimensions** (each scored independently as `yes` / `no` / `not documented`):
  - `budget_control` — a configurable recurring or aggregate spend ceiling (e.g., "monthly budget").
  - `per_payment_limit` — a cap on the size of a single transaction/call.
  - `payee_allowlist` — a documented mechanism to restrict or block which counterparties/merchants/addresses can be paid.
  - `human_approval` — a documented step where a human must confirm/approve before (or to unblock) a payment.
  - `rate_limits` — a documented cap on transaction *frequency/velocity* (distinct from a dollar budget).
  - `sandbox_mode` — a documented test/sandbox environment using fake or non-live funds.
  - **`not documented` ≠ `no`.** We used `no` only where the source explicitly states the control does not exist (e.g., Paddle: "doesn't gate destructive operations"; Mercury: "all mutations are blocked server-side" — which makes every money-movement control moot, so we also used `not documented` there since the question doesn't really apply). Everywhere else, silence in the sources we could load is recorded as `not documented`, which could mean the control exists but isn't documented publicly, not that it's absent.
- **`maintainer_type`**: `official` = built or published by the payment/platform vendor itself (Stripe, PayPal, Marqeta, Pink, etc.) or by the protocol's own authors (Coinbase for `@x402/mcp`). `community` = third-party/unofficial, including wrappers around an official API (e.g., the Payman and Braintree community servers).

## What we did NOT do

- We did **not** sign up for, authenticate to, or test-call any of these servers. All facts come from public documentation, README files, and vendor-published pages (or, for a handful of rows explicitly flagged in the `notes` column, from search-engine summaries of those pages when the page itself could not be fetched directly — e.g., JS-rendered docs, 403/404s, or OAuth-gated endpoints).
- We did not verify GitHub commit timestamps for most community servers; `last_updated` is `not documented` for all but one row (`agent-pay`, where an aggregator explicitly stated "last updated 2026-03-21"). Treat the dataset as a snapshot of *documented capability*, not of code freshness.
- We did not attempt to be exhaustive on every regional payment gateway (e.g., we found but excluded a Paytm MCP server reference because we could not verify its tool list beyond a FAQ page title, and excluded a couple of other thin leads rather than guess at their capabilities).

## Limitations / known gaps

1. **No direct Official MCP Registry API query.** We relied on mirrors/aggregators. If the registry's own listing differs (e.g., different maintainer field, different last-updated date), this census may be stale relative to the registry itself.
2. **Several official-vendor pages could not be fetched directly** (403 on PayPal's `docs.paypal.ai`, 404 on a stale PayPal path, 401 on Mercury's live MCP endpoint, JS-rendering on Ramp's docs, a non-informative GoCardless root page). For these we cite the best available secondary source (a documentation mirror or a `mcpservers.org`/aggregator summary) and flag it in the `source_directory` / `notes` columns. These rows carry lower confidence than the ones fetched directly from the vendor's own docs (Stripe, Marqeta, Skyfire, Crossmint, Modern Treasury, Paddle, Dwolla, Coinbase, Pink).
3. **x402 micropayment ecosystem is large and churns fast.** We sampled ~12 representative x402-related servers (official reference implementation, Solana variants, discovery/oracle tools, and several Base/USDC payment servers) rather than attempting to enumerate the full long tail; `awesome-x402` alone lists more than appear here.
4. **Visa and Mastercard rows are sourced from press/perspectives pages, not developer-docs tool references**, because we could not locate or load a public tools-reference page for either within budget. They are included because they are highly likely to be named in AI answers to "best payment MCP server" queries, but are flagged as lower-confidence in the `notes` column.
5. **"Can move money" is sometimes a judgment call** on borderline cases (e.g., card-issuance tools, codegen tools, authorization/mandate-protocol servers like AP2). We documented the quote we based each call on so a reader can disagree and re-derive their own classification.

## Official MCP Registry cross-check (2026-10-09)

After the census above was finished, we queried the official MCP Registry API directly (`https://registry.modelcontextprotocol.io/v0/servers?search=payment&limit=100` and the same with `search=pay`, paginated to completion via `metadata.nextCursor`). This cross-check is counts only; it does not re-score or add any row to `census.csv`.

- Search term `payment`: 244 raw results across 3 pages.
- Search term `pay`: 770 raw results across 8 pages.
- Combined raw results: 1,014. After deduplicating by server `name` (the registry lists multiple versions of the same server as separate entries), **341 distinct server names** matched one of the two search terms.
- Those 341 names span **210 distinct publisher namespaces** (the part of the name before the `/`).
- The largest single namespace is **`app.wishpool`, with 81 of the 341 names (24%)**. Each of these is a per-country templated server (e.g. `app.wishpool/algeria-payments-mcp`, `app.wishpool/brazil-payments-mcp`, `app.wishpool/belgium-payments-mcp`), one server per country wrapping a local payment rail (Chargily Pay, Mercado Pago, Mollie, SSLCommerz, etc.) behind the same description pattern ("… for AI agents — …. Never holds funds."). The next-largest namespaces are `io.github.xpaysh` (12), `io.github.codespar` (11), `io.github.mcp-dir` (5), `io.github.pipeworx-io` (4), `io.github.Rumblingb` (4), and `io.github.noah-silver` (4).
- The raw deduplicated list (name, namespace, description, repository URL where present) is saved as `registry-payment-servers-2026-10-09.csv`. None of these 341 names were added to `census.csv`; this cross-check exists to show how much larger the full registry-matched surface is than the 49-row curated census, and to document the registry's own namespace concentration.

## How Pink was scored

Pink Agentic AI Payments was scored using exactly the same six-dimension rubric and the same "no money moves" standard applied to everyone else, using only the public page `https://pinkwallet.com/agentic/developers/` (fetched directly) and the third-party registry listing at `https://mcpservers.org/servers/pinkwallet-com-agentic-developers` (used only to confirm the listing exists, not for capability claims). Pink's sandbox is explicitly test-money-only ("test credentials only, no money moves"), which is disclosed in the `notes` column of its row, consistent with the task's instruction to be exact and conservative.
