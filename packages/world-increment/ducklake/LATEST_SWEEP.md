# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-04-10 (autonomous sweep)
**DuckDB version:** v1.5.1 (Variegata)
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 589 |
| Total Repo Snapshots | 86 unique repos |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GitHub Social Graph Sweep

### Repo Counts per Org/User

| Org/User       | Repos Swept | Notable Languages     | Most Stars Repo           |
|----------------|-------------|----------------------|---------------------------|
| plurigrid      | 30          | Zig, Rust, Haskell   | ontology (7 stars)        |
| kubeflow       | 30          | Go, Python, YAML     | kubeflow (15565 stars)    |
| TeglonLabs     | 4           | Ruby, JavaScript     | mathpix-gem (2 stars)     |
| bmorphism      | 30          | JavaScript, Rust     | anti-bullshit-mcp (23 stars) |
| zubyul         | 30          | Python, Julia, Zig   | gay-world (1 star)        |
| migalkin       | 19          | Python, Rust         | NodePiece (143 stars)     |
| DJedamski      | 6           | R                    | School (1 star)           |
| wasita         | 9           | Svelte, Python       | magic-garden (1 star)     |
| kristinezheng  | 6           | HTML, Python         | Portfolio (0 stars)       |
| M1shaaa        | 8           | TypeScript, Python   | lab-bookshelf (0 stars)   |
| AustinCStone   | 30          | Python               | TextGAN (92 stars)        |

**Total unique repos indexed:** 86

### Notable Recent Pushes (within 7 days of sweep)

| Repo                               | Pushed At            | Notes                                      |
|------------------------------------|----------------------|--------------------------------------------|
| plurigrid/web-browser              | 2026-04-10T02:54:47Z | web-browser from prepostweb lineage        |
| kubeflow/internal-acls             | 2026-04-10T07:31:19Z | Group ACLs management, very active         |
| kubeflow/pipelines                 | 2026-04-10T05:28:58Z | 4119 stars, 471 open issues                |
| kubeflow/trainer                   | 2026-04-10T02:00:59Z | Distributed AI Training on Kubernetes      |
| M1shaaa/M1shaaa                    | 2026-04-10T02:10:53Z | Profile config updated today               |
| plurigrid/nanoclj-zig              | 2026-04-09T19:53:30Z | NaN-boxed Clojure in Zig 0.15, 20 issues  |
| zubyul/big-bad-plurigrid-quiz      | 2026-04-09T18:51:31Z | 27 flashcards from plurigrid ecosystem     |
| kristinezheng/kristinezheng.github.io | 2026-04-09T17:09:42Z | Personal site updated                   |
| kubeflow/manifests                 | 2026-04-09T12:31:19Z | Kubeflow platform manifests                |
| plurigrid/zig-syrup                | 2026-04-09T11:21:29Z | OCapN Syrup in Zig, 2 stars               |
| plurigrid/tree-sitter-nanoclj-zig  | 2026-04-04T07:48:21Z | Tree-sitter grammar companion              |

---

## Aptos Wallet Snapshot (Hamming Swarm — 26 worlds A-Z + alice + bob)

All 28 wallets queried via Aptos mainnet fullnode. All returned 0.0000 APT — accounts exist but hold no CoinStore APT balance (unfunded or use delegated staking/different coin types).

| Label | Address (truncated)       | Balance (APT) |
|-------|---------------------------|---------------|
| alice | 0xc793acdec12b4a63...     | 0.0000        |
| bob   | 0x0a3c00c58fdf9020...     | 0.0000        |
| A     | 0x8699edc0960dd5b9...     | 0.0000        |
| B     | 0x3f892ebe6e45164e...     | 0.0000        |
| C     | 0x38b99e63ada9b6fe...     | 0.0000        |
| D     | 0xf77656248f64d5dd...     | 0.0000        |
| E     | 0xdc1d9d533bac3507...     | 0.0000        |
| F     | 0x18a14b5b4bec118c...     | 0.0000        |
| G     | 0x69a394c0b0ac8421...     | 0.0000        |
| H     | 0xce67c327a7844e54...     | 0.0000        |
| I     | 0x070fe5d74e4eda30...     | 0.0000        |
| J     | 0x4d964db8f5383740...     | 0.0000        |
| K     | 0xa732040a6b0d5590...     | 0.0000        |
| L     | 0x7c2eaeafad972549...     | 0.0000        |
| M     | 0x6fed37a7553ef16b...     | 0.0000        |
| N     | 0xe7dde6da0a65f510...     | 0.0000        |
| O     | 0x73252b6011a75115...     | 0.0000        |
| P     | 0x6218792de4a9bc38...     | 0.0000        |
| Q     | 0xac40fa50b81b4ca6...     | 0.0000        |
| R     | 0x7ce605cc8fda4f8e...     | 0.0000        |
| S     | 0xb8753014e4888ea4...     | 0.0000        |
| T     | 0x35781dc0e42fef3f...     | 0.0000        |
| U     | 0x75860da47565f650...     | 0.0000        |
| V     | 0xb59dd8170321dfab...     | 0.0000        |
| W     | 0x5f32aef70f5ba530...     | 0.0000        |
| X     | 0xa95cbbd116548ac9...     | 0.0000        |
| Y     | 0xd8e32848f1dffa81...     | 0.0000        |
| Z     | 0x7af0ef6e1bd706f4...     | 0.0000        |

---

## Multisig Contract Probes

All 5 multisig pairs healthy. All require 2-of-N signatures.

| Pair | Address (truncated)       | Sigs Required | Healthy |
|------|---------------------------|---------------|---------|
| A-B  | 0x0da4f428a0c007da...     | 2             | true    |
| A-G  | 0xf56c4a1c09062144...     | 2             | true    |
| Y-Z  | 0xd3ffe1812b2df406...     | 2             | true    |
| S-T  | 0x3b1c3ae905d44c3a...     | 2             | true    |
| V-W  | 0x40fad7b423a84365...     | 2             | true    |

---

## MNX Markets Status

**testnet.mnx.fi/api/markets:** Unavailable as JSON API. Endpoint returns HTML (Next.js SPA), no machine-readable market data accessible via REST at this path. Status: **UNAVAILABLE (HTML only)**

---

## GF(3) Color Chain Stats

GF(3) field mapping:
- `id%3==0` → trit=0, ERGODIC, #d3869b
- `id%3==1` → trit=1, PLUS, #b8bb26
- `id%3==2` → trit=-1, MINUS, #cc241d

| GF3 Trit | Color   | Name    | World Increment Records |
|----------|---------|---------|------------------------|
| 0        | #d3869b | ERGODIC | ~195                   |
| 1        | #b8bb26 | PLUS    | ~198                   |
| 2        | #cc241d | MINUS   | ~196                   |

**Total world_increments:** 589 | **repo_snapshots:** 86 | **aptos_snapshots:** 28 | **multisig_probes:** 5

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

## Notable Highlights
- **kubeflow/pipelines**: 4119 stars — most popular ML pipeline for Kubernetes (actively pushed 2026-04-10)
- **kubeflow/kubeflow**: 15565 stars — flagship ML Toolkit for Kubernetes
- **kubeflow/spark-operator**: 3111 stars — Kubernetes operator for Apache Spark
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure interpreter in Zig 0.15 with interaction nets (pushed 2026-04-09)
- **plurigrid/web-browser**: Most recently pushed plurigrid repo (2026-04-10)
- **bmorphism/anti-bullshit-mcp-server**: Top bmorphism repo by stars (23 stars)
- **migalkin/NodePiece**: Top migalkin repo (143 stars) — parameter-efficient KG representations
- **AustinCStone/TextGAN**: Top AustinCStone repo (92 stars) — GAN for text generation
- All 5 Aptos multisig contracts healthy with sigs_required=2
