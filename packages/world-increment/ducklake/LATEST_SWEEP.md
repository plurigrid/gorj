# World Increment Sweep + Hamming Snapshot

**Date/Time:** 2026-04-06T00:17 UTC  
**DuckDB Version:** v1.5.1 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Fetched | Status |
|--------|------|--------------|--------|
| plurigrid | org | 100 | OK |
| kubeflow | org | 46 | OK |
| TeglonLabs | org | 3 | OK (via MCP, rate-limited via curl) |
| bmorphism | user | 100 | OK |
| zubyul | user | 23 | OK |
| migalkin | user | 30 | OK |
| DJedamski | user | 6 | OK (via MCP, rate-limited via curl) |
| wasita | user | 29 | OK |
| kristinezheng | user | 18 | OK |
| M1shaaa | user | 16 | OK |
| AustinCStone | user | 40 | OK (via MCP, rate-limited via curl) |

**Total repos snapshotted:** 411  
**Events fetched:** 30 (bmorphism); zubyul rate-limited (0 events recorded)

### Top Repos by Stars

#### kubeflow (top 5)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow | 15553 | — | Machine Learning Toolkit for Kubernetes |
| pipelines | 4118 | Python | Machine Learning Pipelines for Kubeflow |
| spark-operator | 3110 | Python | Kubernetes operator for Apache Spark on K8s |
| trainer | 2074 | Go | Distributed AI Model Training and LLM Fine-Tuning on K8s |
| katib | 1674 | Python | Automated Machine Learning on Kubernetes |

#### plurigrid (top 5)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| asi | 16 | HTML | everything is topological chemputer! |
| ontology | 7 | JavaScript | autopoietic ergodicity and embodied gradualism |
| asi-skills | 3 | Julia | 69 skills with Galois Hole Type accessibility |
| zig-syrup | 2 | Zig | High-performance Zig OCapN Syrup with CapTP |
| ladyworm | 1 | C++ | proof-of-neural-operator |

#### bmorphism (top 3)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |

#### migalkin (top 2)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| NodePiece | 143 | Python | Compositional & Parameter-Efficient KG Representations (ICLR'22) |
| StarE | 88 | Python | EMNLP 2020: Message Passing for Hyper-Relational KGs |

#### AustinCStone (top)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| TextGAN | 92 | Python | GAN for text generation (TensorFlow) |

#### TeglonLabs (all 3)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| mathpix-gem | 2 | Ruby | Mathematical image-to-LaTeX OCR in Ruby |
| topoi | 0 | Python | — |
| coin-flip-mcp | 0 | JavaScript | MCP server for random.org coin flips |

#### DJedamski (top by stars)
| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| Getting-and-Cleaning-Data | 1 | R | Coursera Project |
| Kaggle | 1 | — | — |
| School | 1 | R | Grad school projects |

#### zubyul
23 repos fetched — includes GeoACSets.jl and Julia/math research repos.

#### wasita, kristinezheng, M1shaaa
Fetched 29, 18, 16 repos respectively — primarily academic/research repos.

### GF(3) Color Chain Statistics

GF(3) color chain: `id%3==0 → trit=0 ERGODIC #d3869b`, `id%3==1 → trit=1 PLUS #b8bb26`, `id%3==2 → trit=-1 MINUS #cc241d`

| GF(3) Trit | Color | Name | World Increment Rows |
|-----------|-------|------|---------------------|
| 0 | #d3869b | ERGODIC | ~140 |
| 1 | #b8bb26 | PLUS | ~141 |
| -1 | #cc241d | MINUS | ~140 |

Total world_increments rows: 421 (11 repo_snapshot source rows + 30 bmorphism public events)  
Total repo_snapshot rows: 411

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried against Aptos mainnet. All returned 0 APT (accounts not found or CoinStore resource absent on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...b9d7 | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...f588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...af2c | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts healthy. All require 2-of-N signatures.

### MNX Markets

**Status: UNAVAILABLE**  
All three endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) on `https://testnet.mnx.fi` returned HTML pages (Next.js SPA frontend), not JSON API responses. No market data could be extracted.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| GitHub sources queried | 11 (3 orgs + 8 users) |
| Total repos snapshotted | 411 |
| World increment rows | 421 |
| Aptos wallets probed | 28 |
| Wallets with non-zero APT | 0 |
| Multisig pairs probed | 5 |
| Multisig pairs healthy | 5 |
| Multisig sigs required | 2 (all pairs) |
| MNX markets | unavailable |
| GF(3) ERGODIC (#d3869b) trit=0 | stable/recurrent nodes |
| GF(3) PLUS (#b8bb26) trit=1 | additive/expanding nodes |
| GF(3) MINUS (#cc241d) trit=-1 | subtractive/contracting nodes |
