# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-25

## Sweep Metadata
- **Date:** 2026-06-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 11 |
| Total Repo Snapshots (this run) | 315 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |
| MNX Markets | Unavailable (Vercel auth wall) |

---

## GF(3) Color Chain — This Run (11 Increments)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism (user) | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs (org) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (social) | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita (social) | +1 | `#b8bb26` | **PLUS** |
| 8  | AustinCStone (social) | -1 | `#cc241d` | **MINUS** |
| 9  | DJedamski (social) | 0 | `#d3869b` | **ERGODIC** |
| 10 | kristinezheng (social) | +1 | `#b8bb26` | **PLUS** |
| 11 | M1shaaa (social) | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source (2026-06-25 Snapshot)

### kubeflow (48 repos) — most starred
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4157 | 2026-06-24 |
| spark-operator | Python | 3128 | 2026-06-24 |
| trainer | Go | 2080+ | 2026-06-24 |
| community-distribution | YAML | 1028 | 2026-06-25 |

### migalkin (19 repos) — knowledge graphs
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| RWL | Python | 8 | 2026-05-28 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos) — ML/CV
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |
| EpsteinSearch | Python | 0 | 2026-02-11 |

### bmorphism (100 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| Gay.jl | Julia | 2 | 2026-06-25 |
| satreadout | HTML | 0 | 2026-06-20 |

### plurigrid (100 repos) — most active
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| gorj | Clojure | 0 | 2026-06-25 |
| place | TeX | 1 | 2026-06-24 |
| eirobri | Clojure | 0 | 2026-06-23 |
| asi | HTML | 26 | 2026-06-10 |
| nash-portal | Rust | 2 | 2026-05-19 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

---

## Repo Counts by Source (2026-06-25)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | social | 40 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| wasita | social | 11 |
| M1shaaa | social | 8 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses — mainnet)
All queried against `https://fullnode.mainnet.aptoslabs.com`

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z (26) | various | 0.0 each |

> **Note:** All 28 wallets return 0 APT. The `CoinStore<AptosCoin>` resource either returns value=0 or is unfunded on mainnet. No wallet in the swarm currently holds APT.

### Multisig Contract Probes
| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | healthy |
| A-G | 0xf56c4a... | 2 | healthy |
| Y-Z | 0xd3ffe1... | 2 | healthy |
| S-T | 0x3b1c3a... | 2 | healthy |
| V-W | 0x40fad7... | 2 | healthy |

> All 5 multisig contracts are **healthy** with uniform 2-of-N threshold. Probed via `0x1::multisig_account::num_signatures_required`.

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — `testnet.mnx.fi` is a Vercel-deployed SPA protected by a visitor password. No market data accessible without credentials. `mnx_snapshots` table remains empty.

---

## DuckDB Table Counts (cumulative across all runs)

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 1259 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable Highlights (2026-06-25)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,157 stars — pushed 2026-06-24 (active)
- **kubeflow/community-distribution**: pushed 2026-06-25 (most recent)
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/Gay.jl**: Julia, pushed 2026-06-25 — most recently active bmorphism repo
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/gorj**: This very repo — pushed 2026-06-25 (active)
- **plurigrid/asi**: 26 stars — pushed 2026-06-10 (up from 16 in April)
- **TeglonLabs/jank-crane**: new since last sweep — crane-jank converged-IR hub, GF3 convergence maps
- **Hamming swarm**: All 28 Aptos wallets at 0 APT; all 5 multisigs at 2-of-N (healthy)
