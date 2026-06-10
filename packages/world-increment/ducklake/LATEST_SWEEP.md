# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-10  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 15 (sample) |
| zubyul | user | 8 (sample) |
| migalkin | social graph | 5 (sample) |
| AustinCStone | social graph | 3 (sample) |
| wasita | social graph | 3 (sample) |
| DJedamski | social graph | 3 (sample) |
| kristinezheng | social graph | 2 (sample) |
| M1shaaa | social graph | 2 (sample) |
| **Total** | | **194** |

### Notable Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,713 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-09 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,112 | Go | 2026-06-09 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |

### Most Active (Recent Push)
| Repo | Pushed | Issues |
|------|--------|--------|
| plurigrid/gorj | 2026-06-10 | 468 |
| kubeflow/hub | 2026-06-09 | 44 |
| kubeflow/pipelines | 2026-06-09 | 494 |
| TeglonLabs/jank-crane | 2026-06-08 | 0 |
| kristinezheng/kristinezheng.github.io | 2026-06-07 | 0 |
| wasita/wasita.github.io | 2026-06-01 | 8 |

### GF(3) World Increment Distribution (194 total)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 64 |
| 1 | #b8bb26 | PLUS | 65 |
| -1 | #cc241d | MINUS | 65 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Query timestamp:** 2026-06-10  
**Method:** `/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses returned `resource_not_found` — accounts exist on-chain but have no APT CoinStore
resource (unfunded or never received APT deposits).

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | resource_not_found |
| bob | 0.0 | resource_not_found |
| A–Z (26 addrs) | 0.0 each | resource_not_found |

**Total APT across swarm:** 0.0

### Multisig Contract Probes
| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

All 5 multisig contracts are live on Aptos mainnet, each configured as **2-of-N threshold**.

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE — Vercel deployment protection requires authentication. `mnx_snapshots` table is empty.

---

## DuckDB Schema Summary
**File:** `packages/world-increment/ducklake/world-increments.duckdb`
**Engine:** DuckDB v1.5.3

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 194 | GF(3)-colored increment log |
| `repo_snapshots` | 194 | GitHub repo metadata |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Aptos multisig contract probes |
| `mnx_snapshots` | 0 | MNX market data (unavailable) |

### Example Queries
```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color spread
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1,2;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos swarm total
SELECT SUM(balance_apt) total_apt, COUNT(*) wallets FROM aptos_snapshots;
```
