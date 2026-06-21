# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-21 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) chain run:** 13 increments, colors cycling PLUS→MINUS→ERGODIC

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| ID | GF3 | Color | Source | Type | Repos |
|----|-----|-------|--------|------|-------|
| 1 | PLUS | `#b8bb26` | plurigrid | org | 100 |
| 2 | MINUS | `#cc241d` | kubeflow | org | 48 |
| 3 | ERGODIC | `#d3869b` | TeglonLabs | org | 5 |
| 4 | PLUS | `#b8bb26` | bmorphism | user | 100 |
| 5 | MINUS | `#cc241d` | zubyul | user | 49 |
| 6 | ERGODIC | `#d3869b` | migalkin | user | 19 |
| 7 | PLUS | `#b8bb26` | DJedamski | user | 6 |
| 8 | MINUS | `#cc241d` | wasita | user | 11 |
| 9 | ERGODIC | `#d3869b` | kristinezheng | user | 5 |
| 10 | PLUS | `#b8bb26` | M1shaaa | user | 8 |
| 11 | MINUS | `#cc241d` | AustinCStone | user | 40 |
| 12 | ERGODIC | `#d3869b` | hamming_swarm | aptos | 28 wallets |
| 13 | PLUS | `#b8bb26` | multisig | aptos | 5 contracts |

**Total repos snapshotted:** 391  
**GF(3) chain:** `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Most Recently Pushed (top 10)

| Org/User | Repo | Pushed At |
|----------|------|-----------|
| plurigrid | gorj | 2026-06-21T21:12:44Z |
| M1shaaa | M1shaaa | 2026-06-21T14:01:52Z |
| kubeflow | dashboard | 2026-06-21T00:56:24Z |
| bmorphism | Gay.jl | 2026-06-21T00:43:51Z |
| kubeflow | katib | 2026-06-20T23:29:45Z |
| kubeflow | pipelines | 2026-06-20T19:12:02Z |
| kubeflow | notebooks | 2026-06-20T17:12:47Z |
| kubeflow | hub | 2026-06-20T15:40:26Z |
| bmorphism | satreadout | 2026-06-20T13:05:41Z |
| kubeflow | kale | 2026-06-20T11:20:36Z |

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,739 | 2,680 |
| kubeflow/pipelines | Python | 4,156 | 2,009 |
| kubeflow/spark-operator | Python | 3,127 | 1,490 |
| kubeflow/trainer | Go | 2,118 | 970 |
| kubeflow/katib | Python | 1,684 | 528 |
| kubeflow/examples | Jsonnet | 1,460 | 756 |
| kubeflow/community-distribution | YAML | 1,026 | 1,065 |
| migalkin/NodePiece | Python | 144 | 21 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 |

### Notable Activity
- **plurigrid/gorj** (this repo) most recently pushed — active today at 21:12 UTC
- **bmorphism/Gay.jl** pushed 2026-06-21 — active Julia project
- **M1shaaa** profile README updated today (14:01 UTC)
- **TeglonLabs/jank-crane** — C++ GF3 convergence maps project, pushed 2026-06-08
- **kubeflow star delta:** 15,739 (up from 15,565 on 2026-04-12)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-21)

Queried via `0x1::coin::balance` view function. All 28 accounts exist on-chain.

| World | Balance (APT) | Address |
|-------|--------------|---------|
| **bob** | **12.6570** | `0x0a3c00c5...d5d` |
| **F** | **1.9605** | `0x18a14b5b...f71` |
| **L** | **1.9273** | `0x7c2eaeaf...ba9` |
| **J** | **1.8951** | `0x4d964db8...f54` |
| alice | 0.4364 | `0xc793acde...c7b` |
| O | 0.2101 | `0x73252b60...89d` |
| K | 0.1620 | `0xa732040a...dc4` |
| P | 0.1401 | `0x62187920...948` |
| M | 0.1123 | `0x6fed37a7...2e9` |
| N | 0.1061 | `0xe7dde6da...b2c` |
| Q | 0.1032 | `0xac40fa50...9a9` |
| S | 0.0918 | `0xb8753014...386` |
| R | 0.0902 | `0x7ce605cc...e10` |
| T | 0.0737 | `0x35781dc0...588` |
| U | 0.0558 | `0x75860da4...956` |
| A | 0.0518 | `0x8699edc0...97a` |
| V | 0.0488 | `0xb59dd817...2c3` |
| X | 0.0426 | `0xa95cbbd1...47d` |
| Y | 0.0444 | `0xd8e32848...4c4` |
| W | 0.0407 | `0x5f32aef7...b0` |
| B | 0.0363 | `0x3f892ebe...b13` |
| Z | 0.0243 | `0x7af0ef6e...97c` |
| C | 0.0102 | `0x38b99e63...35e` |
| D | 0.0116 | `0xf7765624...dd1` |
| E | 0.0094 | `0xdc1d9d53...d36` |
| H | 0.0017 | `0xce67c327...00f` |
| G | 0.0007 | `0x69a394c0...f32` |
| I | 0.0007 | `0x070fe5d7...fc9` |

**Total swarm APT: ~22.48 APT**

**Notable:** alice (`0xc793...`) is an active DeFi participant — on-chain resources include `multiverse::MultiverseState`, `lending_pool::UserPosition`, and `address_book::Mapping`. bob holds the most APT in the swarm (12.66 APT).

### Multisig Probes (Aptos Mainnet)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428...003` | 2 | ✅ healthy |
| A-G | `0xf56c4a1c...096` | 2 | ✅ healthy |
| Y-Z | `0xd3ffe181...883` | 2 | ✅ healthy |
| S-T | `0x3b1c3ae9...883` | 2 | ✅ healthy |
| V-W | `0x40fad7b4...b6d` | 2 | ✅ healthy |

All multisig accounts are 2-of-N threshold, all responding healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication for all endpoints. No market data obtainable without credentials. `mnx_snapshots` table empty this run.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 13 | GF(3) color-chained sweep events |
| `repo_snapshots` | 391 | Full repo metadata across 11 sources |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig threshold verification |
| `mnx_snapshots` | 0 | MNX markets (unavailable this run) |

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

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-06-21*
