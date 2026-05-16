# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-16T21:15:00Z  
**Branch:** world-increment/sweep-2026-05-16  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Snapshotted | GF(3) | Color |
|--------|------|-------------------|-------|-------|
| plurigrid | org | 214 | PLUS (+1) | #b8bb26 |
| kubeflow | org | 106 | MINUS (-1) | #cc241d |
| TeglonLabs | org | 110 | ERGODIC (0) | #d3869b |
| bmorphism | user | 207 | PLUS (+1) | #b8bb26 |
| zubyul | user | 56 | MINUS (-1) | #cc241d |
| migalkin | social graph | 65 | ERGODIC (0) | #d3869b |
| DJedamski | social graph | 22 | PLUS (+1) | #b8bb26 |
| wasita | social graph | 60 | MINUS (-1) | #cc241d |
| kristinezheng | social graph | 36 | ERGODIC (0) | #d3869b |
| M1shaaa | social graph | 32 | PLUS (+1) | #b8bb26 |
| AustinCStone | social graph | 86 | MINUS (-1) | #cc241d |

**Total repo snapshots in ducklake:** 994

### Top Repos by Stars (This Sweep)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,636 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,139 | 2026-05-15 |
| kubeflow/spark-operator | Python | 3,125 | 2026-05-15 |
| kubeflow/trainer | Go | 2,098 | 2026-05-15 |
| kubeflow/katib | Python | 1,682 | 2026-05-09 |
| kubeflow/manifests | YAML | 1,017 | 2026-05-16 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| plurigrid/asi | HTML | 23 | 2026-04-26 |

### Notable Activity (plurigrid ecosystem, past 30 days)

- **plurigrid/gorj** (Clojure) — forj + Rama topology nREPL routing + GF(3) gay trit coloring; 217 open issues
- **plurigrid/zig-syrup** (Zig) — High-performance OCapN Syrup with CapTP optimizations; pushed 2026-04-30
- **plurigrid/nanoclj-zig** (Zig) — NaN-boxed Clojure interpreter in Zig 0.15; 20 open issues
- **bmorphism/Gay.jl** (Julia) — Wide-gamut SPI color sampling; 188 open issues, pushed today
- **bmorphism/oxgame** (OCaml) — Stellar resolution + open-game composition; pushed 2026-05-15
- **zubyul/voice-observatory** (Python) — Passive macOS TUI; pushed 2026-04-24

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming-swarm wallets (alice, bob, A–Z) queried against Aptos mainnet `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | empty / no CoinStore registered |
| bob | 0.0 | empty / no CoinStore registered |
| A–Z (26 wallets) | 0.0 each | empty / no CoinStore registered |

**Note:** All wallets returned 0 APT. Addresses appear not to have registered APT CoinStore on-chain, or balances are genuinely zero. The Aptos fullnode API at `fullnode.mainnet.aptoslabs.com` responded successfully for all 28 addresses.

### Multisig Contract Probes

POST `0x1::multisig_account::num_signatures_required` to Aptos mainnet:

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✅ |
| A-G | 0xf56c4a1c...0096 | 2 | ✅ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✅ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✅ |
| V-W | 0x40fad7b4...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy.** All require 2-of-N signatures (threshold = 2).

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no REST API available.**  
The site is a Next.js/Vercel SPA. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, etc.) return HTML. The CSP header reveals the backend at `api.testnet.mnx.fi`, but that endpoint returns Express "Cannot GET" errors for all probed paths. Market data is rendered client-side and requires a browser runtime. No rows inserted into `mnx_snapshots`.

---

## DuckDB Schema Summary

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 31 | GF(3) color-tagged event ledger |
| `repo_snapshots` | 994 | GitHub repo metadata across all sources |
| `aptos_snapshots` | 28 | Hamming-swarm wallet balances (alice, bob, A–Z) |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 0 | MNX market data (SPA — unavailable) |

## GF(3) Color Chain

- **id % 3 == 0** → trit=0 ERGODIC `#d3869b` (pink/rose)
- **id % 3 == 1** → trit=+1 PLUS `#b8bb26` (yellow-green)
- **id % 3 == 2** → trit=-1 MINUS `#cc241d` (red)
