# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 43 |
| bmorphism | user | 30 |
| kubeflow | org | 20 |
| zubyul | user | 10 |
| migalkin | user | 5 |
| wasita | user | 5 |
| TeglonLabs | org | 4 |
| AustinCStone | user | 4 |
| M1shaaa | user | 3 |
| kristinezheng | user | 3 |
| DJedamski | user | 3 |
| **Total** | | **130** |

### Star Counts by Source

| Source | Total Stars |
|--------|------------|
| kubeflow | 33,222 |
| migalkin | 276 |
| bmorphism | 215 |
| AustinCStone | 103 |
| plurigrid | 64 |
| wasita | 4 |
| TeglonLabs | 2 |
| DJedamski | 2 |
| zubyul | 1 |

### Top 10 Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |

### Highlight Repos (Social Graph)

**bmorphism** (most active MCP ecosystem):
- `bmorphism/Gay.jl` — 189 open issues, pushed 2026-06-06 — Wide-gamut GF(3) color sampling (Julia)
- `bmorphism/ocaml-mcp-sdk` — 61 stars — OCaml SDK for Model Context Protocol (Jane Street oxcaml_effect)
- `bmorphism/anti-bullshit-mcp-server` — 23 stars — Epistemological claim analysis MCP
- `bmorphism/risc0-cosmwasm-example` — 23 stars — CosmWasm + zkVM RISC-V EFI template
- `bmorphism/say-mcp-server` — 20 stars — macOS TTS MCP

**plurigrid** (most active org):
- `plurigrid/gorj` — 399 open issues, pushed 2026-06-06 — GF(3) gay trit coloring REPL orchestration (this repo)
- `plurigrid/eirobri` — 29 issues — EiRoBri replay world (Clojure)
- `plurigrid/asi` — 25 stars — topological chemputer (HTML)
- `plurigrid/nanoclj-zig` — 20 issues — NaN-boxed Clojure interpreter in Zig 0.15

**zubyul social graph**:
- `zubyul/plurigrid-site` — 11 issues — Plurigrid world site deployment (Svelte)
- `zubyul/tilelang-kernels` — TileLang GPU kernels for GF(3) trit on Blackwell GB10

**migalkin** (Knowledge Graph research):
- `migalkin/NodePiece` — 144 stars — ICLR'22 Knowledge Graph embeddings (Python)
- `migalkin/StarE` — 89 stars — Hyper-Relational KG message passing (EMNLP 2020)
- `migalkin/kgcourse2021` — 25 stars — Knowledge Graphs course materials

**kubeflow** (newest active repos):
- `kubeflow/mcp-apache-spark-history-server` — 174 stars — MCP Server for Spark History Server (2026)
- `kubeflow/notebooks` — pushed 2026-06-06 — Kubeflow Notebooks for AI/ML on Kubernetes
- `kubeflow/pipelines` — pushed 2026-06-06 — 4,152 stars, 491 open issues

### GF(3) Chain Distribution

```
ERGODIC #d3869b (trit=0):  43 increments
PLUS    #b8bb26 (trit=1):  44 increments
MINUS   #cc241d (trit=2):  43 increments
Total:                    130 increments
```

### DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 130 |
| repo_snapshots | 130 |

### Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**All 28 wallets queried against `fullnode.mainnet.aptoslabs.com`.**  
**Result: All returned `resource_not_found` (APT coin store not initialized).**  
API response: `"error_code": "resource_not_found"` at ledger version 5,603,944,603.  
Addresses exist in the swarm configuration but have no on-chain APT CoinStore resources.

| World | Address | APT Balance |
|-------|---------|------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...35e | NULL |
| D | 0xf776...dd1 | NULL |
| E | 0xdc1d...d36 | NULL |
| F | 0x18a1...f71 | NULL |
| G | 0x69a3...f32 | NULL |
| H | 0xce67...00f | NULL |
| I | 0x070f...fc9 | NULL |
| J | 0x4d96...f54 | NULL |
| K | 0xa732...dc4 | NULL |
| L | 0x7c2e...ba9 | NULL |
| M | 0x6fed...2e9 | NULL |
| N | 0xe7dd...b2c | NULL |
| O | 0x7325...89d | NULL |
| P | 0x6218...948 | NULL |
| Q | 0xac40...89a | NULL |
| R | 0x7ce6...e10 | NULL |
| S | 0xb875...386 | NULL |
| T | 0x3578...588 | NULL |
| U | 0x7586...956 | NULL |
| V | 0xb59d...2c3 | NULL |
| W | 0x5f32...b0 | NULL |
| X | 0xa95c...47d | NULL |
| Y | 0xd8e3...4c4 | NULL |
| Z | 0x7af0...97c | NULL |

### Multisig Contract Probes

All 5 multisig accounts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...6d | 2 | ✓ |

**5/5 multisigs healthy. All require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All endpoints (`/`, `/api/markets`, `/api/v1/markets`, `/markets`) return HTTP 200 with a Vercel authentication challenge page. No market data accessible without Vercel credentials.

### DuckDB Table Counts

| Table | Rows |
|-------|------|
| aptos_snapshots | 28 (all NULL balance) |
| multisig_probes | 5 (all healthy) |
| mnx_snapshots | 0 (unavailable) |

### Schema

```sql
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

---

## GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,  gf3_color=ERGODIC,  gf3_name=#d3869b
id mod 3 == 1  →  trit=1,  gf3_color=PLUS,     gf3_name=#b8bb26
id mod 3 == 2  →  trit=2,  gf3_color=MINUS,    gf3_name=#cc241d
```
