# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos epoch at query time:** 16532 (mainnet chain_id=1)

---

## Summary Counts

| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 35 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 1: GitHub Social Graph Sweep

Sources snapshotted (IDs 13–24):

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 13 | plurigrid (org) | gorj | +1 | `#b8bb26` | **PLUS** |
| 14 | bmorphism (user) | Gay.jl | -1 | `#cc241d` | **MINUS** |
| 15 | zubyul (user) | tilelang-kernels | 0 | `#d3869b` | **ERGODIC** |
| 16 | kubeflow (org) | pipelines | +1 | `#b8bb26` | **PLUS** |
| 17 | TeglonLabs (org) | jank-crane | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin (user) | NodePiece | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski (user) | DJedamski.github.io | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita (user) | wm-cv | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng (user) | kristinezheng.github.io | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa (user) | M1shaaa.github.io | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone (user) | TextGAN | -1 | `#cc241d` | **MINUS** |
| 24 | world-increment-sweep | aptos-mainnet | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain conservation (IDs 13–24): 4×PLUS + 4×MINUS + 4×ERGODIC = 0 mod 3 ✓

**Note:** Direct GitHub REST API blocked by proxy; MCP tools scoped to plurigrid/gorj. gorj current state: 1,158 open issues, latest commit 2026-07-14.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — All 28 Addresses

Query method: `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>`
(Previous runs used GET CoinStore and got 0 — view function returns actual balances.)

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...12d5 | **12.65700700** |
| A | 0x8699...b9d7 | 0.05176700 |
| B | 0x3f89...b13 | 0.03625600 |
| C | 0x38b9...535e | 0.01018500 |
| D | 0xf776...fdd1 | 0.01162900 |
| E | 0xdc1d...d36 | 0.00937200 |
| F | 0x18a1...cf71 | 1.96051600 |
| G | 0x69a3...f32 | 0.00068100 |
| H | 0xce67...300f | 0.00168100 |
| I | 0x070f...1fc9 | 0.00068100 |
| J | 0x4d96...f54 | **1.89509300** |
| K | 0xa732...5dc4 | 0.16196100 |
| L | 0x7c2e...eba9 | **1.92726900** |
| M | 0x6fed...2e9 | 0.11228500 |
| N | 0xe7dd...1b2c | 0.10612100 |
| O | 0x7325...89d | 0.21013600 |
| P | 0x6218...c948 | 0.14013600 |
| Q | 0xac40...89a9 | 0.10324000 |
| R | 0x7ce6...e10 | 0.09021700 |
| S | 0xb875...0386 | 0.09178800 |
| T | 0x3578...4588 | 0.07371300 |
| U | 0x7586...9956 | 0.05577300 |
| V | 0xb59d...af2c | 0.04883299 |
| W | 0x5f32...c7b0 | 0.04070500 |
| X | 0xa95c...047d | 0.04257700 |
| Y | 0xd8e3...44c4 | 0.04444900 |
| Z | 0x7af0...97c | 0.02426800 |

**Total swarm balance: 20.34477251 APT**

Top holders: bob (12.657 APT) · F (1.961 APT) · L (1.927 APT) · J (1.895 APT)

### Multisig Contract Probes — All 5 Healthy

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All multisig contracts on Aptos mainnet respond and require 2-of-N signatures.

### MNX Markets

`testnet.mnx.fi` — **Unavailable**: Vercel deployment protection active. No public REST API accessible without bypass token.

---

## Notable Delta vs Previous Sweeps

- **First successful non-zero Aptos balance capture** — prior runs (all of 2026-07-13/14) got 0 APT using legacy CoinStore path. This run used `0x1::coin::balance` view POST and captured real on-chain balances.
- bob is dominant holder at 12.657 APT (~62% of swarm total)
- F, J, L each hold ~1.9 APT (second-tier holders)
- All 5 multisigs stable at 2-of-2 threshold
- plurigrid/gorj at 1,158 open issues; latest master commit 2026-05-08
- 9 prior sweep PRs open and unmerged from today + yesterday
