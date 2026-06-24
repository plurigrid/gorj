# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep Date:** 2026-06-24  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Chain:** trit=0 ERGODIC #d3869b | trit=1 PLUS #b8bb26 | trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |
| **TOTAL** | | **391** |

### Top Repos by Stars

| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15,742 | – | 2026-06-18 |
| kubeflow | pipelines | 4,157 | Python | 2026-06-23 |
| kubeflow | spark-operator | 3,128 | Python | 2026-06-24 |
| kubeflow | trainer | 2,119 | Go | 2026-06-24 |
| kubeflow | katib | 1,685 | Python | 2026-06-23 |
| kubeflow | arena | 813 | Go | 2025-05-07 |
| migalkin | NodePiece | 144 | Python | 2021-06-14 |
| AustinCStone | TextGAN | 92 | Python | 2016-09-19 |
| migalkin | StarE | 89 | Python | 2020-09-17 |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid | ontology | 8 | JavaScript | 2025-05-27 |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Most Active Recent Repos (plurigrid/bmorphism ecosystem)

- **gorj** (Clojure, 786 open issues) — forj + Rama topology nREPL routing + GF(3) — pushed 2026-06-24
- **Gay.jl** (bmorphism, Julia) — Wide-gamut color sampling with splittable determinism — pushed 2026-06-24
- **eirobri** (Clojure) — EiRoBri replay world — pushed 2026-06-23
- **place** (TeX) — pushed 2026-06-24
- **asi** (HTML, 26 stars) — everything is topological chemputer! — pushed 2026-06-10
- **kubeflow/mcp-server** (Python, 17 stars) — MCP Server for AI-Assisted Development with Kubeflow Tools — pushed 2026-06-24

### TeglonLabs Repos (5 total)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | – | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### GF(3) Increment Chain (id mod 3)

| id | Source | Trit | Color | Name |
|----|--------|------|-------|------|
| 1 | AustinCStone | +1 | #b8bb26 | PLUS |
| 2 | DJedamski | -1 | #cc241d | MINUS |
| 3 | M1shaaa | 0 | #d3869b | ERGODIC |
| 4 | TeglonLabs | +1 | #b8bb26 | PLUS |
| 5 | bmorphism | -1 | #cc241d | MINUS |
| 6 | kristinezheng | 0 | #d3869b | ERGODIC |
| 7 | kubeflow | +1 | #b8bb26 | PLUS |
| 8 | migalkin | -1 | #cc241d | MINUS |
| 9 | plurigrid | 0 | #d3869b | ERGODIC |
| 10 | wasita | +1 | #b8bb26 | PLUS |
| 11 | zubyul | -1 | #cc241d | MINUS |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

Queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s sleep between calls.

| World | APT Balance | Status |
|-------|-------------|--------|
| alice | 0.0 | unfunded |
| bob | 0.0 | unfunded |
| A–Z (26 wallets) | 0.0 each | unfunded |

**All 28 wallets returned 0 APT.** The `CoinStore<AptosCoin>` resource returned value=0 or was absent for all addresses — these appear to be unfunded/inactive accounts on Aptos mainnet.

### Multisig Contract Probes (5 Hamming pairs)

Probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | **2** | HEALTHY |
| A-G | 0xf56c4a1c... | **2** | HEALTHY |
| Y-Z | 0xd3ffe181... | **2** | HEALTHY |
| S-T | 0x3b1c3ae9... | **2** | HEALTHY |
| V-W | 0x40fad7b4... | **2** | HEALTHY |

All 5 multisig contracts require exactly **2-of-N signatures** and are live on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Protected by Vercel deployment authentication. API paths `/api/markets`, `/api/v1/markets`, `/api/tickers` all return auth challenge. No market data extractable without bypass token or Vercel CLI. No rows inserted to `mnx_snapshots`.

---

## DuckDB Table Summary

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 34 | GF(3)-colored source events |
| repo_snapshots | 1,268 | GitHub repo metadata |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | Multisig contract sig counts |
| mnx_snapshots | 0 | MNX markets (unavailable) |

**DuckDB file:** `packages/world-increment/ducklake/world-increments.duckdb`
