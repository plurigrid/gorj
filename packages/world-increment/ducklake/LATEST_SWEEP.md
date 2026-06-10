# World Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-10  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos (this run) |
|--------|------|---------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| AustinCStone | user | 40 |
| **TOTAL** | | **391 new repos** |

### DuckDB Totals (cumulative, all sweeps)

| Table | Rows |
|-------|------|
| repo_snapshots | 1337 |
| world_increments | 416 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

### GF(3) Color Chain

- `trit=0` → **ERGODIC** `#d3869b` (dusty rose)
- `trit=1` → **PLUS** `#b8bb26` (olive green)
- `trit=-1` → **MINUS** `#cc241d` (red)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (FA primary store)

All 28 addresses queried via `0x1::primary_fungible_store::balance` view function.

| World | APT Balance |
|-------|-------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| I | 0.000681 |
| G | 0.000681 |

**Total swarm APT: ~22.03 APT**

> Note: Addresses use the newer Aptos fungible asset standard; no old `CoinStore` resources found. Balances fetched via `primary_fungible_store::balance` with APT metadata `0x000...000a`.

### Multisig Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig contracts require 2-of-N signatures. All healthy.

### MNX Markets

`testnet.mnx.fi` — **Unavailable** (requires Vercel authentication). No market data extractable without auth token.

---

## Notable Observations

- **alice** address (`0xc793...`) has custom resources: `store_v2::ACSetMeta2`, `address_book::Mapping`, `multiverse::MultiverseState`, `lending_pool::UserPosition` — active on-chain program
- **bob** holds the largest balance at 12.66 APT
- **plurigrid** org is most active: 100 repos, multiple pushing to 2026-06-10
- **M1shaaa** profile pushed today (2026-06-10T03:24:43Z) — active
- **TeglonLabs/jank-crane** focuses on "GF3 convergence maps" — directly related to this sweep's GF(3) color chain
