# World Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-02T07:00:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 38 |
| kubeflow | org | 16 |
| TeglonLabs | org | 4 |
| bmorphism | user | 16 |
| zubyul | user | 12 (public) |
| migalkin | user (social graph) | 6 |
| wasita | user (social graph) | 4 |
| DJedamski | user (social graph) | 3 |
| kristinezheng | user (social graph) | 2 |
| M1shaaa | user (social graph) | 2 |
| AustinCStone | user (social graph) | 3 |
| **Total** | | **105 repo snapshots** |

### GF(3) Color Chain Distribution

| GF3 Trit | Color | Name | Count |
|----------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 35 |
| +1 | `#b8bb26` | PLUS | 35 |
| −1 | `#cc241d` | MINUS | 35 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,700 | — |
| kubeflow/pipelines | 4,151 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,109 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 24 | HTML |

### Most Active Repos (by open issues)

| Repo | Open Issues | Language |
|------|------------|---------|
| kubeflow/pipelines | 486 | Python |
| kubeflow/fairing | 134 | Jsonnet |
| kubeflow/trainer | 130 | Go |
| plurigrid/gorj | 303 | Clojure |
| bmorphism/Gay.jl | 189 | Julia |
| plurigrid/eirobri | 28 | Clojure |
| plurigrid/nanoclj-zig | 20 | Zig |
| plurigrid/ontology | 16 | JavaScript |

### Social Graph Observations

- **bmorphism** is the primary hub: MCP server ecosystem (OCaml, JS, Rust), Gay.jl color system, world-computing infrastructure
- **zubyul** builds on bmorphism patterns: Gay.jl fork, keyboard tooling, world launchers; many private repos
- **migalkin** is a knowledge graph ML researcher (NodePiece 144★, StarE 89★, KG course)
- **wasita** builds Svelte web apps and research tools; active personal site
- **DJedamski** and **kristinezheng**: primarily academic repos (Coursera, HackMIT)
- **M1shaaa**: Yale/Lookit developmental psychology research
- **AustinCStone**: ML/CV work (TextGAN 92★, StereoVisionMRF), bitmind forks
- **plurigrid/gorj** (this repo) is the hottest by recent activity (pushed 2026-06-02)
- **TeglonLabs/mathpix-gem**: Ruby gem for mathematical OCR

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses probed via Aptos mainnet fullnode. All returned 0 APT — the `CoinStore` resource was absent on every account, indicating these are pre-funded or non-active addresses on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z (26 addrs) | 0x8699...e197c | 0.0 each |

**Total APT across swarm:** 0.0

### Multisig Contract Probes

All 5 multisig contracts are live and responsive. All require **2-of-N signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy (2-of-N, fully operational).**

### MNX Testnet Markets (testnet.mnx.fi)

MNX `/api/markets` returned 404; market data extracted from SPA root.

#### Equities
| Ticker | Name | Price | Δ% |
|--------|------|-------|-----|
| INTC | Intel | $108.75 | −5.77% |
| TSLA | Tesla | $414.10 | −4.73% |
| META | Meta | $601.37 | −4.94% |
| AMZN | Amazon | $259.47 | −4.01% |
| NVDA | NVIDIA | $224.08 | +5.32% |
| MU | Micron | $1,000 | +7.79% |
| TSM | TSMC | $438.03 | +4.60% |
| MSFT | Microsoft | $451.86 | +0.48% |
| AAPL | Apple | $305.17 | −1.92% |
| GOOGL | Alphabet | $373.00 | −1.94% |
| ASML | ASML | $1,600 | +0.65% |

#### Indices & Commodities
| Ticker | Name | Price | Δ% |
|--------|------|-------|-----|
| SPX | S&P 500 | 7,594 | +0.25% |
| GOLD | Gold | $4,500 | +0.05% |
| SILVER | Silver | $76.78 | +1.25% |
| VIX | Volatility | 16.05 | +4.56% |
| USO | US Oil Fund | $135.69 | +5.04% |
| CPER | US Copper Index | $39.98 | +2.72% |

#### Prediction Markets
| Ticker | Description | Price | Δ% |
|--------|-------------|-------|-----|
| OAI26 | OpenAI 2026 Valuation | $527B | −0.19% |
| ANT26 | Anthropic 2026 Valuation | $417B | −0.95% |
| DPREZ | Democrat President 2028 | 51% | +1.60% |
| INVADE27 | China invades Taiwan by 2027 | 16% | +3.14% |

---

## DuckDB Schema Summary

```
world_increments  : 105 rows  — GF(3) color-chained GitHub events
repo_snapshots    : 105 rows  — full repo metadata per increment
aptos_snapshots   :  28 rows  — Hamming swarm wallet balances
multisig_probes   :   5 rows  — multisig contract sig requirements
mnx_snapshots     :  21 rows  — MNX testnet market data
```

**GF(3) ergodicity achieved:** equal trit distribution (35 ERGODIC / 35 PLUS / 35 MINUS).
