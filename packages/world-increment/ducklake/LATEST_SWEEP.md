# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-06-12T09:10 UTC  
**Branch:** world-increment/sweep-2026-06-12-0910  
**DuckDB version:** v1.5.3 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Indexed | Total Stars | Top Repo |
|--------|------|---------------|-------------|----------|
| kubeflow | org | 142 | 101,917 | kubeflow/kubeflow ★15,714 |
| migalkin | user (zubyul social) | 60 | 554 | NodePiece ★143 |
| bmorphism | user | 300 | 509 | ocaml-mcp-sdk ★61 |
| AustinCStone | user (zubyul social) | 126 | 324 | TextGAN ★92 |
| plurigrid | org | 300 | 156 | asi ★25 |
| zubyul | user | 97 | 40 | Nikolova_lab_data_analysis ★2 |
| TeglonLabs | org | 106 | 12 | vibespace/mathpix-gem ★2 |
| DJedamski | user (zubyul social) | 22 | 14 | kaggle-titanic ★2 |
| wasita | user (zubyul social) | 71 | 11 | magic-garden ★2 |
| kristinezheng | user (zubyul social) | 36 | 0 | kristinezheng.github.io ★0 |
| M1shaaa | user (zubyul social) | 32 | 0 | OWLET ★0 |
| **TOTAL** | | **1,292** | **103,537** | |

### GF(3) Color Chain — World Increments (29 events)

| trit | name | color | meaning |
|------|------|-------|---------|
| 0 | ERGODIC | `#d3869b` | id % 3 == 0 |
| 1 | PLUS | `#b8bb26` | id % 3 == 1 |
| 2 | MINUS | `#cc241d` | id % 3 == 2 |

GF(3) chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → …` (29 total events)

### Top Repos by Source
| Source | Repo | Stars | Language | Last Push |
|--------|------|-------|----------|-----------|
| kubeflow | kubeflow/kubeflow | 15,714 | — | 2026-06-11 |
| kubeflow | kubeflow/pipelines | 4,152 | Python | 2026-06 |
| kubeflow | kubeflow/spark-operator | 3,127 | Go | 2026-06 |
| migalkin | NodePiece | 143 | Python | 2022-02 |
| AustinCStone | TextGAN | 92 | Python | 2016-10 |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml | 2026-03 |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript | — |
| plurigrid | asi | 25 | HTML | 2026-06-10 |
| wasita | magic-garden | 2 | Python | 2026-01 |
| TeglonLabs | jank-crane | 0 | C++ | 2026-06-08 |
| TeglonLabs | mathpix-gem | 2 | Ruby | 2026-01 |
| M1shaaa | OWLET | 0 | Python | 2025-06 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-12)
All 28 addresses (alice, bob, A–Z) queried via  
`GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All addresses returned `resource_not_found` — accounts exist on-chain but have no registered APT CoinStore (0.0 APT).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…512d | 0.0 |
| A–Z (26 addrs) | 0x8699…→ 0x7af0… | 0.0 each |

### Multisig Contract Probes (5 contracts)
Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

**All 5 multisigs healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)
**Status: Unavailable** — both root URL and `/api/markets` endpoint returned HTTP 401 Unauthorized.  
The testnet SPA requires authentication. No market data extracted; recorded as `MNX_UNAVAILABLE` in mnx_snapshots.

---

## DuckDB Tables Summary

```
Table              Rows
─────────────────────────────────
world_increments    29    (GF3 color chain events)
repo_snapshots    1292    (11 sources, includes pagination)
aptos_snapshots     28    (all wallets, all 0.0 APT)
multisig_probes      5    (all healthy, sigs_required=2)
mnx_snapshots        1    (unavailable marker)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=2, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,714 stars — ML Toolkit for Kubernetes (pushed 2026-06-11, actively developed)
- **kubeflow/pipelines**: 4,152 stars — most active ML pipeline framework for K8s
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embedding via entity anchors
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's effect system
- **AustinCStone/TextGAN**: 92 stars — text generation with adversarial training
- **plurigrid/asi**: 25 stars — topological chemputer (pushed 2026-06-10, most recent plurigrid activity)
- **TeglonLabs/jank-crane**: C++ — crane-jank converged-IR hub with GF3 convergence maps (2026-06-08)
- **M1shaaa/M1shaaa**: profile repo pushed 2026-06-12 (today) — active social graph node
- **Hamming swarm**: All 28 wallets at 0 APT; all 5 multisigs healthy at 2-of-N
