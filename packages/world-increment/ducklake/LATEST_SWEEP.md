# World-Increment Sweep + Hamming Snapshot — 2026-07-08

## Sweep Metadata
- **Date:** 2026-07-08
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.4 (via Python pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 78 |
| zubyul | user | 47 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 11 |
| AustinCStone | social-graph | 40 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| M1shaaa | social-graph | 8 |
| **TOTAL** | | **368+** |

### Notable Repos

**plurigrid** — 100 repos spanning Clojure, Rust, Zig, Julia, Scheme, Haskell
- `plurigrid/gorj` — Clojure, 1066 open issues, last push 2026-07-08 (active today)
- `plurigrid/asi` — 30⭐, "everything is topological chemputer!"
- `plurigrid/vcg-auction` — 7⭐ Rust, CosmWasm VCG auction
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15 with GF(3) trit conservation

**kubeflow** — 49 repos, active ML/K8s ecosystem (multiple pushes today)
- `kubeflow/kubeflow` — 15,768⭐ (ML Toolkit for Kubernetes)
- `kubeflow/pipelines` — 4,169⭐, pushed 2026-07-08
- `kubeflow/spark-operator` — 3,135⭐
- `kubeflow/trainer` — 2,133⭐ (Distributed AI + LLM Fine-Tuning on K8s)
- `kubeflow/katib` — 1,689⭐ (AutoML on Kubernetes)

**TeglonLabs** — 5 repos
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub with GF3 convergence maps (2026-06-08)
- `TeglonLabs/mathpix-gem` — 2⭐ Ruby, math image→LaTeX OCR gem

**bmorphism** — 78 repos
- `bmorphism/ocaml-mcp-sdk` — 61⭐ OCaml, Jane Street oxcaml_effect SDK for MCP
- `bmorphism/anti-bullshit-mcp-server` — 23⭐ JavaScript
- `bmorphism/risc0-cosmwasm-example` — 23⭐ Rust, CosmWasm + RISC0 zkVM

**Social graph (zubyul connections):**
- `migalkin/NodePiece` — 144⭐ Python, KG representation (ICLR'22)
- `migalkin/StarE` — 89⭐ Python, Message Passing for Hyper-Relational KGs (EMNLP'20)
- `AustinCStone/TextGAN` — 92⭐ Python, GAN for text generation (TensorFlow)
- `AustinCStone/StereoVisionMRF` — 11⭐ Python, depth from stereo via MRF + LBP
- `wasita/wasita.github.io` — Svelte personal site, active (2026-07-06)

### GF(3) Distribution (this sweep)

| GF3 Name | Color | Count |
|----------|-------|-------|
| PLUS | #b8bb26 | 45 |
| MINUS | #cc241d | 44 |
| ERGODIC | #d3869b | 43 |
| **Total world_increments** | | **132** |

GF(3) rule: `id%3==0` → ERGODIC #d3869b · `id%3==1` → PLUS #b8bb26 · `id%3==2` → MINUS #cc241d

### DuckDB State After Sweep

```
world_increments : 132 rows
repo_snapshots   : 1053 rows
aptos_snapshots  :  28 rows
multisig_probes  :   5 rows
mnx_snapshots    :   0 rows (unavailable)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

28 wallets queried against `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).

**Result: All 28 wallets returned 0 APT.** Accounts are either unfunded or do not have the `CoinStore<AptosCoin>` resource registered on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...e9d7a | 0.0 |
| B | 0x3f89...7cb13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...cfdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...c7f32 | 0.0 |
| H | 0xce67...5300f | 0.0 |
| I | 0x070f...c1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...7f2e9 | 0.0 |
| N | 0xe7dd...51b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...ec948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...d0386 | 0.0 |
| T | 0x3578...f4588 | 0.0 |
| U | 0x7586...f9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5/5 multisig contracts healthy — 2-of-N threshold confirmed on mainnet.**

### MNX Markets

`https://testnet.mnx.fi/api/markets` → **401 Unauthorized**  
API requires authentication credentials. No market data available without a valid session. `mnx_snapshots` table has 0 rows.

---

## Schema Reference

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
