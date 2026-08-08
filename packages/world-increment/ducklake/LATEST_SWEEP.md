# World Increment Sweep + Hamming Swarm Snapshot
**Generated:** 2026-08-08 UTC  
**DB:** `world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph | 19 |
| DJedamski | social-graph | 6 |
| wasita | social-graph | 14 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| AustinCStone | social-graph | 41 |

### Notable Activity (most recently pushed)
- **plurigrid/gorj** — Clojure, 1717 issues open, pushed 2026-08-08 (active development)
- **kubeflow/trainer** — Go, ⭐2175, pushed 2026-08-08 (distributed AI training)
- **kubeflow/pipelines** — Python, ⭐4181, pushed 2026-08-07
- **kubeflow/spark-operator** — Python, ⭐3145, pushed 2026-08-06
- **bmorphism/Gay.jl** — Julia, pushed 2026-08-07 (deterministic color sampling)
- **wasita/wm-cv** — Svelte, pushed 2026-08-07
- **wasita/xoxowasita-analysis** — Python, pushed 2026-08-06 (new repo)

### GF(3) Color Chain Applied
Increments colored in GF(3) chain:
- `id%3==0` → trit=0 **ERGODIC** `#d3869b`
- `id%3==1` → trit=1 **PLUS** `#b8bb26`
- `id%3==2` → trit=-1 **MINUS** `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-08-08)
> Note: Accounts use Fungible Asset standard (`0x1::coin::balance` view); CoinStore resource absent.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...12d5 | **12.657007** |
| A | 0x8699...9d7a | 0.051767 |
| B | 0x3f89...b13 | 0.036256 |
| C | 0x38b9...35e | 0.010185 |
| D | 0xf776...dd1 | 0.011629 |
| E | 0xdc1d...d36 | 0.009372 |
| F | 0x18a1...71 | **1.960516** |
| G | 0x69a3...f32 | 0.000681 |
| H | 0xce67...00f | 0.001681 |
| I | 0x070f...fc9 | 0.000681 |
| J | 0x4d96...f54 | **1.895093** |
| K | 0xa732...dc4 | 0.161961 |
| L | 0x7c2e...ba9 | **1.927269** |
| M | 0x6fed...2e9 | 0.112285 |
| N | 0xe7dd...b2c | 0.106121 |
| O | 0x7325...89d | 0.210136 |
| P | 0x6218...948 | 0.140136 |
| Q | 0xac40...a9 | 0.10324 |
| R | 0x7ce6...e10 | 0.090217 |
| S | 0xb875...386 | 0.091788 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| V | 0xb59d...2c3 | 0.04883299 |
| W | 0x5f32...7b0 | 0.040705 |
| X | 0xa95c...47d | 0.042577 |
| Y | 0xd8e3...4c4 | 0.044449 |
| Z | 0x7af0...97c | 0.024268 |

**Total APT (this snapshot): 20.344773 APT**  
**Largest holder: bob (12.66 APT)**

### Multisig Contract Probes
All 5 multisig accounts healthy — require 2 signatures.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
Status: **SPA — no JSON API accessible**. The site (`testnet.mnx.fi`) is a Next.js single-page application. All routes return the same HTML shell; no REST/JSON market data endpoint is exposed. Market data noted as unavailable for this snapshot.

---

## DuckDB Summary
| Table | Row Count |
|-------|-----------|
| world_increments | 67 |
| repo_snapshots | 988 |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 (unavailable) |
