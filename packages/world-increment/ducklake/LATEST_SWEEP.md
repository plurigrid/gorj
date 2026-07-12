# World-Increment Sweep — 2026-07-12

## Run Summary
- **Sweep date**: 2026-07-12T00:00:00Z
- **GF(3) chain position**: id=13 (PLUS #b8bb26) → id=14 (MINUS #cc241d) — 5th full cycle
- **GitHub sweep**: repo-scoped proxy only; org-level API blocked in this environment (944 snapshots from prior sweeps retained)
- **Aptos Hamming swarm**: 28 addresses probed (alice, bob, A–Z)
- **Multisig contracts**: 5 probed via on-chain view call
- **MNX Markets**: unavailable (testnet.mnx.fi requires Vercel auth — 401)

## DuckDB Ducklake Totals
| Table | Rows |
|-------|------|
| world_increments | 25 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |

## GF(3) World-Increment Chain (last 5)
| id | timestamp | trit | color | name | source | event |
|----|-----------|------|-------|------|--------|-------|
| 14 | 2026-07-12 00:00:00 | -1 | #cc241d | MINUS | hamming-swarm | sweep_complete |
| 13 | 2026-07-12 00:00:00 | 1 | #b8bb26 | PLUS | hamming-swarm | sweep_start |
| 12 | 2026-04-12 00:00:00 | 0 | #d3869b | ERGODIC | bmorphism | sweep_complete |
| 11 | 2026-04-14 01:48:57 | -1 | #cc241d | MINUS | AustinCStone | repo_sweep |
| 11 | 2026-04-10 23:10:18 | -1 | #cc241d | MINUS | AustinCStone | repo_snapshot |

## Hamming Swarm — Aptos Wallet Balances (2026-07-12)
All 28 addresses probed against Aptos Mainnet fullnode.
All returned HTTP 404 for CoinStore resource — accounts exist on-chain but have not registered 0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| A | 0x8699edc0...be9d7a | 0.0 APT (uninitialized) |
| B | 0x3f892ebe...77cb13 | 0.0 APT (uninitialized) |
| C | 0x38b99e63...91535e | 0.0 APT (uninitialized) |
| D | 0xf7765624...fcfdd1 | 0.0 APT (uninitialized) |
| E | 0xdc1d9d53...958d36 | 0.0 APT (uninitialized) |
| F | 0x18a14b5b...c3cf71 | 0.0 APT (uninitialized) |
| G | 0x69a394c0...cc7f32 | 0.0 APT (uninitialized) |
| H | 0xce67c327...e5300f | 0.0 APT (uninitialized) |
| I | 0x070fe5d7...0c1fc9 | 0.0 APT (uninitialized) |
| J | 0x4d964db8...e87f54 | 0.0 APT (uninitialized) |
| K | 0xa732040a...425dc4 | 0.0 APT (uninitialized) |
| L | 0x7c2eaeaf...37eba9 | 0.0 APT (uninitialized) |
| M | 0x6fed37a7...b7f2e9 | 0.0 APT (uninitialized) |
| N | 0xe7dde6da...551b2c | 0.0 APT (uninitialized) |
| O | 0x73252b60...25a89d | 0.0 APT (uninitialized) |
| P | 0x6218792d...1ec948 | 0.0 APT (uninitialized) |
| Q | 0xac40fa50...5c89a9 | 0.0 APT (uninitialized) |
| R | 0x7ce605cc...d76e10 | 0.0 APT (uninitialized) |
| S | 0xb8753014...9d0386 | 0.0 APT (uninitialized) |
| T | 0x35781dc0...3f4588 | 0.0 APT (uninitialized) |
| U | 0x75860da4...ef9956 | 0.0 APT (uninitialized) |
| V | 0xb59dd817...9af2c3 | 0.0 APT (uninitialized) |
| W | 0x5f32aef7...ccc7b0 | 0.0 APT (uninitialized) |
| X | 0xa95cbbd1...33047d | 0.0 APT (uninitialized) |
| Y | 0xd8e32848...2444c4 | 0.0 APT (uninitialized) |
| Z | 0x7af0ef6e...4e197c | 0.0 APT (uninitialized) |
| alice | 0xc793acde...24cc7b | 0.0 APT (uninitialized) |
| bob | 0x0a3c00c5...512d5d | 0.0 APT (uninitialized) |

## Multisig Contract Probes
All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✓ |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✓ |
| V-W | 0x40fad7b4...80eb6d | 2 | ✓ |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✓ |

## MNX Markets
testnet.mnx.fi returned HTTP 401 (Vercel deployment protection). No market data captured this sweep.

## GitHub Social Graph Coverage
Org-level GitHub API endpoints (`/orgs/{org}/repos`, `/users/{user}/repos`) are blocked in this
session by the proxy scope restriction (only `plurigrid/gorj` repo-scoped endpoints available).

Repo snapshots in DB (from prior sweeps):
| Source | Count |
|--------|-------|
| plurigrid | 200 |
| bmorphism | 200 |
| TeglonLabs | 106 |
| kubeflow | 94 |
| AustinCStone | 86 |
| wasita | 60 |
| migalkin | 60 |
| zubyul | 48 |
| kristinezheng | 36 |
| M1shaaa | 32 |
| DJedamski | 22 |

Top repos by stars (prior sweep data):
| Source | Repo | Language | Stars |
|--------|------|----------|-------|
| kubeflow | kubeflow | — | 15572 |
| kubeflow | kubeflow | — | 15565 |
| kubeflow | pipelines | Python | 4119 |
| kubeflow | pipelines | Python | 4119 |
| kubeflow | spark-operator | Python | 3114 |
| kubeflow | spark-operator | Python | 3111 |
| kubeflow | trainer | Go | 2082 |
| kubeflow | trainer | Go | 2080 |
| kubeflow | katib | Python | 1678 |
| kubeflow | katib | Python | 1676 |
