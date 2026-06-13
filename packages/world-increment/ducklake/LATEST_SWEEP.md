# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-06-13  
**DuckDB:** `v1.5.3 (Variegata)` — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Unique Repos | Total Stars |
|--------|------|-------------|-------------|
| kubeflow | org | 50 | 101,924 |
| migalkin | user (zubyul social) | 30 | 830 |
| bmorphism | user | 109 | 438 |
| AustinCStone | user (zubyul social) | 43 | 322 |
| plurigrid | org | 106 | 138 |
| zubyul | user | 45 | 28 |
| DJedamski | user (zubyul social) | 11 | 17 |
| TeglonLabs | org | 54 | 14 |
| wasita | user (zubyul social) | 31 | 10 |
| M1shaaa | user (zubyul social) | 16 | 0 |
| kristinezheng | user (zubyul social) | 18 | 0 |

### Notable Repos (Most Recently Pushed)

- **plurigrid/gorj** (Clojure) — `2026-06-13` — 540 open issues — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **bmorphism/Gay.jl** (Julia) — `2026-06-13` — 189 open issues — Wide-gamut color sampling with splittable determinism
- **kubeflow/trainer** (Go) — `2026-06-13` — 2,112★ — Distributed AI Model Training and LLM Fine-Tuning on Kubernetes
- **bmorphism/satreadout** (Lean) — `2026-06-10` — Machine-checked saturating non-Riemannian perceptual readout
- **plurigrid/asi** (HTML) — `2026-06-10` — 26★ — everything is topological chemputer!
- **kubeflow/spark-operator** (Python) — `2026-06-12` — 3,127★ — Kubernetes operator for Apache Spark
- **kubeflow/katib** (Python) — `2026-06-12` — 1,683★ — Automated Machine Learning on Kubernetes
- **TeglonLabs/jank-crane** (C++) — `2026-06-08` — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **bmorphism/ocaml-mcp-sdk** (OCaml) — `2026-03-16` — 61★ — OCaml SDK for Model Context Protocol (Jane Street oxcaml_effect)
- **migalkin/NodePiece** (Python) — 144★ — ICLR'22 compositional KG representations
- **AustinCStone/TextGAN** (Python) — 92★ — GAN for text generation (TensorFlow)

### GF(3) Color Chain Distribution

| Trit | Name | Hex Color | Count |
|------|------|-----------|-------|
| 0 | ERGODIC | `#d3869b` | 51 |
| 1 | PLUS | `#b8bb26` | 53 |
| -1 | MINUS | `#cc241d` | 52 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS  
**Total world_increments:** 156 | **Repo snapshots:** 1,077

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets queried against `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).

| World | Address (abbreviated) | APT Balance |
|-------|----------------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

**All 28 Hamming-swarm wallets show 0 APT balance.** Wallets are either unfunded or hold non-APT assets not captured by `CoinStore<AptosCoin>`.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address (abbreviated) | Sigs Required | Status |
|------|----------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

All 5 probed multisig contracts via `0x1::multisig_account::num_signatures_required` return `sigs_required = 2`. 5/5 healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/prices`) return HTTP 401 with an authentication challenge. No market data extractable without a Vercel bypass token.

---

## DuckDB Tables Summary

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 156 | GF(3) color-tagged events |
| `repo_snapshots` | 1,077 | GitHub repo metadata snapshots |
| `aptos_snapshots` | 28 | Hamming swarm APT wallet balances |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 1 | MNX market data (unavailable marker) |

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
