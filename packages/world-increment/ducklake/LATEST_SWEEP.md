# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 sources (GF3 × 4 cycles) |
| Total Repo Snapshots | 1019 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice + bob + A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (auth required) |

---

## GF(3) Color Chain — 12 Sources

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| 12 | (sweep complete) | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) cycle: PLUS → MINUS → ERGODIC (repeating × 4)

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 213 |
| bmorphism | user | 215 |
| TeglonLabs | org | 111 |
| kubeflow | org | 108 |
| AustinCStone | user | 90 |
| migalkin | user | 65 |
| wasita | user | 65 |
| zubyul | user | 56 |
| kristinezheng | user | 38 |
| M1shaaa | user | 34 |
| DJedamski | user | 24 |
| **TOTAL** | | **1019** |

### Top Repos by Stars

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,764 | 2026-06-18 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-05 |
| kubeflow/spark-operator | Python | 3,132 | 2026-07-02 |
| kubeflow/trainer | Go | 2,129 | 2026-07-03 |
| kubeflow/katib | Python | 1,689 | 2026-07-01 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| plurigrid/asi | HTML | 28 | 2026-06-29 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

### Most Active (pushed 2026-07-06)
- **plurigrid/gorj** — 1006 open issues — forj + Rama topology nREPL + GF(3)
- **plurigrid/place** — TeX/forester forest

### Zubyul Social Graph

| Handle | Domain | Notable |
|--------|--------|---------|
| migalkin | KG/ML research | NodePiece, StarE |
| wasita | network neuroscience | voice-observatory |
| kristinezheng | cognitive science (MIT) | lookit-jenga |
| M1shaaa | lab researcher (Yale) | lab-bookshelf- |
| AustinCStone | ML/CV engineer | TextGAN, StereoVisionMRF |
| DJedamski | data scientist | kaggle_ncaa18 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

**Result:** All 28 return `resource_not_found`. No APT CoinStore on mainnet for any address. Likely unfunded/testnet addresses.

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…003 | 2 | HEALTHY |
| A-G | 0xf56c…096 | 2 | HEALTHY |
| Y-Z | 0xd3ff…883 | 2 | HEALTHY |
| S-T | 0x3b1c…883 | 2 | HEALTHY |
| V-W | 0x40fa…eb6d | 2 | HEALTHY |

All 5 multisig pairs require 2-of-N signatures. All live on Aptos mainnet.

### MNX Testnet Markets

**Status:** UNAVAILABLE — `https://testnet.mnx.fi` returns `Authentication Required` for all API paths. No market data extracted.

---

## Schema Reference

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name, source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Rule
- id%3==0 → trit=0, #d3869b, ERGODIC
- id%3==1 → trit=+1, #b8bb26, PLUS
- id%3==2 → trit=-1, #cc241d, MINUS

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-06*
