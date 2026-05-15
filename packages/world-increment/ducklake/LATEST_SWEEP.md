# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

**Date:** 2026-05-15  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) · `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Org / User | Type | Repos | Stars | Latest Push |
|---|---|---|---|---|
| kubeflow | Org | 48 | 34,057 | 2026-05-15 |
| migalkin | User (zubyul social graph) | 19 | 279 | 2026-05-07 |
| bmorphism | User | 100 | 246 | 2026-05-15 |
| AustinCStone | User (zubyul social graph) | 29 | 107 | 2026-04-01 |
| plurigrid | Org | 100 | 74 | 2026-05-15 |
| zubyul | User | 49 | 14 | 2026-04-24 |
| wasita | User (zubyul social graph) | 11 | 4 | 2026-05-14 |
| DJedamski | User (zubyul social graph) | 6 | 3 | 2023-04-21 |
| TeglonLabs | Org | 4 | 2 | 2026-01-01 |
| kristinezheng | User (zubyul social graph) | 6 | 0 | 2026-05-14 |
| M1shaaa | User (zubyul social graph) | 8 | 0 | 2026-02-04 |
| **TOTAL** | | **380** | **34,786** | |

### Top 10 Repos by Stars

| Repo | Stars | Forks | Open Issues | Language | Latest Push |
|---|---|---|---|---|---|
| kubeflow/kubeflow | 15,632 | 2,648 | 2 | — | 2026-05-07 |
| kubeflow/pipelines | 4,140 | 1,992 | 467 | Python | 2026-05-15 |
| kubeflow/spark-operator | 3,125 | 1,482 | 93 | Python | 2026-05-15 |
| kubeflow/trainer | 2,098 | 949 | 103 | Go | 2026-05-15 |
| kubeflow/katib | 1,682 | 522 | 124 | Python | 2026-05-09 |
| kubeflow/examples | 1,463 | 757 | 111 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,017 | 1,064 | 29 | YAML | 2026-05-13 |
| kubeflow/arena | 810 | 190 | 57 | Go | 2026-05-07 |
| kubeflow/kale | 687 | 156 | 57 | Python | 2026-05-15 |
| kubeflow/mpi-operator | 526 | 235 | 100 | Go | 2026-05-12 |

### Notable Signal

- **plurigrid/gorj** — 207 open issues, pushed 2026-05-15 (this repo)
- **bmorphism/Gay.jl** — 188 open issues; Wide-gamut GF(3) color sampling, pushed 2026-05-15
- **bmorphism/anti-bullshit-mcp-server** — 23 stars; top bmorphism star
- **migalkin/NodePiece** — 144 stars; compositional KG representations (ICLR'22)
- **kubeflow/mcp-apache-spark-history-server** — 170 stars; Spark history via MCP
- **bmorphism/ocaml-mcp-sdk** — 61 stars; OCaml SDK for MCP with Jane Street oxcaml_effect
- **zubyul/plurigrid-site** — 11 open issues; actively developed world site

### GF(3) Trit Color Chain

| Trit | Name | Color | Count |
|---|---|---|---|
| +1 | PLUS | `#b8bb26` | 127 |
| −1 | MINUS | `#cc241d` | 127 |
| 0 | ERGODIC | `#d3869b` | 126 |

**Total world_increments:** 380 (IDs 1–380, GF3 assignment: `id%3==1→PLUS, id%3==2→MINUS, id%3==0→ERGODIC`)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

Queried 2026-05-15 via `fullnode.mainnet.aptoslabs.com`.  
All 28 addresses return **0.00000000 APT** — `CoinStore<AptosCoin>` resource not registered on these addresses (accounts uninitialized or using alternate resource paths).

| World | Address | APT |
|---|---|---|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required` — **all healthy, 2-of-N**.

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | 0x0da4…003 | 2 | ✓ healthy |
| A-G | 0xf56c…096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…883 | 2 | ✓ healthy |
| S-T | 0x3b1c…883 | 2 | ✓ healthy |
| V-W | 0x40fa…b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable via API.** `https://testnet.mnx.fi` returns a Next.js SPA shell. Common API paths (`/api/markets`, `/api/v1/markets`) returned the same SPA HTML with no embedded market data. `mnx_snapshots` table created but empty.

---

## DuckDB Schema Summary

```
world-increments.duckdb
├── world_increments   380 rows  — GF(3) trit-colored increment log
├── repo_snapshots     380 rows  — GitHub repo metadata per increment
├── aptos_snapshots     28 rows  — Hamming swarm APT balances
├── multisig_probes      5 rows  — Aptos multisig contract health
└── mnx_snapshots        0 rows  — MNX market data (SPA, unavailable)
```

## GF(3) Assignment Rule

```
id mod 3 == 0  →  trit=0,   color=#d3869b,  name=ERGODIC
id mod 3 == 1  →  trit=1,   color=#b8bb26,  name=PLUS
id mod 3 == 2  →  trit=-1,  color=#cc241d,  name=MINUS
```
