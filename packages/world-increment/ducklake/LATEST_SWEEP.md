# World-Increment Sweep + Hamming Swarm — 2026-07-29

## Sweep Metadata
- **Date:** 2026-07-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (this run)

| Metric | Value |
|--------|-------|
| World Increments (this run) | 70 |
| Sources Covered | 3 orgs + 8 users |
| Total Repo Snapshots (cumulative) | 1014 |

### GF(3) Color Chain Distribution (ids 1–70)

| GF3 State | Color | Trit | Count |
|-----------|-------|------|-------|
| ERGODIC | #d3869b | 0 | 30 |
| PLUS | #b8bb26 | +1 | 32 |
| MINUS | #cc241d | −1 | 31 |

GF(3) chain cycles: `PLUS → MINUS → ERGODIC → ...` (70 steps = 23 full cycles + 1 step)

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 17 |
| kubeflow | org | 13 |
| TeglonLabs | org | 9 |
| bmorphism | user | 8 |
| zubyul | user | 9 |
| migalkin | social-graph | 4 |
| DJedamski | social-graph | 2 |
| wasita | social-graph | 2 |
| kristinezheng | social-graph | 2 |
| M1shaaa | social-graph | 2 |
| AustinCStone | social-graph | 2 |
| **Total** | | **70** |

### Top Repos by Stars (this run)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/pipelines | 4170 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3142 | Python | 2026-07-25 |
| kubeflow/trainer | 2161 | Go | 2026-07-27 |
| kubeflow/katib | 1693 | Python | 2026-07-26 |
| kubeflow/community-distribution | 1029 | YAML | 2026-07-29 |
| kubeflow/arena | 815 | Go | 2026-07-29 |
| kubeflow/kale | 698 | Python | 2026-07-27 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| plurigrid/asi | 53 | HTML | 2026-07-10 |

### Notable Observations

- **plurigrid/gorj** (this repo): 1487 open issues, pushed 12:15 UTC today
- **kubeflow/mcp-server** (31 stars): Kubeflow entering the MCP ecosystem
- **TeglonLabs/vibespace**: balanced ternary + NATS — GF(3) aligned
- **bmorphism/Gay.jl**: 188 open issues, pushed 02:30 UTC today
- **zubyul** social graph is Plurigrid-aligned: Gay.jl fork, ghostel-emacs-worlds, gay-world

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet ledger ~6.51B)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. The `0x1::coin::CoinStore<AptosCoin>` resource is **not found** for any address — accounts exist (e.g. alice has sequence_number=72) but hold no native APT via legacy CoinStore. Wallets likely operate via the fungible asset standard.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

**Total APT across swarm: 0.0 APT (CoinStore resource absent on all)**

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → HTTP 404
- Root `/` → SPA shell only (JavaScript rendering required)
- **Status: unavailable** — recorded as N/A in mnx_snapshots

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
