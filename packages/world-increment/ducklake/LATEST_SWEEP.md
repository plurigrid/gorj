# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp**: 2026-07-27T10:14:46Z  
**Agent**: world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version**: v1.5.5 (Variegata)  
**Database**: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source Type | Name | Repos Snapshotted |
|-------------|------|-------------------|
| org | plurigrid | 100 (of 103 total) |
| org | kubeflow | 49 |
| org | TeglonLabs | 5 |
| user | bmorphism | 100 (of 106 total) |
| user | zubyul | 49 |
| social (zubyul graph) | migalkin | 19 |
| social (zubyul graph) | DJedamski | 2 |
| social (zubyul graph) | wasita | 3 |
| social (zubyul graph) | kristinezheng | 2 |
| social (zubyul graph) | M1shaaa | 1 |
| social (zubyul graph) | AustinCStone | 3 |
| **TOTAL** | | **333 repos / 333 increments** |

### GF(3) Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 111 |
| 1 | #b8bb26 | PLUS | 111 |
| -1 | #cc241d | MINUS | 111 |

GF(3) assignment: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

### Top Repos by Stars

| Repo | Stars | Forks | Language |
|------|-------|-------|----------|
| kubeflow/kubeflow | 15,791 | 2,686 | — |
| kubeflow/pipelines | 4,170 | 2,067 | Python |
| kubeflow/spark-operator | 3,142 | 1,506 | Python |
| kubeflow/trainer | 2,155 | 997 | Go |
| kubeflow/katib | 1,692 | 532 | Python |
| migalkin/NodePiece | 144 | 21 | Python |
| migalkin/StarE | 89 | 16 | Python |
| AustinCStone/TextGAN | 92 | 30 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml |
| plurigrid/asi | 51 | 11 | HTML |

### Notable Recent Activity

- **plurigrid/gorj** (this repo): 1,437 open issues, pushed 2026-07-27 — active GF(3) REPL project
- **bmorphism/Gay.jl**: Julia, 188 open issues, pushed 2026-07-27 — wide-gamut deterministic color
- **kubeflow/pipelines**: Python, pushed 2026-07-27 — very active ML pipeline
- **kubeflow/trainer**: Go, distributed AI model training, pushed 2026-07-27
- **wasita/wasita.github.io**: Svelte personal site, pushed 2026-07-21
- **TeglonLabs/jank-crane**: C++ GF3 convergence maps, pushed 2026-06-08
- **zubyul/from-possible-worlds**: TeX, pushed 2026-07-18

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets returned `resource_not_found` from Aptos mainnet fullnode — no CoinStore resource at these addresses. Recorded as **0.0 APT** each.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...c7b | 0.0 | resource_not_found |
| bob | 0x0a3c...d5d | 0.0 | resource_not_found |
| A | 0x8699...d7a | 0.0 | resource_not_found |
| B | 0x3f89...b13 | 0.0 | resource_not_found |
| C | 0x38b9...35e | 0.0 | resource_not_found |
| D | 0xf776...dd1 | 0.0 | resource_not_found |
| E | 0xdc1d...d36 | 0.0 | resource_not_found |
| F | 0x18a1...f71 | 0.0 | resource_not_found |
| G | 0x69a3...f32 | 0.0 | resource_not_found |
| H | 0xce67...00f | 0.0 | resource_not_found |
| I | 0x070f...fc9 | 0.0 | resource_not_found |
| J | 0x4d96...f54 | 0.0 | resource_not_found |
| K | 0xa732...dc4 | 0.0 | resource_not_found |
| L | 0x7c2e...ba9 | 0.0 | resource_not_found |
| M | 0x6fed...e9 | 0.0 | resource_not_found |
| N | 0xe7dd...b2c | 0.0 | resource_not_found |
| O | 0x7325...89d | 0.0 | resource_not_found |
| P | 0x6218...948 | 0.0 | resource_not_found |
| Q | 0xac40...a9 | 0.0 | resource_not_found |
| R | 0x7ce6...e10 | 0.0 | resource_not_found |
| S | 0xb875...386 | 0.0 | resource_not_found |
| T | 0x3578...588 | 0.0 | resource_not_found |
| U | 0x7586...956 | 0.0 | resource_not_found |
| V | 0xb59d...2c3 | 0.0 | resource_not_found |
| W | 0x5f32...cb0 | 0.0 | resource_not_found |
| X | 0xa95c...47d | 0.0 | resource_not_found |
| Y | 0xd8e3...4c4 | 0.0 | resource_not_found |
| Z | 0x7af0...97c | 0.0 | resource_not_found |

**Total APT across Hamming swarm**: 0.0 APT

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed successfully via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-2 signatures.

### MNX Markets (testnet.mnx.fi)

**Status**: Unavailable via API. The site is a Next.js SPA; all paths including `/api/markets` return HTML. No structured market data could be extracted. Recorded as 0 rows in `mnx_snapshots`.

---

## DuckDB State (`world-increments.duckdb`)

| Table | Rows |
|-------|------|
| world_increments | 333 |
| repo_snapshots | 333 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |

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
