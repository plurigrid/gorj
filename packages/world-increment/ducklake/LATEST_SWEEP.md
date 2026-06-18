# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-18  
**Sweep agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| # | Source | Type | Repos | GF3 Trit | Color |
|---|--------|------|-------|----------|-------|
| 1 | plurigrid | org | 100 | PLUS +1 | #b8bb26 |
| 2 | kubeflow | org | 48 | MINUS -1 | #cc241d |
| 3 | TeglonLabs | org | 5 | ERGODIC 0 | #d3869b |
| 4 | bmorphism | user | 100 | PLUS +1 | #b8bb26 |
| 5 | zubyul | user | 49 | MINUS -1 | #cc241d |
| 6 | migalkin | user | 19 | ERGODIC 0 | #d3869b |
| 7 | AustinCStone | user | 30 | PLUS +1 | #b8bb26 |
| 8 | wasita | user | 11 | MINUS -1 | #cc241d |
| 9 | DJedamski | user | 6 | ERGODIC 0 | #d3869b |
| 10 | kristinezheng | user | 5 | PLUS +1 | #b8bb26 |
| 11 | M1shaaa | user | 8 | MINUS -1 | #cc241d |

**Total repos snapshotted:** 381

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,734 | - | 2026-06-18 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-18 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-18 |
| kubeflow/trainer | 2,116 | Go | 2026-06-18 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |

### Notable Recent Activity (pushed within 7 days of sweep)

- **plurigrid/gorj** -- pushed 2026-06-18 (655 open issues, active development)
- **plurigrid/place** -- pushed 2026-06-15
- **kubeflow/hub**, **kubeflow/community-distribution**, **kubeflow/pipelines** -- all pushed 2026-06-18
- **bmorphism/Gay.jl** -- pushed 2026-06-18 (187 open issues)
- **wasita/wasita.github.io** -- pushed 2026-06-15
- **M1shaaa/M1shaaa** -- pushed 2026-06-18

### Social Graph Highlights

- **plurigrid** (org): Heavy Clojure/Zig/Rust activity; GF3 coloring work (Gay.jl ecosystem), nash-portal WASM TUI, eirobri Clojure world
- **kubeflow** (org): Major ML-on-K8s ecosystem; hub (Model Registry) and spark-operator actively maintained; new MCP servers added
- **TeglonLabs** (org): jank-crane (C++ IR hub), mathpix-gem (Ruby OCR), coin-flip-mcp
- **bmorphism**: Prolific MCP server author; Gay.jl (GF3 color), ocaml-mcp-sdk, satreadout (Lean), oxgame (OCaml)
- **zubyul**: nash-tui/nash-web Rust TUI work; voice-observatory; ghostel-emacs-worlds GLSL
- **migalkin**: Knowledge graph research (NodePiece 144 stars, StarE 89 stars, NBFNet_mlx)
- **AustinCStone**: TextGAN 92 stars (TF text GAN); mostly ML research
- **wasita**: Svelte + Typst personal site; magic-garden Discord bot
- **DJedamski**: Kaggle/statistics repos (inactive, last push 2018)
- **kristinezheng**: Cognitive science research (lookit studies, auditory illusion)
- **M1shaaa**: Active profile (pushed today), neuroscience/ML work

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A-Z) queried via fullnode.mainnet.aptoslabs.com.

**Result: All balances = 0.0 APT**

The Aptos mainnet API returned no CoinStore<AptosCoin> resource for any of these addresses.
This indicates the accounts have not been initialized on mainnet or hold no APT.
All 28 addresses stored in aptos_snapshots table with balance_apt = 0.0.

### Multisig Contract Probes

All 5 multisig contracts probed via 0x1::multisig_account::num_signatures_required:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

All 5 multisigs healthy -- all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** -- testnet.mnx.fi is behind Vercel deployment protection.
All API paths returned a Vercel auth wall. No market data extractable.

---

## DuckDB Schema Summary

```
world-increments.duckdb
  world_increments   (11 rows)  -- GF3-colored sweep events
  repo_snapshots    (381 rows)  -- GitHub repo metadata
  aptos_snapshots    (28 rows)  -- Hamming swarm wallet balances
  multisig_probes     (5 rows)  -- Aptos multisig health checks
  mnx_snapshots       (0 rows)  -- MNX markets (unavailable)
```

## GF(3) Color Chain

```
id=1  plurigrid     PLUS    +1  #b8bb26
id=2  kubeflow      MINUS   -1  #cc241d
id=3  TeglonLabs    ERGODIC  0  #d3869b
id=4  bmorphism     PLUS    +1  #b8bb26
id=5  zubyul        MINUS   -1  #cc241d
id=6  migalkin      ERGODIC  0  #d3869b
id=7  AustinCStone  PLUS    +1  #b8bb26
id=8  wasita        MINUS   -1  #cc241d
id=9  DJedamski     ERGODIC  0  #d3869b
id=10 kristinezheng PLUS    +1  #b8bb26
id=11 M1shaaa       MINUS   -1  #cc241d
```
