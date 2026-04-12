# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-12

## Sweep Metadata
- **Date:** 2026-04-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) color chain:** ERGODIC `#d3869b` (trit=0) → PLUS `#b8bb26` (trit=1) → MINUS `#cc241d` (trit=2≡-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 47 | 33,860 |
| migalkin | user (zubyul graph) | 30 | 277 |
| bmorphism | user | 100 | 131 |
| AustinCStone | user (zubyul graph) | 43 | 108 |
| plurigrid | org | 100 | 40 |
| zubyul | user | 24 | 13 |
| DJedamski | user (zubyul graph) | 11 | 7 |
| TeglonLabs | org | 53 | 6 |
| kristinezheng | user (zubyul graph) | 18 | 0 |
| M1shaaa | user (zubyul graph) | 16 | 0 |
| wasita | user (zubyul graph) | — | rate-limited |

> `wasita` hit the unauthenticated GitHub API rate limit (60 req/hr). Data not captured.

**Events captured:** bmorphism (30), zubyul (30)

### World Increment Totals

| Metric | Count |
|--------|-------|
| `world_increments` rows | 502 |
| `repo_snapshots` rows | 442 |
| GF3 ERGODIC (#d3869b, trit=0) | 167 |
| GF3 PLUS (#b8bb26, trit=1) | 168 |
| GF3 MINUS (#cc241d, trit=-1) | 167 |

### Top Repos by Stars

| Source | Repo | Language | Stars | Pushed At |
|--------|------|----------|-------|-----------|
| kubeflow | kubeflow | — | 15,568 | 2026-01-05 |
| kubeflow | pipelines | Python | 4,119 | 2026-04-12 |
| kubeflow | spark-operator | Python | 3,112 | 2026-04-11 |
| kubeflow | trainer | Go | 2,080 | 2026-04-10 |
| kubeflow | katib | Python | 1,677 | 2026-04-12 |
| kubeflow | examples | Jsonnet | 1,459 | — |
| kubeflow | manifests | YAML | 1,010 | — |
| kubeflow | arena | Go | 808 | — |
| migalkin | NodePiece | Python | 143 | — |
| AustinCStone | TextGAN | Python | 92 | — |
| bmorphism | ocaml-mcp-sdk | OCaml | 60 | — |

### Top Languages Across All Sources

| Language | Repos |
|----------|-------|
| Python | 76 |
| Go | 18 |
| HTML | 16 |
| Rust | 15 |
| JavaScript | 12 |
| TypeScript | 10 |
| Jupyter Notebook | 10 |
| Clojure | 8 |
| R | 8 |
| Jsonnet | 8 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z) — 28 addresses

Queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).

**Result:** All 28 addresses returned `resource_not_found` — accounts have no funded APT CoinStore on mainnet. All balances recorded as `NULL` in `aptos_snapshots`.

Addresses queried: alice, bob, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z

### Multisig Contract Probes — 5/5 Healthy

Probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisigs healthy** — all configured as 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)

Next.js SPA. REST endpoints (`/api/markets`, `/api/tickers`, `/api/v1/*`) return 404. Live prices unavailable without JavaScript runtime. 32 ticker symbols extracted from HTML/JS bundles:

| Category | Tickers |
|----------|---------|
| Equities | AAPL, AMZN, ASML, CRWV, GOOGL, INTC, META, MSFT, MU, NVDA, TSLA, TSM |
| Commodities | CPER, GOLD, SILVER, USO |
| Indices | H100, SPX, VIX |
| Bonds | IEF, TLT |
| Synthetic/26-series | ANT26, ARC26, CPI26, DPREZ, ECI26, FMATH26, INVADE27, OAI26, OAITOP26, SFHOME26, URA |

Prices stored as `NULL` in `mnx_snapshots`.

---

## DuckDB Schema

```
world-increments.duckdb
├── world_increments    502 rows   (GF3-tagged sweep events)
├── repo_snapshots      442 rows   (org/user repos)
├── aptos_snapshots      28 rows   (hamming swarm wallets, all NULL APT)
├── multisig_probes       5 rows   (all 2-of-2, healthy)
└── mnx_snapshots        32 rows   (tickers, prices NULL — SPA)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,568 stars — flagship ML platform for Kubernetes (active 2026-01-05)
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-12)
- **kubeflow/spark-operator**: 3,112 stars — Kubernetes operator for Apache Spark (pushed 2026-04-11)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **5/5 Hamming multisigs**: all 2-of-2, all healthy on Aptos mainnet
- **Hamming swarm wallets**: 28 addresses, all unfunded on mainnet (resource_not_found)
