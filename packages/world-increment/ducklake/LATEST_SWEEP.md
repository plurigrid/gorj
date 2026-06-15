# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-15  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Repos Captured | Type |
|--------|---------------|------|
| plurigrid | 100 | org |
| kubeflow | 48 | org |
| TeglonLabs | 5 | org |
| bmorphism | 49 | user |
| zubyul | 100 | user |
| zubyul social graph (migalkin) | 19 | user |
| wasita | 11 | user |
| kristinezheng | 5 | user |
| DJedamski | 6 | user |
| M1shaaa | 8 | user |
| AustinCStone | 40 | user |
| **TOTAL** | **391** | |

### GF3 Color Chain Distribution

| GF3 Name | GF3 Color | Count |
|----------|-----------|-------|
| ERGODIC (trit=0) | #d3869b | 130 |
| PLUS (trit=1) | #b8bb26 | 131 |
| MINUS (trit=-1) | #cc241d | 130 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,725 | — | 2026-06-11 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-15 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-14 |
| kubeflow/trainer | 2,115 | Go | 2026-06-13 |
| kubeflow/katib | 1,683 | Go | 2026-06-04 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Language Distribution (Top 8)

| Language | Count |
|----------|-------|
| Python | 81 |
| Rust | 26 |
| JavaScript | 26 |
| TypeScript | 23 |
| Go | 15 |
| HTML | 15 |
| Jupyter Notebook | 15 |
| Clojure | 13 |

### Notable Recent Activity

- `kubeflow/pipelines` last pushed 2026-06-15 (today)
- `TeglonLabs/jank-crane` (C++, GF3 crane-jank converged-IR hub) pushed 2026-06-08
- `kristinezheng/kristinezheng.github.io` pushed 2026-06-07
- `M1shaaa/M1shaaa` (profile config) pushed 2026-06-15 (today)
- `wasita/wasita.github.io` (Svelte personal site) pushed 2026-06-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned **NULL** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These accounts have no APT CoinStore resource registered — either zero-balance wallets or they hold non-APT assets only.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793... | NULL |
| bob | 0x0a3c... | NULL |
| A | 0x8699... | NULL |
| B | 0x3f89... | NULL |
| C | 0x38b9... | NULL |
| D | 0xf776... | NULL |
| E | 0xdc1d... | NULL |
| F | 0x18a1... | NULL |
| G | 0x69a3... | NULL |
| H | 0xce67... | NULL |
| I | 0x070f... | NULL |
| J | 0x4d96... | NULL |
| K | 0xa732... | NULL |
| L | 0x7c2e... | NULL |
| M | 0x6fed... | NULL |
| N | 0xe7dd... | NULL |
| O | 0x7325... | NULL |
| P | 0x6218... | NULL |
| Q | 0xac40... | NULL |
| R | 0x7ce6... | NULL |
| S | 0xb875... | NULL |
| T | 0x3578... | NULL |
| U | 0x7586... | NULL |
| V | 0xb59d... | NULL |
| W | 0x5f32... | NULL |
| X | 0xa95c... | NULL |
| Y | 0xd8e3... | NULL |
| Z | 0x7af0... | NULL |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts respond **healthy** with `sigs_required=2`.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | yes |
| A-G | 0xf56c4a1c... | 2 | yes |
| Y-Z | 0xd3ffe181... | 2 | yes |
| S-T | 0x3b1c3ae9... | 2 | yes |
| V-W | 0x40fad7b4... | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — testnet.mnx.fi is behind Vercel Deployment Protection and requires authentication. No market data fetched. `mnx_snapshots` table is empty.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 391 |
| repo_snapshots | 391 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth required) |
