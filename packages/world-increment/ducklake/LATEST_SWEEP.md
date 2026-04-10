# World-Increment Sweep — 2026-04-10

## Sweep Metadata
- **Date:** 2026-04-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Ledger version (Aptos mainnet):** ~4,831,200,231

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 515 |
| Total Repo Snapshots (cumulative) | 682 |
| Sources Covered This Sweep | 3 orgs + 8 users |
| Aptos Wallets Sampled | 28 |
| Multisig Contracts Probed | 5 |
| MNX Instruments Captured | 14 |
| Total APT in Hamming Swarm | **20.344962 APT** |

---

## GF(3) Color Chain — 12 New Increments (This Sweep)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|----------|-------|------|
| +1 | plurigrid | PushEvent (gorj) | +1 | `#b8bb26` | **PLUS** |
| +2 | plurigrid | PushEvent (asi) | -1 | `#cc241d` | **MINUS** |
| +3 | plurigrid | PushEvent (nanoclj-zig) | 0 | `#d3869b` | **ERGODIC** |
| +4 | kubeflow | PushEvent (pipelines) | +1 | `#b8bb26` | **PLUS** |
| +5 | kubeflow | PushEvent (trainer) | -1 | `#cc241d` | **MINUS** |
| +6 | TeglonLabs | PushEvent (vibespace) | 0 | `#d3869b` | **ERGODIC** |
| +7 | bmorphism | PushEvent (ocaml-mcp-sdk) | +1 | `#b8bb26` | **PLUS** |
| +8 | bmorphism | CreateEvent (anti-bullshit-mcp-server) | -1 | `#cc241d` | **MINUS** |
| +9 | zubyul | PushEvent (gay-world) | 0 | `#d3869b` | **ERGODIC** |
| +10 | migalkin | PushEvent (NodePiece) | +1 | `#b8bb26` | **PLUS** |
| +11 | kristinezheng | PushEvent (pddlgym) | -1 | `#cc241d` | **MINUS** |
| +12 | AustinCStone | PushEvent (TextGAN) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source (This Sweep)

### plurigrid (15 repos sampled, 584 total)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| asi | HTML | 16 | everything is topological chemputer! |
| asi-skills | Julia | 3 | 69 skills with Galois Hole Type accessibility |
| zig-syrup | Zig | 2 | High-performance OCapN Syrup implementation |
| horse | TeX | 1 | — |
| vivarium | Clojure | 1 | — |
| gorj | Clojure | 0 | forj + GF(3) gay trit coloring (this repo) |
| nanoclj-zig | Zig | 0 | NaN-boxed Clojure interpreter in Zig 0.15 |
| graywall | Go | 0 | Container-free deny-by-default sandbox for AI agents |

### kubeflow (10 repos sampled)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| kubeflow | — | 15,565 | Machine Learning Toolkit for Kubernetes |
| pipelines | Python | 4,119 | ML Pipelines for Kubeflow |
| spark-operator | Python | 3,111 | Kubernetes operator for Apache Spark |
| trainer | Go | 2,079 | Distributed AI Model Training + LLM Fine-Tuning |
| katib | Python | 1,675 | Automated Machine Learning on Kubernetes |
| manifests | YAML | 1,010 | Kubeflow AI Platform Manifests |
| mpi-operator | Go | 522 | Kubernetes Operator for MPI-based apps |
| mcp-apache-spark | Python | 150 | MCP Server for Spark History Server |

### TeglonLabs (10 repos sampled, 30 total)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| mathpix-gem | Ruby | 2 | Transform math images to LaTeX |
| vibespace | HTML | 2 | MCP experience with NATS streaming |
| acp.el | Emacs Lisp | 1 | ACP implementation in Emacs lisp |
| mcp-terminal | Rust | 1 | Hardware-accelerated GPU terminal emulator |
| Stahl | Rust | 0 | Embedded scheme interpreter in xenoironic Rost |
| narya | OCaml | 0 | Proof assistant for higher-dimensional type theory |

### bmorphism (10 repos sampled, 427 total)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| ocaml-mcp-sdk | OCaml | 60 | OCaml SDK for MCP using Jane Street oxcaml |
| anti-bullshit-mcp-server | JavaScript | 23 | MCP server for claim analysis |
| shitcoin | Python | 5 | cw20 asset denom for IBC |
| open-location-code-zig | Zig | 3 | Open Location Code for Zig (first ever) |
| flox-mcp-bb | Clojure | 0 | Open-source MCP server for Flox |

### zubyul (8 repos sampled)
| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| gay-world | Python | 1 | Goblin world builder with MLX task decomposition |
| EyeGestures | Python | 1 | Gaze tracking software |
| tilelang-kernels | Python | 0 | TileLang GPU kernels for GF(3) classification |
| Gay.jl | Julia | 0 | Wide-gamut color sampling with splittable determinism |

### Zubyul Social Graph
| User | Repo | Language | Stars | Description |
|------|------|----------|-------|-------------|
| migalkin | NodePiece | Python | 143 | Compositional KG representations (ICLR'22) |
| migalkin | StarE | Python | 88 | Message Passing for Hyper-Relational KGs (EMNLP'20) |
| migalkin | kgcourse2021 | HTML | 25 | Course materials on Knowledge Graphs |
| AustinCStone | TextGAN | Python | 92 | GAN for text generation in TensorFlow |
| AustinCStone | StereoVisionMRF | Python | 11 | MRF with loopy belief propagation for stereo depth |
| DJedamski | kaggle-titanic | Python | 2 | Kaggle Titanic tutorial |
| wasita | magic-garden | Python | 1 | Discord Magic Garden bot |
| kristinezheng | pddlgym | PDDL | 0 | PDDL domain → OpenAI Gym environment |

---

## Hamming Swarm — Aptos APT Balances

*Queried via `0x1::coin::balance` view function, Aptos mainnet*

| World | Balance (APT) | GF3 Trit |
|-------|--------------|----------|
| **bob** | **12.657007** | PLUS |
| **F** | 1.960516 | PLUS |
| **L** | 1.927269 | ERGODIC |
| **J** | 1.895093 | MINUS |
| K | 0.161961 | ERGODIC |
| alice | 0.436434 | PLUS |
| O | 0.210136 | MINUS |
| P | 0.140136 | PLUS |
| M | 0.112285 | ERGODIC |
| N | 0.106121 | MINUS |
| Q | 0.103240 | PLUS |
| S | 0.091788 | ERGODIC |
| R | 0.090217 | MINUS |
| T | 0.073713 | PLUS |
| U | 0.055773 | ERGODIC |
| A | 0.051767 | MINUS |
| V | 0.047833 | PLUS |
| W | 0.040705 | ERGODIC |
| X | 0.042577 | MINUS |
| Y | 0.044449 | PLUS |
| B | 0.036256 | ERGODIC |
| Z | 0.023268 | MINUS |
| E | 0.012561 | PLUS |
| D | 0.011629 | ERGODIC |
| C | 0.010185 | MINUS |
| G | 0.000681 | PLUS |
| H | 0.000681 | ERGODIC |
| I | 0.000681 | MINUS |

**Total swarm balance: 20.344962 APT**

> Note: Addresses used new FA framework (no `CoinStore` resource); balances retrieved via `0x1::coin::balance` view function.

---

## Multisig Probes (Aptos Mainnet)

*All probed via `0x1::multisig_account::num_signatures_required`*

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

**5/5 multisig contracts healthy — all require 2-of-N signatures.**

---

## MNX Markets Snapshot (testnet.mnx.fi)

| Ticker | Name | Category | Price | Change |
|--------|------|----------|-------|--------|
| CRWV | CoreWeave | Stocks | $104.70 | **+14.60%** |
| INTC | Intel | Stocks | $62.90 | +4.33% |
| NVDA | NVIDIA | Stocks | $189.14 | +3.33% |
| AMZN | Amazon | Stocks | $238.52 | +2.85% |
| MU | Micron Technology | Stocks | $418.05 | +2.68% |
| TSM | Taiwan Semiconductor | Stocks | $374.19 | +2.51% |
| AAPL | Apple | Stocks | $261.18 | +1.35% |
| GOOGL | Alphabet (Google) | Stocks | $318.83 | +0.70% |
| SPX | S&P 500 Index | Financial | 6,819 | +0.38% |
| MSFT | Microsoft | Stocks | $370.99 | +0.39% |
| IEF | iShares 7-10Y Treasury | Financial | $95.41 | -0.14% |
| META | Meta (Facebook) | Stocks | $626.58 | -0.87% |
| OAI26 | OpenAI 2026 Valuation | Valuations | $518B | -1.89% |
| VIX | CBOE Volatility Index | Financial | 19.56 | -3.74% |

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML toolkit for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — top ML pipeline project
- **plurigrid/asi**: 16 stars — topological chemputer (active push 2026-04-10)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK via Jane Street oxcaml
- **migalkin/NodePiece**: 143 stars — ICLR'22 KG representation work
- **AustinCStone/TextGAN**: 92 stars — classic TensorFlow text GAN
- **bob wallet**: 12.657 APT — highest balance in hamming swarm
- **F, L, J wallets**: ~1.9 APT each — second tier of swarm
- **CRWV (CoreWeave)**: +14.60% — largest MNX mover today
- **All 5 multisigs**: 2-of-N, fully healthy
- **plurigrid/gorj**: This very repo — forj MCP server + GF(3) gay trit coloring
