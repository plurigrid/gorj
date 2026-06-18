# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-18

## Sweep Metadata
- **Date:** 2026-06-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Most Recent Push |
|--------|------|-------------|-----------------|
| plurigrid | org | 101 | 2026-06-18 (gorj) |
| kubeflow | org | 48 | 2026-06-18 (notebooks, website, internal-acls) |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| bmorphism | user | 104 | 2026-06-18 (Gay.jl) |
| zubyul | user | 49 | 2026-04-24 (voice-observatory) |
| migalkin | user (social) | 19 | 2025-08-04 (kgcourse2021) |
| DJedamski | user (social) | 6 | 2018-03-07 |
| wasita | user (social) | 11 | 2026-06-15 (wasita.github.io) |
| kristinezheng | user (social) | 5 | 2026-06-07 |
| M1shaaa | user (social) | 8 | 2026-06-18 |
| AustinCStone | user (social) | 40 | 2026-02-11 |

**Total repos indexed across all sources:** 396  
**DuckDB entries (representative):** 62 world_increments / 62 repo_snapshots

### Notable Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,734 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,154 | Python | Machine Learning Pipelines |
| kubeflow/spark-operator | 3,127 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,116 | Go | Distributed AI Model Training |
| kubeflow/katib | 1,683 | Python | Automated Machine Learning |
| kubeflow/examples | 1,460 | Jsonnet | Extended examples and tutorials |
| migalkin/NodePiece | 144 | Python | Representations for Large Knowledge Graphs (ICLR'22) |
| migalkin/StarE | 89 | Python | Hyper-Relational Knowledge Graphs (EMNLP 2020) |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for Model Context Protocol |

### Recently Active (pushed 2026-06)

- **plurigrid/gorj** — 654 open issues, Clojure, forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **plurigrid/place** — TeX, 8 open issues
- **TeglonLabs/jank-crane** — C++, GF3 convergence maps, loopify pass spec (newest TeglonLabs repo, created 2026-06-08)
- **bmorphism/Gay.jl** — Julia, 187 open issues, wide-gamut color sampling with splittable determinism
- **bmorphism/satreadout** — Lean, machine-checked saturating non-Riemannian perceptual readout
- **kubeflow/notebooks, website, internal-acls** — all pushed within 24h of sweep

### GF(3) Increment Chain (62 entries)
- PLUS (#b8bb26, trit=1): 21 increments (id mod 3 == 1)
- MINUS (#cc241d, trit=2): 20 increments (id mod 3 == 2)
- ERGODIC (#d3869b, trit=0): 21 increments (id mod 3 == 0)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm addresses probed against `fullnode.mainnet.aptoslabs.com`.

**Result: 0 APT across all 28 addresses** — accounts not found / no CoinStore on mainnet.

| Label | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z (24) | various | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts responded successfully via `0x1::multisig_account::num_signatures_required`.  
All require **2-of-N signatures** — canonical 2-sig governance confirmed.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401, Vercel preview auth gate. All paths (`/`, `/api/markets`, `/api/v1/markets`, `/api/v1/tickers`) return authentication required. Requires `vercel curl` CLI or Vercel MCP server with credentials. No market data extracted; mnx_snapshots table is empty.

---

## DuckDB Schema

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 62 | GF(3)-colored event log (PLUS/MINUS/ERGODIC chain) |
| repo_snapshots | 62 | Repo metadata: org/user, language, stars, forks, issues, pushed_at |
| aptos_snapshots | 28 | Hamming swarm wallet balances (all 0 APT) |
| multisig_probes | 5 | Aptos multisig health checks (all 2-sig, all healthy) |
| mnx_snapshots | 0 | MNX market data (unavailable — auth gated) |

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
- `id mod 3 == 2` → trit=2, color=#cc241d, name=MINUS

---

## Key Findings

1. **plurigrid/gorj** is the most issue-laden repo (654 open issues) — active development hub as of 2026-06-18.
2. **Kubeflow ecosystem** remains highly active — all major repos pushed within 24h.
3. **bmorphism/Gay.jl** has 187 open issues and was pushed today — living research workspace.
4. **TeglonLabs/jank-crane** is the newest TeglonLabs repo (created 2026-06-08), focused on GF3 convergence.
5. **All 28 Hamming swarm Aptos addresses have zero balance** — not yet funded on mainnet.
6. **All 5 multisig pairs are healthy** with 2-of-N threshold.
7. **MNX testnet is auth-gated** — revisit with Vercel credentials or Vercel MCP server.
