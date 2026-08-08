# World-Increment Sweep — 2026-08-08

## Sweep Metadata
- **Date:** 2026-08-08 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger Version at sweep:** 6672554709 (epoch 16838)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total Repo Snapshots (this sweep) | 334 |
| Sources Covered | 3 orgs + 2 users + 6 social graph |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (404) |

---

## Job 1: GitHub Social Graph Sweep

### GF(3) Increment Chain

| # | Source | Type | GF3 Trit | Color | Repos |
|---|--------|------|----------|-------|-------|
| 1 | plurigrid | org | 1 PLUS | #b8bb26 | 100 |
| 2 | kubeflow | org | -1 MINUS | #cc241d | 49 |
| 3 | TeglonLabs | org | 0 ERGODIC | #d3869b | 5 |
| 4 | bmorphism | user | 1 PLUS | #b8bb26 | 100 |
| 5 | zubyul | user | -1 MINUS | #cc241d | 49 |
| 6 | migalkin | social | 0 ERGODIC | #d3869b | 19 |
| 7 | DJedamski | social | 1 PLUS | #b8bb26 | 6 |
| 8 | wasita | social | -1 MINUS | #cc241d | 14 |
| 9 | kristinezheng | social | 0 ERGODIC | #d3869b | 5 |
| 10 | M1shaaa | social | 1 PLUS | #b8bb26 | 8 |
| 11 | AustinCStone | social | -1 MINUS | #cc241d | 41 |

### Org Highlights

**plurigrid** (100 repos, latest push: 2026-08-08)
- Top starred: `plurigrid/asi` (59★, "everything is topological chemputer!")
- Most active: `plurigrid/gorj` (1728 open issues — this repo!), `plurigrid/place`
- Notable new: `plurigrid/zig-syrup` (Zig OCapN Syrup), `plurigrid/nanoclj-zig`, `plurigrid/nash-portal` (WASM TUI)
- Languages: Clojure, Rust, Zig, TypeScript, Python, Julia, Scheme, Go, Swift

**kubeflow** (49 repos, latest push: 2026-08-08)
- Top starred: `kubeflow/kubeflow` (15,806★), `kubeflow/pipelines` (4,182★), `kubeflow/spark-operator` (3,145★)
- Most active: `kubeflow/trainer` (Go, 2176★ — distributed AI training on K8s), `kubeflow/katib` (1694★ — AutoML)
- Notable: `kubeflow/mcp-apache-spark-history-server` (188★), `kubeflow/mcp-server` (31★)
- CNCF ML Toolkit — busy as of 2026-08-08

**TeglonLabs** (5 repos)
- `jank-crane` (C++, "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps")
- `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, 2 forks), `monad-mcp-server`, `topoi` (Python)

### User Highlights

**bmorphism** (100 repos, latest push: 2026-08-07)
- `Gay.jl` (Julia, 2★, 188 open issues — core GF3 color library)
- `ocaml-mcp-sdk` (OCaml, 61★ — Jane Street oxcaml_effect MCP SDK)
- `anti-bullshit-mcp-server` (JS, 23★), `manifold-mcp-server` (JS, 14★)
- Focus: MCP servers, OCaml/Zig/Clojure, open games, Gay.jl ecosystem

**zubyul** (49 repos, latest push: 2026-04-24)
- `voice-observatory`, `ghostel-emacs-worlds`, `nash-tui` (Rust NASH TUI)
- `Gay.jl` fork, `tilelang-kernels` (GPU kernels for GF3), `gay-terminal-colors`
- Focus: plurigrid ecosystem, BCI/OpenBCI, Gay.jl tooling

### Social Graph

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 19 | `NodePiece` (144★ ICLR'22 KG), `StarE` (89★ EMNLP), `NBFNet_mlx` (10★) |
| wasita | 14 | Latest: `wm-cv` (2026-08-07), `xoxowasita-analysis` (2026-08-06) |
| DJedamski | 6 | Data science / Kaggle repos (older, inactive) |
| kristinezheng | 5 | MIT neuroscience / Lookit studies |
| M1shaaa | 8 | Yale/Lookit child cognition lab work |
| AustinCStone | 41 | `TextGAN` (92★), `StereoVisionMRF` (11★), `byteruckus` (2026-07-15) |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Result: **resource_not_found** for all — CoinStore not initialized on any address.
This indicates all Hamming swarm wallets hold 0 APT (accounts exist but no coin resource).

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Total swarm APT: 0.0** — all accounts uninitialized or empty.

### Multisig Contract Probes

All 5 multisig accounts successfully probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7... | 2 | ✓ HEALTHY |

**All multisig contracts healthy (2-of-N threshold confirmed on all 5 pairs).**

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **HTTP 404 Not Found**
MNX testnet market API unavailable. No market data captured this sweep.

---

## DuckDB Schema Status

```
world_increments   — 34 rows total (11 new this sweep)
repo_snapshots     — cumulative across all sweeps
aptos_snapshots    — 28 new rows (all 0.0 APT)
multisig_probes    — 5 new rows (all healthy)
mnx_snapshots      — 0 rows (API unavailable)
```

---

## Key Signals

1. **plurigrid/gorj** has 1728 open issues — active development on this codebase.
2. **kubeflow** is very active across ML infra (trainer, spark-operator, pipelines).
3. **bmorphism** is iterating heavily on Gay.jl, MCP servers, and OCaml tooling.
4. **All Hamming swarm wallets at 0 APT** — CoinStore not initialized; no on-chain funds detected.
5. **All 5 multisig pairs healthy** with 2-sig threshold — governance infrastructure intact.
6. **wasita** pushed `xoxowasita-analysis` and `joint-planning-lit` on 2026-08-06/07 — very recent activity.
