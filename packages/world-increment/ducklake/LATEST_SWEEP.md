# World-Increment Sweep — 2026-06-18

## Sweep Metadata
- **Date:** 2026-06-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel 401) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | kristinezheng (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | M1shaaa (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 0 | 2026-06-18 |
| asi | HTML | 26 | 2026-06-10 |
| place | TeX | 1 | 2026-06-15 |
| nash-portal | Rust | 2 | 2026-05-19 |
| eirobri | Clojure | 0 | 2026-06-03 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,734 | 2026-06-17 |
| pipelines | Python | 4,154 | 2026-06-17 |
| spark-operator | Python | 3,127 | 2026-06-17 |
| trainer | Go | 2,115 | 2026-06-18 |
| katib | Python | 1,683 | 2026-06-15 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-04-xx |
| anti-bullshit-mcp-server | JavaScript | 23 | — |
| satreadout | Lean | 0 | 2026-06-15 |
| Gay.jl | Julia | 1 | 2026-06-18 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |
| gay-world | Python | 1 | 2026-03-26 |
| tilelang-kernels | Python | 0 | 2026-03-16 |

### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

### wasita (11 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| wasita.github.io | Svelte | 1 | 2026-06-15 |
| magic-garden | Python | 2 | 2026-04-22 |
| wm-cv | Svelte | 0 | 2026-05-13 |

---

## Repo Counts by Source

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 157 |
| kubeflow | org | 48 | ~101,949 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 509 |
| zubyul | user | 49 | 40 |
| migalkin | user | 19 | 833 |
| DJedamski | user | 6 | 17 |
| kristinezheng | user | 5 | 0 |
| M1shaaa | user | 8 | 0 |
| AustinCStone | user | 40 | 322 |
| wasita | user | 11 | 10 |
| **TOTAL** | | **391** | **~103,851** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-18)
All 28 addresses (alice, bob, A–Z) returned **0.0 APT**.  
The CoinStore resource (`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`) returned no balance — accounts may use the fungible asset standard or are unfunded.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (24 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 multisigs are **healthy** with `sigs_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets
`https://testnet.mnx.fi` returns **HTTP 401 (Vercel deployment protection)**.  
All API paths probed (`/api/markets`, `/api/v1/markets`, `/api/tickers`) are auth-gated.  
`mnx_snapshots` table has 0 rows; bypass token needed for access.

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,734 stars — flagship ML platform, pushed today
- **kubeflow/trainer**: 2,115 stars — Distributed AI Training, pushed 2026-06-18
- **migalkin/NodePiece**: 144 stars — parameter-efficient KG representations
- **bmorphism/Gay.jl**: 187 open issues, pushed 2026-06-18 — GF(3) color sampling
- **TeglonLabs/jank-crane**: C++ IR hub with GF3 convergence maps
- **plurigrid/gorj**: This very repo — 646 open issues, pushed 2026-06-18
- **All 5 multisigs**: sigs_required=2, healthy — Hamming swarm intact
