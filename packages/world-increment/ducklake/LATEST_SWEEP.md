# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-05-10T10:04 UTC  
**DuckDB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| # | Source | Type | Repos | GF(3) Trit | Color | Name |
|---|--------|------|-------|-----------|-------|------|
| 1 | plurigrid | org | 100 | +1 | #b8bb26 | PLUS |
| 2 | kubeflow | org | 48 | -1 | #cc241d | MINUS |
| 3 | TeglonLabs | org | 4 | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | user | 100 | +1 | #b8bb26 | PLUS |
| 5 | zubyul | user | 49 | -1 | #cc241d | MINUS |
| 6 | DJedamski | social | 6 | 0 | #d3869b | ERGODIC |
| 7 | kristinezheng | social | 6 | +1 | #b8bb26 | PLUS |
| 8 | M1shaaa | social | 8 | -1 | #cc241d | MINUS |
| 9 | migalkin | social | 19 | 0 | #d3869b | ERGODIC |
| 10 | AustinCStone | social | 30 | +1 | #b8bb26 | PLUS |
| 11 | wasita | social | 11 | -1 | #cc241d | MINUS |

**Total: 381 repo snapshots across 11 world_increments**

### Highlights

**plurigrid** (100 repos, latest: gorj → 2026-05-10):
- `gorj` (Clojure) — forj + Rama topology nREPL routing + GF(3) gay trit coloring, 134 open issues
- `zig-syrup` (Zig) — High-performance OCapN Syrup, pushed 2026-04-30
- `asi` (HTML) ★21 — "everything is topological chemputer!"
- `nanoclj-zig` (Zig) — NaN-boxed Clojure interpreter with interaction nets + GF(3)
- `nash-portal` (Rust) — NASH token TUI in browser via ratzilla WASM

**kubeflow** (48 repos, latest: internal-acls → 2026-05-09):
- `kubeflow` ★15628 — Machine Learning Toolkit for Kubernetes
- `pipelines` ★4137 — ML Pipelines, 497 open issues
- `spark-operator` ★3125 — Kubernetes operator for Apache Spark
- `trainer` ★2097 — Distributed AI Model Training, 111 issues
- `mcp-apache-spark-history-server` ★167 — MCP Server for Spark debugging

**TeglonLabs** (4 repos):
- `mathpix-gem` (Ruby) — Mathematical image to LaTeX OCR, pushed 2026-01-01
- `monad-mcp-server` — Monad MCP Server
- `coin-flip-mcp` (JS) — Random.org coin flips MCP
- `topoi` (Python) — Mathematical topology workspace

**bmorphism** (100 repos, latest: Gay.jl → 2026-05-10):
- `Gay.jl` (Julia) ★1 — Wide-gamut color sampling with SPI, 187 open issues
- `ocaml-mcp-sdk` (OCaml) ★61 — OCaml SDK for MCP with Jane Street oxcaml_effect
- `anti-bullshit-mcp-server` ★23 — Claims analysis MCP
- `say-mcp-server` ★20 — macOS TTS MCP
- `zig-syrup` (Zig) — OCapN Syrup encoder/decoder

**zubyul** (49 repos, latest: voice-observatory → 2026-04-24):
- `voice-observatory` — Passive macOS TUI observing voice-download pathways
- `nash-tui` (Rust) — NASH token TUI via GeckoTerminal OHLCV
- `tilelang-kernels` (Python) — GPU kernels for GF(3) trit classification, Blackwell target
- `gay-world` (Python) ★1 — Goblin world builder with MLX task decomposition
- `kinesis-kb360pro` — Kinesis Advantage360 Pro keyboard with GF(3) color analysis

**Social Graph (migalkin/DJedamski/wasita/kristinezheng/M1shaaa/AustinCStone)**:
- migalkin: KG researcher — `StarE` ★89, `NBFNet_mlx` ★10, `kgcourse2021` ★25
- DJedamski: 6 data science repos (Kaggle, Coursera, R)
- wasita: 11 repos — `magic-garden` ★2, `vocoder` (JS), `wasita.github.io`
- kristinezheng: 6 repos — neuroscience/MIT student portfolio
- M1shaaa: 8 repos — Lookit studies, MNIST classifier
- AustinCStone: 30 repos — various Python/bitmind forks

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Ledger version at query time:** 5,208,333,013  
**Status:** All 28 addresses returned HTTP 404 `resource_not_found`

All addresses (alice, bob, A–Z) do not have an initialized `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource at this ledger version. The accounts have not been funded with APT on mainnet.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acd... | null (unfunded) |
| bob | 0x0a3c00c... | null (unfunded) |
| A–Z | 0x8699edc...–0x7af0ef6... | null (all unfunded) |

### Multisig Contract Probes
All 5 contracts responded successfully to `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | **2** | ✓ |
| A-G | 0xf56c4a1c... | **2** | ✓ |
| Y-Z | 0xd3ffe181... | **2** | ✓ |
| S-T | 0x3b1c3ae9... | **2** | ✓ |
| V-W | 0x40fad7b4... | **2** | ✓ |

All multisig contracts require 2-of-N signatures. All are healthy (on-chain, callable).

### MNX Markets (testnet.mnx.fi)
**Status:** SPA (Next.js) — HTTP 200 but no REST API endpoints accessible.  
Paths probed: `/api/markets`, `/api/v1/markets`, `api.testnet.mnx.fi/markets`.  
Data: **unavailable** (client-side rendered, no public JSON API).

---

## DuckDB Schema Summary

```
world_increments:  11 rows  (one per source, GF3 chain)
repo_snapshots:   381 rows  (all repos from 11 sources)
aptos_snapshots:   28 rows  (all NULL balance — unfunded)
multisig_probes:    5 rows  (all 2-of-N, healthy=true)
mnx_snapshots:      1 row   (SPA-unavailable)
```

## GF(3) Color Chain Legend
- **ERGODIC** `#d3869b` (trit=0): TeglonLabs, DJedamski, migalkin
- **PLUS** `#b8bb26` (trit=+1): plurigrid, bmorphism, kristinezheng, AustinCStone
- **MINUS** `#cc241d` (trit=-1): kubeflow, zubyul, M1shaaa, wasita
