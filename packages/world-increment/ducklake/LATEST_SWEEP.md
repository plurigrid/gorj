# World-Increment Sweep — 2026-08-09

## Sweep Metadata
- **Date:** 2026-08-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 34 |
| New Increments This Sweep | 11 |
| Total Repo Snapshots (all time) | 1297 |
| New Repo Snapshots This Sweep | 353 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (SPA) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — New Increments (IDs 13–23)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 9 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 5 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 14 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 9 | -1 | `#cc241d` | **MINUS** |

### Notable Repos Observed

| Repo | Stars | Lang | Last Push | Notes |
|------|-------|------|-----------|-------|
| migalkin/NodePiece | 144 | Python | 2026-05-07 | ICLR'22 KG representations |
| migalkin/StarE | 89 | Python | 2026-04-16 | EMNLP 2020 hyper-relational KG |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 | TensorFlow text GAN |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 | GF3 convergence maps (new!) |
| wasita/wm-cv | 0 | Svelte | 2026-08-07 | Latest push: 2 days ago |
| wasita/xoxowasita-analysis | 0 | Python | 2026-08-06 | New repo (3 days old) |
| kristinezheng/kristinezheng.github.io | 0 | HTML | 2026-07-01 | Active personal site |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

**Status:** All 28 addresses returned no APT CoinStore resource on mainnet.  
This indicates these accounts either have zero APT balance, have not been initialized on mainnet, or hold assets in other token types only.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acde... | not found |
| bob | 0x0a3c00c5... | not found |
| A–Z | 0x8699edc0... (etc) | not found (all 26) |

### Multisig Contracts (5 probes)

**All 5 multisig contracts are HEALTHY — 2-of-N threshold.**

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

API endpoints (`/api/markets`, `/api/v1/markets`) return a Next.js SPA shell — no market data extractable via HTTP. Status: **unavailable (client-rendered SPA)**.

---

## Database State

| Table | Total Rows |
|-------|-----------|
| world_increments | 34 |
| repo_snapshots | 1297 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Signal Summary

- **wasita** is the most active social-graph node right now: `wm-cv` pushed 2026-08-07, new `xoxowasita-analysis` repo created 2026-08-04.
- **TeglonLabs/jank-crane** is a new repo (2026-06-08) explicitly referencing GF3 convergence maps — directly relevant to this sweep's GF(3) chain.
- **Aptos Hamming swarm**: all 28 wallet addresses return no on-chain APT CoinStore. Swarm may be operating via other token modules or accounts may be pre-funded via different paths.
- **All 5 multisig contracts** remain at 2-of-N threshold — no threshold changes detected.
