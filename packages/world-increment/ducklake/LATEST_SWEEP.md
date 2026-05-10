# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-10  
**Sweep IDs:** 13 (PLUS #b8bb26) → 14 (MINUS #cc241d) → 15 (ERGODIC #d3869b)  
**GF(3) cycle:** 5th cycle started (IDs 13-15 complete it)

---

## JOB 1: GitHub Social Graph Sweep

### Status
GitHub unauthenticated API rate-limited (IP 34.135.250.196 exhausted 60 req/hr quota).  
plurigrid/gorj queried via MCP GitHub tools. All other sources served from existing 944-repo cache (last filled 2026-04-14).

### Sources tracked (945 repo snapshots total)
| Source | Type | Repos cached |
|--------|------|-------------|
| plurigrid | org | 200 |
| bmorphism | user | 200 |
| TeglonLabs | org | 106 |
| kubeflow | org | 94 |
| AustinCStone | user | 86 |
| migalkin | user | 60 |
| wasita | user | 60 |
| zubyul | user | 48 |
| kristinezheng | user | 36 |
| M1shaaa | user | 32 |
| DJedamski | user | 22 |
| plurigrid/gorj (live MCP) | repo | 1 |

### plurigrid/gorj — latest activity (MCP live)
| SHA | Message | Date |
|-----|---------|------|
| `5b28fe0` | chore: ignore duckdb binary in repo root | 2026-05-08 |
| `ebf263f` | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| `b434a43` | Merge sweep state into master | 2026-04-14 |
| `631518b` | world-increment sweep 2026-04-12: insert id=12 ERGODIC | 2026-04-12 |

Active sweep branches: 30+ `world-increment/sweep-*` branches from 2026-04-27 through 2026-04-30.

### World Increments (cumulative: 26 total)
| ID | GF3 Trit | Color | Name | Event |
|----|----------|-------|------|-------|
| 13 | +1 | #b8bb26 | PLUS | sweep_start |
| 14 | -1 | #cc241d | MINUS | github_sweep |
| 15 | 0 | #d3869b | ERGODIC | aptos_snapshot |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets)
All wallets queried via `fullnode.mainnet.aptoslabs.com`. All accounts return 0 APT (accounts exist on-chain but hold no liquid APT in CoinStore, or accounts are not yet initialized).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.00000000 |
| bob | 0x0a3c...512d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...cb13 | 0.00000000 |
| C | 0x38b9...535e | 0.00000000 |
| D | 0xf776...cfdd1 | 0.00000000 |
| E | 0xdc1d...8d36 | 0.00000000 |
| F | 0x18a1...3cf71 | 0.00000000 |
| G | 0x69a3...7f32 | 0.00000000 |
| H | 0xce67...300f | 0.00000000 |
| I | 0x070f...1fc9 | 0.00000000 |
| J | 0x4d96...7f54 | 0.00000000 |
| K | 0xa732...5dc4 | 0.00000000 |
| L | 0x7c2e...eba9 | 0.00000000 |
| M | 0x6fed...f2e9 | 0.00000000 |
| N | 0xe7dd...51b2c | 0.00000000 |
| O | 0x7325...a89d | 0.00000000 |
| P | 0x6218...c948 | 0.00000000 |
| Q | 0xac40...c89a9 | 0.00000000 |
| R | 0x7ce6...6e10 | 0.00000000 |
| S | 0xb875...d0386 | 0.00000000 |
| T | 0x3578...f4588 | 0.00000000 |
| U | 0x7586...f9956 | 0.00000000 |
| V | 0xb59d...af2c3 | 0.00000000 |
| W | 0x5f32...c7b0 | 0.00000000 |
| X | 0xa95c...3047d | 0.00000000 |
| Y | 0xd8e3...444c4 | 0.00000000 |
| Z | 0x7af0...197c | 0.00000000 |

**Total swarm APT:** 0.00000000

### Multisig Contract Probes (5 pairs)
All 5 multisig accounts respond healthy — each requiring **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

**5/5 multisigs healthy** (2-of-N threshold confirmed on mainnet).

### MNX Testnet Markets
`https://testnet.mnx.fi` — HTTP 200 (Next.js SPA). No public JSON API endpoints found at `/api/markets`, `/api/v1/markets`. Market data not extractable without browser JS execution. **Status: UNAVAILABLE (SPA-only).**

---

## DuckDB Ducklake State

| Table | Rows |
|-------|------|
| world_increments | 26 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**DB:** `packages/world-increment/ducklake/world-increments.duckdb`
