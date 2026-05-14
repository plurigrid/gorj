# World-Increment Sweep — 2026-05-14

## Sweep Metadata
- **Date:** 2026-05-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 26 |
| Total Repo Snapshots | 945 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA, no REST API) |

---

## GF(3) Color Chain — This Sweep (IDs 13–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | sweep_start | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos-mainnet (chain) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | claude-agent (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `… ERGODIC → PLUS → MINUS → ERGODIC` (5th full cycle closes)

### Full GF(3) History (IDs 1–15)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
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
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 13 | plurigrid (org) | sweep_start | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos-mainnet (chain) | balance_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | claude-agent (meta) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 1: GitHub Social Graph

**Note:** GitHub MCP access in this session is restricted to `plurigrid/gorj`. No `gh` CLI is available. The 944 repo snapshots from prior sweeps cover the full social graph (plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, and the 6 zubyul social-graph users). This sweep appended 1 new gorj snapshot.

### New Repo Snapshot (this sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| plurigrid/gorj | Clojure | 0 | 2026-05-08 |

### Cumulative Repo Counts by Source (all sweeps)

| Source | Type | Repos |
|--------|------|-------|
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
| plurigrid/gorj (new) | repo | 1 |
| **TOTAL** | | **472** |

### Notable Highlights (from prior sweeps)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet — Wallet Balances

All 28 Hamming swarm addresses queried via `https://fullnode.mainnet.aptoslabs.com/v1`.
All accounts returned 0 APT (CoinStore resource absent — unfunded/inactive accounts).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…e9d7a | 0.0 |
| B | 0x3f89…cb13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…cfdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…cf71 | 0.0 |
| G | 0x69a3…7f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…25dc4 | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…7f2e9 | 0.0 |
| N | 0xe7dd…51b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…c89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…d386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…f956 | 0.0 |
| V | 0xb59d…af2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…3047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…197c | 0.0 |

### Multisig Contract Probes

All 5 contracts healthy — each requires **2-of-2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — site returns a Next.js SPA. Probed endpoints `/api/markets`, `/api/v1/markets`, `/api/tickers` — all return HTML or 404. No market data captured; `mnx_snapshots` table remains empty.

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
