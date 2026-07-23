# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-23

## Sweep Metadata
- **Date:** 2026-07-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments | 68 |
| Repo Snapshots | 68 |
| Sources Covered | 3 orgs + 8 users (11 sources) |
| Aptos Wallets | 28 |
| Multisig Probes | 5 (all healthy) |
| Total APT (swarm) | 20.344773 |
| MNX Markets | SPA-only, no API |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 15 (of 103 total) |
| kubeflow | org | 15 (of 49 total) |
| TeglonLabs | org | 5 (of 5 total) |
| bmorphism | user | 10 (of 106 total) |
| zubyul | user | 10 (of 49 total) |
| migalkin | social graph | 4 |
| wasita | social graph | 3 |
| AustinCStone | social graph | 3 |
| DJedamski | social graph | 1 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 1 |
| **TOTAL** | | **68 repo snapshots** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,788 | — |
| kubeflow/pipelines | 4,169 | Python |
| kubeflow/spark-operator | 3,142 | Python |
| kubeflow/trainer | 2,153 | Go |
| kubeflow/katib | 1,692 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,029 | YAML |
| kubeflow/arena | 815 | Go |
| kubeflow/kale | 695 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/NodePiece | 144 | Python |
| plurigrid/asi | 31 | HTML |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript |

### Most Active Repos (by recency)

- **kubeflow/sdk** — pushed 2026-07-23T00:21 (same day as sweep)
- **plurigrid/gorj** — pushed 2026-07-23T00:14 (this repo — 1,332 open issues)
- **kubeflow/mpi-operator** — pushed 2026-07-22T23:00
- **kubeflow/kale** — pushed 2026-07-22T19:55
- **plurigrid/eirobri** — pushed 2026-07-21T02:24

### GF(3) Color Chain Distribution

| GF(3) Name | Trit | Color | Count |
|------------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 22 |
| PLUS | +1 | `#b8bb26` | 23 |
| MINUS | −1 | `#cc241d` | 23 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version at sweep:** ~6,408,865,909
**Method:** `0x1::coin::balance` view function (FA-compatible)

### Wallet Balances

| World | Address (short) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793...cc7b | 0.436434 |
| **bob** | **0x0a3c...2d5d** | **12.657007** ★ richest |
| A | 0x8699...9d7a | 0.051767 |
| B | 0x3f89...b13 | 0.036256 |
| C | 0x38b9...535e | 0.010185 |
| D | 0xf776...fdd1 | 0.011629 |
| E | 0xdc1d...8d36 | 0.009372 |
| **F** | **0x18a1...cf71** | **1.960516** |
| G | 0x69a3...7f32 | 0.000681 |
| H | 0xce67...300f | 0.001681 |
| I | 0x070f...1fc9 | 0.000681 |
| **J** | **0x4d96...7f54** | **1.895093** |
| K | 0xa732...dc4 | 0.161961 |
| **L** | **0x7c2e...eba9** | **1.927269** |
| M | 0x6fed...f2e9 | 0.112285 |
| N | 0xe7dd...1b2c | 0.106121 |
| O | 0x7325...a89d | 0.210136 |
| P | 0x6218...948 | 0.140136 |
| Q | 0xac40...89a9 | 0.103240 |
| R | 0x7ce6...6e10 | 0.090217 |
| S | 0xb875...386 | 0.091788 |
| T | 0x3578...588 | 0.073713 |
| U | 0x7586...956 | 0.055773 |
| V | 0xb59d...2c3 | 0.048833 |
| W | 0x5f32...7b0 | 0.040705 |
| X | 0xa95c...47d | 0.042577 |
| Y | 0xd8e3...44c4 | 0.044449 |
| Z | 0x7af0...97c | 0.024268 |

**Total APT (28 wallets): 20.344773 APT**
Top 3: bob (12.657), F (1.961), L (1.927)

### Multisig Contract Probes

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (short) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5/5 multisig contracts healthy, all require 2-of-N signatures.**

### MNX Markets (`testnet.mnx.fi`)

Site reachable (Next.js SPA confirmed). No structured JSON API endpoint found at `/api/markets`, `/api/tickers`, or `api.testnet.mnx.fi/markets`. Data requires browser JS execution — recorded as unavailable in mnx_snapshots.

---

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/sdk**: pushed 2026-07-23 00:21 UTC — same hour as this sweep
- **plurigrid/gorj**: 1,332 open issues — most active issue tracker in sweep
- **kubeflow/kubeflow**: 15,788 stars (+223 since April sweep)
- **bmorphism/Gay.jl**: 187 open issues — color/SPI work very active
- **bob wallet**: 12.66 APT — dominates swarm (62% of total)
- **All 5 multisigs**: healthy, 2-of-N threshold consistent across the Hamming swarm
- **TeglonLabs/jank-crane**: new repo since last sweep (GF3 crane-jank + simonw workflow)
