# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-01

## Sweep Metadata
- **Date:** 2026-05-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 11 |
| New Repo Snapshots (this run) | 389 |
| Sources Covered | 3 orgs + 8 users |
| Total Rows in world_increments | 34 (cumulative) |
| Total Rows in repo_snapshots | 1333 (cumulative) |

---

### GF(3) Color Chain — This Sweep's 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Repo Counts by Source (This Sweep)

| Source | Type | Repos | Top Stars |
|--------|------|-------|-----------|
| plurigrid | org | 98 | asi (17★), ontology (7★), agent (5★) |
| kubeflow | org | 47 | kubeflow (15609★), pipelines (4130★), spark-operator (3121★) |
| TeglonLabs | org | 4 | mathpix-gem (2★) |
| bmorphism | user | 85 | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★) |
| zubyul | user | 47 | jonikas_lab_data_analysis_misc (2★), gay-world (1★) |
| migalkin | user | 19 | NodePiece (143★), StarE (89★), kgcourse2021 (25★) |
| DJedamski | user | 6 | Kaggle (1★), Getting-and-Cleaning-Data (1★), School (1★) |
| wasita | user | 10 | magic-garden (2★), wasita.github.io (1★) |
| kristinezheng | user | 6 | (all 0★) |
| M1shaaa | user | 8 | (all 0★) |
| AustinCStone | user | 40 | TextGAN (92★), StereoVisionMRF (11★) |
| **TOTAL** | | **370** | |

### Notable GitHub Highlights

- **kubeflow/kubeflow**: 15,609 stars — flagship ML platform for Kubernetes (pushed 2026-04-29)
- **kubeflow/pipelines**: 4,130 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-30)
- **kubeflow/spark-operator**: 3,121 stars — Kubernetes operator for Apache Spark (pushed 2026-04-28)
- **migalkin/NodePiece**: 143 stars — compositional KG embeddings (ICLR'22)
- **migalkin/StarE**: 89 stars — hyper-relational KG message passing (EMNLP 2020)
- **AustinCStone/TextGAN**: 92 stars — TensorFlow text GAN
- **bmorphism/Gay.jl**: Julia, 187 open issues — wide-gamut color sampling with splittable determinism (pushed 2026-05-01, most recent commit)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK via Jane Street oxcaml_effect
- **plurigrid/gorj**: 29 open issues — this very repo, Clojure, pushed 2026-05-01
- **plurigrid/asi**: 17 stars — topological chemputer, pushed 2026-04-26

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-05-01)

> Query method: `0x1::coin::balance` view function (accounts exist but use coin API, not CoinStore resource)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob   | 12.6570 | `0x0a3c00c58fdf...` |
| F     | 1.9605  | `0x18a14b5b4bec...` |
| L     | 1.9273  | `0x7c2eaeafad97...` |
| J     | 1.8951  | `0x4d964db8f538...` |
| alice | 0.4364  | `0xc793acdec12b...` |
| O     | 0.2101  | `0x73252b601...` |
| K     | 0.1620  | `0xa732040a6b0d...` |
| P     | 0.1401  | `0x62187...` |
| M     | 0.1123  | `0x6fed37a7553e...` |
| N     | 0.1061  | `0xe7dde6da0a65...` |
| Q     | 0.1032  | `0xac40fa50b81b...` |
| S     | 0.0918  | `0xb8753014e488...` |
| R     | 0.0902  | `0x7ce605cc8fda...` |
| T     | 0.0737  | `0x35781dc0e42f...` |
| U     | 0.0558  | `0x75860da47565...` |
| A     | 0.0518  | `0x8699edc0960d...` |
| X     | 0.0426  | `0xa95cbbd11654...` |
| Y     | 0.0444  | `0xd8e32848f1df...` |
| B     | 0.0363  | `0x3f892ebe6e45...` |
| V     | 0.0488  | `0xb59dd8170321...` |
| W     | 0.0407  | `0x5f32aef70f5b...` |
| D     | 0.0116  | `0xf77656248f64...` |
| C     | 0.0102  | `0x38b99e63ada9...` |
| H     | 0.0017  | `0xce67c327a784...` |
| Z     | 0.0243  | `0x7af0ef6e1bd7...` |
| E     | 0.0094  | `0xdc1d9d533bac...` |
| G     | 0.0007  | `0x69a394c0b0ac...` |
| I     | 0.0007  | `0x070fe5d74e4e...` |

**Total across all 28 wallets: ~21.36 APT**
**Richest**: bob (12.66 APT) — holds 59.3% of total swarm balance
**Poorest**: G and I (0.00068 APT each)

---

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | `0x0da4f428a0c007...` | 2 | ✓ |
| A-G | `0xf56c4a1c090621...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c...` | 2 | ✓ |
| V-W | `0x40fad7b423a843...` | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold universally observed.

---

### MNX Markets (testnet.mnx.fi)

**Status: SPA — API endpoints unavailable (404)**
The site returns a 292KB React SPA at the root URL but all API paths (`/api/markets`, `/api/v1/markets`, `/api/tokens`) return 404. Market data could not be extracted without browser JavaScript execution.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
