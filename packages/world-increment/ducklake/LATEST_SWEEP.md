# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-07-12  
**DB:** `world-increments.duckdb`  
**GF(3) Color Chain:** ERGODIC `#d3869b` (id%3=0) · PLUS `#b8bb26` (id%3=1) · MINUS `#cc241d` (id%3=2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 17 (key repos) |
| zubyul | user | 5 (key repos) |
| migalkin | social graph | 5 (key repos) |
| wasita | social graph | 3 (key repos) |
| DJedamski | social graph | 2 (key repos) |
| M1shaaa | social graph | 2 (key repos) |
| AustinCStone | social graph | 3 (key repos) |
| kristinezheng | social graph | 2 (key repos) |
| **Total** | | **193** |

### Top Repos by Stars
| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,770 | 2026-07 |
| kubeflow/pipelines | Python | 4,169 | 2026-07 |
| kubeflow/spark-operator | Python | 3,137 | 2026-07 |
| kubeflow/trainer | Go | 2,136 | 2026-07 |
| kubeflow/katib | Python | 1,690 | 2026-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03 |
| migalkin/NodePiece | Python | 144 | 2026-05 |
| migalkin/StarE | Python | 89 | 2026-04 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2025-05 |

### Recent Activity Highlights (plurigrid org)
- **plurigrid/asi** (HTML, ⭐30) — pushed 2026-07-10
- **plurigrid/gorj** (Clojure, ⭐1) — pushed 2026-07-12 *(this repo)*
- **plurigrid/place** (TeX, ⭐1) — pushed 2026-07-07

### bmorphism Recent
- **satreadout** (HTML) — Machine-checked saturating non-Riemannian perceptual readout (2026-06-20)
- **Gay.jl** (Julia, 187 open issues) — Wide-gamut color sampling, splittable determinism (2026-06-20)
- **penrose-mcp** (JS, ⭐9) — Penrose server for Infinity-Topos (2026-06-24)

### zubyul Recent
- **voice-observatory** (Python) — Passive macOS TUI, say-mcp-server companion (2026-04-24)
- **nash-tui** (Rust, private) — NASH token TUI via GeckoTerminal (2026-04-13)
- **tilelang-kernels** (Python) — GPU kernels for GF(3) trit classification (2026-03-16)

### TeglonLabs Recent
- **jank-crane** (C++) — crane-jank converged-IR hub, GF3 convergence maps (2026-06-08)

### GF(3) Distribution over 193 increments
- ERGODIC `#d3869b` (trit=0): **64** increments
- PLUS `#b8bb26` (trit=1): **65** increments
- MINUS `#cc241d` (trit=-1): **64** increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned **`resource_not_found`** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~623,728,058. These accounts exist on-chain but hold no APT in the legacy CoinStore resource (may use FungibleAsset store or have zero balance).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contracts (5 probed)

All 5 multisig contracts are **healthy** and require **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi requires Vercel authentication (returns 401 "Authentication Required" for all endpoints including `/`, `/api`, `/api/markets`). No market data could be extracted.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 193 |
| repo_snapshots | 193 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth blocked) |

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
