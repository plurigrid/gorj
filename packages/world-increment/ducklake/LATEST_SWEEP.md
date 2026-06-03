# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-03  
**DuckDB:** `world-increments.duckdb`  
**Sweep rows:** 223 world_increments · 223 repo_snapshots · 28 aptos_snapshots · 5 multisig_probes · 15 mnx_snapshots

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Org / User       | Type    | Repos | Total Stars |
|-----------------|---------|------:|------------:|
| kubeflow         | org     |    48 |      34,174 |
| migalkin         | user    |     6 |         279 |
| bmorphism        | user    |    28 |         216 |
| AustinCStone     | user    |     7 |         107 |
| plurigrid        | org     |   100 |          75 |
| zubyul           | user    |    14 |           8 |
| wasita           | user    |     5 |           4 |
| DJedamski        | user    |     4 |           3 |
| TeglonLabs       | org     |     4 |           2 |
| M1shaaa          | user    |     3 |           0 |
| kristinezheng    | user    |     4 |           0 |
| **TOTAL**        |         | **223** | **34,868** |

### GF(3) Color Chain Distribution

| Trit | Name    | Color   | Count |
|------|---------|---------|------:|
| 0    | ERGODIC | #d3869b |    74 |
| 1    | PLUS    | #b8bb26 |    75 |
| -1   | MINUS   | #cc241d |    74 |

### Top Repos by Stars (this sweep)

| Org/User   | Repo            | Stars  | Language |
|------------|-----------------|-------:|----------|
| kubeflow   | kubeflow        | 15,704 | —        |
| kubeflow   | pipelines       |  4,152 | Python   |
| kubeflow   | spark-operator  |  3,125 | Python   |
| kubeflow   | trainer         |  2,110 | Go       |
| kubeflow   | katib           |  1,685 | Python   |
| migalkin   | NodePiece       |    144 | Python   |
| AustinCStone | TextGAN       |     92 | Python   |
| migalkin   | StarE           |     89 | Python   |
| bmorphism  | anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism  | risc0-cosmwasm-example | 23 | Rust |

### Notable Repos Observed

- **bmorphism/world** (2026-06-02): Local worlds launcher for SA3, jank, world proofs — pushed yesterday
- **bmorphism/Gay.jl**: Wide-gamut color sampling with splittable determinism (GF3 SPI) — 189 open issues
- **bmorphism/ocaml-mcp-sdk**: OCaml SDK for MCP using Jane Street's oxcaml_effect — 61 stars
- **zubyul/tilelang-kernels**: TileLang GPU kernels for GF(3) trit classification, targeting NVIDIA GB10 Blackwell
- **migalkin/NodePiece**: ICLR'22 paper on compositional KG representations — 144 stars
- **TeglonLabs/mathpix-gem**: Mathematical image→LaTeX/SMILES/markdown with security-first design
- **plurigrid**: 100 repos total across the org spanning Clojure, Julia, Go, TypeScript

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All balances queried via `0x1::coin::balance` view function. 1s sleep between calls.

| World | Balance (APT) | Address (prefix) |
|-------|-------------:|-----------------|
| bob   |   12.657007  | 0x0a3c00c58f... |
| F     |    1.960516  | 0x18a14b5b4b... |
| L     |    1.927269  | 0x7c2eaeafad... |
| J     |    1.895093  | 0x4d964db8f5... |
| alice |    0.436434  | 0xc793acdec1... |
| O     |    0.210136  | 0x73252b6011... |
| K     |    0.161961  | 0xa732040a6b... |
| P     |    0.140136  | 0x6218792de4... |
| M     |    0.112285  | 0x6fed37a755... |
| N     |    0.106121  | 0xe7dde6da0a... |
| Q     |    0.103240  | 0xac40fa50b8... |
| S     |    0.091788  | 0xb8753014e4... |
| R     |    0.090217  | 0x7ce605cc8f... |
| T     |    0.073713  | 0x35781dc0e4... |
| U     |    0.055773  | 0x75860da475... |
| A     |    0.051767  | 0x8699edc096... |
| V     |    0.048833  | 0xb59dd81703... |
| Y     |    0.044449  | 0xd8e32848f1... |
| X     |    0.042577  | 0xa95cbbd116... |
| W     |    0.040705  | 0x5f32aef70f... |
| B     |    0.036256  | 0x3f892ebe6e... |
| Z     |    0.024268  | 0x7af0ef6e1b... |
| D     |    0.011629  | 0xf77656248f... |
| C     |    0.010185  | 0x38b99e63ad... |
| E     |    0.009372  | 0xdc1d9d533b... |
| H     |    0.001681  | 0xce67c327a7... |
| G     |    0.000681  | 0x69a394c0b0... |
| I     |    0.000681  | 0x070fe5d74e... |

**Total swarm APT:** ~20.69 APT  
**Note:** All accounts exist on mainnet. Legacy CoinStore not present; balances retrieved via FA view function `0x1::coin::balance`.

### Multisig Contract Probes

| Pair | Address (prefix)       | Sigs Required | Healthy |
|------|------------------------|:-------------:|:-------:|
| A-B  | 0x0da4f428a0c007...   |       2       |    ✓    |
| A-G  | 0xf56c4a1c09062...    |       2       |    ✓    |
| Y-Z  | 0xd3ffe1812b2df4...   |       2       |    ✓    |
| S-T  | 0x3b1c3ae905d44c...   |       2       |    ✓    |
| V-W  | 0x40fad7b423a843...   |       2       |    ✓    |

All 5 multisig contracts are 2-of-2 and healthy.

### MNX Markets Snapshot (testnet.mnx.fi)

Source: SPA rendered content (Next.js). `/api/markets` returned 404; data extracted from rendered page via WebFetch.

| Ticker    | Name                    | Category    |    Price | Change % |
|-----------|------------------------|-------------|----------:|--------:|
| NVDA      | NVIDIA                  | stock       |   $221.19 |   -3.33% |
| TSLA      | Tesla                   | stock       |   $418.53 |   +0.03% |
| MSFT      | Microsoft               | stock       |   $436.87 |   -3.08% |
| AAPL      | Apple                   | stock       |   $314.61 |   +2.81% |
| GOOGL     | Alphabet                | stock       |   $361.04 |   -1.49% |
| SPX       | S&P 500                 | index       |  7,605.00 |   +0.21% |
| GOLD      | Gold                    | commodity   |  $4,400.0 |   -1.85% |
| SILVER    | Silver                  | commodity   |    $74.03 |   -3.03% |
| USO       | Oil Fund                | commodity   |   $141.63 |   +6.25% |
| CPER      | Copper                  | commodity   |    $40.05 |   -0.67% |
| OAI26     | OpenAI 2026 Valuation   | derivative  |    $525B  |     0.0% |
| ANT26     | Anthropic 2026          | derivative  |    $423B  |     0.0% |
| VIX       | VIX                     | index       |    16.10  |   -0.31% |
| DPREZ     | Democrat 2028           | prediction  |      50%  |     0.0% |
| INVADE27  | Taiwan invasion 2027    | prediction  |      17%  |     0.0% |

---

## Database Summary

```
world-increments.duckdb
  ├── world_increments  (cumulative GF3 chain)
  ├── repo_snapshots    (223 repos this sweep, 11 sources)
  ├── aptos_snapshots   (28 wallets: Hamming A-Z + alice/bob)
  ├── multisig_probes   (5 contracts, all 2-of-2 healthy)
  └── mnx_snapshots     (15 markets: stocks, commodities, derivatives, predictions)
```
