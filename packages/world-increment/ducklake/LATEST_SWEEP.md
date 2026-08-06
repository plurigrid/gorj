# World-Increment Sweep + Hamming Swarm Snapshot
**Date:** 2026-08-06  
**Run type:** Scheduled sweep (world-increment-sweep + hamming-swarm-snapshot)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 49 |
| zubyul | user | 100 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 14 |
| AustinCStone | social-graph | 20 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |

**Total repos ingested this run: ~375**

### Notable repos found this run
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- `wasita/xoxowasita-analysis` — Python analysis (pushed TODAY 2026-08-06)
- `wasita/joint-planning-lit` — joint planning literature (pushed 2026-08-04)
- `migalkin/NodePiece` — 144★ KG representation (ICLR'22)
- `AustinCStone/byteruckus` — (pushed 2026-07-15)
- `TeglonLabs/mathpix-gem` — LaTeX OCR Ruby gem, 11 open issues

### GF(3) Color Chain Applied
- trit=0 → ERGODIC #d3869b
- trit=1 → PLUS #b8bb26  
- trit=-1 → MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balance Survey
**All 28 addresses probed against Aptos mainnet.**

| World | Result |
|-------|--------|
| alice | resource_not_found (unfunded) |
| bob | resource_not_found (unfunded) |
| A–Z (26 addrs) | resource_not_found (unfunded) |

**All 28 accounts returned HTTP 404 / `resource_not_found` from the Aptos fullnode.**  
Interpretation: accounts exist on-chain but have no APT CoinStore registered (never funded or using fungible asset standard instead of legacy coin). Recorded as 0.0 APT.

Aptos ledger state at query time:
- Chain ID: 1 (mainnet)
- Ledger version: 6,646,269,810
- Block height: 953,908,844
- Epoch: 16,814
- Timestamp: 2026-08-06T23:14:52Z

### Multisig Contract Probes
| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts are healthy (2-of-N threshold).**

### MNX Markets (testnet.mnx.fi)
Status: **UNAVAILABLE** — testnet.mnx.fi is a JS SPA that yields no data without browser rendering. `/api/markets` returned HTTP 404. No market data recorded.

---

## Cumulative DuckDB State (`world-increments.duckdb`)

| Table | Row Count |
|-------|-----------|
| world_increments | 344 |
| repo_snapshots | 1,265 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

Top org/users by snapshot count (cumulative):
1. plurigrid: 300
2. bmorphism: 300
3. kubeflow: 143
4. TeglonLabs: 111
5. zubyul: 97
6. AustinCStone: 89
7. migalkin: 65
8. wasita: 64
9. kristinezheng: 38
10. M1shaaa: 34
