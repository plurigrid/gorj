# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-08

## Sweep Metadata
- **Date:** 2026-06-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 (101 total) |
| bmorphism | user | 100 (103 total) |
| kubeflow | org | 30 (48 total, top by activity/stars) |
| zubyul | user | 19 public repos |
| TeglonLabs | user | 5 |
| migalkin | user | 10 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 10 |
| **TOTAL** | | **234 repo snapshots** |

### Top Repos by Stars (GF3 colored)
| Repo | Stars | Language | GF3 | Color |
|------|-------|----------|-----|-------|
| kubeflow/kubeflow | 15,707 | — | MINUS | #cc241d |
| kubeflow/pipelines | 4,152 | Python | ERGODIC | #d3869b |
| kubeflow/spark-operator | 3,126 | Python | PLUS | #b8bb26 |
| kubeflow/trainer | 2,112 | Go | MINUS | #cc241d |
| kubeflow/katib | 1,685 | Python | ERGODIC | #d3869b |
| kubeflow/examples | 1,462 | Jsonnet | ERGODIC | #d3869b |
| kubeflow/manifests | 1,020 | YAML | PLUS | #b8bb26 |
| kubeflow/arena | 812 | Go | MINUS | #cc241d |
| kubeflow/kale | 691 | Python | PLUS | #b8bb26 |
| kubeflow/mpi-operator | 528 | Go | MINUS | #cc241d |
| AustinCStone/TextGAN | 92 | Python | ERGODIC | #d3869b |
| migalkin/NodePiece | 144 | Python | PLUS | #b8bb26 |
| migalkin/StarE | 89 | Python | MINUS | #cc241d |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | PLUS | #b8bb26 |
| plurigrid/asi | 25 | HTML | ERGODIC | #d3869b |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | ERGODIC | #d3869b |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | MINUS | #cc241d |

### Notable Activity (High Open Issues)
| Repo | Open Issues | Notes |
|------|------------|-------|
| plurigrid/gorj | 438 | this repo — forj + Rama + GF(3) |
| kubeflow/docs-agent | 151 | AI Documentation Agent |
| kubeflow/sdk | 137 | Universal Python SDK |
| bmorphism/Gay.jl | 189 | Wide-gamut color sampling (very active!) |
| plurigrid/eirobri | 29 | EiRoBri replay world |

### GF(3) Color Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 78 |
| 1 | PLUS | #b8bb26 | 78 |
| -1 | MINUS | #cc241d | 78 |

Perfectly balanced: 234 increments = 78 × 3 full GF(3) cycles.

### Top Pushed Since Last Sweep (2026-04-12 → 2026-06-08)
| Repo | Pushed | Source |
|------|--------|--------|
| TeglonLabs/jank-crane | 2026-06-08 | crane-jank converged-IR hub with GF3 |
| plurigrid/gorj | 2026-06-08 | this repo |
| kubeflow/hub | 2026-06-08 | Model Registry |
| kubeflow/kubeflow | 2026-06-08 | flagship |
| bmorphism/Gay.jl | 2026-06-08 | 189 open issues! |
| kubeflow/pipelines | 2026-06-07 | ML pipelines |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode.

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Accounts exist on-chain but have not initialized an APT CoinStore (or hold tokens via an alternate path).
**Recorded balance: 0.0 APT** for all 28 addresses in `aptos_snapshots`.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793ac...cc7b | 0.0 |
| bob | 0x0a3c00...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — All 5/5 Healthy ✓
All 5 contracts responded to `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f4...7003 | 2 | ✓ |
| A-G | 0xf56c4a...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

All pairwise multisigs require 2-of-N. Swarm topology is intact.

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Protected by Vercel deployment authentication. All API paths (`/`, `/api/markets`, `/api/v1/markets`) return auth challenge. No market data extractable without bypass token. `mnx_snapshots` table is empty.

---

## DuckDB Tables Summary
| Table | Rows |
|-------|------|
| world_increments | 234 |
| repo_snapshots | 234 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Query Examples
```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color distribution
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY ALL;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos swarm (all 0 APT — no CoinStore resource found)
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;

-- Recently pushed repos
SELECT full_name, pushed_at FROM repo_snapshots
WHERE pushed_at > '2026-06-01' ORDER BY pushed_at DESC;
```
