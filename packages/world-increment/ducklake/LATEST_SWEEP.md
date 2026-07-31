# World-Increment Sweep — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.5 Variegata)
- **GF(3) color chain:** ERGODIC `#d3869b` (trit=0) · PLUS `#b8bb26` (trit=1) · MINUS `#cc241d` (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 30 |
| kubeflow | org | 20 |
| TeglonLabs | org | 5 |
| bmorphism | user | 5 |
| zubyul | user | 3 |
| zubyul social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) | social | 7 |
| **Total** | | **70** |

### GF(3) Trit Distribution (70 increments)
| Name | Color | Count |
|------|-------|-------|
| ERGODIC | `#d3869b` | 23 |
| PLUS | `#b8bb26` | 24 |
| MINUS | `#cc241d` | 23 |

Chain: `ERGODIC → PLUS → MINUS → ERGODIC → ...` (id%3: 0→ERGODIC, 1→PLUS, 2→MINUS)

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/pipelines | 4171 | Python |
| kubeflow/spark-operator | 3142 | Python |
| kubeflow/trainer | 2165 | Go |
| kubeflow/katib | 1695 | Python |
| kubeflow/community-distribution | 1029 | YAML |
| kubeflow/arena | 816 | Go |
| kubeflow/kale | 698 | Python |
| kubeflow/mpi-operator | 530 | Go |
| migalkin/NodePiece | 144 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |

### Recently Pushed (plurigrid org, top 5)
| Repo | Language | Pushed |
|------|----------|--------|
| plurigrid/gorj | Clojure | 2026-07-31 |
| plurigrid/zig-syrup | Zig | 2026-07-28 |
| plurigrid/eirobri | Clojure | 2026-07-21 |
| plurigrid/place | TeX | 2026-07-14 |
| plurigrid/asi | HTML | 2026-07-10 |

### Notable Highlights
- **plurigrid/gorj** (this repo): pushed 2026-07-31, 1537 open issues, Clojure — GF(3)/Rama/nREPL topology
- **plurigrid/asi**: 56 stars, HTML — topological chemputer, pushed 2026-07-10
- **kubeflow/mcp-server**: 31 stars, Python — MCP Server for AI dev with Kubeflow, pushed 2026-07-31
- **TeglonLabs/jank-crane**: C++ — crane-jank converged-IR hub with GF3 convergence maps
- **bmorphism/Gay.jl**: Julia — wide-gamut color sampling with 188 open issues, default branch `gay`
- **bmorphism/anti-bullshit-mcp-server**: 22★ — claim validation MCP server
- **migalkin/NodePiece**: 144★ ICLR'22 — compositional KG representations

### Social Graph Notes
- **migalkin**: KG researcher, active (kgcourse2021 pushed 2026-07-10), NBFNet on Apple Silicon
- **wasita**: personal site active 2026-07-21, academic/research repos
- **AustinCStone**: byteruckus (2026-07-15), bmfork repos referencing plurigrid
- **DJedamski**, **kristinezheng**, **M1shaaa**: lower-activity academic profiles

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT** on mainnet. The accounts either have
no CoinStore resource (uninitialized) or are testnet/devnet addresses not present on mainnet.

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…35e | 0.0 |
| D | 0xf776…dd1 | 0.0 |
| E | 0xdc1d…d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…00f | 0.0 |
| I | 0x070f…fc9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…2e9 | 0.0 |
| N | 0xe7dd…b2c | 0.0 |
| O | 0x7325…89d | 0.0 |
| P | 0x6218…948 | 0.0 |
| Q | 0xac40…89a9 | 0.0 |
| R | 0x7ce6…e10 | 0.0 |
| S | 0xb875…386 | 0.0 |
| T | 0x3578…588 | 0.0 |
| U | 0x7586…956 | 0.0 |
| V | 0xb59d…2c3 | 0.0 |
| W | 0x5f32…7b0 | 0.0 |
| X | 0xa95c…47d | 0.0 |
| Y | 0xd8e3…4c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)
All 5 multisig accounts are **healthy** — 2-of-N signature requirement confirmed via
`0x1::multisig_account::num_signatures_required` view call.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)
Site is a **Next.js SPA** — no REST API endpoints exposed server-side.
- `/api/markets` → 404
- `/api/v1/markets` → 404
- `/api/tickers` → 404
- `/markets` → 200 (SPA HTML, no embedded market data)

Market data **unavailable** without browser JS execution.

---

## DuckDB Schema & Row Counts
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 70 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 70 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy) -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```
