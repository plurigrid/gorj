# World-Increment Sweep + Hamming Snapshot

**Run date:** 2026-08-02  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Job 1: GitHub Social Graph Sweep

### Sources Queried (This Run)
| Source | Type | Repos | Stars | Forks |
|--------|------|-------|-------|-------|
| plurigrid | org | 100 | 190 | 88 |
| kubeflow | org | 49 | 102,176 | 40,535 |
| TeglonLabs | org | 5 | 2 | 2 |
| bmorphism | user | 50 | 377 | 39 |
| zubyul | user | 49 | 40 | 4 |
| migalkin | social | 19 | 833 | 146 |
| AustinCStone | social | 20 | 323 | 112 |

**Total repo_snapshots in DB (cumulative):** 1,236 rows

### Top Repos by Stars (This Run)
| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,803 | 2,690 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,173 | 2,074 | 2026-08-01 |
| kubeflow/spark-operator | Python | 3,142 | 1,508 | 2026-07-31 |
| kubeflow/trainer | Go | 2,165 | 1,006 | 2026-07-31 |
| kubeflow/katib | Python | 1,694 | 534 | 2026-08-01 |
| kubeflow/examples | Jsonnet | 1,461 | 755 | 2025-04-14 |
| migalkin/* | various | 833 total | 146 | — |
| AustinCStone/* | various | 323 total | 112 | — |
| plurigrid/asi | HTML | 58 | 13 | 2026-07-10 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |

### Most Recently Pushed
**plurigrid:** gorj (2026-08-02), place (2026-08-01), zig-syrup (2026-07-28)  
**bmorphism:** Gay.jl (2026-08-02, active!), gay-chat (2026-07-14)  
**kubeflow:** katib (2026-08-01), docs-agent (2026-08-01), pipelines (2026-08-01)  
**zubyul:** voice-observatory (2026-04-24), ghostel-emacs-worlds (2026-04-24)  

### GF(3) Color Chain
| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-08-02)

All 28 wallets (alice, bob, A–Z) return **0.00 APT** on
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts exist
on-chain but hold no native APT in the legacy CoinStore resource
(possible FA migration or unfunded wallets).

### Multisig Contract Probes (5/5 Healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

All 5 multisig accounts healthy — 2-of-N signature threshold confirmed.

### MNX Markets (testnet.mnx.fi)

Next.js SPA — client-side only. API paths return HTML. No market data
extractable without JS execution. Status: unavailable via direct HTTP.

---

## DuckDB Table Summary

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 28+ |
| repo_snapshots | 1,236 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA) |

## GF(3) Assignment Rule

- id%3==0: trit=0, #d3869b, ERGODIC
- id%3==1: trit=+1, #b8bb26, PLUS
- id%3==2: trit=-1, #cc241d, MINUS
