# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-16

**Timestamp:** 2026-05-16T01:21 UTC  
**Branch:** `world-increment/sweep-2026-05-16-0121`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 26 |
| kubeflow | org | 20 |
| TeglonLabs | org | 4 |
| bmorphism | user | 42 |
| zubyul | user | 15 |
| migalkin | user (zubyul social graph) | 7 |
| DJedamski | user (zubyul social graph) | 5 |
| wasita | user (zubyul social graph) | 7 |
| kristinezheng | user (zubyul social graph) | 5 |
| M1shaaa | user (zubyul social graph) | 5 |
| AustinCStone | user (zubyul social graph) | 10 |
| **Total** | | **146** |

### Notable Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,632 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,140 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,125 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,098 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1,682 | Python | Automated ML on Kubernetes |
| kubeflow/examples | 1,463 | Jsonnet | Extended examples and tutorials |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| migalkin/NodePiece | 144 | Python | Compositional KG Representations (ICLR'22) |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/gorj | 0 | Clojure | forj + Rama nREPL routing + GF(3) trit coloring |

### Recently Active (pushed ≤ 24h of sweep)

- `bmorphism/Gay.jl` — pushed 2026-05-16T00:32 — Wide-gamut color sampling with SPI
- `kubeflow/dashboard` — pushed 2026-05-16T00:25 — Kubeflow Central Dashboard
- `plurigrid/gorj` — pushed 2026-05-16T00:11 — **this repo**
- `kubeflow/pipelines` — pushed 2026-05-15T21:36 — ML Pipelines
- `kubeflow/kale` — pushed 2026-05-15T19:04 — Kubeflow superfood for Data Scientists
- `kubeflow/mcp-apache-spark-history-server` — pushed 2026-05-13T19:15 — MCP for Spark

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 48 |
| +1 | PLUS | `#b8bb26` | 49 |
| -1 | MINUS | `#cc241d` | 49 |

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (146 steps, completing 48.67 full GF(3) cycles)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses in the Hamming swarm (alice, bob, A–Z) queried via Aptos mainnet fullnode. All returned **0.0 APT** — wallets are either uninitialized or hold no APT in `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…535e | 0.0 |
| D | 0xf776…cdd1 | 0.0 |
| E | 0xdc1d…8d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…300f | 0.0 |
| I | 0x070f…1fc9 | 0.0 |
| J | 0x4d96…7f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…eba9 | 0.0 |
| M | 0x6fed…f2e9 | 0.0 |
| N | 0xe7dd…1b2c | 0.0 |
| O | 0x7325…a89d | 0.0 |
| P | 0x6218…c948 | 0.0 |
| Q | 0xac40…c89a9 | 0.0 |
| R | 0x7ce6…6e10 | 0.0 |
| S | 0xb875…0386 | 0.0 |
| T | 0x3578…4588 | 0.0 |
| U | 0x7586…9956 | 0.0 |
| V | 0xb59d…f2c3 | 0.0 |
| W | 0x5f32…c7b0 | 0.0 |
| X | 0xa95c…047d | 0.0 |
| Y | 0xd8e3…44c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts **healthy** — all require 2-of-2 signatures:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is a Next.js SPA — all market data fetched client-side via JavaScript bundles. No public REST API endpoint found. Status: **UNAVAILABLE (SPA, no REST endpoint exposed)**.

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

## Row Counts

```
world_increments  : 146 rows  (GF3 trit-colored repo events)
repo_snapshots    : 146 rows  (github repo metadata)
aptos_snapshots   :  28 rows  (hamming swarm wallet balances)
multisig_probes   :   5 rows  (2-of-2 multisig contracts, all healthy)
mnx_snapshots     :   0 rows  (SPA, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**
