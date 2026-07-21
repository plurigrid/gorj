# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 125 |
| Total Repo Snapshots | 125 |
| Sources Covered | 3 orgs + 8 users |
| GF(3) ERGODIC (#d3869b) | 41 |
| GF(3) PLUS (#b8bb26) | 42 |
| GF(3) MINUS (#cc241d) | 42 |

---

## JOB 1: GitHub Social Graph Sweep

### Notable Recent Activity (pushed today 2026-07-21)

- `plurigrid/gorj` — 21:13 UTC (1,306 open issues — this repo)
- `kubeflow/mlflow-integration` — 18:41 UTC
- `kubeflow/dashboard` — 17:02 UTC
- `kubeflow/pipelines` — 16:11 UTC
- `kubeflow/katib` — 16:22 UTC
- `kubeflow/internal-acls` — 13:25 UTC
- `bmorphism/Gay.jl` — 12:55 UTC (187 open issues)
- `wasita/wasita.github.io` — 15:55 UTC

### Repo Counts by Source

| Source | Type | Repos Captured | Notes |
|--------|------|----------------|-------|
| plurigrid | org | 100 (103 total) | gorj has 1,306 open issues; asi 31 ⭐ |
| kubeflow | org | 49 | flagship 15,789 ⭐; pipelines 4,168 ⭐ |
| TeglonLabs | org | 5 | jank-crane (C++, GF3 maps), mathpix-gem (Ruby) |
| bmorphism | user | 100 (106 total) | ocaml-mcp-sdk 61 ⭐; say-mcp-server 20 ⭐ |
| zubyul | user | 49 | from-possible-worlds latest push |
| migalkin | social | 19 | NodePiece 144 ⭐; StarE 89 ⭐ |
| DJedamski | social | 6 | data science / Kaggle |
| wasita | social | 12 | active today, personal site in Svelte |
| kristinezheng | social | 5 | MIT neuro research |
| M1shaaa | social | 8 | Yale CS / Lookit cognitive research |
| AustinCStone | social | 41 | TextGAN 92 ⭐; StereoVisionMRF 11 ⭐ |

### Top Repos by Stars (All Sources)

| Repo | Stars | Forks | Language | Pushed |
|------|-------|-------|----------|--------|
| kubeflow/kubeflow | 15,789 | 2,687 | — | 2026-07-10 |
| kubeflow/pipelines | 4,168 | 2,048 | Python | 2026-07-21 |
| kubeflow/spark-operator | 3,142 | 1,501 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | 992 | Go | 2026-07-20 |
| kubeflow/katib | 1,692 | 533 | Python | 2026-07-21 |
| kubeflow/examples | 1,460 | 756 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | 1,072 | YAML | 2026-07-21 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-03-16 |
| plurigrid/asi | 31 | 10 | HTML | 2026-07-10 |
| bmorphism/risc0-cosmwasm-example | 23 | 2 | Rust | 2022-10-20 |
| bmorphism/anti-bullshit-mcp-server | 22 | 7 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | 9 | JavaScript | 2025-01-07 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet 2026-07-21)

> API: `0x1::coin::balance` view function on `fullnode.mainnet.aptoslabs.com`  
> Note: Accounts use FA model; CoinStore not present, view function returns current balance.

| World | Address (short) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...512d | **12.65700700** |
| A | 0x8699...9d7a | 0.05176700 |
| B | 0x3f89...b13 | 0.03625600 |
| C | 0x38b9...35e | 0.01018500 |
| D | 0xf776...dd1 | 0.01162900 |
| E | 0xdc1d...d36 | 0.00937200 |
| F | 0x18a1...f71 | **1.96051600** |
| G | 0x69a3...f32 | 0.00068100 |
| H | 0xce67...00f | 0.00168100 |
| I | 0x070f...c9 | 0.00068100 |
| J | 0x4d96...f54 | **1.89509300** |
| K | 0xa732...dc4 | 0.16196100 |
| L | 0x7c2e...ba9 | **1.92726900** |
| M | 0x6fed...e9 | 0.11228500 |
| N | 0xe7dd...b2c | 0.10612100 |
| O | 0x7325...89d | 0.21013600 |
| P | 0x6218...948 | 0.14013600 |
| Q | 0xac40...9a9 | 0.10324000 |
| R | 0x7ce6...e10 | 0.09021700 |
| S | 0xb875...386 | 0.09178800 |
| T | 0x3578...588 | 0.07371300 |
| U | 0x7586...956 | 0.05577300 |
| V | 0xb59d...2c3 | 0.04883299 |
| W | 0x5f32...b0 | 0.04070500 |
| X | 0xa95c...47d | 0.04257700 |
| Y | 0xd8e3...4c4 | 0.04444900 |
| Z | 0x7af0...97c | 0.02426800 |

**Total APT across swarm: 20.34477251 APT**  
**bob dominates: 12.657 APT (62.2% of total)**  
**Top 5 (bob, F, L, J, alice): 85.6% of total**

### Multisig Contract Probes

All 5 probed multisig contracts are healthy and require exactly 2 signatures:

| Pair | Contract Address (short) | Sigs Required | Status |
|------|--------------------------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ healthy |
| A-G | 0xf56c...096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✅ healthy |
| S-T | 0x3b1c...883 | 2 | ✅ healthy |
| V-W | 0x40fa...b6d | 2 | ✅ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` returns a mobile-only SPA with no accessible REST API.  
`/api/markets` → HTTP 404. Site displays only a rotation prompt for mobile device.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)   -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row (N/A)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Delta vs Previous Sweep (2026-04-12)

| Metric | 2026-04-12 | 2026-07-21 | Delta |
|--------|-----------|-----------|-------|
| kubeflow/kubeflow stars | 15,565 | 15,789 | +224 |
| kubeflow/pipelines stars | 4,119 | 4,168 | +49 |
| kubeflow/spark-operator stars | 3,111 | 3,142 | +31 |
| kubeflow/trainer stars | 2,080 | 2,152 | +72 |
| migalkin/NodePiece stars | 143 | 144 | +1 |
| bmorphism/ocaml-mcp-sdk stars | 60 | 61 | +1 |
| plurigrid/asi stars | 16 | 31 | +15 |
| Hamming swarm APT total | — | 20.34 APT | new |
| Multisig probes | — | 5/5 healthy | new |
