# World Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-19  
**Branch:** world-increment/sweep-2026-05-19  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Snapshotted

| # | GF3 | Color | Source | Type | Repos |
|---|-----|-------|--------|------|-------|
| 1 | PLUS #b8bb26 | plurigrid | org | 100 |
| 2 | MINUS #cc241d | kubeflow | org | 48 |
| 3 | ERGODIC #d3869b | TeglonLabs | org | 4 |
| 4 | PLUS #b8bb26 | bmorphism | user | 117 |
| 5 | MINUS #cc241d | zubyul | user | 50 |
| 6 | ERGODIC #d3869b | migalkin | user (zubyul graph) | 19 |
| 7 | PLUS #b8bb26 | wasita | user (zubyul graph) | 11 |
| 8 | MINUS #cc241d | AustinCStone | user (zubyul graph) | 40 |
| 9 | ERGODIC #d3869b | DJedamski | user (zubyul graph) | 6 |
| 10 | PLUS #b8bb26 | kristinezheng | user (zubyul graph) | 6 |
| 11 | MINUS #cc241d | M1shaaa | user (zubyul graph) | 8 |

**Total orgs/users swept:** 11  
**Total repos discovered:** 409 (141 representative stored in ducklake)

### Notable Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,647 | — | 2026-05-07 |
| kubeflow/pipelines | 4,140 | Python | 2026-05-18 |
| kubeflow/spark-operator | 3,126 | Python | 2026-05-19 |
| kubeflow/trainer | 2,100 | Go | 2026-05-18 |
| kubeflow/katib | 1,682 | Python | 2026-05-09 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |

### Most Active (pushed within 48h of sweep)

- `kubeflow/notebooks` — 2026-05-19T00:32:23Z
- `bmorphism/Gay.jl` — 2026-05-19T00:37:58Z (189 open issues!)
- `kubeflow/spark-operator` — 2026-05-19T00:16:25Z
- `plurigrid/gorj` — 2026-05-19T00:16:50Z (250 open issues)
- `wasita/wasita.github.io` — 2026-05-18T22:47:03Z

### Plurigrid Org Highlights (100 repos)

- Language spread: Clojure, Zig, Rust, Python, Julia, Haskell, Go, Scheme, Racket, TypeScript
- Most starred: `asi` (23), `ontology` (8), `vcg-auction` (7), `agent` (5), `StochFlow` (4)
- Most open issues: `gorj` (250), `ducklings` (15), `ontology` (16)
- Notable new: `zig-syrup` (OCapN Syrup in Zig), `nanoclj-zig` (NaN-boxed Clojure interpreter), `nash-portal` (NASH TUI in WASM)

### TeglonLabs Org (4 repos)

- `mathpix-gem` — Ruby gem for mathematical image → LaTeX, last pushed 2026-01-01
- `coin-flip-mcp` — MCP server using random.org (2 forks)
- `monad-mcp-server` — Monad MCP Server
- `topoi` — Python, 1 open issue

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Sweep time:** 2026-05-19  
All 28 wallets (alice, bob, A–Z) returned **0 APT**.  
Accounts have no initialized `CoinStore<AptosCoin>` resource — addresses are created but not funded on mainnet.

| World | Address (first 12 chars) | Balance (APT) |
|-------|--------------------------|---------------|
| alice | 0xc793acdec1… | 0.00000000 |
| bob   | 0x0a3c00c58f… | 0.00000000 |
| A–Z   | (26 addresses) | 0.00000000 |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig accounts are **healthy** with `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0… | 2 | HEALTHY |
| A-G | 0xf56c4a1c09… | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b… | 2 | HEALTHY |
| S-T | 0x3b1c3ae905… | 2 | HEALTHY |
| V-W | 0x40fad7b423… | 2 | HEALTHY |

All pairs use 2-of-2 multisig scheme — standard Hamming threshold for pairwise swarm coordination.

### MNX Markets (testnet.mnx.fi)

**Status:** SPA (Next.js) — no REST API endpoint exposed at `/api/markets` or `/api/v1/markets`.  
The site loads client-side JavaScript and requires browser execution for market data.  
Stored as `ticker=N/A, category=SPA-unavailable` in `mnx_snapshots`.

---

## DuckDB Ducklake Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 141 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

### GF(3) Chain for This Sweep

```
id=1  plurigrid     trit=+1  PLUS    #b8bb26
id=2  kubeflow      trit=-1  MINUS   #cc241d
id=3  TeglonLabs    trit=0   ERGODIC #d3869b
id=4  bmorphism     trit=+1  PLUS    #b8bb26
id=5  zubyul        trit=-1  MINUS   #cc241d
id=6  migalkin      trit=0   ERGODIC #d3869b
id=7  wasita        trit=+1  PLUS    #b8bb26
id=8  AustinCStone  trit=-1  MINUS   #cc241d
id=9  DJedamski     trit=0   ERGODIC #d3869b
id=10 kristinezheng trit=+1  PLUS    #b8bb26
id=11 M1shaaa       trit=-1  MINUS   #cc241d
```
