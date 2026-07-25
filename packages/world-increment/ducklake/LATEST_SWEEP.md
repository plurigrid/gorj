# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-25T19:30:00Z  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | ~60 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 12 |
| DJedamski | social-graph | 5 |
| wasita | social-graph | 12 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 5 |
| AustinCStone | social-graph | 11 |

**Total this sweep:** 311 repos  
**Cumulative in DB:** 1,255 repo snapshots across all runs

### Notable Activity (pushed within 7 days of sweep)

- **plurigrid/gorj** — Clojure, pushed 2026-07-25 — *forj + Rama topology nREPL routing + GF(3) gay trit coloring* (1,398 open issues)
- **kubeflow/pipelines** — Python, ★4170, pushed 2026-07-25 — *Machine Learning Pipelines for Kubeflow*
- **kubeflow/trainer** — Go, ★2153, pushed 2026-07-25 — *Distributed AI Model Training and LLM Fine-Tuning on Kubernetes*
- **kubeflow/spark-operator** — Python, ★3143, pushed 2026-07-25 — *Kubernetes operator for managing Apache Spark lifecycle*
- **kubeflow/dashboard** — TypeScript, pushed 2026-07-25 — *Kubeflow Central Dashboard*
- **kubeflow/sdk** — Python, pushed 2026-07-25 — *Universal Python SDK to run AI workloads on Kubernetes*
- **bmorphism/Gay.jl** — Julia, ★2, pushed 2026-07-25 — *Wide-gamut color sampling with splittable determinism (188 open issues)*
- **plurigrid/eirobri** — Clojure, pushed 2026-07-21 — *EiRoBri replay world*
- **zubyul/from-possible-worlds** — TeX, pushed 2026-07-18
- **wasita/wasita.github.io** — Svelte, pushed 2026-07-21

### Top Starred Repos in Sweep

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,793 | — |
| kubeflow/pipelines | 4,170 | Python |
| kubeflow/spark-operator | 3,143 | Python |
| kubeflow/trainer | 2,153 | Go |
| kubeflow/katib | 1,692 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/arena | 815 | Go |
| kubeflow/mpi-operator | 530 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| plurigrid/asi | 31 | HTML |
| plurigrid/ontology | 8 | JavaScript |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A–Z) queried against Aptos Mainnet fullnode.  
**Result: All balances 0.00000000 APT** — accounts either unfunded or CoinStore resource not yet initialized on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...cf32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...76e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...ef9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...cc7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...e197c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts responded successfully. All require **2 signatures** — healthy 2-of-N configuration.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the Next.js SPA shell HTML. No public REST endpoints expose structured market data. Market data is loaded client-side via private API calls not accessible without browser execution.

---

## DuckDB State

```
Table            | Rows
-----------------|------
repo_snapshots   | 1,255
aptos_snapshots  |    28
multisig_probes  |     5
world_increments |    25
mnx_snapshots    |     0 (SPA — no data available)
```

**DB path:** `packages/world-increment/ducklake/world-increments.duckdb`
