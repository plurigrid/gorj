# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-09  
**GF3 color chain:** ERGODIC #d3869b (id%3=0) · PLUS #b8bb26 (id%3=1) · MINUS #cc241d (id%3=2)

---

## JOB 1: GitHub Social Graph Sweep

### Orgs

| Org | Repos Snapshotted | Most Recent Push | Top Stars |
|-----|-------------------|-----------------|-----------|
| plurigrid | 100 | gorj (2026-07-09, Clojure) | asi (30★), nash-portal (2★), zig-syrup (2★) |
| kubeflow | 49 | pipelines, mpi-operator, trainer (2026-07-09) | kubeflow (15,770★), spark-operator (3,136★), pipelines (4,169★), trainer (2,134★) |
| TeglonLabs | 5 | jank-crane (2026-06-08, C++) | mathpix-gem (2★) |

### Users

| User | Repos | Most Recent | Notes |
|------|-------|-------------|-------|
| bmorphism | 100 | Gay.jl, bci-preview, world | Cross-org with plurigrid/zubyul |
| zubyul | 49 | voice-observatory (2026-04-24, Python) | nash-tui/nash-web (private Rust), Gay.jl (Julia) |

### Zubyul Social Graph

| User | Repos | Notable |
|------|-------|---------|
| migalkin | 19 | NodePiece (144★), StarE (89★), kgcourse2021 (25★) — KG/GNN researcher |
| DJedamski | 6 | Data science / R projects (Coursera era) |
| wasita | 11 | wasita.github.io (updated 2026-07-06), magic-garden Discord bot |
| kristinezheng | 5 | kristinezheng.github.io (updated 2026-07-01), cognitive science |
| M1shaaa | 8 | lab-bookshelf (TypeScript), Yale CS / cognitive science tooling |
| AustinCStone | 40 | TextGAN (92★), StereoVisionMRF (11★), EpsteinSearch (2026-02) |

### GF3 Distribution (this run — 267 new increments)
- ERGODIC #d3869b (trit=0): 96 increments
- PLUS #b8bb26 (trit=1): 97 increments
- MINUS #cc241d (trit=-1): 97 increments — balanced triadic sweep

**Cumulative DB state:** 290 world_increments, 1211 repo_snapshots across all runs

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` on mainnet.  
All 28 accounts exist and responded successfully.

| World | Balance (APT) | | World | Balance (APT) |
|-------|---------------|-|-------|----------------|
| alice | 0.436434 | | N | 0.106121 |
| bob | **12.657007** | | O | 0.210136 |
| A | 0.051767 | | P | 0.140136 |
| B | 0.036256 | | Q | 0.103240 |
| C | 0.010185 | | R | 0.090217 |
| D | 0.011629 | | S | 0.091788 |
| E | 0.009372 | | T | 0.073713 |
| F | **1.960516** | | U | 0.055773 |
| G | 0.000681 | | V | 0.048832 |
| H | 0.001681 | | W | 0.040705 |
| I | 0.000681 | | X | 0.042577 |
| J | **1.895093** | | Y | 0.044449 |
| K | 0.161961 | | Z | 0.024268 |
| L | **1.927269** | | M | 0.112285 |

**Total APT (28 wallets):** 20.344772 APT  
**Richest wallets:** bob (12.657), F (1.961), L (1.927), J (1.895)  
**Note:** Addresses returning "resource not found" for CoinStore use the new fungible asset standard on Aptos — the view function correctly surfaces balances for all.

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...b6d | 2 | ✓ HEALTHY |

All 5 multisig pairs require 2-of-N signatures and are accessible on mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Returns HTTP 401 Vercel authentication. No market data accessible.  
No mnx_snapshots inserted this run.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments     (290 rows cumulative)
├── repo_snapshots       (1211 rows cumulative)
├── aptos_snapshots      (28 rows this run — all live mainnet balances)
├── multisig_probes      (5 rows this run — all 5/5 healthy)
└── mnx_snapshots        (0 rows — source requires auth)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
