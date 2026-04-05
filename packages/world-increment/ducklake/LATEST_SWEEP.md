# World-Increment Sweep + Hamming Snapshot — 2026-04-05

## Sweep Metadata
- **Date:** 2026-04-05
- **Agent:** world-increment-sweep + hamming-swarm
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (DB) | 391 |
| Total Repo Snapshots (DB) | 478 |
| Sources Covered This Sweep | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repos Found Per Org/User

| Source | Type | Total Repos | Top Repos (stars) |
|--------|------|-------------|-------------------|
| plurigrid | org | 95 | asi (15★), ontology (7★), vcg-auction (7★), agent (5★), StochFlow (4★) |
| kubeflow | org | 46 | kubeflow (15553★), pipelines (4118★), spark-operator (3110★), trainer (2074★), katib (1674★) |
| TeglonLabs | org | 3 | mathpix-gem (2★), coin-flip-mcp (0★), topoi (0★) |
| bmorphism | user | 98 | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★), risc0-cosmwasm-example (23★) |
| zubyul | user | 44 | WGCNA (2★), jonikas_lab (2★), Nikolova_lab (2★), gay-world (1★) |
| migalkin | user | 19 | NodePiece (143★), StarE (88★), kgcourse2021 (25★), NBFNet_mlx (10★) |
| DJedamski | user | 6 | Getting-and-Cleaning-Data (1★), Kaggle (1★), School (1★) |
| wasita | user | 9 | magic-garden (1★), wins-search (1★) |
| kristinezheng | user | 6 | all 0★ |
| M1shaaa | user | 8 | all 0★ |
| AustinCStone | user | 40 | TextGAN (92★), StereoVisionMRF (11★), SpectralClustering (3★) |

### Notable Highlights
- **plurigrid/gorj** (this repo!): 98 open issues — "forj + Rama topology nREPL routing + GF(3) gay trit coloring"
- **plurigrid/nanoclj-zig**: 20 open issues — NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation
- **kubeflow/pipelines**: 4118★, most active ML pipeline for Kubernetes
- **bmorphism**: 98 repos, heavily MCP-server focused; ocaml-mcp-sdk uses Jane Street oxcaml_effect
- **zubyul**: Gay.jl — GF(3) wide-gamut color sampling with splittable determinism
- **migalkin**: NodePiece (143★) — compositional KG representations (ICLR'22)
- **AustinCStone**: TextGAN (92★) — GAN for text generation in TensorFlow

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses queried against Aptos mainnet. All returned 0 APT (CoinStore resource not found — accounts unfunded on mainnet).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...3ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 multisig contracts are healthy (sigs_required=2, no errors from `0x1::multisig_account::num_signatures_required`).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets

All three endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) at `testnet.mnx.fi` returned
HTML (Next.js frontend), not JSON API data. No market data available. No rows inserted into `mnx_snapshots`.

---

## GF(3) Chain Summary

The GF(3) color chain assigns trits to each world-increment by `id % 3`:

| id%3 | Trit | Color | Name | Sources (this sweep) |
|------|------|-------|------|----------------------|
| 1 | +1 | #b8bb26 (yellow-green) | PLUS | plurigrid, bmorphism, DJedamski, M1shaaa |
| 2 | -1 | #cc241d (red) | MINUS | kubeflow, zubyul, wasita, AustinCStone |
| 0 | 0 | #d3869b (pink) | ERGODIC | TeglonLabs, migalkin, kristinezheng |

GF(3) chain repeats: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

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
