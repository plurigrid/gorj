# World Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 49 |
| zubyul | user | 19 |
| migalkin | user | 100 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |
| **Total** | | **391** |

### Top Starred Repos

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,760 | — |
| kubeflow/pipelines | 4,168 | Python |
| kubeflow/spark-operator | 3,132 | Python |
| kubeflow/trainer | 2,129 | Go |
| kubeflow/katib | 1,688 | Python |
| kubeflow/examples | 1,460 | Jsonnet |
| kubeflow/community-distribution | 1,028 | YAML |
| kubeflow/arena | 814 | Go |
| kubeflow/kale | 694 | Python |
| kubeflow/mpi-operator | 529 | Go |

### Notable Recent Activity

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **TeglonLabs/mathpix-gem** (Ruby, pushed 2026-01-01): 2 stars, 11 open issues
- **M1shaaa/M1shaaa** — pushed 2026-07-03 (today)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01
- **wasita/wasita.github.io** (Svelte) — pushed 2026-07-02

### GF(3) Color Chain Distribution

| Name | Color | Trit | Count |
|------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 130 |
| PLUS | #b8bb26 | +1 | 131 |
| MINUS | #cc241d | -1 | 130 |

Chain rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried via Aptos fullnode mainnet.  
**All balances: 0.0 APT** — CoinStore resources absent or zero for each address at time of sweep.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793acde... | 0.0 |
| bob | 0x0a3c00c5... | 0.0 |
| A–Z | 0x8699edc0...–0x7af0ef6e... | 0.0 each |

### Multisig Contract Probes

All probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

All 5 multisigs healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — protected by Vercel deployment authentication.  
API paths `/api/markets` and `/api/v1/markets` return auth wall. No market data extracted.

---

## DuckDB Schema Summary

```
world_increments  — 391 rows  (GF3-labeled GitHub repo events)
repo_snapshots    — 391 rows  (repo metadata: stars, forks, language, pushed_at)
aptos_snapshots   —  28 rows  (Hamming world wallet balances, all 0.0 APT)
multisig_probes   —   5 rows  (A-B, A-G, Y-Z, S-T, V-W; all healthy sigs=2)
mnx_snapshots     —   0 rows  (unavailable — Vercel auth)
```
