# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-29  
**Branch:** `world-increment/sweep-2026-07-29-0707`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.5 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 2 |
| wasita | user (social) | 4 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 3 |
| **TOTAL** | | **321 repos** |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,794 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-25 |
| kubeflow/trainer | 2,160 | Go | 2026-07-27 |
| kubeflow/katib | 1,693 | Python | 2026-07-26 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-28 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |

### Language Distribution (Top 10)

| Language | Repos |
|----------|-------|
| Python | 54 |
| Rust | 25 |
| TypeScript | 22 |
| JavaScript | 20 |
| HTML | 16 |
| Go | 15 |
| Clojure | 14 |
| Jupyter Notebook | 13 |
| Julia | 9 |
| Zig | 7 |

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski | user | −1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | org | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | user | −1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin | user | −1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | user | −1 | `#cc241d` | **MINUS** |

GF(3) rule: `id%3==1 → PLUS (+1 / #b8bb26)`, `id%3==2 → MINUS (−1 / #cc241d)`, `id%3==0 → ERGODIC (0 / #d3869b)`

### Notable Activity (2026-07)
- **kubeflow/arena** — pushed 2026-07-29 06:03 UTC (most recent kubeflow push)
- **kubeflow/hub** — pushed 2026-07-29 06:05 UTC
- **kubeflow/pipelines** — pushed 2026-07-29 00:30 UTC
- **wasita/wasita.github.io** — pushed 2026-07-21 (Svelte personal site)
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (crane-jank converged-IR hub, GF3 convergence maps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned  
`resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
on Aptos mainnet (ledger version ~6,507,521,714).

**Status:** All accounts uninitialized / no APT CoinStore registered.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | null |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | null |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | null |
| B–Z | (see aptos_snapshots table) | null |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts responded healthy:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

**All 5 multisig contracts live and require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no static JSON API endpoint responded.  
Market data unavailable via direct REST probe; requires browser rendering.

**Status:** SPA — data unavailable via REST.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| `world_increments` | 11 |
| `repo_snapshots` | 321 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (SPA, no REST data) |

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
