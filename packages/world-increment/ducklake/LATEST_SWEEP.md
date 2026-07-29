# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-29
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 50 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social-graph | 6 (top by activity) |
| wasita | social-graph | 5 |
| DJedamski | social-graph | 3 |
| kristinezheng | social-graph | 2 |
| M1shaaa | social-graph | 2 |
| AustinCStone | social-graph | 4 |
| **TOTAL** | | **225** |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC (trit=0) | #d3869b | 75 |
| PLUS (trit=1) | #b8bb26 | 75 |
| MINUS (trit=-1) | #cc241d | 75 |

### Top Repos by Stars

| Owner | Repo | Language | Stars |
|-------|------|----------|-------|
| kubeflow | kubeflow | — | 15,796 |
| kubeflow | pipelines | Python | 4,171 |
| kubeflow | spark-operator | Python | 3,142 |
| kubeflow | trainer | Go | 2,162 |
| kubeflow | katib | Python | 1,694 |
| kubeflow | examples | Jsonnet | 1,461 |
| kubeflow | community-distribution | YAML | 1,029 |
| kubeflow | arena | Go | 815 |
| migalkin | NodePiece | Python | 144 |
| AustinCStone | TextGAN | Python | 92 |

### Notable Recent Activity (pushed_at)
- `wasita/wasita.github.io` — 2026-07-21 (most recent in social graph)
- `AustinCStone/byteruckus` — 2026-07-15
- `kristinezheng/kristinezheng.github.io` — 2026-07-01
- `TeglonLabs/jank-crane` — 2026-06-08 (crane-jank converged-IR hub, GF3 maps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned 0 APT — these accounts either have no `CoinStore<AptosCoin>` resource initialized (unfunded/uninitialized accounts) or genuinely hold zero.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26) | — | 0.0 each |

**Interpretation:** Accounts exist in the hamming-world keyspace but no on-chain APT balance is registered. Consistent with addresses created locally but never funded on mainnet.

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — responding with `sigs_required = 2`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All contracts require 2-of-N signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

The `testnet.mnx.fi` endpoint returns HTTP 200 but serves a Next.js SPA with no accessible REST API at `/api/markets` or `/api/v1/markets`. Market data is rendered client-side; no structured data could be extracted from server responses. Status: **SPA — data unavailable via curl**.

---

## DuckDB Schema

```
world_increments  — 225 rows (one per repo event, GF3 color-coded)
repo_snapshots    — 225 rows (stars, forks, language, pushed_at)
aptos_snapshots   — 28 rows  (alice, bob, A-Z wallets)
multisig_probes   —  5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     —  0 rows  (SPA, no parseable data)
```
