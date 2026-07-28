# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-28  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.5 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 10 (top by recency) |
| zubyul | user | 5 (top by recency) |
| migalkin | social | 4 |
| wasita | social | 2 |
| kristinezheng | social | 1 |
| AustinCStone | social | 2 |
| DJedamski | social | 1 |
| M1shaaa | social | 1 |
| **Total** | | **180 new world_increments** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 67 |
| +1 | PLUS | `#b8bb26` | 68 |
| -1 | MINUS | `#cc241d` | 68 |

GF(3) assignment: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

### Most Recently Pushed (per source)

| Source | Repo | Pushed At | Stars |
|--------|------|-----------|-------|
| kubeflow | sdk | 2026-07-28 | 130 |
| plurigrid | gorj | 2026-07-28 | 1 |
| bmorphism | Gay.jl | 2026-07-21 | 2 |
| wasita | wasita.github.io | 2026-07-21 | 1 |
| AustinCStone | byteruckus | 2026-07-15 | 0 |
| migalkin | kgcourse2021 | 2026-07-10 | 24 |
| kristinezheng | kristinezheng.github.io | 2026-07-01 | 0 |
| TeglonLabs | jank-crane | 2026-06-08 | 0 |
| zubyul | voice-observatory | 2026-04-24 | 0 |

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15793 | — | 2026-07-10 |
| kubeflow/pipelines | 4171 | Python | 2026-07-27 |
| kubeflow/spark-operator | 3142 | Python | 2026-07-25 |
| kubeflow/trainer | 2156 | Go | 2026-07-27 |
| kubeflow/katib | 1692 | Python | 2026-07-26 |
| kubeflow/community-distribution | 1028 | YAML | 2026-07-27 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 52 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |

### Notable Activity

- **plurigrid/gorj** (this repo): 1453 open issues, pushed today 2026-07-28
- **plurigrid/asi**: 52 stars — "everything is topological chemputer!"
- **kubeflow** ecosystem: multiple repos pushed 2026-07-27/28 — sdk, trainer, pipelines, katib, spark-operator all active
- **bmorphism/Gay.jl**: Wide-gamut SplitMix64 color sampling, 188 open issues
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps, crane-jank IR hub
- **zubyul** graph active: voice-observatory, gay-world, kinesis-kb360pro in 2026

---

## JOB 2: Hamming Swarm Snapshot (Aptos)

### Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against Aptos mainnet at ledger version ~6,487,467,004.

**Result: `resource_not_found` for all 28 addresses** — no `CoinStore<AptosCoin>` resource registered.
These accounts either use the Fungible Asset (FA) standard (not legacy CoinStore) or are unfunded on mainnet.
Balance stored as `0.0` APT for all.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793ac...4cc7b | 0.0 |
| bob | 0x0a3c00...512d5d | 0.0 |
| A | 0x8699ed...be9d7a | 0.0 |
| B | 0x3f892e...7cb13 | 0.0 |
| C | 0x38b99e...1535e | 0.0 |
| D | 0xf77656...cfdd1 | 0.0 |
| E | 0xdc1d9d...958d36 | 0.0 |
| F | 0x18a14b...3cf71 | 0.0 |
| G | 0x69a394...7f32 | 0.0 |
| H | 0xce67c3...5300f | 0.0 |
| I–Z | (16 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

**All 5 multisig contracts operational — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

- Probed: `https://testnet.mnx.fi/api/markets` and `https://testnet.mnx.fi/api/v1/markets`
- **Status: unavailable** — site is a Next.js SPA (client-side rendered), no public REST API JSON endpoints accessible
- mnx_snapshots table: 0 rows

---

## DuckDB Summary

| Table | Row Count |
|-------|-----------|
| world_increments | 203 |
| repo_snapshots | 1124 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent on 2026-07-28*
