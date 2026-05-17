# World-Increment Sweep + Hamming Snapshot — 2026-05-17

## Sweep Metadata
- **Date:** 2026-05-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Covered

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| kubeflow | org | 48 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| TeglonLabs | org | 4 |
| migalkin | user (zubyul social) | 4 |
| wasita | user (zubyul social) | 3 |
| AustinCStone | user (zubyul social) | 3 |
| kristinezheng | user (zubyul social) | 2 |
| DJedamski | user (zubyul social) | 2 |
| M1shaaa | user (zubyul social) | 2 |
| **TOTAL** | | **143** |

### Top Repos by Stars

| Rank | Repo | Stars | Language | Pushed |
|------|------|-------|----------|--------|
| 1 | kubeflow/kubeflow | 15,639 | — | 2026-05-07 |
| 2 | kubeflow/pipelines | 4,139 | Python | 2026-05-15 |
| 3 | kubeflow/spark-operator | 3,125 | Python | 2026-05-15 |
| 4 | kubeflow/trainer | 2,099 | Go | 2026-05-15 |
| 5 | kubeflow/katib | 1,682 | Python | 2026-05-09 |
| 6 | kubeflow/examples | 1,463 | Jsonnet | 2025-04-14 |
| 7 | kubeflow/manifests | 1,017 | YAML | 2026-05-16 |
| 8 | kubeflow/arena | 810 | Go | 2026-05-07 |
| 9 | kubeflow/kale | 687 | Python | 2026-05-15 |
| 10 | kubeflow/mpi-operator | 527 | Go | 2026-05-12 |

**plurigrid highlights (50 repos, 100 total in org):**
- `gorj` — Clojure REPL + GF(3) trit coloring, 224 open issues (most active, pushed 2026-05-17)
- `asi` — 23⭐ topological chemputer (HTML, pushed 2026-04-26)
- `zig-syrup` — 2⭐ OCapN Syrup in Zig (pushed 2026-04-30)
- `nanoclj-zig` — NaN-boxed Clojure interpreter in Zig with GF(3) trit conservation
- `nash-portal` — NASH token TUI in browser (ratzilla WASM + GeckoTerminal)

**bmorphism highlights (102 total repos):**
- `ocaml-mcp-sdk` — 61⭐ OCaml SDK for MCP using oxcaml_effect (pushed 2026-05-08)
- `anti-bullshit-mcp-server` — 23⭐ epistemological claim analysis MCP server
- `Gay.jl` — wide-gamut GF(3) color sampling, 189 open issues (default branch: `gay`)
- `oxgame` — Stellar resolution + open-game composition in OCaml (very recent: 2026-05-15)

**TeglonLabs highlights:**
- `mathpix-gem` — 2⭐ Ruby gem for math image → LaTeX OCR, 11 open issues

**migalkin (zubyul social):**
- `NodePiece` — 144⭐ ICLR'22 knowledge graph embeddings
- `StarE` — 89⭐ EMNLP'20 hyper-relational KGs
- `NBFNet_mlx` — 10⭐ Neural Bellman-Ford networks in MLX for Apple Silicon

**AustinCStone (zubyul social):**
- `TextGAN` — 92⭐ text GAN in TensorFlow
- `StereoVisionMRF` — 11⭐ 3D depth from stereo using MRF

### GF(3) Color Chain Distribution

| Trit | Name | Color | Semantics | Increment Count |
|------|------|-------|-----------|----------------|
| 0 | ERGODIC | `#d3869b` | ergodic / pink | 47 |
| +1 | PLUS | `#b8bb26` | additive / yellow-green | 48 |
| −1 | MINUS | `#cc241d` | subtractive / red | 48 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

Probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
All wallets returned 0.0 APT — accounts either unfunded or lack a registered CoinStore resource.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A | 0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a | 0.0 |
| B | 0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13 | 0.0 |
| C | 0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e | 0.0 |
| D | 0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1 | 0.0 |
| E | 0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36 | 0.0 |
| F | 0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71 | 0.0 |
| G | 0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32 | 0.0 |
| H | 0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f | 0.0 |
| I | 0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9 | 0.0 |
| J | 0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54 | 0.0 |
| K | 0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4 | 0.0 |
| L | 0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9 | 0.0 |
| M | 0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9 | 0.0 |
| N | 0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c | 0.0 |
| O | 0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d | 0.0 |
| P | 0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948 | 0.0 |
| Q | 0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9 | 0.0 |
| R | 0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10 | 0.0 |
| S | 0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386 | 0.0 |
| T | 0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588 | 0.0 |
| U | 0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956 | 0.0 |
| V | 0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3 | 0.0 |
| W | 0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0 | 0.0 |
| X | 0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d | 0.0 |
| Y | 0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4 | 0.0 |
| Z | 0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c | 0.0 |

**Total swarm APT:** 0.0 across 28 wallets.

### Multisig Contract Probes (5 pairs)

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

**All 5 multisig contracts healthy.** All configured as 2-of-N signatories.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA. No direct REST API accessible at `/api/markets`
or `/api/tickers`. Market data loads client-side via JS bundles (dpl=dpl_BMQ5avRxv...).
**Status: unavailable via curl** — `mnx_snapshots` table is empty this sweep.

---

## DuckDB Tables Summary

```
world_increments  — 143 rows  (GF(3) color-chained GitHub repo events)
repo_snapshots    — 143 rows  (repo metadata: stars, forks, language, pushed_at)
aptos_snapshots   —  28 rows  (Hamming swarm APT balances, all 0.0)
multisig_probes   —   5 rows  (2-of-N multisig health probes, all healthy)
mnx_snapshots     —   0 rows  (SPA, no REST API accessible)
```

## Schema

```sql
CREATE TABLE world_increments (
  id INTEGER, timestamp TIMESTAMP, gf3_trit INTEGER,
  gf3_color VARCHAR, gf3_name VARCHAR, source_type VARCHAR,
  source_name VARCHAR, event_type VARCHAR, repo_name VARCHAR,
  actor VARCHAR, snapshot_hash VARCHAR);

CREATE TABLE repo_snapshots (
  id INTEGER, timestamp TIMESTAMP, increment_id INTEGER,
  org_or_user VARCHAR, repo_name VARCHAR, full_name VARCHAR,
  language VARCHAR, stars INTEGER, forks INTEGER, open_issues INTEGER,
  pushed_at VARCHAR, description VARCHAR);

CREATE TABLE aptos_snapshots (
  timestamp TIMESTAMP, world VARCHAR, address VARCHAR, balance_apt DOUBLE);

CREATE TABLE multisig_probes (
  timestamp TIMESTAMP, pair VARCHAR, address VARCHAR,
  sigs_required INTEGER, healthy BOOLEAN);

CREATE TABLE mnx_snapshots (
  timestamp TIMESTAMP, ticker VARCHAR, name VARCHAR, category VARCHAR,
  price DOUBLE, change_pct DOUBLE);
```
