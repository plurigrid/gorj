# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (cumulative) |
| Total Repo Snapshots | 1267 (cumulative) |
| Sources Covered | 3 orgs + 8 users (this run: 389 new repos) |
| Aptos Wallets Probed | 28 (alice–Z) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Run (increments 1–11)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source (2026-07-05)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 28 | 2026-06-29 |
| nash-portal | Rust | 2 | 2026-05-19 |
| place | TeX | 1 | 2026-06-29 |
| shrimp | — | 0 | 2026-07-03 |
| eirobri | Clojure | 0 | 2026-06-30 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4169 | 2026-07-05 |
| hub | Go | 175 | 2026-07-04 |
| website | HTML | 184 | 2026-07-03 |
| dashboard | TypeScript | 16 | 2026-07-05 |
| internal-acls | Go | 19 | 2026-07-03 |

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
| Gay.jl | Julia | 2 | 2026-07-05 |
| satreadout | HTML | 0 | 2026-06-20 |
| world | Python | 0 | 2026-06-02 |
| oxgame | OCaml | 0 | 2026-05-15 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| RWL | Python | 8 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (this run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 4 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **389** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 addresses)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger ~6115437350. No APT coin stores initialized — these are likely contract/multisig/unfunded accounts.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...c7b | NULL |
| bob   | 0x0a3c...d5d | NULL |
| A–Z   | 26 addresses | NULL (all) |

### Multisig Contract Probes

All 5 contracts **HEALTHY** — `num_signatures_required` = 2.

| Pair | Contract | Sigs | Status |
|------|----------|------|--------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel authentication required for all endpoints. No market data extractable without credentials.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-07-05)
- **bmorphism/Gay.jl** — Julia, pushed TODAY (2026-07-05), stars: 2
- **wasita/wasita.github.io** — Svelte personal site, pushed TODAY (2026-07-05)
- **kubeflow/pipelines** — 4169 stars, pushed TODAY; **kubeflow/dashboard** also active today
- **plurigrid/asi** — HTML, 28 stars (up from 16 in April sweep), pushed 2026-06-29
- **migalkin/NodePiece** — 144 stars (ICLR'22 KG paper)
- **AustinCStone/TextGAN** — 92 stars, TF text GAN
- **Hamming swarm health** — All 5 multisig pairs report 2-of-N, no anomalies

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-05*
