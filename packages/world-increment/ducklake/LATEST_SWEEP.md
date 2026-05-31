# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-31T21:28:52Z  
**Branch:** world-increment/sweep-2026-05-31-2128  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 50 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| AustinCStone | user (social) | 30 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 6 |
| **Total** | | **383 repos** |

### DuckDB Schema

- `world_increments` — 381 rows, GF(3) trit-colored increment chain
- `repo_snapshots` — 381 rows, full repo metadata
- `aptos_snapshots` — 28 rows, Hamming swarm wallet balances
- `multisig_probes` — 5 rows, multisig contract health
- `mnx_snapshots` — 0 rows (MNX testnet SPA, no public REST API)

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 127 |
| 1 | #b8bb26 | PLUS | 127 |
| -1 | #cc241d | MINUS | 127 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,695 | — |
| kubeflow/pipelines | 4,149 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,109 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| kubeflow/manifests | 1,019 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| migalkin/NodePiece | 144 | Python |

### Notable Plurigrid Repos

| Repo | Issues | Notes |
|------|--------|-------|
| plurigrid/gorj | 280 | forj + Rama topology nREPL — most active |
| plurigrid/eirobri | 28 | EiRoBri replay world |
| plurigrid/asi | 23★ | everything is topological chemputer! |
| plurigrid/ontology | 8★ | autopoietic ergodicity and embodied gradualism |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com`. All wallets returned **0 APT** — accounts exist but hold no CoinStore resource for APT (likely empty or unregistered for APT coin type).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (24 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisig contracts are **healthy** with 2-of-N signature requirement.

### MNX Markets (testnet.mnx.fi)

Site is a **Next.js SPA** — no public REST API endpoints found at `/api/markets` or `/api/v1/markets`. Market data is client-side rendered. Status: **unavailable via API**.

---

## DuckDB Query Examples

```sql
-- Top repos by stars
SELECT full_name, stars, language
FROM repo_snapshots
ORDER BY stars DESC LIMIT 10;

-- GF3 chain for plurigrid
SELECT id, gf3_name, gf3_color, repo_name
FROM world_increments
WHERE source_name = 'plurigrid'
ORDER BY id;

-- Aptos swarm snapshot
SELECT world, address, balance_apt
FROM aptos_snapshots;

-- Multisig health check
SELECT pair, sigs_required, healthy
FROM multisig_probes;
```
