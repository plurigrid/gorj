# World-Increment Sweep + Hamming Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 113 |
| Total Repo Snapshots | 113 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| GF3 Trit | Name | Color | Count |
|----------|------|-------|-------|
| +1 | PLUS | `#b8bb26` | 38 |
| -1 | MINUS | `#cc241d` | 38 |
| 0 | ERGODIC | `#d3869b` | 37 |

GF(3) rule: `id%3==0 → ERGODIC | id%3==1 → PLUS | id%3==2 → MINUS`

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 25 |
| kubeflow | org | 27 |
| TeglonLabs | org | 4 |
| bmorphism | user | 25 |
| zubyul | user | 10 |
| migalkin | user (zubyul graph) | 5 |
| DJedamski | user (zubyul graph) | 3 |
| wasita | user (zubyul graph) | 4 |
| kristinezheng | user (zubyul graph) | 3 |
| M1shaaa | user (zubyul graph) | 2 |
| AustinCStone | user (zubyul graph) | 5 |
| **TOTAL** | | **113** |

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15628 | — | 2026-05-07 |
| kubeflow/pipelines | 4137 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3125 | Python | 2026-05-08 |
| kubeflow/trainer | 2096 | Go | 2026-05-08 |
| kubeflow/mpi-operator | 524 | Go | 2026-05-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| plurigrid/asi | 21 | HTML | 2026-04-26 |
| plurigrid/gorj | 0 | Clojure | 2026-05-08 |

### Most Recently Pushed

```
kubeflow/mcp-apache-spark-history-server  2026-05-09
kubeflow/pipelines                        2026-05-08
kubeflow/trainer                          2026-05-08
kubeflow/spark-operator                   2026-05-08
kubeflow/mlflow-integration               2026-05-08
bmorphism/ocaml-mcp-sdk                   2026-05-08
plurigrid/gorj                            2026-05-08
plurigrid/horse                           2026-05-07
kubeflow/kubeflow                         2026-05-07
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**Result:** All wallets returned 0 APT — accounts exist but hold no `AptosCoin` resource (unfunded test addresses in the Hamming swarm).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes

5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on Aptos mainnet.**

### MNX Markets

`https://testnet.mnx.fi` serves a Next.js SPA with no public REST API.  
Market data unavailable; recorded as `N/A` in `mnx_snapshots`.

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,628 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,137 stars — ML pipelines (pushed 2026-05-08, very active)
- **kubeflow/mcp-apache-spark-history-server**: pushed 2026-05-09 (today)
- **migalkin/NodePiece**: 144 stars — ICLR'22 knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK (Jane Street oxcaml_effect)
- **plurigrid/gorj**: This repo — forj + Rama topology nREPL routing + GF(3) coloring
- **Hamming swarm**: 28 Aptos wallets + 5 multisig contracts — all multisigs healthy at 2-of-N
