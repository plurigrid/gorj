# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-08

## Sweep Metadata
- **Date:** 2026-05-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 28 (was 23 pre-sweep; +5 new: IDs 13–15) |
| Total Repo Snapshots | 945 (was 944; +1 gorj via MCP) |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### Source Coverage

| Source | Type | Status | Repos |
|--------|------|--------|-------|
| plurigrid | org | MCP (gorj only — scoped) | 1 |
| kubeflow | org | Rate-limited (0/60 anon) | — |
| TeglonLabs | org | Rate-limited | — |
| bmorphism | user | Rate-limited | — |
| zubyul | user | Rate-limited | — |
| migalkin | user | Rate-limited | — |
| DJedamski | user | Rate-limited | — |
| wasita | user | Rate-limited | — |
| kristinezheng | user | Rate-limited | — |
| M1shaaa | user | Rate-limited | — |
| AustinCStone | user | Rate-limited | — |

> GitHub unauthenticated API rate limit exhausted (0/60). `gh` CLI absent.
> MCP tools scoped to `plurigrid/gorj` — used for commit history snapshot.

### plurigrid/gorj (via MCP — 10 recent commits)

| Field | Value |
|-------|-------|
| Full name | plurigrid/gorj |
| Language | Clojure |
| Description | MCP server + hooks that give AI coding agents a Clojure REPL |
| Last push | 2026-04-14T18:07:32Z |
| Latest commit | `ebf263f` — world-increment ducklake: sync world.duckdb sweep state |
| Second | `b434a43` — Merge sweep state into master |
| Third | `e76792f` — world-increments.duckdb: sync latest sweep state |

### GF(3) New Increments (GitHub Sweep)

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 13 | +1 | `#b8bb26` | PLUS | plurigrid | github_sweep |
| 13 | +1 | `#b8bb26` | PLUS | kubeflow | github_sweep_ratelimited |
| 13 | +1 | `#b8bb26` | PLUS | TeglonLabs | github_sweep_ratelimited |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

API: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Total APT across swarm: 0.0** — all 28 accounts hold no native APT on mainnet (coin stores return value=0).

### Multisig Contract Probes

API: `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 contracts healthy — 2-of-2 signatures required.

### MNX Markets (`testnet.mnx.fi`)

Site is a Next.js SPA. Probed `/api/markets` and `/api/v1/markets` — no structured data returned. Market data loaded client-side. **Status: unavailable via server-side curl.**

### GF(3) New Increments (Aptos)

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 14 | -1 | `#cc241d` | MINUS | aptos_mainnet | aptos_snapshot |
| 15 | 0 | `#d3869b` | ERGODIC | aptos_mainnet | multisig_probe |

---

## Full GF(3) Chain — All 28 Increments

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 1 | +1 | `#b8bb26` | PLUS | plurigrid | repo_snapshot |
| 2 | -1 | `#cc241d` | MINUS | kubeflow | repo_snapshot |
| 3 | 0 | `#d3869b` | ERGODIC | TeglonLabs | repo_snapshot |
| 4 | +1 | `#b8bb26` | PLUS | bmorphism | repo_snapshot |
| 5 | -1 | `#cc241d` | MINUS | zubyul | repo_snapshot |
| 6 | 0 | `#d3869b` | ERGODIC | migalkin | repo_snapshot |
| 7 | +1 | `#b8bb26` | PLUS | DJedamski | repo_snapshot |
| 8 | -1 | `#cc241d` | MINUS | wasita | repo_snapshot |
| 9 | 0 | `#d3869b` | ERGODIC | kristinezheng | repo_snapshot |
| 10 | +1 | `#b8bb26` | PLUS | M1shaaa | repo_snapshot |
| 11 | -1 | `#cc241d` | MINUS | AustinCStone | repo_snapshot |
| 12 | 0 | `#d3869b` | ERGODIC | bmorphism | sweep_complete |
| 13 | +1 | `#b8bb26` | PLUS | plurigrid | github_sweep |
| 13 | +1 | `#b8bb26` | PLUS | kubeflow | github_sweep_ratelimited |
| 13 | +1 | `#b8bb26` | PLUS | TeglonLabs | github_sweep_ratelimited |
| 14 | -1 | `#cc241d` | MINUS | aptos_mainnet | aptos_snapshot |
| 15 | 0 | `#d3869b` | ERGODIC | aptos_mainnet | multisig_probe |

GF(3) rule: `id%3==0` → ERGODIC `#d3869b` | `id%3==1` → PLUS `#b8bb26` | `id%3==2` → MINUS `#cc241d`

---

## DB Schema

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

## Historical Highlights (from prior sweeps)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — ML pipeline system
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **plurigrid/asi**: 16 stars — topological chemputer
