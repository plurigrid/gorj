# World-Increment Sweep — 2026-07-15

**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 (103 total) |
| kubeflow | org | 29 active |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 (106 total) |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 41 |

### Notable Activity (pushed ≤ 24h as of 2026-07-15)
- **plurigrid/gorj** — Clojure, 1185 open issues, pushed today (active forj development)
- **plurigrid/eirobri** — EiRoBri replay world, pushed yesterday
- **plurigrid/place** — TeX, pushed yesterday
- **bmorphism/gay-chat** — gay://chat over Spritely Brassica, pushed yesterday
- **bmorphism/Gay.jl** — Julia, 187 open issues, pushed yesterday
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, pushed 2026-07-12
- **kubeflow/spark-operator** — 3136 stars, pushed today
- **kubeflow/pipelines** — 4167 stars, pushed today
- **wasita/wasita.github.io** — Svelte personal site, pushed yesterday
- **AustinCStone/byteruckus** — new repo, pushed today

### Top Repos by Stars (this sweep)
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15778 | — |
| kubeflow/pipelines | 4167 | Python |
| kubeflow/spark-operator | 3136 | Python |
| kubeflow/trainer | 2149 | Go |
| kubeflow/katib | 1690 | Python |
| kubeflow/examples | 1460 | Jsonnet |
| kubeflow/community-distribution | 1029 | YAML |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### Star Growth Since Last Sweep (2026-04-12 → 2026-07-15)
| Repo | Previous Stars | Current Stars | Delta |
|------|----------------|---------------|-------|
| kubeflow/kubeflow | 15565 | 15778 | +213 |
| kubeflow/pipelines | 4119 | 4167 | +48 |
| kubeflow/spark-operator | 3111 | 3136 | +25 |
| kubeflow/trainer | 2080 | 2149 | +69 |
| bmorphism/anti-bullshit-mcp-server | ~23 | 22 | ≈0 |

### DuckDB Tables
- **world_increments** — 81 total rows (GF3-colored, cumulative)
- **repo_snapshots** — 1002 total rows (cumulative across sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (APT mainnet, 2026-07-15)
All 28 swarm addresses (alice, bob, A–Z) returned **0.0 APT** from the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource. Accounts exist on-chain but CoinStore not registered or balance is zero.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–Z (26 wallets) | various | 0.0 each |

**Total swarm APT balance: 0.0 APT**

### Multisig Contract Probes — ALL HEALTHY ✓
All 5 probed multisig accounts returned **2 signatures required**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `https://testnet.mnx.fi` returns a Vercel authentication gate. No `/api/markets` or `/api/v1/markets` endpoint accessible without Vercel auth token. `mnx_snapshots` table: 0 rows.

---

## Database Summary
```
world-increments.duckdb
├── world_increments:  81 rows (GF3-colored increments, cumulative)
├── repo_snapshots:  1002 rows (cumulative GitHub snapshots)
├── aptos_snapshots:  28 rows (alice, bob, A–Z — all 0.0 APT)
├── multisig_probes:   5 rows (all healthy, 2-of-N each)
└── mnx_snapshots:     0 rows (auth-gated, unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```
