# World-Increment Sweep — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-07-06-2306`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this sweep) | 11 |
| Total World Increments (all time) | 34 |
| New Repo Snapshots (this sweep) | 392 |
| Total Repo Snapshots (all time) | 1336 |
| Sources Covered | 3 orgs + 8 users |

### Sources Swept

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | `shrimp` (pushed 2026-07-03), `asi` (HTML, 28★), `place` (TeX, pushed today) |
| kubeflow | org | 49 | `pipelines` (Python, 4169★), `hub` (Go, 175★), `sdk` (Python, 123★) |
| TeglonLabs | org | 5 | `jank-crane` (C++, GF3/jank-crane), `mathpix-gem` (Ruby, 2★) |
| bmorphism | user | 100 | `Gay.jl` (Julia, 2★, pushed today), `satreadout` (HTML) |
| zubyul | user | 49 | `voice-observatory` (Python), `ghostel-emacs-worlds` (GLSL), `nash-tui` (Rust) |
| migalkin | user | 19 | `kgcourse2021` (HTML, 25★), `NBFNet_mlx` (Python, 10★) |
| DJedamski | user | 6 | Kaggle/stats work (R, Jupyter) |
| wasita | user | 11 | `wasita.github.io` (Svelte, pushed 2026-07-05) |
| kristinezheng | user | 5 | `kristinezheng.github.io` (HTML, pushed 2026-07-01) |
| M1shaaa | user | 8 | `M1shaaa` profile (pushed today 2026-07-06) |
| AustinCStone | user | 40 | `EpsteinSearch`, `bmforkupdate`, `bmfork` (Python) |

### GF(3) Color Chain

| Increment ID | Trit | Color | Name | Source |
|-------------|------|-------|------|--------|
| id%3==0 | 0 | #d3869b | ERGODIC | plurigrid, TeglonLabs, migalkin, kristinezheng |
| id%3==1 | 1 | #b8bb26 | PLUS | kubeflow, bmorphism, DJedamski, M1shaaa |
| id%3==2 | -1 | #cc241d | MINUS | zubyul, wasita, AustinCStone |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) queried via Aptos mainnet fullnode.

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
This indicates coin stores have **not been initialized** — accounts exist on-chain but hold 0 APT.

| World | Balance |
|-------|---------|
| alice–bob, A–Z (all 28) | 0.0 APT (coin store not initialized) |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...` | 2 | ✅ Healthy |
| A-G | `0xf56c4a1c...` | 2 | ✅ Healthy |
| Y-Z | `0xd3ffe181...` | 2 | ✅ Healthy |
| S-T | `0x3b1c3ae9...` | 2 | ✅ Healthy |
| V-W | `0x40fad7b4...` | 2 | ✅ Healthy |

All 5 multisig contracts respond correctly and require **2-of-N signatures**.

### MNX Markets

`testnet.mnx.fi` requires **Vercel authentication** — no market data accessible without a session token. Recorded as unavailable.

---

## Key Signals

- **M1shaaa** pushed to profile repo today (2026-07-06 15:23 UTC) — active
- **plurigrid/place** (TeX) pushed today — active development
- **bmorphism/Gay.jl** pushed today — Julia work ongoing
- **kubeflow/pipelines** (4169★) and **kubeflow/hub** (175★) both active (pushed today)
- All 5 Hamming multisig pairs are **healthy** (2-of-N, responsive)
- Aptos wallets: **all 28 coin stores uninitialized** — no APT balances on mainnet
- MNX testnet: **behind auth wall**, data unavailable
