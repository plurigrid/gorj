# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-06

**Generated:** 2026-05-06  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos Captured | Total Stars |
|--------|------|---------------|-------------|
| kubeflow | org | 20 | 32,272 |
| plurigrid | org | 100 | 68 |
| bmorphism | user | 50 | 120 |
| zubyul | user | 49 | 14 |
| migalkin | user | 19 | 278 |
| TeglonLabs | org | 4 | 2 |
| AustinCStone | user | 4 | 103 |
| DJedamski | user | 3 | 0 |
| wasita | user | 4 | 4 |
| kristinezheng | user | 3 | 0 |
| M1shaaa | user | 3 | 0 |
| **Total** | | **259** | **32,861** |

### Notable Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,622 | — | ML Toolkit for Kubernetes |
| kubeflow/pipelines | 4,132 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,123 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,096 | Go | Distributed AI Model Training |
| kubeflow/katib | 1,683 | Python | AutoML on Kubernetes |
| kubeflow/examples | 1,460 | Jsonnet | Extended examples and tutorials |
| kubeflow/manifests | 1,015 | YAML | Deployment Manifests |
| kubeflow/arena | 810 | Go | CLI for Kubeflow |
| kubeflow/kale | 684 | Python | Kubeflow superfood for Data Scientists |
| migalkin/NodePiece | 143 | Python | KG representations (LOG 2022) |
| migalkin/StarE | 89 | Python | EMNLP 2020 hyper-relational KGs |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TF |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for MCP |
| plurigrid/gorj | 0 | Clojure | forj + Rama topology nREPL (this repo) |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 86 |
| +1 | `#b8bb26` | PLUS | 87 |
| -1 | `#cc241d` | MINUS | 86 |

259 world-increments, GF(3) balanced (±1 deviation).

### Recently Active Plurigrid Repos (top 10 by push date)

| Repo | Language | Pushed |
|------|----------|--------|
| gorj | Clojure | 2026-05-06 |
| zig-syrup | Zig | 2026-04-30 |
| horse | TeX | 2026-04-29 |
| asi | HTML | 2026-04-26 |
| nash-portal | Rust | 2026-04-26 |
| asi-skills | Julia | 2026-04-26 |
| bci-blue-share | JavaScript | 2026-04-26 |
| nanoclj-zig | Zig | 2026-04-25 |
| spi-race | Swift | 2026-04-21 |
| reafference | HTML | 2026-04-16 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet at ledger version ~5,155,730,935.

**Result:** `resource_not_found` for all — CoinStore<AptosCoin> not initialized. Hamming swarm addresses are unfunded on mainnet.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793acde… | 0.00 |
| bob | 0x0a3c00c5… | 0.00 |
| A–Z | 0x8699edc0…–0x7af0ef6e… | 0.00 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts healthy. All require **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable as structured data. All routes return Next.js HTML shell — no JSON API accessible. No `mnx_snapshots` rows inserted.

---

## DuckDB Schema Summary

```
world_increments   -- 259 rows  (GF3-colored repo push events)
repo_snapshots     -- 259 rows  (full repo metadata)
aptos_snapshots    --  28 rows  (alice, bob, A-Z balances)
multisig_probes    --   5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots      --   0 rows  (SPA, no API data)
```

### Query Examples

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots
ORDER BY stars DESC LIMIT 10;

-- GF3 color distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments
GROUP BY gf3_name, gf3_color;

-- Healthy multisigs
SELECT pair, sigs_required FROM multisig_probes WHERE healthy = true;

-- Active plurigrid repos
SELECT repo_name, pushed_at FROM repo_snapshots
WHERE org_or_user = 'plurigrid'
ORDER BY pushed_at DESC LIMIT 10;
```

---

## Sweep Metadata
- **Date:** 2026-04-12
- **Agent:** world-increment-sweep
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
