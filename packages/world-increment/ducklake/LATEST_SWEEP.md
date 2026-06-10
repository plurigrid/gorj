# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-10

## Sweep Metadata
- **Date:** 2026-06-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 220 |
| Total Repo Snapshots | 220 |
| Sources Covered | 3 orgs + 8 users |

### Repos by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 65 |
| kubeflow | org | 25 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | user (social) | 7 |
| wasita | user (social) | 5 |
| AustinCStone | user (social) | 5 |
| M1shaaa | user (social) | 3 |
| DJedamski | user (social) | 3 |
| kristinezheng | user (social) | 3 |
| **TOTAL** | | **220** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 73 |
| 1 | `#b8bb26` | PLUS | 74 |
| -1 | `#cc241d` | MINUS | 73 |

GF(3) chain over 220 increments: balanced across all three states (~73.3 per trit).

### Notable Repos (by stars)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,714 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-10 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-09 |
| kubeflow/trainer | 2,112 | Go | 2026-06-10 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2025-01-05 |
| plurigrid/asi | 25 | HTML | 2026-04-26 |

### Most Active (recent pushes 2026-06-10)

- `plurigrid/place` → 2026-06-10T12:08Z
- `kubeflow/pipelines` → 2026-06-10T11:29Z
- `kubeflow/hub` → 2026-06-10T11:10Z
- `plurigrid/gorj` → 2026-06-10T11:14Z (477 open issues)
- `kubeflow/dashboard` → 2026-06-10T04:48Z
- `kubeflow/trainer` → 2026-06-10T03:16Z
- `bmorphism/Gay.jl` → 2026-06-10T00:42Z (189 open issues)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried at 1s intervals via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned **0.0 APT** — accounts carry zero native APT balance in their CoinStore resource.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z (24 more) | (see aptos_snapshots table) | 0.0 each |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`. All returned `sigs_required = 2` (2-of-N threshold).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment authentication. All API paths return HTTP 200 with an auth-challenge SPA (no market data accessible without bypass token). `mnx_snapshots` table is empty.

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
- **kubeflow/kubeflow**: 15,714 stars — flagship ML Toolkit for Kubernetes (↑149 since April sweep)
- **kubeflow/pipelines**: 4,153 stars — pushed to main on 2026-06-10 (day of sweep)
- **plurigrid/gorj**: 477 open issues — this repo's own GF(3) trit orchestration hub
- **bmorphism/Gay.jl**: 189 open issues — wide-gamut GF(3) color engine, pushed 2026-06-10
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK via Jane Street oxcaml_effect
- **Hamming swarm**: all 28 Aptos worlds (alice, bob, A–Z) at 0.0 APT; 5 multisigs healthy at 2-of-N
- **MNX testnet**: behind Vercel auth — no market data extractable without bypass token
