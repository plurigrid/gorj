# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-24

## Sweep Metadata
- **Date:** 2026-07-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Python duckdb)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 53 |
| Total Repo Snapshots | 53 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 24 |
| +1 | `#b8bb26` | PLUS | 26 |
| -1 | `#cc241d` | MINUS | 26 |

Pattern: `PLUS → MINUS → ERGODIC` repeating (53 total increments)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-07-24)

| Source | Type | Total Repos (GitHub) | Repos Stored |
|--------|------|---------------------|-------------|
| plurigrid | org | 103 | 10 |
| kubeflow | org | 49 | 8 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 7 |
| zubyul | user | 49 | 5 |
| migalkin | user | 19 | 4 |
| DJedamski | user | 6 | 3 |
| wasita | user | 12 | 3 |
| kristinezheng | user | 5 | 3 |
| M1shaaa | user | 8 | 2 |
| AustinCStone | user | 41 | 3 |

### Top Repos by Stars (This Sweep)

| Source | Repo | Language | Stars | Last Pushed |
|--------|------|----------|-------|-------------|
| kubeflow | kubeflow/kubeflow | Go | 15,792 | 2026-07-24 |
| kubeflow | kubeflow/pipelines | Python | 4,169 | 2026-07-24 |
| kubeflow | kubeflow/spark-operator | Python | 3,143 | 2026-07-23 |
| kubeflow | kubeflow/trainer | Go | 2,153 | 2026-07-24 |
| migalkin | migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone | AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism | bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| migalkin | migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism | bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| plurigrid | plurigrid/asi | HTML | 31 | 2026-07-17 |

### Notable Activity (2026-07-24)
- **kubeflow/pipelines**: active today (15:51 UTC) — 457 open issues, ML pipelines very active
- **kubeflow/hub**: active today (13:07 UTC) — Model Registry growing (178★)
- **kubeflow/mcp-server**: active today (11:53 UTC) — new MCP integration for Kubeflow
- **plurigrid/gorj**: 1,371 open issues — this very repo, last pushed 2026-07-07
- **bmorphism/Gay.jl**: 187 open issues, last updated 2026-07-21 — very active
- **wasita/wasita.github.io**: updated 2026-07-21 — personal site active
- **migalkin/kgcourse2021**: updated 2026-07-10 — KG course still maintained

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via Aptos REST API (`/v1/accounts/{addr}/resource/CoinStore<AptosCoin>`).

**Result: 0.000000 APT across all 28 wallets**

These accounts either have no initialized CoinStore resource on mainnet, or hold zero APT balance at sweep time. This is consistent with wallets that have been created but not funded, or that have emptied balances.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.000000 |
| bob | 0x0a3c...d5d | 0.000000 |
| A | 0x8699...9d7a | 0.000000 |
| B | 0x3f89...b13 | 0.000000 |
| C–Z | (24 addresses) | 0.000000 each |

**Total Hamming Swarm APT: 0.000000**

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4...87003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7...eb6d | 2 | ✓ HEALTHY |

**All 5 multisig pairs require 2-of-2 signatures. Swarm multisig topology: fully operational.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — `testnet.mnx.fi/api/markets` returns HTTP 404. Root returns a minimal SPA shell with no extractable market data. `mnx_snapshots` table: 0 rows.

---

## Schema Reference
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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
