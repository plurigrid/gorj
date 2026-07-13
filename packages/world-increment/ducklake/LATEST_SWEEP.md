# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-13

## Sweep Metadata
- **Date:** 2026-07-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-07-13`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments | 11 |
| New Repo Snapshots | 67 (representative sample) |
| Orgs Covered | 3 (plurigrid, kubeflow, TeglonLabs) |
| Users Covered | 8 (bmorphism, zubyul + 6 social graph) |

### GF(3) Color Chain — All 11 New Increments

| ID | Source | Type | Repos (total) | GF3 Trit | Color | Name |
|----|--------|------|--------------|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 105 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 11 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 40 | -1 | `#cc241d` | **MINUS** |

### Notable Repos (by stars)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,774 | — | 2026-07-13 |
| kubeflow/pipelines | 4,165 | Python | 2026-07-13 |
| kubeflow/spark-operator | 3,135 | Python | 2026-07-13 |
| kubeflow/trainer | 2,138 | Go | 2026-07-13 |
| kubeflow/katib | 1,690 | Python | 2026-07-11 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 30 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |

### Hot Activity (pushed today 2026-07-13)
- `plurigrid/gorj` — 1156 open issues, active nREPL/GF(3) dev
- `kubeflow/trainer`, `kubeflow/kubeflow`, `kubeflow/hub` — active CI/release work
- `kubeflow/spark-operator` — continued Kubernetes operator work

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Hamming Universe A-Z + alice/bob)

All 28 addresses probed against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...b7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All balances returned 0.0 APT — accounts either uninitialized, or the `CoinStore<AptosCoin>` resource has not been registered on these addresses yet.

### Multisig Contract Probes

All 5 multisig accounts probed for `num_signatures_required` via Aptos `/v1/view`.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...003 | **2** | ✅ HEALTHY |
| A-G | 0xf56c...096 | **2** | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | **2** | ✅ HEALTHY |
| S-T | 0x3b1c...883 | **2** | ✅ HEALTHY |
| V-W | 0x40fa...b6d | **2** | ✅ HEALTHY |

All multisig contracts report 2-of-N threshold. All **healthy**.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication (deployment protection). Neither public API paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) nor the root SPA returned accessible market data. No snapshot recorded.

---

## GF(3) Trit Conservation Check

| Color | Count | Trit Sum |
|-------|-------|----------|
| PLUS (#b8bb26) | 4 | +4 |
| MINUS (#cc241d) | 4 | -4 |
| ERGODIC (#d3869b) | 3 | 0 |
| **Net** | 11 | **0** ✅ |

Trit conservation: PLUS and MINUS balanced at ±4, ERGODIC = 3. Net = 0 (conserved mod 3).

---

## Database State

```
world_increments: 23 total (11 new today)
repo_snapshots:   67+ rows (new today)
aptos_snapshots:  28 rows (all 0.0 APT)
multisig_probes:  5 rows (all healthy, sigs=2)
mnx_snapshots:    0 rows (unavailable)
```
