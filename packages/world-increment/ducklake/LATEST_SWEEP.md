# World Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-07-05  
**GF(3) Chain:** ERGODIC(trit=0,#d3869b) → PLUS(trit=1,#b8bb26) → MINUS(trit=-1,#cc241d) → repeat

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **Unique repos indexed:** 645
- **World increment entries:** 34
- **Sources covered:** plurigrid, kubeflow, TeglonLabs (orgs); bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone (users)

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | user | 19 |
| AustinCStone | user | 40 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |

### Top Repos by Stars

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | ★15762 |
| kubeflow/pipelines | Python | ★4169 |
| kubeflow/spark-operator | Python | ★3132 |
| kubeflow/trainer | Go | ★2129 |
| kubeflow/katib | Python | ★1689 |
| kubeflow/examples | Jsonnet | ★1460 |
| kubeflow/community-distribution | YAML | ★1028 |
| kubeflow/manifests | YAML | ★1010 |
| migalkin/NodePiece | Python | ★144 |
| AustinCStone/TextGAN | Python | ★92 |
| migalkin/StarE | Python | ★89 |
| migalkin/kgcourse2021 | HTML | ★25 |
| TeglonLabs/mathpix-gem | Ruby | ★2 |

### Notable Social Graph Signals

- **migalkin**: KG/GNN researcher — NodePiece (★144), StarE (★89), NBFNet MLX impl (★10), RWL (★8)
- **AustinCStone**: TextGAN (★92), bmfork/bmforkupdate repos suggest active bitmind subnet work (2025-05)
- **wasita**: Active Svelte/web dev — wasita.github.io last pushed **2026-07-05T03:54** (today)
- **kristinezheng**: MIT cognitive science researcher — Lookit studies, last push 2026-07-01
- **TeglonLabs/jank-crane**: `crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow` — C++, last push 2026-06-08
- **TeglonLabs/coin-flip-mcp**: Random.org coin flip MCP server, 2 forks

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acdec1… | 0.0 APT |
| bob | 0x0a3c00c58f… | 0.0 APT |
| A | 0x8699edc096… | 0.0 APT |
| B | 0x3f892ebe6e… | 0.0 APT |
| C | 0x38b99e63ad… | 0.0 APT |
| D | 0xf77656248f… | 0.0 APT |
| E | 0xdc1d9d533b… | 0.0 APT |
| F | 0x18a14b5b4b… | 0.0 APT |
| G | 0x69a394c0b0… | 0.0 APT |
| H | 0xce67c327a7… | 0.0 APT |
| I | 0x070fe5d74e… | 0.0 APT |
| J | 0x4d964db8f5… | 0.0 APT |
| K | 0xa732040a6b… | 0.0 APT |
| L | 0x7c2eaeafad… | 0.0 APT |
| M | 0x6fed37a755… | 0.0 APT |
| N | 0xe7dde6da0a… | 0.0 APT |
| O | 0x73252b6011… | 0.0 APT |
| P | 0x6218792de4… | 0.0 APT |
| Q | 0xac40fa50b8… | 0.0 APT |
| R | 0x7ce605cc8f… | 0.0 APT |
| S | 0xb8753014e4… | 0.0 APT |
| T | 0x35781dc0e4… | 0.0 APT |
| U | 0x75860da475… | 0.0 APT |
| V | 0xb59dd81703… | 0.0 APT |
| W | 0x5f32aef70f… | 0.0 APT |
| X | 0xa95cbbd116… | 0.0 APT |
| Y | 0xd8e32848f1… | 0.0 APT |
| Z | 0x7af0ef6e1b… | 0.0 APT |

**Note:** All 28 addresses returned 0.0 APT. Accounts either have no CoinStore<AptosCoin> resource initialized or hold zero balance on Aptos mainnet.

### Multisig Contract Probes (5 pairs)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0… | 2-of-N | healthy |
| A-G | 0xf56c4a1c09… | 2-of-N | healthy |
| Y-Z | 0xd3ffe1812b… | 2-of-N | healthy |
| S-T | 0x3b1c3ae905… | 2-of-N | healthy |
| V-W | 0x40fad7b423… | 2-of-N | healthy |

All 5 multisig contracts respond correctly, all configured as 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

Status: HTTP 401 — Vercel deployment protection active (password required). Market data unavailable this run.

---

## DuckDB Schema

File: packages/world-increment/ducklake/world-increments.duckdb

Tables:
  world_increments  — 34 rows — GF(3) color-chained event log
  repo_snapshots    — 1266 rows — per-repo GitHub metadata
  aptos_snapshots   — 28 rows — Aptos wallet balances (alice,bob,A-Z)
  multisig_probes   — 5 rows — on-chain multisig threshold config
  mnx_snapshots     — 0 rows — MNX market data (unavailable this run)
