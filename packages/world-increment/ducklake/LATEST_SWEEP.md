# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 340 |
| Sources Covered | 3 orgs + 9 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (all healthy) |
| MNX Testnet | 401 Unauthorized (auth-gated) |

---

## JOB 1: GitHub Social Graph

### GF(3) Color Chain — All 12 Increments

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | gorj | sweep | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

### Top Repos by Source

#### plurigrid (100 repos) — latest push: 2026-07-14
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |

#### kubeflow (49 repos) — latest push: 2026-07-13
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| kubeflow | — | 15,777 | 2026-07-10 |
| pipelines | Python | 4,165 | 2026-07-13 |
| spark-operator | Python | 3,135 | 2026-07-13 |
| trainer | Go | 2,138 | 2026-07-13 |

#### TeglonLabs (5 repos) — latest push: 2026-06-08
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| jank-crane | C++ | 0 | 2026-06-08 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

#### bmorphism (100 repos) — latest push: 2026-07-14
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |

#### zubyul (49 repos) — latest push: 2026-04-24
_(see repo_snapshots table for full list)_

#### migalkin (19 repos) — Knowledge Graphs researcher
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |
| RWL | Python | 8 | 2026-05-28 |

#### DJedamski (6 repos) — Data science / stats
_(Kaggle, R projects, grad school work — last push 2023)_

#### wasita (11 repos) — Svelte/web developer
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| wasita.github.io | Svelte | 1 | 2026-07-06 |
| magic-garden | Python | 2 | 2026-04-22 |
| send2kobo | TypeScript | 1 | 2026-05-19 |

#### kristinezheng (5 repos) — Cognitive science / MIT
_(Lookit studies, auditory illusion — last active 2026-07-01)_

#### M1shaaa (8 repos) — Yale / Lookit researcher
_(Python, TypeScript, Lookit uploads — last active 2026-02-04)_

#### AustinCStone (40 repos) — ML/CV/systems
| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — Mainnet (28 wallets)

All 28 wallets (alice, bob, A–Z) returned **0.00 APT**. The CoinStore resource was absent for every address, indicating these accounts are not initialized on Aptos mainnet.

| Wallet | Status |
|--------|--------|
| alice | 0.000000 APT (not initialized) |
| bob | 0.000000 APT (not initialized) |
| A–Z (26 wallets) | 0.000000 APT each (not initialized) |

### Multisig Contract Probes — 5 contracts

All 5 multisig contracts are **healthy** and on-chain, requiring **2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Both `https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` returned HTTP 401 Unauthorized. The testnet requires authentication; no market data was retrievable in this sweep.

---

## Changes Since Last Sweep (2026-04-12)

| Metric | Previous | Current | Delta |
|--------|----------|---------|-------|
| plurigrid top star (asi) | 16★ | 30★ | **+14★** |
| TeglonLabs/jank-crane | not present | C++ GF3 IR hub | **new** |
| Multisig contracts | not probed | 5/5 healthy | — |
| Aptos wallet funding | not probed | 0 APT all | — |
| MNX testnet | not probed | 401 auth-gated | — |

---

_Generated by world-increment-sweep + hamming-swarm-snapshot agent on 2026-07-14_
