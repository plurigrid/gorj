# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-05T13:10Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | Org | 100 |
| kubeflow | Org | 48 |
| TeglonLabs | Org | 4 |
| bmorphism | User | 100 |
| zubyul | User | 49 |
| migalkin | Social graph | 19 |
| wasita | Social graph | 11 |
| AustinCStone | Social graph | 30 |
| DJedamski | Social graph | 6 |
| kristinezheng | Social graph | 5 |
| M1shaaa | Social graph | 8 |
| **TOTAL** | | **380** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 126 |
| 1 | `#b8bb26` | PLUS | 127 |
| -1 | `#cc241d` | MINUS | 127 |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,706 | — |
| kubeflow | pipelines | 4,152 | Python |
| kubeflow | spark-operator | 3,125 | Python |
| kubeflow | trainer | 2,111 | Go |
| kubeflow | katib | 1,684 | Python |
| kubeflow | examples | 1,462 | Jsonnet |
| kubeflow | manifests | 1,020 | YAML |
| kubeflow | arena | 811 | Go |
| kubeflow | kale | 690 | Python |
| kubeflow | mpi-operator | 528 | Go |

### TeglonLabs Repos

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 wallets (alice, bob, A–Z) via Aptos fullnode mainnet API.

| Result | Count |
|--------|-------|
| Wallets queried | 28 |
| Wallets with balance > 0 APT | 0 |
| Wallets with 0 APT (empty/unregistered CoinStore) | 28 |

All addresses returned 0 APT — accounts either have no APT CoinStore registered or hold zero balance on mainnet.

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | yes |
| A-G | `0xf56c4a1c...c0096` | 2 | yes |
| Y-Z | `0xd3ffe181...b883` | 2 | yes |
| S-T | `0x3b1c3ae9...7883` | 2 | yes |
| V-W | `0x40fad7b4...eb6d` | 2 | yes |

All 5/5 multisig contracts healthy — each requires 2-of-N signatures.

### MNX Markets

**Status: Unavailable** — `https://testnet.mnx.fi` is protected by Vercel deployment authentication. API endpoints `/api/markets` and `/api/v1/markets` returned auth-wall HTML (not JSON). No market data extracted. No rows inserted into `mnx_snapshots`.

---

## DuckDB Schema Summary

| Table | Rows |
|-------|------|
| `world_increments` | 380 |
| `repo_snapshots` | 380 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (unavailable) |

### Sample DuckDB Queries

```sql
-- Top repos by stars
SELECT org_or_user, repo_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) trit distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color;

-- Aptos swarm status
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
