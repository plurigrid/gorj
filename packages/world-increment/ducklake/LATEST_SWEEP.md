# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-24

## Sweep Metadata
- **Date:** 2026-06-24
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 403 |
| Total Repo Snapshots | 1324 |
| Distinct Repos | 645 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | ~135 |
| +1 | PLUS | #b8bb26 | ~135 |
| -1 | MINUS | #cc241d | ~135 |

GF(3) rule: `id mod 3 == 0` → ERGODIC #d3869b · `id mod 3 == 1` → PLUS #b8bb26 · `id mod 3 == 2` → MINUS #cc241d

---

## Top Repos by Stars (2026-06-24 Snapshot)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15742 | 2026-06-18 |
| kubeflow/pipelines | Python | 4157 | 2026-06-24 |
| kubeflow/spark-operator | Python | 3128 | 2026-06-24 |
| kubeflow/trainer | Go | 2119 | 2026-06-24 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| bmorphism | user | 103 |
| plurigrid | org | 102 |
| zubyul | user | 51 |
| kubeflow | org | 50 |
| AustinCStone | user | 42 |
| migalkin | user | 21 |
| M1shaaa | user | 10 |
| DJedamski | user | 8 |
| TeglonLabs | org | 7 |
| kristinezheng | user | 7 |
| wasita | user | 2 |
| **TOTAL** | | **403** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-06-24)

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c...512d5d | 12.6570 |
| F | 0x18a1...3cf71 | 1.9605 |
| L | 0x7c2e...eba9 | 1.9273 |
| J | 0x4d96...7f54 | 1.8951 |
| alice | 0xc793...cc7b | 0.4364 |
| O | 0x7325...a89d | 0.2101 |
| K | 0xa732...dc4 | 0.1620 |
| P | 0x6218...c948 | 0.1401 |
| M | 0x6fed...f2e9 | 0.1123 |
| N | 0xe7dd...1b2c | 0.1061 |
| Q | 0xac40...89a9 | 0.1032 |
| S | 0xb875...0386 | 0.0918 |
| R | 0x7ce6...6e10 | 0.0902 |
| T | 0x3578...4588 | 0.0737 |
| U | 0x7586...f956 | 0.0558 |
| A | 0x8699...9d7a | 0.0518 |
| V | 0xb59d...2c3 | 0.0488 |
| Y | 0xd8e3...44c4 | 0.0444 |
| X | 0xa95c...047d | 0.0426 |
| W | 0x5f32...c7b0 | 0.0407 |
| B | 0x3f89...b13 | 0.0363 |
| Z | 0x7af0...97c | 0.0243 |
| D | 0xf776...dd1 | 0.0116 |
| C | 0x38b9...35e | 0.0102 |
| E | 0xdc1d...d36 | 0.0094 |
| H | 0xce67...300f | 0.0017 |
| I | 0x070f...c9 | 0.0007 |
| G | 0x69a3...f32 | 0.0007 |

**Total APT across 28 wallets: ~22.28 APT**  
**Top holder:** bob (12.66 APT, 56.8% of swarm total)

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — SPA returns no parseable API data.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
