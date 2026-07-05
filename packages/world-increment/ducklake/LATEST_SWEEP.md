# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (cumulative) |
| Total Repo Snapshots | 1265 (cumulative) |
| Sources Covered | 3 orgs + 8 users + 6 social-graph users |
| Aptos wallets snapshotted | 28 |
| Multisig contracts probed | 5 (all healthy) |
| MNX markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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
- **kubeflow/kubeflow**: 15,762 stars — flagship ML platform for Kubernetes (pushed 2026-06-18)
- **kubeflow/pipelines**: 4,169 stars — most popular ML pipeline for Kubernetes (pushed 2026-07-05)
- **kubeflow/spark-operator**: 3,132 stars — Kubernetes operator for Apache Spark (pushed 2026-07-02)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings, ICLR'22
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **TeglonLabs/jank-crane**: New C++ GF3 convergence maps repo (pushed 2026-06-08)
- **wasita/wasita.github.io**: Active Svelte personal site (pushed 2026-07-05, today)

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances
| World | APT Balance | Address |
|-------|------------|---------|
| bob | **12.65700700** | `0x0a3c00c5…5d` |
| F | **1.96051600** | `0x18a14b5b…71` |
| L | **1.92726900** | `0x7c2eaeaf…a9` |
| J | **1.89509300** | `0x4d964db8…54` |
| alice | 0.43643352 | `0xc793acde…7b` |
| O | 0.21013600 | `0x73252b60…9d` |
| K | 0.16196100 | `0xa732040a…c4` |
| P | 0.14013600 | `0x62187920…48` |
| M | 0.11228500 | `0x6fed37a7…e9` |
| N | 0.10612100 | `0xe7dde6da…2c` |
| Q | 0.10324000 | `0xac40fa50…a9` |
| S | 0.09178800 | `0xb8753014…86` |
| R | 0.09021700 | `0x7ce605cc…10` |
| T | 0.07371300 | `0x35781dc0…88` |
| U | 0.05577300 | `0x75860da4…56` |
| A | 0.05176700 | `0x8699edc0…7a` |
| V | 0.04883299 | `0xb59dd817…c3` |
| Y | 0.04444900 | `0xd8e32848…c4` |
| X | 0.04257700 | `0xa95cbbd1…7d` |
| W | 0.04070500 | `0x5f32aef7…b0` |
| B | 0.03625600 | `0x3f892ebe…13` |
| Z | 0.02426800 | `0x7af0ef6e…7c` |
| D | 0.01162900 | `0xf7765624…d1` |
| C | 0.01018500 | `0x38b99e63…5e` |
| E | 0.00937200 | `0xdc1d9d53…36` |
| H | 0.00168100 | `0xce67c327…0f` |
| I | 0.00068100 | `0x070fe5d7…c9` |
| G | 0.00068100 | `0x69a394c0…32` |

**Total swarm balance:** ~21.49 APT  
**Method:** `0x1::coin::balance` view function (FA migration: CoinStore not present, coin::balance works)

### Multisig Contract Probes
| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428…03` | 2 | ✅ HEALTHY |
| A-G | `0xf56c4a1c…96` | 2 | ✅ HEALTHY |
| Y-Z | `0xd3ffe181…83` | 2 | ✅ HEALTHY |
| S-T | `0x3b1c3ae9…83` | 2 | ✅ HEALTHY |
| V-W | `0x40fad7b4…6d` | 2 | ✅ HEALTHY |

All 5 multisig contracts healthy with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel authentication required (HTTP 401). SPA requires login; no public API endpoint accessible.
