# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-08-01T06:15Z  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## Job 1 — GitHub Social Graph Sweep

### Sources swept (11 increments this run)

| # | GF3 | Source | Type | Repos captured |
|---|-----|--------|------|---------------|
| 1 | PLUS #b8bb26 | plurigrid | org | 11 |
| 2 | MINUS #cc241d | kubeflow | org | 10 |
| 3 | ERGODIC #d3869b | TeglonLabs | org | 5 |
| 4 | PLUS #b8bb26 | bmorphism | user | 8 |
| 5 | MINUS #cc241d | zubyul | user | 7 |
| 6 | ERGODIC #d3869b | migalkin | social_graph | 5 |
| 7 | PLUS #b8bb26 | DJedamski | social_graph | 2 |
| 8 | MINUS #cc241d | wasita | social_graph | 4 |
| 9 | ERGODIC #d3869b | kristinezheng | social_graph | 2 |
| 10 | PLUS #b8bb26 | M1shaaa | social_graph | 2 |
| 11 | MINUS #cc241d | AustinCStone | social_graph | 3 |

### Notable repos by stars

| Repo | Stars | Lang | Last pushed |
|------|-------|------|------------|
| kubeflow/kubeflow | 15,802 | — | 2026-07-10 |
| kubeflow/pipelines | 4,172 | Python | 2026-08-01 |
| kubeflow/spark-operator | 3,141 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| kubeflow/katib | 1,695 | Python | 2026-07-26 |
| kubeflow/examples | 1,461 | Jsonnet | 2025-04-14 |
| kubeflow/arena | 816 | Go | 2026-07-29 |
| kubeflow/mpi-operator | 530 | Go | 2026-07-28 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| plurigrid/asi | 57 | HTML | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

### Active today (pushed 2026-08-01)

- `plurigrid/gorj` — forj Rama topology nREPL routing (1552 open issues!)
- `kubeflow/pipelines` — ML Pipelines for Kubeflow
- `bmorphism/Gay.jl` — Wide-gamut color sampling (188 open issues!)

### Social graph summary

| User | Focus | Most active repo |
|------|-------|-----------------|
| migalkin | Knowledge graphs, graph ML | NodePiece (144★), StarE (89★) |
| DJedamski | Data science / kaggle | kaggle_ncaa18 |
| wasita | Svelte/personal sites | wasita.github.io (active Jul 2026) |
| kristinezheng | MIT neurosci / web | personal site (active Jul 2026) |
| M1shaaa | Yale / lookit studies | lab-bookshelf- |
| AustinCStone | Python ML tools | byteruckus (active Jul 2026) |

---

## Job 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Timestamp:** 2026-08-01T06:15Z  
**Network:** Mainnet (`fullnode.mainnet.aptoslabs.com`)  
**Result:** All 28 wallets (alice, bob, A–Z) show **0 APT** at time of sweep.

| World | Address (truncated) | APT Balance |
|-------|-------------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A–Z | (26 addresses) | 0.00000000 each |

> Zero balance may indicate accounts are registered without a funded CoinStore, or the CoinStore resource is not yet initialized.

### Multisig Contract Probes

**All 5 probed multisig accounts are HEALTHY** — 2-of-N threshold confirmed on each.

| Pair | Address (truncated) | Sigs Required | Status |
|------|-------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API endpoint.**  
`testnet.mnx.fi` serves a Next.js SPA. Probed `/api/markets` and `/api/v1/markets` — both return HTML shell. No machine-readable market data extractable without a headless browser. Recorded as unavailable.

---

## DuckDB Ducklake Totals

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 34 |
| repo_snapshots | 1003 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, unavailable) |
