# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 (103 total) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (106 total) |
| zubyul | user | 49 |
| migalkin | social graph | 4 (highlights) |
| wasita | social graph | 3 (highlights) |
| AustinCStone | social graph | 3 (highlights) |
| kristinezheng | social graph | 1 (highlight) |
| M1shaaa | social graph | 2 (highlights) |
| DJedamski | social graph | 2 (highlights) |

**Total repo increments this sweep:** 318  
**Total world_increments in DB:** 341  
**GF(3) distribution:** ERGODIC(0)=113 · PLUS(+1)=114 · MINUS(-1)=114

### Top Repos by Stars (new this sweep)

| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,778 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,167 | 2026-07-16 |
| kubeflow/spark-operator | Python | 3,137 | 2026-07-15 |
| kubeflow/trainer | Go | 2,150 | 2026-07-15 |
| kubeflow/katib | Python | 1,690 | 2026-07-15 |
| kubeflow/examples | Jsonnet | 1,460 | 2025-04-14 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |

### Notable Activity

- **plurigrid/gorj** (this repo): Clojure, pushed **2026-07-16** — active today
- **plurigrid/asi**: HTML, pushed 2026-07-10 — "everything is topological chemputer!" (30 stars, up from 16)
- **plurigrid/place**: TeX, pushed 2026-07-14
- **plurigrid/eirobri**: Clojure, pushed 2026-07-14 — EiRoBri replay world
- **bmorphism/gay-chat**: Scheme, pushed 2026-07-14
- **bmorphism/Gay.jl**: Julia, pushed 2026-07-14 (2 stars)
- **bmorphism/ocaml-mcp-sdk**: OCaml, 61 stars (was 60) — growing
- **wasita/wasita.github.io**: Svelte, pushed 2026-07-14 — active
- **AustinCStone/byteruckus**: HTML, pushed **2026-07-15** — newest repo in sweep

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### APT Wallet Balances

> Method: `0x1::primary_fungible_store::balance` (FungibleAsset API, not legacy CoinStore)

| World | Balance (APT) | Address (short) |
|-------|--------------|----------------|
| bob | **12.657007** | 0x0a3c... |
| F | 1.960516 | 0x18a1... |
| L | 1.927269 | 0x7c2e... |
| J | 1.895093 | 0x4d96... |
| alice | 0.436434 | 0xc793... |
| O | 0.210136 | 0x7325... |
| K | 0.161961 | 0xa732... |
| P | 0.140136 | 0x6218... |
| M | 0.112285 | 0x6fed... |
| N | 0.106121 | 0xe7dd... |
| Q | 0.103240 | 0xac40... |
| S | 0.091788 | 0xb875... |
| R | 0.090217 | 0x7ce6... |
| T | 0.073713 | 0x3578... |
| U | 0.055773 | 0x7586... |
| A | 0.051767 | 0x8699... |
| V | 0.048833 | 0xb59d... |
| Y | 0.044449 | 0xd8e3... |
| X | 0.042577 | 0xa95c... |
| W | 0.040705 | 0x5f32... |
| B | 0.036256 | 0x3f89... |
| Z | 0.024268 | 0x7af0... |
| D | 0.011629 | 0xf776... |
| C | 0.010185 | 0x38b9... |
| E | 0.009372 | 0xdc1d... |
| H | 0.001681 | 0xce67... |
| I | 0.000681 | 0x070f... |
| G | 0.000681 | 0x69a3... |

**Total across 28 wallets:** ~20.95 APT  
**Top 3:** bob (12.657), F (1.961), L (1.927)

### Multisig Contract Probes

All 5 contracts healthy — unanimous 2-of-N threshold.

| Pair | Sigs Required | Healthy | Address (short) |
|------|--------------|---------|----------------|
| A-B | 2 | ✓ | 0x0da4... |
| A-G | 2 | ✓ | 0xf56c... |
| Y-Z | 2 | ✓ | 0xd3ff... |
| S-T | 2 | ✓ | 0x3b1c... |
| V-W | 2 | ✓ | 0x40fa... |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — returns Vercel authentication gate on all endpoints  
(`/api/markets`, `/api/v1/markets`, `/` all require authenticated session)

---

## DuckDB Schema

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

## GF(3) Color Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
