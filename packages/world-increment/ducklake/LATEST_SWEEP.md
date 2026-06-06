# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 371 |
| Total Repo Snapshots | 371 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos Wallets Probed | 28 |
| Total APT Swarm Balance | 20.344773 APT |
| Multisig Contracts Probed | 5 (all healthy, 2-of-N) |
| MNX Markets | unavailable (Vercel auth) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-06-06)

> Queried via `0x1::coin::balance` view (FA-compatible). Legacy `CoinStore` absent on all accounts.

| World | APT Balance | Address (prefix) |
|-------|-------------|-----------------|
| bob | **12.657007** | 0x0a3c… |
| F | 1.960516 | 0x18a1… |
| L | 1.927269 | 0x7c2e… |
| J | 1.895093 | 0x4d96… |
| alice | 0.436434 | 0xc793… |
| O | 0.210136 | 0x7325… |
| K | 0.161961 | 0xa732… |
| P | 0.140136 | 0x6218… |
| M | 0.112285 | 0x6fed… |
| N | 0.106121 | 0xe7dd… |
| Q | 0.103240 | 0xac40… |
| S | 0.091788 | 0xb875… |
| R | 0.090217 | 0x7ce6… |
| T | 0.073713 | 0x3578… |
| U | 0.055773 | 0x7586… |
| A | 0.051767 | 0x8699… |
| V | 0.048833 | 0xb59d… |
| Y | 0.044449 | 0xd8e3… |
| W | 0.040705 | 0x5f32… |
| X | 0.042577 | 0xa95c… |
| B | 0.036256 | 0x3f89… |
| Z | 0.024268 | 0x7af0… |
| D | 0.011629 | 0xf776… |
| C | 0.010185 | 0x38b9… |
| E | 0.009372 | 0xdc1d… |
| H | 0.001681 | 0xce67… |
| G | 0.000681 | 0x69a3… |
| I | 0.000681 | 0x070f… |

**Total swarm: 20.344773 APT**

### Multisig Contract Probes

All 5 contracts healthy — all return `num_signatures_required = 2`.

| Pair | Contract Address (prefix) | Sigs | Healthy |
|------|--------------------------|------|---------|
| A-B | 0x0da4… | 2 | ✓ |
| A-G | 0xf56c… | 2 | ✓ |
| Y-Z | 0xd3ff… | 2 | ✓ |
| S-T | 0x3b1c… | 2 | ✓ |
| V-W | 0x40fa… | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` — behind **Vercel deployment protection** (visitor password required). No market data retrievable without bypass token. `mnx_snapshots` table left empty.

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
| zubyul | user | 49 |
| kubeflow | org | 48 |
| AustinCStone | user (social) | 30 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 11 |
| TeglonLabs | org | 4 |
| M1shaaa | user (social) | 4 |
| kristinezheng | user (social) | 3 |
| DJedamski | user (social) | 3 |
| **TOTAL** | | **371** |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
