# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-03  
**GF(3) Color Chain:** ERGODIC=#d3869b (id%3=0) · PLUS=#b8bb26 (id%3=1) · MINUS=#cc241d (id%3=2)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted | Top Star |
|--------|------|-------------------|----------|
| plurigrid | org | 100 | asi (28★) |
| kubeflow | org | 48 | pipelines (4168★) |
| TeglonLabs | org | 5 | mathpix-gem (2★) |
| bmorphism | user | 100 | shitcoin (5★) · Gay.jl (2★) |
| zubyul | user | 10 | gay-world (1★) |
| migalkin | user | 5 | NodePiece (144★) |
| DJedamski | user | 3 | Kaggle (1★) |
| wasita | user | 5 | magic-garden (2★) |
| kristinezheng | user | 3 | — |
| M1shaaa | user | 2 | — |
| AustinCStone | user | 4 | TextGAN (92★) |

**Total world_increments rows (cumulative):** 308  
**Total repo_snapshots rows (cumulative):** 1229

### Most Recently Pushed (plurigrid org, as of 2026-07-03)
- `plurigrid/shrimp` — pushed 2026-07-03
- `plurigrid/gorj` — pushed 2026-07-03 (this repo!)
- `plurigrid/eirobri` — pushed 2026-06-30 (Clojure)
- `plurigrid/asi` — pushed 2026-06-29, 28★ (HTML)
- `plurigrid/place` — pushed 2026-06-29 (TeX)

### Most Recently Pushed (bmorphism)
- `bmorphism/Gay.jl` — pushed 2026-07-03 (Julia)
- `bmorphism/satreadout` — pushed 2026-06-20
- `bmorphism/bci-preview` — pushed 2026-06-20

### Notable Ecosystem Repos
- **kubeflow/kubeflow** 15760★ — ML platform flagship
- **kubeflow/pipelines** 4168★ — ML workflow orchestration
- **kubeflow/spark-operator** 3132★ — Spark on Kubernetes
- **migalkin/NodePiece** 144★ — KG embedding (ICLR'22)
- **AustinCStone/TextGAN** 92★ — Text generative adversarial network
- **TeglonLabs/jank-crane** — C++ crane-jank converged-IR hub (newest, Jun 2026)

### GF(3) Distribution (this run)
```
ERGODIC (#d3869b, trit=0):  102 increments
PLUS    (#b8bb26, trit=1):  103 increments
MINUS   (#cc241d, trit=-1): 103 increments
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances

All 28 addresses (alice, bob, A–Z) probed against Aptos mainnet at ledger version ~6081549176.

**Result: ALL addresses returned `resource_not_found`** — none have an initialized `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on mainnet. Balance recorded as 0.000 APT for all worlds.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.000 |
| bob | 0x0a3c...2d5d | 0.000 |
| A | 0x8699...e9d7a | 0.000 |
| B | 0x3f89...cb13 | 0.000 |
| C | 0x38b9...535e | 0.000 |
| D | 0xf776...cdd1 | 0.000 |
| E | 0xdc1d...8d36 | 0.000 |
| F | 0x18a1...cf71 | 0.000 |
| G | 0x69a3...7f32 | 0.000 |
| H | 0xce67...300f | 0.000 |
| I | 0x070f...1fc9 | 0.000 |
| J | 0x4d96...7f54 | 0.000 |
| K | 0xa732...5dc4 | 0.000 |
| L | 0x7c2e...eba9 | 0.000 |
| M | 0x6fed...2e9 | 0.000 |
| N | 0xe7dd...1b2c | 0.000 |
| O | 0x7325...a89d | 0.000 |
| P | 0x6218...c948 | 0.000 |
| Q | 0xac40...89a9 | 0.000 |
| R | 0x7ce6...6e10 | 0.000 |
| S | 0xb875...0386 | 0.000 |
| T | 0x3578...4588 | 0.000 |
| U | 0x7586...f956 | 0.000 |
| V | 0xb59d...f2c3 | 0.000 |
| W | 0x5f32...c7b0 | 0.000 |
| X | 0xa95c...047d | 0.000 |
| Y | 0xd8e3...44c4 | 0.000 |
| Z | 0x7af0...197c | 0.000 |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — endpoint returns HTTP 401 (Vercel authentication required). Market data could not be extracted. No records inserted into `mnx_snapshots`.

---

## DuckDB Schema (ducklake/world-increments.duckdb)

```sql
world_increments   -- GF3-colored event log (308 rows cumulative)
repo_snapshots     -- full repo metadata (1229 rows cumulative)
aptos_snapshots    -- wallet balances (28 rows this run)
multisig_probes    -- multisig health (5 rows this run)
mnx_snapshots      -- market data (0 rows — unavailable)
```
