# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-09  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 50 |
| kubeflow | org | 50 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 50 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 14 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,808 | — | 2026-07-10 |
| kubeflow/pipelines | 4,180 | Python | 2026-08-09 |
| kubeflow/spark-operator | 3,146 | Python | 2026-08-08 |
| kubeflow/trainer | 2,177 | Go | 2026-08-08 |
| kubeflow/katib | 1,694 | Python | 2026-08-06 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 60 | HTML | 2026-07-10 |

### Most Active (pushed 2026-08-09)

- **plurigrid/gorj** — 1,747 open issues, Clojure, GF(3) REPL orchestration
- **plurigrid/place** — TeX
- **kubeflow/mpi-operator** — Go, pushed 2026-08-09T13:46
- **kubeflow/hub** — Go model registry, pushed 2026-08-09T13:25
- **kubeflow/pipelines** — Python, pushed 2026-08-09T07:28
- **wasita/xoxowasita-analysis** — Python, pushed 2026-08-06
- **wasita/wm-cv** — Svelte CV, pushed 2026-08-07

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 27 |
| -1 | `#cc241d` | MINUS | 27 |
| 0 | `#d3869b` | ERGODIC | 25 |

### DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 79 |
| repo_snapshots | 1,000 (490 distinct repos, cumulative across runs) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, 2026-08-09)

All 28 Hamming swarm addresses (alice, bob, A–Z) queried against Aptos mainnet.  
**Result: All returned 0.0 APT** — accounts do not hold APT CoinStore on mainnet (may be fresh/unfunded addresses or APT held in other resource types).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| ... (24 more) | | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 pairs, 2026-08-09)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.  
**All healthy — 2-of-N threshold confirmed.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `https://testnet.mnx.fi` is a Next.js SPA. The root HTML loads (62,957 bytes) but all market data is fetched client-side via JavaScript. API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` return no JSON. No market data could be extracted from a server-side probe.  
`mnx_snapshots` table left empty for this run.

---

## Summary

- **GitHub:** Snapshotted 56 repos this run across 11 sources (3 orgs + 2 primary users + 6 social graph nodes). DB cumulative total: 1,000 repo_snapshot rows (490 distinct).
- **Aptos Hamming swarm:** All 28 wallets show 0 APT (unfunded or non-APT holding). 5/5 multisig pairs healthy at 2-sig threshold.
- **MNX:** SPA blocks server-side data extraction; marked unavailable.
- **GF(3) chain:** 79 world_increment events, balanced across ERGODIC/PLUS/MINUS.
