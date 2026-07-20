# World-Increment Sweep + Hamming Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 28 |
| TeglonLabs | org | 5 |
| bmorphism | user | 23 |
| zubyul | user | 13 |
| migalkin | user (social) | 6 |
| wasita | user (social) | 5 |
| DJedamski | user (social) | 3 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| AustinCStone | user (social) | 6 |
| **TOTAL** | | **195** |

### GF(3) Increment Chain (this sweep, cumulative now 34)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 1 | PLUS | `#b8bb26` | 12 |
| -1 | MINUS | `#cc241d` | 11 |
| 0 | ERGODIC | `#d3869b` | 11 |

GF(3) rule: `id mod 3 == 0` → ERGODIC `#d3869b` | `id mod 3 == 1` → PLUS `#b8bb26` | `id mod 3 == 2` → MINUS `#cc241d`

### Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | ★15,783 | — |
| kubeflow/pipelines | ★4,169 | Python |
| kubeflow/spark-operator | ★3,140 | Python |
| kubeflow/trainer | ★2,152 | Go |
| kubeflow/katib | ★1,691 | Python |
| kubeflow/examples | ★1,460 | Jsonnet |
| kubeflow/arena | ★815 | Go |
| migalkin/NodePiece | ★144 | Python |
| migalkin/StarE | ★89 | Python |
| AustinCStone/TextGAN | ★92 | Python |
| bmorphism/ocaml-mcp-sdk | ★61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | ★22 | JavaScript |

### Notable Recent Activity (2026-07)

- **kubeflow/spark-operator**: Apache Spark on Kubernetes, updated 2026-07-20
- **kubeflow/sdk**: Universal Python SDK for AI on Kubernetes, updated 2026-07-19
- **kubeflow/mcp-server**: MCP Server for AI-Assisted Dev with Kubeflow, updated 2026-07-19
- **bmorphism/gay-chat**: gay:// chat over Spritely Brassica, created 2026-07-14
- **bmorphism/anti-bullshit-mcp-server**: Epistemological manipulation detector, updated 2026-07-12
- **wasita/wasita.github.io**: Personal site (Svelte), updated 2026-07-16
- **migalkin/kgcourse2021**: Knowledge Graphs course materials, updated 2026-07-10

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**Result:** All 28 addresses returned HTTP 404 — accounts have no APT CoinStore resource on mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9... | NULL (404) |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf78... | NULL (404) |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8... | NULL (404) |
| B–Z | (25 more addresses) | NULL (404) |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 multisig accounts return 2 signatures required (2-of-2):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee2084... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df6... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Result:** HTTP 401 Unauthorized on all probed paths (`/api/markets`, `/api/v1/markets`, `/markets`, `/api/instruments`). Market data requires authentication. Recorded as `UNAVAILABLE`.

---

## DuckDB State (cumulative)

| Table | Records |
|-------|---------|
| world_increments | 34 |
| repo_snapshots | 1,139 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
