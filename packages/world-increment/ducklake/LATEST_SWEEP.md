# World-Increment Sweep + Hamming Snapshot — 2026-06-03

## Sweep Metadata
- **Date:** 2026-06-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 103 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| DJedamski | user (zubyul graph) | 6 |
| wasita | user (zubyul graph) | 11 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 40 |
| **TOTAL** | | **~394** |

### Top Repos — plurigrid
| Repo | Stars | Open Issues | Language | Pushed |
|------|-------|-------------|----------|--------|
| plurigrid/gorj | 0 | 320 | Clojure | 2026-06-03 |
| plurigrid/asi | 24 | 4 | HTML | 2026-04-26 |
| plurigrid/ontology | 8 | 16 | JavaScript | 2025-05-27 |
| plurigrid/vcg-auction | 7 | 1 | Rust | 2023-03-16 |
| plurigrid/agent | 5 | 6 | Python | 2023-03-31 |

### Top Repos — kubeflow
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,704 | — | 2026-06-02 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-03 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,110 | Go | 2026-06-02 |
| kubeflow/katib | 1,685 | Python | 2026-05-28 |

### Top Repos — bmorphism
| Repo | Stars | Description |
|------|-------|-------------|
| bmorphism/ocaml-mcp-sdk | 61 | OCaml SDK for MCP |
| bmorphism/anti-bullshit-mcp-server | 23 | MCP epistemological framework |
| bmorphism/risc0-cosmwasm-example | 23 | CosmWasm + zkVM |
| bmorphism/say-mcp-server | 20 | macOS TTS MCP |
| bmorphism/babashka-mcp-server | 18 | Babashka MCP server |

### GF(3) Color Chain (72 new increments, id%3)
- **trit=0 (ERGODIC)** `#d3869b` — id%3==0
- **trit=+1 (PLUS)** `#b8bb26` — id%3==1
- **trit=−1 (MINUS)** `#cc241d` — id%3==2

### DuckDB State (cumulative)
| Table | Total Rows |
|-------|-----------|
| world_increments | 95 |
| repo_snapshots | 1,016 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets (alice, bob, A–Z) queried via `https://fullnode.mainnet.aptoslabs.com/v1`.

**All balances: 0.0 APT** — swarm wallets are provisioned but unfunded at time of sweep.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B–Z | (26 addresses) | 0.0 each |

**Total swarm holdings:** 0 APT

### Multisig Contract Probes (Aptos Mainnet)
All 5 contracts are **2-of-2 multisig** — healthy.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...c0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...5b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ |

### MNX Markets Snapshot (testnet.mnx.fi)
15 instruments captured from MNX testnet (SPA rendered).

| Ticker | Name | Price | Change |
|--------|------|-------|--------|
| OAI26 | OpenAI Final 2026 Valuation | $523B | -1.13% |
| ANT26 | Anthropic Final 2026 Valuation | $422B | — |
| TSLA | Tesla Inc | $422.33 | +2.05% |
| INTC | Intel | $106.20 | -2.27% |
| H100 | SemiAnalysis H100 Spot Rental | $2.96 | +1.51% |
| GOLD | Gold Spot | $4,500 | -1.74% |
| AMZN | Amazon | $256.26 | -1.23% |
| TSM | Taiwan Semiconductor | $445.61 | +1.66% |
| NVDA | NVIDIA | $221.95 | -1.00% |
| MSFT | Microsoft | $438.66 | -3.09% |
| AAPL | Apple | $314.80 | +3.15% |
| GOOGL | Alphabet (Google) | $361.82 | -3.06% |
| META | Meta (Facebook) | $601.03 | -0.06% |
| SPX | S&P 500 Index | 7,605 | +0.21% |
| VIX | CBOE Volatility Index | 15.77 | -1.93% |

**Notable:** OpenAI ($523B) leads AI valuations; Anthropic ($422B). AAPL +3.15% top gainer. MSFT -3.09% biggest drop.

### Hamming DuckDB State
| Table | Rows |
|-------|------|
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 15 |

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,704 stars — flagship ML platform for Kubernetes (updated 2026-06-02)
- **kubeflow/pipelines**: 4,151 stars — most popular ML pipeline (active push 2026-06-03)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — TF text generation
- **plurigrid/gorj**: This very repo — 320 open issues, active GF(3) trit REPL orchestration
- **All 5 multisig contracts**: Healthy 2-of-2 on Aptos mainnet
- **MNX AI valuations**: OpenAI $523B, Anthropic $422B on testnet prediction market
