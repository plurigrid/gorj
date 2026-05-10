# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-10T09:14–09:28 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Increment | Source | Type | GF(3) Trit | Color | Repos |
|-----------|--------|------|-----------|-------|-------|
| 1 | plurigrid | org | +1 PLUS | #b8bb26 | 30 |
| 2 | kubeflow | org | −1 MINUS | #cc241d | 25 |
| 3 | TeglonLabs | org | 0 ERGODIC | #d3869b | 4 |
| 4 | bmorphism | user | +1 PLUS | #b8bb26 | 29 |
| 5 | zubyul | user | −1 MINUS | #cc241d | 23 |
| 6 | social_migalkin | social | 0 ERGODIC | #d3869b | 7 |
| 7 | social_wasita | social | +1 PLUS | #b8bb26 | 6 |
| 8 | social_kristinezheng | social | −1 MINUS | #cc241d | 4 |
| 9 | social_M1shaaa | social | 0 ERGODIC | #d3869b | 2 |
| 10 | social_AustinCStone | social | +1 PLUS | #b8bb26 | 5 |
| 11 | social_DJedamski | social | −1 MINUS | #cc241d | 1 |

**Total:** 11 world-increments · 136 repo snapshots

### GF(3) Color Chain

- `id % 3 == 0` → trit=0 **ERGODIC** `#d3869b` (rose)
- `id % 3 == 1` → trit=+1 **PLUS** `#b8bb26` (yellow-green)
- `id % 3 == 2` → trit=−1 **MINUS** `#cc241d` (red)

### Notable Repos by Language (star-weighted)

| Language | Total Stars | Repos |
|----------|-------------|-------|
| Python | 31,117 | 191 |
| Go | 11,749 | 44 |
| Jsonnet | 7,123 | 20 |
| TypeScript | 863 | 30 |
| HTML | 690 | 43 |
| JavaScript | 166 | 43 |

### Highlights

- **kubeflow/kubeflow**: 15,628 ⭐ — Machine Learning Toolkit for Kubernetes
- **kubeflow/pipelines**: 4,137 ⭐ — ML Pipelines
- **kubeflow/trainer**: 2,097 ⭐ — Distributed AI Training
- **kubeflow/spark-operator**: 3,125 ⭐ — Spark on Kubernetes
- **bmorphism/Gay.jl**: active today (2026-05-10), 187 open issues — wide-gamut GF(3) color sampling
- **plurigrid/gorj**: active today — forj + Rama topology nREPL + GF(3) trit coloring
- **migalkin/NodePiece**: 144 ⭐ — Parameter-Efficient KG Representations (ICLR'22)
- **migalkin/StarE**: 89 ⭐ — Hyper-Relational KG message passing (EMNLP'20)
- **bmorphism/ocaml-mcp-sdk**: 61 ⭐ — OCaml SDK for MCP using oxcaml_effect

### GitHub API Note

Public REST API rate-limited (60 req/hr, unauthenticated). Repo data collected via GitHub MCP search tools with authenticated token.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (alice, bob, A–Z)

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | — no CoinStore |
| bob | 0x0a3c…512d | — no CoinStore |
| A | 0x8699…b97a | — no CoinStore |
| B | 0x3f89…b13 | — no CoinStore |
| C | 0x38b9…35e | — no CoinStore |
| D | 0xf776…dd1 | — no CoinStore |
| E | 0xdc1d…d36 | — no CoinStore |
| F | 0x18a1…f71 | — no CoinStore |
| G | 0x69a3…f32 | — no CoinStore |
| H | 0xce67…00f | — no CoinStore |
| I | 0x070f…c9 | — no CoinStore |
| J | 0x4d96…f54 | — no CoinStore |
| K | 0xa732…dc4 | — no CoinStore |
| L | 0x7c2e…ba9 | — no CoinStore |
| M | 0x6fed…e9 | — no CoinStore |
| N | 0xe7dd…2c | — no CoinStore |
| O | 0x7325…89d | — no CoinStore |
| P | 0x6218…948 | — no CoinStore |
| Q | 0xac40…9a9 | — no CoinStore |
| R | 0x7ce6…e10 | — no CoinStore |
| S | 0xb875…386 | — no CoinStore |
| T | 0x3578…588 | — no CoinStore |
| U | 0x7586…956 | — no CoinStore |
| V | 0xb59d…c3 | — no CoinStore |
| W | 0x5f32…b0 | — no CoinStore |
| X | 0xa95c…47d | — no CoinStore |
| Y | 0xd8e3…4c4 | — no CoinStore |
| Z | 0x7af0…97c | — no CoinStore |

All 28 addresses return HTTP 404 for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts are registered on-chain but hold no APT (unfunded or pure contract accounts).

### Multisig Contract Probes (Aptos mainnet)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…003 | 2 | ✓ |
| A-G | 0xf56c…096 | 2 | ✓ |
| Y-Z | 0xd3ff…883 | 2 | ✓ |
| S-T | 0x3b1c…883 | 2 | ✓ |
| V-W | 0x40fa…b6d | 2 | ✓ |

All 5 multisig contracts respond correctly with threshold **2-of-2**. All healthy.

### MNX Testnet Markets

`https://testnet.mnx.fi` is a **Next.js SPA** — no server-rendered JSON API found at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Market data unavailable without browser-side JS execution. Recorded as sentinel in `mnx_snapshots`.

---

## DuckDB Table Summary

```sql
-- world_increments:  11 rows  (one per source swept)
-- repo_snapshots:   136 rows  (repos across all sources)
-- aptos_snapshots:   28 rows  (alice, bob, A–Z; all NULL balance)
-- multisig_probes:    5 rows  (A-B, A-G, Y-Z, S-T, V-W; all 2-of-2 healthy)
-- mnx_snapshots:      1 row   (sentinel: SPA, no JSON API)
```
