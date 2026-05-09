# World-Increment Sweep + Hamming Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Increment ID:** 13 — GF(3) trit=+1 · **PLUS** · `#b8bb26`
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Session:** https://claude.ai/code/session_013qg5MtxEAREQinmdWzdBDW

---

## JOB 1: GitHub Social Graph Sweep

### Status
GitHub REST API rate-limited (unauthenticated: 60 req/hr exhausted by sandbox IP).  
`gh` CLI not installed. GitHub MCP tools scoped to `plurigrid/gorj` only.  
Repo snapshot queries deferred; prior 944 snapshots (ids 1–12) remain in DB.

### plurigrid/gorj — Recent Commits (MCP, live)
| SHA | Date | Message |
|-----|------|---------|
| 5b28fe0 | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | 2026-04-14 | Merge sweep state into master |
| e76792f | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| 631518b | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |
| c4238bc | 2026-04-10 | world-increments.duckdb: sync latest sweep state |

### Cumulative DuckDB State
| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-09)
All 28 accounts returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
All balances: **0.0 APT** (accounts unfunded on mainnet).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob   | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...3cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...5300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...87f54 | 0.0 |
| K | 0xa732...25dc4 | 0.0 |
| L | 0x7c2e...7eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...5a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...3f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...e197c | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)
All 5 pairs **healthy** — 2-of-2 threshold confirmed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
- Root `/`: HTTP 200 — Next.js SPA rendered client-side
- `/api/markets`, `/api/v1/markets`, `/api/tickers`: HTTP 404
- **Status: unavailable** — no public REST API endpoints; SPA loads data client-side only

---

## GF(3) Color Chain

| ID | Source | Event | Trit | Color | Name |
|----|--------|-------|------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| **13** | **world-increment** | **sweep_complete** | **+1** | **`#b8bb26`** | **PLUS** ← this sweep |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

Next (id=14): trit=2≡**MINUS** `#cc241d`

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

## Notable Highlights (cumulative)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer
- **Hamming swarm**: 28 wallets probed (A–Z + alice/bob), all 0 APT on mainnet
- **Multisig**: 5/5 contracts healthy (2-of-2 threshold: A-B, A-G, Y-Z, S-T, V-W)
