# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 14 Increments (this sweep)

| ID | GF(3) | Source | Type | Repos |
|----|-------|--------|------|-------|
| 1  | #b8bb26 PLUS | plurigrid | org | 100 |
| 2  | #cc241d MINUS | kubeflow | org | 10 (top by activity) |
| 3  | #d3869b ERGODIC | TeglonLabs | org | 5 |
| 4  | #b8bb26 PLUS | bmorphism | user | 8 |
| 5  | #cc241d MINUS | zubyul | user | 5 |
| 6  | #d3869b ERGODIC | migalkin | user | 4 |
| 7  | #b8bb26 PLUS | DJedamski | user | 2 |
| 8  | #cc241d MINUS | wasita | user | 3 |
| 9  | #d3869b ERGODIC | kristinezheng | user | 2 |
| 10 | #b8bb26 PLUS | M1shaaa | user | 2 |
| 11 | #cc241d MINUS | AustinCStone | user | 3 |
| 12 | #d3869b ERGODIC | hamming-swarm | aptos | 28 addresses |
| 13 | #b8bb26 PLUS | multisig | aptos | 5 contracts |
| 14 | #cc241d MINUS | testnet.mnx.fi | mnx | unavailable |

### Top Repos by Source (2026-08-03 snapshot)

**plurigrid** (100 repos):
| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| gorj | Clojure | 1 | 2026-07-29 |
| asi | HTML | 58 | 2026-08-01 |
| zig-syrup | Zig | 2 | 2026-07-28 |
| nash-portal | Rust | 2 | 2026-05-19 |

**kubeflow** (49 total, top by activity):
| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| kubeflow | — | 15,803 | 2026-08-01 |
| pipelines | Python | 4,173 | 2026-08-01 |
| spark-operator | Python | 3,142 | 2026-08-01 |
| katib | Python | 1,694 | 2026-08-01 |
| trainer | Go | 2,165 | 2026-07-31 |
| mcp-apache-spark-history-server | Python | 185 | 2026-08-01 |

**bmorphism** (106 total):
| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-08-02 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| Gay.jl | Julia | 2 | 2026-07-21 |

**zubyul social graph highlights**:
| User | Notable Repo | Stars |
|------|-------------|-------|
| migalkin | NodePiece (ICLR'22 KG embeddings) | 144 |
| AustinCStone | TextGAN (GAN for text) | 92 |
| migalkin | StarE (EMNLP'20 hyper-relational KGs) | 89 |
| wasita | magic-garden | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 hamming-swarm addresses queried against Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).

**Result: All 28 addresses return 0 APT** — no `CoinStore<AptosCoin>` resource found on mainnet.
Addresses (alice, bob, A–Z) appear to be testnet/devnet accounts or unfunded mainnet accounts.

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required` called for all 5 pairs:

| Pair | Address (truncated) | sigs_required | Status |
|------|---------------------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ HEALTHY |
| A-G | `0xf56c4a1c...c0096` | 2 | ✓ HEALTHY |
| Y-Z | `0xd3ffe181...5b883` | 2 | ✓ HEALTHY |
| S-T | `0x3b1c3ae9...d7883` | 2 | ✓ HEALTHY |
| V-W | `0x40fad7b4...0eb6d` | 2 | ✓ HEALTHY |

All 5 multisig contracts healthy (2-of-N configurations).

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **HTTP 404**. Base URL serves bare SPA. No market data extractable. `mnx_snapshots` table: 0 rows.

---

## DuckDB Cumulative State

| Table | Rows (total) | New this sweep |
|-------|-------------|----------------|
| world_increments | 37 | 14 |
| repo_snapshots | 1088 | 144 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 0 | 0 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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
