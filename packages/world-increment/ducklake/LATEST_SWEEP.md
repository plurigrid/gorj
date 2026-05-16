# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-05-16 14:13:36 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=+1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources snapshotted

| # | GF(3) | Color | Source | Type | Repos captured |
|---|-------|-------|--------|------|----------------|
| 1 | +1 PLUS | #b8bb26 | plurigrid | org | 13 (sample of 100) |
| 2 | -1 MINUS | #cc241d | kubeflow | org | 11 (sample of 48) |
| 3 | 0 ERGODIC | #d3869b | TeglonLabs | org | 4 |
| 4 | +1 PLUS | #b8bb26 | bmorphism | user | 10 (sample of 102) |
| 5 | -1 MINUS | #cc241d | zubyul | user | 7 (sample of 49) |
| 6 | 0 ERGODIC | #d3869b | migalkin | user | 4 (sample of 19) |
| 7 | +1 PLUS | #b8bb26 | DJedamski | user | 2 (sample of 6) |
| 8 | -1 MINUS | #cc241d | wasita | user | 4 (sample of 11) |
| 9 | 0 ERGODIC | #d3869b | kristinezheng | user | 2 (sample of 6) |
| 10 | +1 PLUS | #b8bb26 | M1shaaa | user | 2 (sample of 8) |
| 11 | -1 MINUS | #cc241d | AustinCStone | user | 3 (sample of 40) |

**Total DB rows:** 11 world_increments · 62 repo_snapshots

### Top repos by source

**kubeflow** (48 total repos):
```
kubeflow/kubeflow       ★15634  Machine Learning Toolkit for Kubernetes
kubeflow/pipelines      ★4139   ML Pipelines (467 open issues)
kubeflow/spark-operator ★3125   Kubernetes operator for Apache Spark
kubeflow/trainer        ★2098   Distributed AI Model Training + LLM Fine-Tuning
kubeflow/katib          ★1682   Automated Machine Learning on Kubernetes
```

**plurigrid** (100 total repos):
```
plurigrid/vcg-auction   ★7    CosmWasm VCG auction contract
plurigrid/agent         ★5    Framework for agency amplification
plurigrid/StochFlow     ★4    Stochastic interpolant models
plurigrid/asi           ★23   topological chemputer
plurigrid/ontology      ★8    autopoietic ergodicity and embodied gradualism
```

**bmorphism** (102 total repos):
```
bmorphism/ocaml-mcp-sdk         ★61  OCaml SDK for Model Context Protocol (Jane Street oxcaml_effect)
bmorphism/anti-bullshit-mcp-server ★23  Claim analysis + fact checking MCP server
bmorphism/risc0-cosmwasm-example   ★23  CosmWasm + zkVM RISC-V EFI template
bmorphism/say-mcp-server           ★20  macOS TTS MCP server
bmorphism/babashka-mcp-server      ★18  Babashka/Clojure MCP server
```

**Notable recent activity:**
- `plurigrid/gorj`: this repo — Rama + GF(3) REPL orchestration (211 open issues)
- `plurigrid/asi`: ★23 topological chemputer, active May 2026
- `bmorphism/Gay.jl`: 188 open issues, active May 2026 (wide-gamut SPI color sampling)
- `bmorphism/oxgame`: new (May 15 2026) — Stellar resolution + open-game composition for OCaml/OxCaml
- `kubeflow/mcp-apache-spark-history-server`: ★170 MCP server for Spark (May 2026 active)
- `kubeflow/mcp-server`: brand new (Apr 2026) — AI-assisted dev with Kubeflow tools

**Zubyul social graph (zubyul's connections):**
- migalkin: KG researcher — NodePiece (★144), StarE (★89), NBFNet MLX (★10)
- wasita: computational neuroscience/Svelte dev — magic-garden bot (★2)
- kristinezheng: MIT neuroscience researcher — auditory illusion study
- M1shaaa: lab bookshelf TypeScript project
- DJedamski: data science / NCAA Kaggle
- AustinCStone: ML researcher — TextGAN (★92), StereoVisionMRF

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Ledger version at query time:** 5,296,590,736  
**Note:** All 28 addresses (alice, bob, A–Z) responded with HTTP 404 on the APT CoinStore resource. The accounts exist on-chain (sequence numbers confirmed for S=11, T=9, U=7, V=5, W=4, X=3, Y=2, Z=2) but hold no APT in the native coin store — likely using FA (Fungible Asset) balances or the accounts are unfunded.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac… | 0.0 (no CoinStore) |
| bob | 0x0a3c00… | 0.0 (no CoinStore) |
| A–Z | 0x8699ed…–0x7af0ef… | 0.0 each (no CoinStore) |

**Total swarm APT:** 0.0 APT across 28 addresses

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N threshold confirmed):

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✓ |
| A-G | 0xf56c4a… | 2 | ✓ |
| Y-Z | 0xd3ffe1… | 2 | ✓ |
| S-T | 0x3b1c3a… | 2 | ✓ |
| V-W | 0x40fad7… | 2 | ✓ |

All multisigs require exactly 2 signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API endpoints available**  
The site is a Next.js SPA. All probed API paths (`/api/markets`, `/api/v1/markets`, `/api/tokens`, `/api/v1/tokens`, `/api/pools`) returned HTML (the SPA shell) rather than JSON. Market data is rendered client-side and not accessible via server-side API without JS execution. Recorded as unavailable in mnx_snapshots.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments   (11 rows)  — GF(3) trit-colored source events
├── repo_snapshots     (62 rows)  — GitHub repo metadata snapshots
├── aptos_snapshots    (28 rows)  — Hamming swarm wallet balances
├── multisig_probes    (5 rows)   — Aptos multisig contract health
└── mnx_snapshots      (1 row)    — MNX market data (unavailable)
```

```sql
-- Query: top repos by stars across all sources
SELECT org_or_user, full_name, stars, language
FROM repo_snapshots
ORDER BY stars DESC
LIMIT 10;
```
