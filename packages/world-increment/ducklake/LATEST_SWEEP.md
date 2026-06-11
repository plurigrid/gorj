# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-11  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | GF3 Trit | GF3 Name | Color |
|--------|------|-------|----------|----------|-------|
| plurigrid | org | 100 | 1 | PLUS | #b8bb26 |
| kubeflow | org | 48 | 2 | MINUS | #cc241d |
| bmorphism | user | 100 | 0 | ERGODIC | #d3869b |
| zubyul | user | 49 | 1 | PLUS | #b8bb26 |
| migalkin | social | 19 | 2 | MINUS | #cc241d |
| wasita | social | 11 | 0 | ERGODIC | #d3869b |
| AustinCStone | social | 30 | 1 | PLUS | #b8bb26 |
| DJedamski | social | 6 | 2 | MINUS | #cc241d |
| kristinezheng | social | 5 | 0 | ERGODIC | #d3869b |
| M1shaaa | social | 8 | 1 | PLUS | #b8bb26 |
| TeglonLabs | org | 5 | 2 | MINUS | #cc241d |

**Total repos snapshotted:** 381  
**World increment rows:** 11 (GF3 chain: PLUS→MINUS→ERGODIC→...)

### GF(3) Color Chain
- `id%3==0` → trit=0, ERGODIC, #d3869b (mauve)
- `id%3==1` → trit=1, PLUS, #b8bb26 (yellow-green)
- `id%3==2` → trit=-1, MINUS, #cc241d (red)

### Notable Repos
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps (C++, pushed 2026-06-08)
- **TeglonLabs/mathpix-gem** — mathematical OCR Ruby gem (2 stars, 11 open issues)
- **kristinezheng/kristinezheng.github.io** — active personal site (HTML, pushed 2026-06-07)
- **M1shaaa/M1shaaa** — active profile repo (pushed 2026-06-11)
- **plurigrid** — 100 repos including MCP tooling and AI infrastructure
- **kubeflow** — 48 repos in ML infrastructure org
- **bmorphism** — 100 repos (most active individual contributor)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 addresses)

All 28 Hamming swarm wallets probed on Aptos mainnet via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A | 0x8699... | 0.0 |
| B | 0x3f89... | 0.0 |
| C | 0x38b9... | 0.0 |
| D | 0xf776... | 0.0 |
| E | 0xdc1d... | 0.0 |
| F | 0x18a1... | 0.0 |
| G | 0x69a3... | 0.0 |
| H | 0xce67... | 0.0 |
| I | 0x070f... | 0.0 |
| J | 0x4d96... | 0.0 |
| K | 0xa732... | 0.0 |
| L | 0x7c2e... | 0.0 |
| M | 0x6fed... | 0.0 |
| N | 0xe7dd... | 0.0 |
| O | 0x7325... | 0.0 |
| P | 0x6218... | 0.0 |
| Q | 0xac40... | 0.0 |
| R | 0x7ce6... | 0.0 |
| S | 0xb875... | 0.0 |
| T | 0x3578... | 0.0 |
| U | 0x7586... | 0.0 |
| V | 0xb59d... | 0.0 |
| W | 0x5f32... | 0.0 |
| X | 0xa95c... | 0.0 |
| Y | 0xd8e3... | 0.0 |
| Z | 0x7af0... | 0.0 |

**Note:** All 28 addresses returned 0.0 APT — accounts are registered on-chain but unfunded at time of sweep.

### Multisig Contract Probes (5 pairs)

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✓ |
| A-G | 0xf56c... | 2 | ✓ |
| Y-Z | 0xd3ff... | 2 | ✓ |
| S-T | 0x3b1c... | 2 | ✓ |
| V-W | 0x40fa... | 2 | ✓ |

**All 5/5 multisig contracts live and healthy (2-of-2 threshold).**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is protected by Vercel deployment authentication — the API returns a Vercel auth challenge. Market data is **unavailable** without a bypass token. `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema Summary

```
world_increments  : 11 rows  (GF3-colored sweep events)
repo_snapshots    : 381 rows (GitHub repos with stars/forks/language/pushed_at)
aptos_snapshots   : 28 rows  (Hamming swarm wallets alice,bob,A–Z)
multisig_probes   : 5 rows   (A-B, A-G, Y-Z, S-T, V-W — all 2-of-2)
mnx_snapshots     : 0 rows   (Vercel auth blocked)
```
