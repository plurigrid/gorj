# World-Increment Sweep + Hamming Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14 00:11 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (Cumulative)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1262 |
| New This Run | 318 repo snapshots |
| Sources Covered (this run) | 3 orgs + 8 users |

---

## GF(3) Color Chain (this run — increments 24–34)

New increments assigned IDs from sequence, continuing chain. Color by `id % 3`:

| Source | Type | GF3 Trit | Color | Name |
|--------|------|-----------|-------|------|
| plurigrid | org | by id | continues chain | — |
| kubeflow | org | by id | continues chain | — |
| TeglonLabs | org | by id | continues chain | — |
| bmorphism | user | by id | continues chain | — |
| zubyul | user | by id | continues chain | — |
| migalkin | user | by id | continues chain | — |
| wasita | user | by id | continues chain | — |
| kristinezheng | user | by id | continues chain | — |
| M1shaaa | user | by id | continues chain | — |
| AustinCStone | user | by id | continues chain | — |
| DJedamski | user | by id | continues chain | — |

GF(3) rule: `id%3==0 → ERGODIC #d3869b` | `id%3==1 → PLUS #b8bb26` | `id%3==2 → MINUS #cc241d`

---

## Top Repos by Source (2026-07-14 Snapshot)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-13 |
| place | TeX | 1 | 2026-07-07 |
| shrimp | — | 0 | 2026-07-03 |
| eirobri | Clojure | 0 | 2026-06-30 |

### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | (main portal) | — |
| pipelines | Python | 4119+ | recent |
| spark-operator | Python | 3111+ | recent |
| trainer | Go | 2080+ | recent |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 repos, top starred)
| Repo | Language | Stars |
|------|----------|-------|
| satreadout | HTML | 0 |
| Gay.jl | Julia | 2 |
| bci-preview | HTML | 0 |
| world | Python | 0 |
| oxgame | OCaml | 0 |

### migalkin (top starred)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |
| NBFNet_mlx | Python | 10 |
| RWL | Python | 8 |

### AustinCStone (top starred)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

### zubyul (top 3)
- `voice-observatory` [Python], `ghostel-emacs-worlds` [GLSL], `nash-tui` [Rust]

### wasita (top)
- `wasita.github.io` [Svelte] ⭐1 — personal site (pushed 2026-07-06)

---

## Repo Counts by Source (this run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user | 3 |
| migalkin | user | 5 |
| TeglonLabs | org | 5 |
| wasita | user | 2 |
| M1shaaa | user | 2 |
| kristinezheng | user | 1 |
| DJedamski | user | 2 |
| **THIS RUN** | | **318** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses queried at 2026-07-14 00:11 UTC via Aptos fullnode REST API.

**Result: All 28 addresses hold 0.0 APT**

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | `0xc793ac...0d624cc7b` | 0.0 |
| bob | `0x0a3c00...e05512d5d` | 0.0 |
| A | `0x8699ed...aebe9d7a` | 0.0 |
| B | `0x3f892e...4577cb13` | 0.0 |
| C–Z | (all 24 remaining) | 0.0 each |

All CoinStore resources returned empty/zero. Accounts registered but unfunded on mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f4...4987003` | 2 | ✅ healthy |
| A-G | `0xf56c4a...bc0096` | 2 | ✅ healthy |
| Y-Z | `0xd3ffe1...75b883` | 2 | ✅ healthy |
| S-T | `0x3b1c3a...ed7883` | 2 | ✅ healthy |
| V-W | `0x40fad7...80eb6d` | 2 | ✅ healthy |

All 5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active (visitor password required). No market data accessible without credentials.

---

## Database State (2026-07-14)

| Table | Cumulative Rows |
|-------|----------------|
| world_increments | 34 |
| repo_snapshots | 1262 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable Highlights (2026-07-14)
- **plurigrid/asi**: ⭐30 (up from 16 in April) — topological chemputer, most-starred active plurigrid repo
- **plurigrid/gorj**: ⭐1, pushed 2026-07-13 — this very repo, most recently pushed
- **TeglonLabs/jank-crane**: new since April — crane-jank converged-IR hub with GF3 convergence maps
- **migalkin/NodePiece**: ⭐144 (up from 143) — ICLR'22 KG embeddings still gaining stars
- **AustinCStone/TextGAN**: ⭐92 — TF text GAN still attracting interest
- **All 5 multisig contracts**: 2-of-N threshold, all healthy
- **Hamming swarm wallets**: All 28 at 0.0 APT — unfunded on mainnet
