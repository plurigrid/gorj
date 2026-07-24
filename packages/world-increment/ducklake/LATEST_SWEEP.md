# World-Increment Sweep + Hamming Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24 03:09–03:11 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 11 |
| Total Repo Snapshots (this run) | 323 |
| Total Aptos Wallets Probed | 28 |
| Multisig Contracts Healthy | 5/5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — This Run's 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski | user | -1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | org | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | user | -1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | user | -1 | `#cc241d` | **MINUS** |

---

## Top Repos by Source (2026-07-24 snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| gorj | Clojure | 1 | 2026-07-24 |
| eirobri | Clojure | 0 | 2026-07-21 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,789 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-24 |
| spark-operator | Python | 3,143 | 2026-07-17 |
| trainer | Go | 2,153 | 2026-07-24 |
| katib | Python | 1,692 | 2026-07-22 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### migalkin social graph
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| RWL | Python | 8 |

### AustinCStone
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) probed via Aptos fullnode mainnet.

**Result:** All 28 returned HTTP 404 `resource_not_found` — no `CoinStore<AptosCoin>` registered on any address. Accounts exist on-chain but have never received APT. Recorded as `0.0 APT` in `aptos_snapshots`.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy at 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)
- `https://testnet.mnx.fi/api/markets` → HTTP 404
- Base URL → SPA shell, no market data extractable
- Status: **Unavailable** — 0 rows in `mnx_snapshots`

---

## DuckDB Cumulative Table Summary

| Table | Rows |
|-------|------|
| world_increments | 34 (11 this run, 23 prior) |
| repo_snapshots | 1,267 (323 this run) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

---

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

---

*Previous sweep: 2026-04-12 (471 snapshots)*  
*This sweep: 2026-07-24 (323 new snapshots, +11 GF3 increments)*
