# World-Increment Sweep + Hamming Snapshot

**Date:** 2026-03-29
**Sweep type:** GitHub Social Graph + Aptos Hamming Swarm + Multisig Probes
**DuckDB database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GitHub Repos Snapshot

### Repo Counts per Org/User

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 87 |
| kubeflow | org | 46 |
| TeglonLabs | org | 53 |
| bmorphism | user | 100 |
| zubyul | user | 44 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| wasita | user | 0 (rate-limited) |
| kristinezheng | user | 3 |
| M1shaaa | user | 16 |
| AustinCStone | user | 43 |
| **TOTAL** | | **430+** |

### Top Repos by Stars

| Source | Repo | Stars |
|--------|------|-------|
| kubeflow | kubeflow | 15,540 |
| kubeflow | pipelines | 4,113 |
| migalkin | NodePiece | 143 |
| AustinCStone | TextGAN | 92 |
| migalkin | StarE | 88 |
| bmorphism | ocaml-mcp-sdk | 60 |
| bmorphism | anti-bullshit-mcp-server | 23 |
| migalkin | kgcourse2021 | 25 |
| plurigrid | asi | 13 |
| plurigrid | ontology | 7 |
| TeglonLabs | vibespace | 2 |
| zubyul | WGCNA | 2 |
| DJedamski | kaggle-titanic | 2 |

---

## Aptos Hamming Swarm Balances

All 28 wallets queried against Aptos mainnet fullnode (`https://fullnode.mainnet.aptoslabs.com`).
All balances returned 0.0 APT — wallets are unfunded or CoinStore not initialized on mainnet.

| World | Address (abbreviated) | Balance (APT) |
|-------|----------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (abbreviated) | Sigs Required | Healthy |
|------|----------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All multisig contracts healthy. All require 2-of-N signatures.

---

## MNX Markets

`https://testnet.mnx.fi/api/markets` — **Unavailable**.
The endpoint returns a Next.js SPA HTML shell with no embedded JSON market data.
The application requires client-side JavaScript rendering to load market data.
No market records inserted into `mnx_snapshots`.

---

## GF3 Color Chain Summary

Each world-increment is assigned a GF(3) trit based on `id % 3`:

| id % 3 | Trit | Hex Color | Name |
|--------|------|-----------|------|
| 0 | 0 | `#d3869b` (pink/rose) | ERGODIC |
| 1 | +1 | `#b8bb26` (yellow-green) | PLUS |
| 2 | -1 | `#cc241d` (red) | MINUS |

Distribution across 442 world-increment records:
- ERGODIC (trit=0, id%3==0): ~148 increments
- PLUS (trit=+1, id%3==1): ~148 increments
- MINUS (trit=-1, id%3==2): ~146 increments

The GF(3) chain cycles: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...`
encoding each world-increment in the Galois field of order 3.

---

## DuckDB Database Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 442 |
| repo_snapshots | 470 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no data) |

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)

multisig_probes(timestamp, pair, address, sigs_required, healthy)

mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,540 stars — flagship MLOps orchestration platform
- **kubeflow/pipelines**: 4,113 stars — ML workflow pipelines for Kubernetes
- **migalkin/NodePiece**: 143 stars — anchor-based graph neural network tokenization
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 13 stars — topological chemputer, pushed 2026-03-28
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) trit coloring
