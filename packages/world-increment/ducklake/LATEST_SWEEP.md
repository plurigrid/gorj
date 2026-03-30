# World-Increment Sweep + Hamming Snapshot — 2026-03-30

## Sweep Metadata
- **Date:** 2026-03-30
- **Agent:** world-increment-sweep (autonomous two-job sweep)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs and Users Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Total Repos Captured: 360

| Source | Repos |
|--------|-------|
| plurigrid | 92 |
| kubeflow | 46 |
| bmorphism | 97 |
| zubyul | 44 |
| migalkin | 19 |
| TeglonLabs | 3 |
| DJedamski | 6 |
| wasita | 9 |
| kristinezheng | 6 |
| M1shaaa | 8 |
| AustinCStone | 30 |

### Top Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15542 | - | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4112 | Python | Machine Learning Pipelines for Kubeflow |
| kubeflow/spark-operator | 3109 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2069 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1673 | Python | Automated Machine Learning on Kubernetes |
| kubeflow/examples | 1459 | Jsonnet | Extended examples and tutorials |
| kubeflow/manifests | 1005 | YAML | Kubeflow Deployment Manifests |
| kubeflow/arena | 810 | Go | A CLI for Kubeflow |
| kubeflow/kale | 681 | Python | Kubeflow superfood for Data Scientists |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation |
| migalkin/StarE | 88 | Python | Message Passing for Hyper-Relational KGs |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |
| plurigrid/asi | 13 | HTML | everything is topological chemputer! |
| plurigrid/ontology | 7 | JavaScript | autopoietic ergodicity and embodied gradualism |

### GF(3) Color Chain (World Increments)
- id%3==0 → trit=0, ERGODIC, #d3869b
- id%3==1 → trit=1, PLUS, #b8bb26
- id%3==2 → trit=-1, MINUS, #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1`.
All wallets returned 0 APT balance (accounts not funded or CoinStore resource not registered).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...5d | 0.0 |
| A | 0x8699...a7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...e5e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Probe Results

All 5 multisig contracts probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.
All contracts responded with `sigs_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | true |
| A-G | 0xf56c...096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...b6d | 2 | true |

### MNX Markets Status

**Status: Unavailable as JSON API**

`https://testnet.mnx.fi/api/markets` returns a Next.js SPA HTML page rather than a JSON response. No structured market data available from REST endpoints. The frontend is JavaScript-rendered; market data would require a browser session.

---

## Database Summary

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 23 |
| repo_snapshots | 400 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
- **kubeflow/kubeflow**: 15,542 stars — top ML toolkit for Kubernetes
- **kubeflow/pipelines**: 4,112 stars — most popular ML pipeline for Kubernetes (pushed 2026-03-28)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **plurigrid/asi**: 13 stars — topological chemputer (pushed 2026-03-30)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- All 5 Hamming swarm multisig contracts are healthy (2-of-N signatures each)
