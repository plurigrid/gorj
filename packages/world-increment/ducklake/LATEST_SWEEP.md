# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-17  
**Agent:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources swept

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 106) |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 12 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 30+ |

**Total repos captured this sweep:** 322+

### GF(3) Color Chain (increment IDs)

| id%3 | trit | color | name |
|------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

### Notable repos (>50 stars)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,779 | — |
| kubeflow/pipelines | 4,167 | Python |
| kubeflow/spark-operator | 3,138 | Python |
| kubeflow/trainer | 2,151 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### Recently active (zubyul social graph)
- `wasita/wasita.github.io` pushed 2026-07-16 (Svelte personal site)
- `wasita/pnas-typst-template` created 2026-07-16
- `wasita/wm-cv` pushed 2026-07-14
- `AustinCStone/byteruckus` pushed 2026-07-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A-Z + alice/bob)

**All 28 addresses returned resource_not_found** on Aptos mainnet ledger v6324499091.  
These accounts do not have an initialized 0x1::coin::CoinStore<AptosCoin> resource —  
the addresses exist in the spec but have not been funded on mainnet.

| World | Address (prefix) | APT Balance |
|-------|-----------------|------------|
| alice | 0xc793... | NOT_FOUND |
| bob | 0x0a3c... | NOT_FOUND |
| A-Z (all 26) | 0x8699...0x7af0... | NOT_FOUND |

### Multisig Contract Probes

All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4... | 2 | YES |
| A-G | 0xf56c... | 2 | YES |
| Y-Z | 0xd3ff... | 2 | YES |
| S-T | 0x3b1c... | 2 | YES |
| V-W | 0x40fa... | 2 | YES |

**All 5 multisig contracts healthy (2-of-2 threshold).**

### MNX Markets (testnet.mnx.fi)

Testnet is a **password-protected Vercel deployment** (HTTP 401).  
No market data available — all API paths (/api/markets, /api/v1/markets, /api/tickers) return:
{"error":{"code":"401","message":"Protected deployment"}}

---

## DuckDB Ducklake State

File: packages/world-increment/ducklake/world-increments.duckdb

| Table | Rows (cumulative) |
|-------|------------------|
| world_increments | 34 |
| repo_snapshots | 1,266 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## Summary

- **GitHub sweep:** 322 repos from 11 sources (3 orgs + 2 primary users + 6 social graph), stored with GF(3) color chain annotation.
- **Aptos swarm:** 28/28 addresses unfunded on mainnet; 5/5 multisig contracts live and healthy (2-of-2).
- **MNX:** Testnet unavailable (password-protected Vercel deployment).
