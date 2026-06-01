# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-01T00:00:00Z  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Captured | Total Stars |
|--------|------|----------------|-------------|
| kubeflow | org | 48 | 34,166 |
| migalkin | user (social) | 19 | 280 |
| bmorphism | user | 100 | 247 |
| AustinCStone | user (social) | 30 | 108 |
| plurigrid | org | 100 | 75 |
| zubyul | user | 49 | 14 |
| wasita | user (social) | 11 | 5 |
| DJedamski | user (social) | 6 | 3 |
| TeglonLabs | org | 4 | 2 |
| kristinezheng | user (social) | 6 | 0 |
| M1shaaa | user (social) | 8 | 0 |
| **TOTAL** | | **381** | **34,900** |

### Top 15 Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,700 | — | 2026-05-24 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-01 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,109 | Go | 2026-05-30 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,019 | YAML | 2026-05-29 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| kubeflow/kale | 691 | Python | 2026-06-01 |
| kubeflow/mpi-operator | 528 | Go | 2026-05-29 |
| kubeflow/fairing | 337 | Jsonnet | 2022-04-11 |
| kubeflow/pytorch-operator | 310 | Jsonnet | 2021-12-01 |
| kubeflow/community | 195 | Jupyter Notebook | 2026-06-01 |
| kubeflow/website | 184 | HTML | 2026-05-28 |
| kubeflow/kfctl | 182 | Go | 2023-08-15 |

### TeglonLabs Repos (org)

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| mathpix-gem | Ruby | 2 | Transform mathematical images to LaTeX; security-first design |
| coin-flip-mcp | JavaScript | 0 | MCP server for coin flipping via random.org |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | — |

### DuckDB Schema

```
world_increments  — 381 rows (GF3-tagged repo push events)
repo_snapshots    — 381 rows (full repo metadata)
aptos_snapshots   — 28 rows  (hamming swarm wallet balances)
multisig_probes   — 5 rows   (multisig contract health)
mnx_snapshots     — 1 row    (MNX testnet, unavailable)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 hamming-swarm wallets (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets return 0 APT.** The CoinStore resource was not found for any address on Aptos mainnet, indicating these are unfunded / uninitialized accounts.

| Wallet | Address (prefix) | Balance (APT) |
|--------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Health

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

**All 5 multisig contracts healthy — each requires 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a Next.js SPA. All API paths (`/api/markets`, `/api/v1/markets`) return the SPA HTML shell — no REST market data is exposed client-side. **MNX snapshot: unavailable.**

---

## DuckDB Location

```
packages/world-increment/ducklake/world-increments.duckdb
```

Query example:
```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 color distribution
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY gf3_name, gf3_color;

-- Aptos swarm summary
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;
```
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

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
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
