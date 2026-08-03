# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (This Run)

| Metric | Value |
|--------|-------|
| New World Increments | 83 |
| Repo Snapshots (cumulative) | 1,027 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| GF3 ERGODIC | 34 |
| GF3 PLUS | 36 |
| GF3 MINUS | 36 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 20 |
| kubeflow | org | 15 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 |
| zubyul | user | 9 |
| migalkin | user (zubyul social) | 7 |
| wasita | user (zubyul social) | 4 |
| DJedamski | user (zubyul social) | 4 |
| kristinezheng | user (zubyul social) | 2 |
| M1shaaa | user (zubyul social) | 2 |
| AustinCStone | user (zubyul social) | 5 |
| **TOTAL** | | **83 repos this run** |

### Top Repos by Stars (This Run)

| Repo | Stars | Language | Source |
|---|---|---|---|
| kubeflow/kubeflow | 15,803 | — | org:kubeflow |
| kubeflow/pipelines | 4,173 | Python | org:kubeflow |
| kubeflow/spark-operator | 3,142 | Python | org:kubeflow |
| kubeflow/trainer | 2,165 | Go | org:kubeflow |
| kubeflow/katib | 1,694 | Python | org:kubeflow |
| kubeflow/examples | 1,461 | Jsonnet | org:kubeflow |
| kubeflow/community-distribution | 1,029 | YAML | org:kubeflow |
| migalkin/NodePiece | 144 | Python | user:migalkin |
| AustinCStone/TextGAN | 92 | Python | user:AustinCStone |
| migalkin/StarE | 89 | Python | user:migalkin |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | user:bmorphism |
| plurigrid/asi | 58 | HTML | org:plurigrid |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | user:bmorphism |
| migalkin/kgcourse2021 | 24 | HTML | user:migalkin |

### Notable Activity (Since Last Sweep 2026-04-12)

- **plurigrid/gorj** (this repo): 1,591 open issues, pushed 2026-08-03 — highest issue-count in plurigrid, active today
- **plurigrid/asi**: Stars grew 16 → 58 (+42 since April sweep) — fastest-growing plurigrid repo
- **bmorphism/Gay.jl**: 188 open issues, pushed 2026-08-03 02:39 UTC — active at sweep time
- **kubeflow/pipelines**: pushed 2026-08-03 03:28 UTC — active at sweep time
- **bmorphism/ocaml-mcp-sdk**: Stars grew 60 → 61 (+1)
- **TeglonLabs/jank-crane**: New repo (created 2026-06-08), C++, GF3 convergence maps
- **zubyul/from-possible-worlds**: TeX, pushed 2026-07-18
- **kubeflow/mcp-apache-spark-history-server**: New (185 stars), MCP server for Spark debugging

### GF(3) Color Chain Distribution (This Run)

| Trit | Name | Color | Count |
|---|---|---|---|
| 0 | ERGODIC | #d3869b | 34 |
| 1 | PLUS | #b8bb26 | 36 |
| -1 | MINUS | #cc241d | 36 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 wallets)

**Result:** All 28 wallets returned **0 APT** — no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found on Aptos mainnet. Wallets exist as registered addresses but hold no APT balance.

| World | Address (truncated) | Balance APT |
|---|---|---|
| alice | 0xc793…4cc7b | 0.0 |
| bob | 0x0a3c…512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts **healthy** — `num_signatures_required = 2` for all pairs.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

- `/api/markets`: **HTTP 404**
- Root `https://testnet.mnx.fi`: SPA shell only — JavaScript required
- **Status:** Unavailable via static fetch. Ticker `MNX` confirmed. No price data extractable.

---

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

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent, 2026-08-03*
