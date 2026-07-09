# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-09

## Sweep Metadata
- **Date:** 2026-07-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 324 |
| Cumulative World Increments | 347 |
| New Repo Snapshots (this run) | 324 |
| Cumulative Repo Snapshots | 1,268 |
| Sources Covered | 3 orgs + 8 users |

### Sources Scanned

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 162 |
| kubeflow | org | 49 | ~102k |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 509 |
| zubyul | user | 49 | 40 |
| migalkin | social graph | 19 | 830 |
| wasita | social graph | 11 | 10 |
| AustinCStone | social graph | 40 | 319 |
| M1shaaa | social graph | 8 | 0 |
| DJedamski | social graph | 6 | 16 |
| kristinezheng | social graph | 5 | 0 |
| **TOTAL** | | **324** | |

### Top Repos by Stars
1. `kubeflow/kubeflow` — 15,768 ⭐ (ML platform for Kubernetes)
2. `kubeflow/pipelines` — 4,169 ⭐ (pushed 2026-07-09)
3. `kubeflow/spark-operator` — 3,136 ⭐
4. `migalkin/NodePiece` — 144 ⭐ (ICLR'22 KG embeddings)
5. `AustinCStone/TextGAN` — 92 ⭐
6. `migalkin/StarE` — 89 ⭐ (EMNLP 2020)
7. `plurigrid/asi` — 30 ⭐ (topological chemputer)

### Notable Recent Activity (2026-07)
- `plurigrid/gorj` pushed **2026-07-09** — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `wasita/wasita.github.io` pushed **2026-07-06** — personal website (Svelte)
- `plurigrid/place` pushed **2026-07-07**
- `kristinezheng/kristinezheng.github.io` pushed **2026-07-01**
- `plurigrid/shrimp` pushed **2026-07-03** — Jank worked example

### GF(3) Trit Chain Distribution (this run)
| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 116 |
| -1 | `#cc241d` | MINUS | 116 |
| 0 | `#d3869b` | ERGODIC | 115 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**Ledger version at query time:** 6,195,763,468  
**Status:** All return `resource_not_found` for `CoinStore<AptosCoin>` — accounts not initialized with APT.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I–Z | ... | 0.0 each |

**Interpretation:** CoinStore is initialized on first APT deposit; these accounts have not received any APT yet.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-2 threshold, all responding.**

### MNX Markets

`https://testnet.mnx.fi` returned **HTTP 401** (authentication required).  
API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` all unavailable.  
No market data captured this sweep.

---

## DuckDB Tables Summary

```
world_increments   : 347 rows  (GF3-colored event log, cumulative)
repo_snapshots     : 1,268 rows (GitHub repo metadata, cumulative)
aptos_snapshots    : 28 rows   (Hamming swarm A–Z + alice + bob, this run)
multisig_probes    : 5 rows    (2-of-2 threshold, all healthy, this run)
mnx_snapshots      : 0 rows    (unavailable: HTTP 401)
```

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
