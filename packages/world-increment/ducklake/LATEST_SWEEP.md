# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-09

## Sweep Metadata
- **Date:** 2026-07-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Color Chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 11 |
| kristinezheng | user | 2 |
| M1shaaa | user | 4 |
| AustinCStone | user | 42 |

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,770 | — | 2026-07-09 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-09 |
| kubeflow/spark-operator | 3,136 | Python | 2026-07-09 |
| kubeflow/trainer | 2,134 | Go | 2026-07-09 |
| kubeflow/katib | 1,689 | Python | 2026-07-09 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-09 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |

### Plurigrid Org Highlights (most active 2026)

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| plurigrid/gorj | Clojure | 1 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| plurigrid/asi | HTML | 30 | everything is topological chemputer! |
| plurigrid/eirobri | Clojure | 0 | EiRoBri replay world |
| plurigrid/place | TeX | 1 | bci.place forester workspace |
| plurigrid/nash-portal | Rust | 2 | NASH token TUI — ratzilla WASM + GeckoTerminal OHLCV |
| plurigrid/zig-syrup | Zig | 2 | High-performance OCapN Syrup in Zig 0.15 |
| plurigrid/nanoclj-zig | Zig | 1 | NaN-boxed Clojure interpreter in Zig 0.15 |

### bmorphism Social Graph Highlights

- **Gay.jl** (Julia, 2★) — Wide-gamut color sampling with splittable determinism (SPI pattern), 187 open issues
- **satreadout** (HTML) — Machine-checked saturating non-Riemannian perceptual readout; Lean 4.28 + mathlib
- **ocaml-mcp-sdk** (OCaml, 61★) — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **anti-bullshit-mcp-server** (JavaScript, 23★) — Multi-framework claim analysis MCP server
- **babashka-mcp-server** (JavaScript, 19★) — MCP server for Babashka/Clojure
- **nanoclj-zig** (Zig) — fork of plurigrid/nanoclj-zig
- **penrose-mcp** (JavaScript, 9★) — Penrose server for Infinity-Topos environment

### zubyul Social Graph Highlights

- **voice-observatory** (Python) — Passive macOS TUI for voice-download pathways (companion to bmorphism/say-mcp-server)
- **gay-world** (Python, 1★) — Goblin world builder; each goblin is a world; MLX task decomposition
- **big-bad-plurigrid-quiz** (Emacs Lisp) — 27 flashcards from bmorphism/plurigrid/zubyul/monaduck1069 activity
- **gay.jl** (Julia) — fork of bmorphism/Gay.jl
- **tilelang-kernels** (Python) — TileLang GPU kernels for SplitMix64/GF3/Sinkhorn OT on NVIDIA GB10 Blackwell

### migalkin Highlights

- **NodePiece** (Python, 144★, ICLR'22) — Compositional and Parameter-Efficient KG Representations
- **StarE** (Python, 89★, EMNLP'20) — Message Passing for Hyper-Relational Knowledge Graphs
- **NBFNet_mlx** (Python, 10★) — Neural Bellman-Ford networks in MLX for Apple Silicon

### DuckDB Tables

```
world_increments:  cumulative increment log (GF3 color chain)
repo_snapshots:    per-repo metadata snapshots
aptos_snapshots:   Hamming swarm wallet balances (28 wallets)
multisig_probes:   multisig contract health (5 pairs)
mnx_snapshots:     MNX market data (unavailable this sweep)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-07-09)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

| World | Address | Balance (APT) |
|-------|---------|---------------|
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

**Note:** All 28 wallets show 0.0 APT. The `CoinStore<AptosCoin>` resource was absent or zero for these addresses — accounts exist on-chain but hold no APT balance.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required` (POST to `/v1/view`):

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on all pairs.**

### MNX Testnet Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** this sweep.  
The endpoint returns a Vercel-authenticated SPA (requires Vercel OIDC token / bypass token). No market data accessible via unauthenticated HTTP. Recorded as placeholder `N/A` in `mnx_snapshots`.

---

## GF(3) Color Distribution

- **ERGODIC** (#d3869b, trit=0): increments where id mod 3 == 0  
- **PLUS** (#b8bb26, trit=1): increments where id mod 3 == 1  
- **MINUS** (#cc241d, trit=-1): increments where id mod 3 == 2

Chain pattern (repeating): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → …`

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

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-07-09*  
*DuckDB path: `packages/world-increment/ducklake/world-increments.duckdb`*
