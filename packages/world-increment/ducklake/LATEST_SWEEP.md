# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-11  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 11 |
| zubyul | user | 7 |
| migalkin | social (zubyul graph) | 4 |
| DJedamski | social (zubyul graph) | 2 |
| wasita | social (zubyul graph) | 3 |
| kristinezheng | social (zubyul graph) | 2 |
| M1shaaa | social (zubyul graph) | 2 |
| AustinCStone | social (zubyul graph) | 4 |
| **TOTAL** | | **188 unique repos** |

### GF(3) Color Chain Distribution

| trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 63 |
| 1 | `#b8bb26` | PLUS | 63 |
| 2 | `#cc241d` | MINUS | 62 |

### Top Languages

| Language | Repos |
|----------|-------|
| Python | 36 |
| TypeScript | 17 |
| Go | 14 |
| Rust | 13 |
| Clojure | 10 |
| Julia | 8 |
| JavaScript | 7 |
| Zig | 5 |

### Notable Recent Activity

- `plurigrid/nanoclj-zig` — NaN-boxed Clojure interpreter in Zig 0.15, GF(3) trit conservation (pushed 2026-04-25)
- `plurigrid/zig-syrup` — OCapN Syrup with CapTP optimizations (pushed 2026-04-30)
- `bmorphism/Gay.jl` — Wide-gamut color sampling + LispSyntax (pushed 2026-06-10, 189 open issues)
- `bmorphism/satreadout` — Machine-checked saturating perceptual readout in Lean 4.28 (pushed 2026-06-10)
- `bmorphism/nanoclj-zig` — NaN-boxed Clojure in Zig (pushed 2026-06-10)
- `kubeflow/pipelines` — ML Pipelines for Kubeflow, 4153★ (pushed 2026-06-10)
- `kubeflow/trainer` — Distributed AI Training on Kubernetes, 2112★ (pushed 2026-06-10)
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- `zubyul/ghostel-emacs-worlds` — Ghostty config + alice/bob emacs-mods (pushed 2026-04-24)
- `wasita/wasita.github.io` — personal website, Svelte+Tailwind (pushed 2026-06-01)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 wallets (alice, bob, A-Z) returned **0.0 APT** — `CoinStore` resource not registered or zero balance on mainnet. Consistent with fresh-generated wallet addresses not yet funded.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A–Z (26) | 0x8699edc...–0x7af0ef6... | 0.0 each |

### Multisig Contract Probes (5/5 healthy)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`. All live, all require **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel deployment protection authentication. Both `/api/markets` and `/api/v1/markets` return auth-gate HTML. No `mnx_snapshots` rows inserted.

---

## DuckDB Schema Summary

```
world_increments  : 188 rows  (GF3 color chain over all repo events)
repo_snapshots    : 188 rows  (org, language, stars, forks, pushed_at)
aptos_snapshots   :  28 rows  (world label, address, balance_apt)
multisig_probes   :   5 rows  (pair, address, sigs_required, healthy)
mnx_snapshots     :   0 rows  (unavailable — auth required)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-11*
