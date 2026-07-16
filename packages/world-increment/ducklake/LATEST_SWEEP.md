# World-Increment Sweep — 2026-07-16

## Sweep Metadata
- **Date:** 2026-07-16
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 24 (this sweep)
- **GF(3):** trit=0 · `#d3869b` · **ERGODIC** (24 mod 3 = 0)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| Total Repo Snapshots (cumulative) | 1,256 |
| Repos this sweep | ~313 |
| Sources Covered | 3 orgs + 8 users (social graph) |
| Aptos addresses probed | 28 |
| Multisig contracts probed | 5 |
| MNX market data | Unavailable (401) |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph (zubyul) | 19 |
| DJedamski | social graph (zubyul) | 6 |
| wasita | social graph (zubyul) | 11 |
| kristinezheng | social graph (zubyul) | 5 |
| M1shaaa | social graph (zubyul) | 8 |
| AustinCStone | social graph (zubyul) | 30+ |

### Recently Active (≤ 48h from 2026-07-16)

- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15
- **kubeflow/pipelines**, **spark-operator**, **trainer** (Python/Go) — pushed 2026-07-15
- **wasita/wasita.github.io**, **wasita/wm-cv** (Svelte) — pushed 2026-07-14
- **TeglonLabs/jank-crane** (C++) — GF3 convergence maps, pushed 2026-06-08

### Top Repos by Stars (cumulative top 10)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,778 | — | 2026-07-10 |
| kubeflow/pipelines | 4,167 | Python | 2026-07-15 |
| kubeflow/spark-operator | 3,136 | Python | 2026-07-15 |
| kubeflow/trainer | 2,150 | Go | 2026-07-15 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| migalkin/kgcourse2021 | 24 | HTML | 2026-07-10 |
| migalkin/NBFNet_mlx | 10 | Python | 2026-03-11 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2026-04-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z = 28 addresses)

**Status: All 28 returned HTTP 404** — APT CoinStore resource not initialized.  
Wallets are unfunded or accounts not registered on mainnet.  
All 28 records inserted with `balance_apt = NULL`.

### Multisig Contract Probes

**All 5 contracts responding — 2-of-2 threshold on all.**

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: HTTP 401 Unauthorized** on all probed endpoints.  
API requires authentication — `mnx_snapshots` table has 0 rows.

---

## GF(3) Color Chain — Increment 24

---

- Increment 24 mod 3 = 0 → **trit=0, color=#d3869b, ERGODIC**
- Closes the 8th full GF(3) cycle (increments 1–24)
- Chain tail: `…PLUS(22) → MINUS(23) → ERGODIC(24)`

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
