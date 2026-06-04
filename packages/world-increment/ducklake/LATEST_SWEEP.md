# World-Increment Sweep — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Aptos Wallets Snapshotted | 28 |
| Multisig Probes | 5 |
| MNX Snapshots | 0 (SPA, no API) |

---

## JOB 1: World Increment — id=13, PLUS #b8bb26

| Field | Value |
|-------|-------|
| Increment ID | 13 |
| GF(3) Trit | +1 |
| GF(3) Color | #b8bb26 |
| GF(3) Name | **PLUS** |
| Source | world-increment-sweep |
| Event Type | sweep_complete |
| Repo | plurigrid/gorj |
| Actor | claude |

GF(3) chain rule: `id=13 → 13%3=1 → trit=+1 → PLUS #b8bb26`

---

## GF(3) Color Chain — Full History

| ID | Source | Event | Trit | Color | Name |
|----|--------|-------|------|-------|------|
| 1  | plurigrid | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 13 | world-increment-sweep | sweep_complete | +1 | `#b8bb26` | **PLUS** ← this run |

---

## GitHub Social Graph Sweep

**Note:** GitHub API rate-limited without auth token (`gh` CLI not available in environment).
Snapshot captured via MCP tools (scoped to `plurigrid/gorj`).

### plurigrid/gorj (captured via MCP)

| Field | Value |
|-------|-------|
| Language | Clojure |
| Last Pushed | 2026-04-14T18:07:32Z |
| Latest Commit | `ebf263f` — "world-increment ducklake: sync world.duckdb sweep state" |
| Master SHA | `ebf263f516935cb93b64101666a01dc5a84b15aa` |
| Active sweep branches | 50+ (`world-increment/sweep-*`, latest: 2026-05-02-1318) |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |

### Social Graph Coverage (previous sweeps)

| Source | Type | Repos (from DB) |
|--------|------|-----------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL (all sweeps)** | | **471 prior + 1 this run = 472** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-05-07)

All 28 addresses queried via Aptos fullnode. Balances 0 APT (addresses not funded on mainnet).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 contracts healthy — 2-of-2 threshold.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — site is a Next.js SPA with no public JSON API endpoints.
Probed: `/api/markets`, `/api/v1/markets`, `/` — all return HTML only.
No rows in `mnx_snapshots`.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable from Prior Sweeps
- **kubeflow/kubeflow**: 15,565 stars
- **kubeflow/pipelines**: 4,119 stars
- **bmorphism/ocaml-mcp-sdk**: 60 stars (OCaml MCP SDK)
- **migalkin/NodePiece**: 143 stars (KG embeddings)
- **AustinCStone/TextGAN**: 92 stars
- **plurigrid/asi**: 16 stars (topological chemputer)
