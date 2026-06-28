# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-28  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources & GF(3) Color Chain

| id | Source | Type | GF3 Trit | GF3 Name | Color | Repos |
|----|--------|------|----------|----------|-------|-------|
| 1 | plurigrid | org | 1 | PLUS | #b8bb26 | 100 |
| 2 | kubeflow | org | 2 | MINUS | #cc241d | 48 |
| 3 | TeglonLabs | org | 0 | ERGODIC | #d3869b | 5 |
| 4 | bmorphism | user | 1 | PLUS | #b8bb26 | 100 |
| 5 | zubyul | user | 2 | MINUS | #cc241d | 49 |
| 6 | migalkin | user | 0 | ERGODIC | #d3869b | 19 |
| 7 | wasita | user | 1 | PLUS | #b8bb26 | 11 |
| 8 | kristinezheng | user | 2 | MINUS | #cc241d | 3 |
| 9 | M1shaaa | user | 0 | ERGODIC | #d3869b | 2 |
| 10 | DJedamski | user | 1 | PLUS | #b8bb26 | 1 |
| 11 | AustinCStone | user | 2 | MINUS | #cc241d | 30 |

**Total: 11 increments, 368 repo snapshots**

### Top Languages (across all repos)

| Language | Repos |
|----------|-------|
| Python | 75 |
| Rust | 26 |
| JavaScript | 24 |
| TypeScript | 23 |
| HTML | 16 |
| Go | 15 |
| Jupyter Notebook | 14 |
| Clojure | 14 |
| Julia | 9 |
| Jsonnet | 7 |

### Notable Repos by Stars

| Source | Repo | Stars | Language | Last Push |
|--------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,751 | — | 2026-06-18 |
| kubeflow | pipelines | 4,159 | Python | 2026-06-27 |
| kubeflow | spark-operator | 3,129 | Python | 2026-06-26 |
| TeglonLabs | mathpix-gem | 2 | Ruby | 2026-01-01 |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (C++): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" — pushed 2026-06-08
- **wasita/wasita.github.io** (Svelte): personal website pushed 2026-06-25
- **kristinezheng/kristinezheng.github.io** (HTML): pushed 2026-06-07
- **M1shaaa/M1shaaa**: profile repo pushed 2026-06-28 (today)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 Hamming-swarm addresses probed via Aptos fullnode API.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | unfunded (no coin store) |
| bob | 0.0 | unfunded (no coin store) |
| A–Z (26 addresses) | 0.0 each | unfunded (no coin stores) |

**All 28 addresses exist on-chain but have no initialized APT CoinStore resource.** The accounts are uninitialized / zero-balance as of ledger version ~5.98B.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts healthy: 2-of-2 threshold, all responsive.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Vercel deployment protection requires authentication (password or bypass token). No market data extracted.

---

## DuckDB Schema

```
world_increments  — 11 rows (GF3 color-coded source increments)
repo_snapshots    — 368 rows (org/user repo metadata)
aptos_snapshots   — 28 rows (Hamming swarm balances)
multisig_probes   — 5 rows (2-of-2 multisig health checks)
mnx_snapshots     — 1 row (unavailable placeholder)
```
