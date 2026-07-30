# World-Increment Sweep — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 56 (33 new this sweep) |
| Total Repo Snapshots | 977 (33 new this sweep) |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users (social graph) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 12 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 41 |

### Top Repos by Stars (this sweep)

| org/user | repo | stars | forks | open_issues | pushed |
|---|---|---|---|---|---|
| kubeflow | kubeflow | 15796 | 2689 | 0 | 2026-07-10 |
| kubeflow | pipelines | 4171 | 2071 | 497 | 2026-07-29 |
| kubeflow | spark-operator | 3142 | 1510 | 112 | 2026-07-29 |
| kubeflow | trainer | 2162 | 1003 | 125 | 2026-07-30 |
| kubeflow | katib | 1694 | 532 | 107 | 2026-07-26 |
| migalkin | NodePiece | 144 | 21 | 0 | 2026-05-07 |
| bmorphism | ocaml-mcp-sdk | 61 | 2 | 0 | 2026-05-08 |
| plurigrid | asi | 56 | 13 | 4 | 2026-07-10 |
| bmorphism | anti-bullshit-mcp-server | 22 | 7 | 1 | 2026-07-12 |
| bmorphism | babashka-mcp-server | 19 | 6 | 3 | 2026-06-05 |

### Star Growth vs April 2026 Baseline
- **kubeflow/kubeflow**: 15565 → 15796 (+231)
- **kubeflow/pipelines**: 4119 → 4171 (+52)
- **kubeflow/spark-operator**: 3111 → 3142 (+31)
- **kubeflow/trainer**: 2080 → 2162 (+82)
- **migalkin/NodePiece**: 143 → 144 (+1)
- **bmorphism/ocaml-mcp-sdk**: 60 → 61 (+1)

### Notable Activity
- **plurigrid/gorj**: 1504 open issues, pushed 2026-07-30 (active today — this repo)
- **bmorphism/Gay.jl**: 188 open issues (active development, GF(3) color system)
- **kubeflow/mcp-server**: 31★, 38 forks — Kubeflow MCP integration expanding fast
- **TeglonLabs/jank-crane**: new C++ crane-jank converged-IR hub (June 2026)
- **zubyul/nash-tui + nash-web**: private NASH token TUI work (April 2026)
- **bmorphism/gay-chat**: new `gay://chat` Spritely Brassica Chat (July 2026)
- **wasita/wasita.github.io**: active Svelte site (pushed 2026-07-21)

### GF(3) Increment Chain (33 new increments, IDs 34–66 cumulative, 1–33 this run)
- PLUS (#b8bb26, trit=+1): 11 increments
- MINUS (#cc241d, trit=-1): 11 increments  
- ERGODIC (#d3869b, trit=0): 11 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All returned `resource_not_found` — wallets either unfunded or using FA (Fungible Asset) module rather than legacy CoinStore. Balance recorded as 0 APT.

| world | address (prefix) | balance_apt |
|---|---|---|
| alice | 0xc793... | 0 |
| bob | 0x0a3c... | 0 |
| A–Z (26 wallets) | various | 0 each |

### Multisig Contract Probes

5/5 multisig contracts **HEALTHY** — all return 2-of-N threshold:

| pair | address (prefix) | sigs_required | status |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`/api/markets` → HTTP 404. Root page renders SPA with only the text "MNX". No structured market data available via public endpoints. `mnx_snapshots` table remains empty.

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
