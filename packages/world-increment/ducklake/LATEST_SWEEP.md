# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-08

## Sweep Metadata
- **Date:** 2026-05-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Notes |
|--------|------|-------|-------|
| plurigrid | org | 100 | full page (per_page=100) |
| kubeflow | org | 47 | |
| TeglonLabs | org | 53 | |
| zubyul | user | 27 | |
| DJedamski | user | 11 | |
| wasita | user | 32 | |
| kristinezheng | user | 18 | |
| AustinCStone | user | 43 | |
| bmorphism | user | — | rate-limited (IP-based, 60 req/hr) |
| migalkin | user | — | rate-limited |
| M1shaaa | user | — | rate-limited |
| bmorphism events | events | 30 | public event stream |
| zubyul events | events | 30 | public event stream |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,625 | — | 2026-05-07 |
| kubeflow/pipelines | 4,136 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-05 |
| kubeflow/trainer | 2,096 | Go | 2026-05-07 |
| kubeflow/katib | 1,683 | Python | 2026-05-08 |
| kubeflow/manifests | 1,015 | YAML | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | — |
| AustinCStone/TextGAN | 92 | Python | — |
| migalkin/NodePiece | 143 | Python | — |

### GF(3) Color Chain — World Increments

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 29 |
| +1 | PLUS | `#b8bb26` | 31 |
| -1 | MINUS | `#cc241d` | 31 |

**Total world_increments (cumulative):** 91 rows  
**Total repo_snapshots (cumulative):** 1,275 rows  
**New increments this sweep:** 68 (8 repo snapshots + 60 event records)

GF(3) assignment: `id%3==0` → ERGODIC `#d3869b` | `id%3==1` → PLUS `#b8bb26` | `id%3==2` → MINUS `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance` view function — handles both legacy CoinStore and
newer fungible asset accounts. (Direct `CoinStore` resource returned `resource_not_found`
for all accounts; view function resolves both storage models correctly.)

| World | APT Balance | Address (truncated) |
|-------|-------------|---------------------|
| bob | 12.657007 | 0x0a3c00c5… |
| F | 1.960516 | 0x18a14b5b… |
| L | 1.927269 | 0x7c2eaeaf… |
| J | 1.895093 | 0x4d964db8… |
| alice | 0.436434 | 0xc793acde… |
| O | 0.210136 | 0x73252b60… |
| K | 0.161961 | 0xa732040a… |
| P | 0.140136 | 0x62187920… |
| M | 0.112285 | 0x6fed37a7… |
| N | 0.106121 | 0xe7dde6da… |
| Q | 0.103240 | 0xac40fa50… |
| S | 0.091788 | 0xb8753014… |
| R | 0.090217 | 0x7ce605cc… |
| T | 0.073713 | 0x35781dc0… |
| U | 0.055773 | 0x75860da4… |
| A | 0.051767 | 0x8699edc0… |
| V | 0.048833 | 0xb59dd817… |
| Y | 0.044449 | 0xd8e32848… |
| X | 0.042577 | 0xa95cbbd1… |
| W | 0.040705 | 0x5f32aef7… |
| B | 0.036256 | 0x3f892ebe… |
| Z | 0.024268 | 0x7af0ef6e… |
| D | 0.011629 | 0xf7765624… |
| C | 0.010185 | 0x38b99e63… |
| E | 0.009372 | 0xdc1d9d53… |
| H | 0.001681 | 0xce67c327… |
| I | 0.000681 | 0x070fe5d7… |
| G | 0.000681 | 0x69a394c0… |

**Total APT across swarm:** 20.344773 APT

### Multisig Contract Probes

All 5 contracts healthy — 2-of-2 threshold required.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f428… | 2 | HEALTHY |
| A-G | 0xf56c4a1c… | 2 | HEALTHY |
| Y-Z | 0xd3ffe181… | 2 | HEALTHY |
| S-T | 0x3b1c3ae9… | 2 | HEALTHY |
| V-W | 0x40fad7b4… | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a pure Next.js SPA (292KB HTML).
All API path probes (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/pools`,
`/api/stats`, `/api/tokens`) return HTML fallback pages. Market data loads client-side
only; no public REST API is exposed. Recorded as placeholder in `mnx_snapshots`.

---

## Database State

| Table | Rows |
|-------|------|
| world_increments | 91 |
| repo_snapshots | 1,275 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

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
