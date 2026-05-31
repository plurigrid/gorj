# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-05-31T00:22 UTC  
**Branch:** `world-increment/sweep-2026-05-31-0022`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | GF(3) Color | Trit |
|--------|------|-------------------|-------------|------|
| AustinCStone | user | 7 | #b8bb26 PLUS | +1 |
| DJedamski | user | 6 | #cc241d MINUS | -1 |
| M1shaaa | user | 5 | #d3869b ERGODIC | 0 |
| TeglonLabs | org | 4 | #b8bb26 PLUS | +1 |
| bmorphism | user | 30 | #cc241d MINUS | -1 |
| kristinezheng | user | 4 | #d3869b ERGODIC | 0 |
| kubeflow | org | 27 | #b8bb26 PLUS | +1 |
| migalkin | user | 7 | #cc241d MINUS | -1 |
| plurigrid | org | 65 | #d3869b ERGODIC | 0 |
| wasita | user | 7 | #b8bb26 PLUS | +1 |
| zubyul | user | 16 | #cc241d MINUS | -1 |

**Total repos snapshotted:** 178  
**Total world_increments:** 11

### GF(3) Color Chain

The increment ID drives the trit: `id % 3 == 0 → trit=0 ERGODIC #d3869b`, `id % 3 == 1 → trit=1 PLUS #b8bb26`, `id % 3 == 2 → trit=-1 MINUS #cc241d`.

### Notable Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,692 | — | 2026-05-24 |
| kubeflow/pipelines | 4,149 | Python | 2026-05-30 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-29 |
| kubeflow/trainer | 2,106 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 23 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |
| plurigrid/gorj | 0★ / **268 issues** | Clojure | 2026-05-30 |
| bmorphism/Gay.jl | 1★ / **189 issues** | Julia | 2026-05-30 |

### Most Active Right Now (by open issues)

- `plurigrid/gorj` → 268 issues (Clojure, pushed 2026-05-30)
- `bmorphism/Gay.jl` → 189 issues (Julia, pushed 2026-05-30)
- `kubeflow/notebooks` → 195 issues
- `kubeflow/pipelines` → 488 issues
- `plurigrid/eirobri` → 28 issues

### zubyul Social Graph Highlights

- **migalkin**: Knowledge Graph ML researcher — NodePiece (144★), StarE (89★), RWL
- **DJedamski**: Data science / Kaggle repos
- **wasita**: Network science, Svelte/TypeScript web projects, send2kobo, magic-garden
- **kristinezheng**: MIT cognitive neuroscience, lookit studies
- **M1shaaa**: Yale, Lookit experiments, TypeScript
- **AustinCStone**: ML/vision — TextGAN (92★), StereoVisionMRF (11★)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.00 APT** — either unfunded or coin store resources not initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | 0x8699... → 0x7af0... | 0.0 each |

**Interpretation:** These are designated swarm addresses. Zero balance may indicate: (a) addresses are pre-funded on testnet only, (b) CoinStore resource not registered, or (c) mainnet wallets not yet funded.

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`. **All healthy, all require 2-of-N signatures.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...87003 | 2 | ✓ |
| A-G | 0xf56c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All multisig contracts healthy. Standard 2-of-N threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)

The MNX testnet responds with a **Next.js SPA** — the `/api/markets` endpoint returns HTML, not JSON. No structured market data extractable from server-side rendering. Status: **SPA / data unavailable via direct API scrape.**

---

## DuckDB Schema

```sql
world_increments   -- 11 rows (one per org/user sweep)
repo_snapshots     -- 178 rows (GitHub repos snapshotted)
aptos_snapshots    -- 28 rows (Hamming swarm wallet balances)
multisig_probes    --  5 rows (Aptos multisig contract health)
mnx_snapshots      --  0 rows (SPA, no JSON available)
```

## GF(3) Trit Glossary

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | #d3869b | ERGODIC | Stationary / self-averaging |
| +1 | #b8bb26 | PLUS | Positive / constructive increment |
| -1 | #cc241d | MINUS | Negative / destructive increment |
