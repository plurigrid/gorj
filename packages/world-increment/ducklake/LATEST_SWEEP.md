# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 34 |
| Total Repo Snapshots (cumulative) | 986 |
| Sources Covered This Run | 3 orgs + 8 users |

---

### GF(3) Color Chain — This Run's Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 24 | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 25 | kubeflow | org | 1 | `#b8bb26` | **PLUS** |
| 26 | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 27 | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 28 | zubyul | user | 1 | `#b8bb26` | **PLUS** |
| 29 | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 30 | wasita | user | 0 | `#d3869b` | **ERGODIC** |
| 31 | DJedamski | user | 1 | `#b8bb26` | **PLUS** |
| 32 | kristinezheng | user | -1 | `#cc241d` | **MINUS** |
| 33 | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 34 | AustinCStone | user | 1 | `#b8bb26` | **PLUS** |

---

### Top Repos by Source (2026-07-20 snapshot)

#### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-20 |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-14 |
| shrimp | — | 0 | 2026-07-03 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,783 | 2026-07-10 |
| pipelines | Python | 4,169 | 2026-07-19 |
| spark-operator | Python | 3,140 | 2026-07-17 |
| trainer | Go | 2,152 | 2026-07-19 |
| katib | Python | 1,691 | 2026-07-16 |
| hub | Go | 178 | 2026-07-20 |
| mcp-apache-spark-history-server | Python | 183 | 2026-07-16 |
| mcp-server | Python | 28 | 2026-07-19 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| jank-crane | C++ | 0 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

#### bmorphism (100 repos, top 5)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-14 |
| gay-chat | Scheme | 0 | 2026-07-14 |
| satreadout | HTML | 0 | 2026-06-20 |
| bci-preview | HTML | 0 | 2026-06-20 |
| world | Python | 0 | 2026-06-02 |

#### zubyul (49 repos, top 3)
| Repo | Language | Pushed At |
|------|----------|-----------|
| voice-observatory | Python | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 2026-04-24 |
| nash-tui | Rust | 2026-04-13 |

#### Social graph (migalkin / wasita / DJedamski / kristinezheng / M1shaaa / AustinCStone)
| User | Top Repo | Stars |
|------|----------|-------|
| migalkin | NodePiece | 144 |
| migalkin | StarE | 89 |
| AustinCStone | TextGAN | 92 |
| AustinCStone | byteruckus | 0 (pushed 2026-07-15) |
| wasita | wasita.github.io | 1 (pushed 2026-07-16) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice + A–Z, 28 addresses)

**Result:** All 28 addresses returned HTTP 404 from Aptos mainnet.  
No `0x1::coin::CoinStore<AptosCoin>` resource found → wallets unfunded on mainnet (balance = 0.0 APT).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 (404) |
| bob | 0x0a3c00... | 0.0 (404) |
| A | 0x8699ed... | 0.0 (404) |
| B–Z | (see DB) | 0.0 (404 each) |

### Multisig Contract Probes — 5/5 Healthy ✓

All 5 multisig accounts on Aptos mainnet are healthy, all require **2-of-N signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** HTTP 401 Unauthorized — all probed API paths require authentication.  
Paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/markets`.  
No market data inserted into `mnx_snapshots`.

---

## DuckDB State

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 34 |
| repo_snapshots | 986 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (auth blocked) |

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

## Notable Highlights (2026-07-20)
- **kubeflow/kubeflow**: 15,783★ — flagship ML toolkit for Kubernetes
- **kubeflow/hub** pushed 2026-07-20 — model registry actively developed
- **plurigrid/gorj** pushed 2026-07-20 — 1,269 open issues; active
- **migalkin/NodePiece**: 144★ — compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92★ — text GAN in TensorFlow
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut color sampling actively tracked
- **Multisig**: All 5 Hamming-swarm pairs healthy, 2-sig threshold confirmed
- **Aptos wallets**: All 28 unfunded on mainnet (404)
- **MNX testnet**: Auth-gated, no public API access
