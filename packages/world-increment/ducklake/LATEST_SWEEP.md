# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-08 UTC  
**Branch:** world-increment/sweep  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Captured

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 168 (distinct names) |
| bmorphism | user | 165 |
| kubeflow | org | 51 |
| zubyul | user | 59 |
| TeglonLabs | org | 54 |
| AustinCStone | user | 43 |
| wasita | user | 31 |
| migalkin | user | 30 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |

**Total:** 394 world increment events · 1315 repo snapshot rows in DuckDB

### GF(3) Distribution (balanced)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 131 |
| 1 | #b8bb26 | PLUS | 132 |
| -1 | #cc241d | MINUS | 131 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15768 | — | 2026-07-08 |
| kubeflow/pipelines | 4169 | Python | 2026-07-08 |
| kubeflow/spark-operator | 3135 | Python | 2026-07-08 |
| kubeflow/trainer | 2134 | Go | 2026-07-08 |
| plurigrid/asi | 30 | HTML | 2026-06-29 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| plurigrid/gorj | 1 | Clojure | 2026-07-08 |

### Notable Recent Activity

- **plurigrid/gorj** (Clojure): pushed 2026-07-08 — "forj + Rama topology nREPL routing + GF(3) gay trit coloring"
- **plurigrid/shrimp**: pushed 2026-07-03 — Jank worked example
- **plurigrid/asi** (HTML, ★30): pushed 2026-06-29 — "everything is topological chemputer!"
- **TeglonLabs/jank-crane** (C++): pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **M1shaaa/M1shaaa**: pushed 2026-07-08 (profile config)
- **wasita/wasita.github.io** (Svelte): pushed 2026-07-06

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Status:** All 28 wallets returned HTTP 404 — accounts not found or CoinStore resource not initialized on mainnet.

This indicates the Hamming swarm addresses (alice, bob, A–Z) are not yet funded on Aptos mainnet. All wallets recorded with `balance_apt = NULL` in DuckDB.

| Label | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | N/A (404) |
| bob | 0x0a3c...2d5d | N/A (404) |
| A–Z | (26 addresses) | N/A (404) |

### Multisig Contract Probes

**Status: ALL 5 HEALTHY — 2/2 signatures required** ✓

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig contracts are live on Aptos mainnet with uniform 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — `testnet.mnx.fi` serves a SPA with no JSON API reachable at standard paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`). All paths returned HTTP errors. Recorded 0 market rows.

---

## DuckDB Schema (world-increments.duckdb)

```
world_increments  — 394 rows  (GF3 color-tagged increment events)
repo_snapshots    — 1315 rows (historical repo snapshots)
aptos_snapshots   — 28 rows   (all NULL balance)
multisig_probes   — 5 rows    (all healthy, sigs_required=2)
mnx_snapshots     — 0 rows    (SPA unavailable)
```

---

## Key Signals

1. **Multisig swarm is live** — all 5 pair contracts (A-B, A-G, Y-Z, S-T, V-W) require 2 signatures and are healthy on Aptos mainnet.
2. **Hamming wallets unfunded** — 28 swarm addresses have no APT on mainnet; initialization needed before wallets can participate in swarm operations.
3. **plurigrid/gorj active** — latest push today (2026-07-08), most active of plurigrid repos by recency.
4. **GF(3) balanced** — ERGODIC:PLUS:MINUS = 131:132:131, near-perfect trit distribution across 394 sweep events.
5. **MNX testnet API offline** — market data unavailable; SPA only.
