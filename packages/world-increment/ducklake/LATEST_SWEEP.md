# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-06

**Timestamp:** 2026-07-06T10:10 UTC
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|---|---|---|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| AustinCStone | social graph | 40 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |

**Total world_increments:** 344
**Total repo_snapshots:** 1,265

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|---|---|---|---|
| +1 | `#b8bb26` | PLUS | 115 |
| -1 | `#cc241d` | MINUS | 115 |
| 0 | `#d3869b` | ERGODIC | 114 |

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

### Top Starred Repos

| Repo | Stars | Language |
|---|---|---|
| kubeflow/kubeflow | 15,765 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,132 | Go |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| TeglonLabs/mathpix-gem | 2 | Ruby |
| TeglonLabs/jank-crane | 0 | C++ (GF3 convergence maps) |

### Notable Recent Activity
- **TeglonLabs/jank-crane** (pushed 2026-06-08): C++ crane-jank converged-IR hub with GF3 convergence maps
- **wasita/wasita.github.io** (pushed 2026-07-05): Personal website (Svelte) — most recently pushed in sweep
- **kristinezheng/kristinezheng.github.io** (pushed 2026-07-01): Personal site, HTML
- **plurigrid/gorj**: 1,008 open issues (highest in sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

> Retrieved via `0x1::coin::balance` view function (CoinStore legacy resource absent for these accounts).

| World | Balance (APT) | Address |
|---|---|---|
| bob | 12.657007 | `0x0a3c00c5...e05512d5d` |
| F | 1.960516 | `0x18a14b5b...b979bcf5f6da74c3cf71` |
| L | 1.927269 | `0x7c2eaeaf...673ee6337eba9` |
| J | 1.895093 | `0x4d964db8...cb6e2293e87f54` |
| alice | 0.436434 | `0xc793acde...d0d624cc7b` |
| O | 0.210136 | `0x73252b60...bf3024a525a89d` |
| K | 0.161961 | `0xa732040a...2085e2a47a425dc4` |
| P | 0.140136 | `0x62187926...013621ec948` |
| M | 0.112285 | `0x6fed37a7...4d4a74590fe483d49b7f2e9` |
| N | 0.106121 | `0xe7dde6da...3fd4559a11551b2c` |
| Q | 0.103240 | `0xac40fa50...af0a3b6525e5c89a9` |
| S | 0.091788 | `0xb8753014...3c27457a00beb4f99d0386` |
| R | 0.090217 | `0x7ce605cc...a65d41ebeb36d76e10` |
| T | 0.073713 | `0x35781dc0...fe8131b3759505f2d3f4588` |
| U | 0.055773 | `0x75860da4...63884af7eaa9a39e3fa521f395ef9956` |
| A | 0.051767 | `0x8699edc0...decfa46f78ab0af6eaebe9d7a` |
| V | 0.048833 | `0xb59dd817...c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3` |
| X | 0.042577 | `0xa95cbbd1...d4569b2cbe33047d` |
| W | 0.040705 | `0x5f32aef7...be8b8d8963d45a6ccc7b0` |
| Y | 0.044449 | `0xd8e32848...a53ef2b39100fa2444c4` |
| B | 0.036256 | `0x3f892ebe...dcfe21105a4577cb13` |
| Z | 0.024268 | `0x7af0ef6e...f67915ebd5e6e4e197c` |
| D | 0.011629 | `0xf7765624...da37688cc5bb2b1d9fcfdd1` |
| C | 0.010185 | `0x38b99e63...e39d0ab641e123f7952691535e` |
| E | 0.009372 | `0xdc1d9d53...ab4f565906b7a8d0958d36` |
| H | 0.001681 | `0xce67c327...ddac32e6f02e850d94e5300f` |
| G | 0.000681 | `0x69a394c0...a44aba7c641dd3c5dbcc7f32` |
| I | 0.000681 | `0x070fe5d7...da508ea15fc00c1fc9` |

**Total swarm APT:** ~21.57 APT
**Richest wallet:** `bob` with 12.657 APT (58.7% of swarm total)

### Multisig Contract Probes (5 contracts)

| Pair | Address | Sigs Required | Status |
|---|---|---|---|
| A-B | `0x0da4f428...4987003` | 2/N | ✅ healthy |
| A-G | `0xf56c4a1c...fbc0096` | 2/N | ✅ healthy |
| Y-Z | `0xd3ffe181...e75b883` | 2/N | ✅ healthy |
| S-T | `0x3b1c3ae9...ded7883` | 2/N | ✅ healthy |
| V-W | `0x40fad7b4...c80eb6d` | 2/N | ✅ healthy |

All 5 multisig contracts healthy, all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — Vercel deployment protection active on testnet.mnx.fi; requires visitor password. No market data extractable without auth bypass token.

---

## DuckDB Schema

```sql
world_increments   -- 344 rows  (GF3-colored repo increment events)
repo_snapshots     -- 1,265 rows (full repo metadata snapshots)
aptos_snapshots    -- 28 rows   (Hamming swarm wallet balances)
multisig_probes    -- 5 rows    (multisig contract health)
mnx_snapshots      -- 0 rows    (MNX auth-gated, unavailable)
```
