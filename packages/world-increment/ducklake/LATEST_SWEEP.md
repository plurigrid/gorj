# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-07

## Sweep Metadata
- **Date:** 2026-07-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 343 |
| Total Repo Snapshots | 320 unique repos |
| Sources Covered | 3 orgs + 8 users |
| Run Date | 2026-07-07 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|---|---|---|---|
| 0 | `#d3869b` | ERGODIC | 113 |
| +1 | `#b8bb26` | PLUS | 115 |
| -1 | `#cc241d` | MINUS | 115 |

Assignment rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

### Repo Counts by Source

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | gorj (1027 issues, pushed today), asi (28★), shrimp |
| bmorphism | user | 100 | Gay.jl (187 issues), ocaml-mcp-sdk (61★), anti-bullshit-mcp |
| kubeflow | org | 49 | kubeflow (15769★), pipelines (4169★), spark-operator (3132★) |
| zubyul | user | 49 | nash-tui, Gay.jl fork, plurigrid-site |
| AustinCStone | user | 40 | TextGAN (92★), StereoVisionMRF (11★) |
| migalkin | user | 19 | NodePiece (144★), StarE (89★) — knowledge graphs |
| wasita | user | 11 | Svelte personal site + magic-garden bot |
| M1shaaa | user | 8 | Yale Lookit lab tooling |
| TeglonLabs | org | 5 | jank-crane (GF3 hub, C++), mathpix-gem (Ruby, 2★) |
| kristinezheng | user | 5 | MIT cognitive science |
| DJedamski | user | 6 | Data science; sparse activity |
| **TOTAL** | | **392** | |

### Top Repos by Stars (2026-07-07 snapshot)

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15769 | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4169 | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3132 | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2129 | Go | Distributed AI Model Training on Kubernetes |
| kubeflow/katib | 1690 | Python | AutoML on Kubernetes |
| kubeflow/arena | 815 | Go | CLI for Kubeflow |
| AustinCStone/TextGAN | 92 | Python | GAN for text generation (TensorFlow) |
| migalkin/NodePiece | 144 | Python | Parameter-efficient KG representations (ICLR'22) |
| migalkin/StarE | 89 | Python | Message Passing for Hyper-Relational KGs (EMNLP'20) |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | OCaml SDK for MCP using Jane Street's oxcaml_effect |

### Notable Orbit Activity (plurigrid/bmorphism/zubyul)
- **plurigrid/gorj** — 1027 open issues, pushed 2026-07-07 (today); forj + GF(3) routing
- **bmorphism/Gay.jl** — 187 open issues (Julia), pushed 2026-07-07; wide-gamut color sampling
- **plurigrid/eirobri** — 30 open issues, pushed 2026-06-30; EiRoBri replay world
- **plurigrid/shrimp** — Jank worked example, pushed 2026-07-03
- **plurigrid/asi** — 28★ HTML, topological chemputer
- **TeglonLabs/jank-crane** — crane-jank GF3 convergence maps, C++, pushed 2026-06-08
- **wasita/wasita.github.io** — personal site (Svelte), updated 2026-07-06

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet — 2026-07-07)

### Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet.

**Result: All 28 addresses returned "Resource not found" (no APT coin stores on mainnet)**

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | null |
| bob | 0x0a3c00... | null |
| A | 0x8699ed... | null |
| B | 0x3f892e... | null |
| C | 0x38b99e... | null |
| D | 0xf77656... | null |
| E | 0xdc1d9d... | null |
| F | 0x18a14b... | null |
| G | 0x69a394... | null |
| H | 0xce67c3... | null |
| I | 0x070fe5... | null |
| J | 0x4d964d... | null |
| K | 0xa73204... | null |
| L | 0x7c2eae... | null |
| M | 0x6fed37... | null |
| N | 0xe7dde6... | null |
| O | 0x73252b... | null |
| P | 0x621879... | null |
| Q | 0xac40fa... | null |
| R | 0x7ce605... | null |
| S | 0xb87530... | null |
| T | 0x35781d... | null |
| U | 0x75860d... | null |
| V | 0xb59dd8... | null |
| W | 0x5f32ae... | null |
| X | 0xa95cbb... | null |
| Y | 0xd8e328... | null |
| Z | 0x7af0ef... | null |

*Signal: The Hamming swarm wallets are unfunded on Aptos mainnet (no CoinStore resources registered).*

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a... | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1... | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a... | 2 | ✅ HEALTHY |
| V-W | 0x40fad7... | 2 | ✅ HEALTHY |

**All 5 multisig accounts healthy. Uniform 2-of-N threshold across all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment authentication.  
All API paths probed returned 401 Vercel auth wall. `mnx_snapshots` table is empty for this run.

---

## DuckDB Ducklake — Table Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 343 | GF(3) color-chained, per-repo increment records |
| `repo_snapshots` | 1264 | Full repo metadata across all runs |
| `aptos_snapshots` | 28 | Hamming swarm wallets, all null balances |
| `multisig_probes` | 5 | All healthy, 2-sig threshold |
| `mnx_snapshots` | 0 | Vercel auth blocked |

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

## Overall Summary

**GitHub sweep (2026-07-07):** 320 repos captured across 11 sources. Kubeflow dominates (15769★ flagship repo). The plurigrid/bmorphism orbit is highly active — both gorj and Gay.jl pushed today. TeglonLabs has 5 repos centered on GF(3)/jank tooling. Knowledge graph researcher migalkin (NodePiece 144★) and ML pioneer AustinCStone (TextGAN 92★) are active in the social graph.

**Hamming swarm (2026-07-07):** All 28 APT wallets unfunded on mainnet (no coin stores). All 5 multisig contracts healthy with 2-sig threshold. MNX testnet inaccessible (Vercel auth wall).
