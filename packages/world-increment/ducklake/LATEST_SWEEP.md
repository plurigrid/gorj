# World-Increment Sweep + Hamming Snapshot
**Date:** 2026-06-13  
**Run:** world-increment-sweep + hamming-swarm-snapshot agent  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Surveyed
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| AustinCStone | social graph | 30 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| DJedamski | social graph | 6 |
| **TOTAL** | | **381** |

### GF(3) Color Chain Distribution
| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 134 |
| PLUS | `#b8bb26` | +1 | 135 |
| MINUS | `#cc241d` | -1 | 135 |

### Top Repos by Stars
| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,720 | — |
| kubeflow/pipelines | 4,153 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/trainer | 2,114 | Go |
| kubeflow/katib | 1,683 | Python |
| kubeflow/examples | 1,461 | Jsonnet |
| kubeflow/community-distribution | 1,023 | YAML |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |

### Notable Active Repos (open issues)
| Repo | Open Issues | Language |
|------|-------------|----------|
| plurigrid/gorj | 544 | Clojure |
| bmorphism/Gay.jl | 189 | Julia |
| kubeflow/pipelines | 489 | Python |
| kubeflow/notebooks | 168 | — |
| kubeflow/docs-agent | 150 | Python |

### Plurigrid Org Highlights
- **plurigrid/gorj** — 544 open issues, Clojure — forj + Rama nREPL routing + GF(3) trit coloring
- **plurigrid/asi** — 26 stars — "everything is topological chemputer!"
- **plurigrid/ontology** — 8 stars — autopoietic ergodicity and embodied gradualism
- Recently pushed: gorj (2026-06-13), asi (2026-06-10), eirobri (2026-06-03)
- Gay.jl ecosystem: gay-rs, gay-go, gay-terminal, gay-tofu (GF3 colorings across langs)

### bmorphism Highlights
- **ocaml-mcp-sdk** — 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **anti-bullshit-mcp-server** — 23 stars — JS
- **risc0-cosmwasm-example** — 23 stars — CosmWasm + zkVM RISC-V
- **say-mcp-server** — 20 stars, babashka-mcp-server — 19 stars
- Active: Gay.jl (189 open issues), vibesnipe-market (9)

### TeglonLabs Highlights
- **jank-crane** — C++ — crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- **mathpix-gem** — Ruby — geodesic path to mathematical OCR
- **coin-flip-mcp** — JS — MCP server with randomness from random.org

### zubyul + Social Graph
- zubyul active: voice-observatory, nash-tui, Gay.jl fork, tilelang-kernels, kinesis-kb360pro
- **migalkin**: Knowledge graphs (NodePiece 144★, StarE 89★), NBFNet_mlx for Apple Silicon
- **wasita**: Svelte personal site, Women in Network Science, magic-garden Discord bot
- **AustinCStone**: TextGAN (92★), StereoVisionMRF (11★), ML/CV-focused
- **kristinezheng**: MIT neuroscience — Lookit studies, auditory illusion
- **M1shaaa**: Yale cognitive dev lab — Lookit, MNIST, bookshelf app
- **DJedamski**: Coursera data science, NCAA Kaggle, R stats

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances
**Timestamp:** 2026-06-13 ~10:00Z  
All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.

| World | APT Balance | Note |
|-------|-------------|------|
| alice–bob, A–Z (all 28) | 0.0 APT | CoinStore not found |

**Note:** All 28 addresses returned 0.0 APT. The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was not found on any address, indicating accounts use Fungible Asset (FA) framework or have no APT balance on mainnet.

### Multisig Contract Probes
Via `0x1::multisig_account::num_signatures_required` on Aptos mainnet.

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4...987003 | 2 | ✅ healthy |
| A-G | 0xf56c...bc0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...75b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...ed7883 | 2 | ✅ healthy |
| V-W | 0x40fa...80eb6d | 2 | ✅ healthy |

**All 5 multisig contracts healthy — 2-of-N signature threshold.**

### MNX Markets (testnet.mnx.fi)
**Status:** UNAVAILABLE  
`https://testnet.mnx.fi` is behind Vercel deployment authentication. Returns a password-protect SPA — no market data accessible without a bypass token.

---

## DuckDB Tables

```
world_increments — 381 rows (this run), GF3 color-chained
repo_snapshots   — 381 repos snapshotted
aptos_snapshots  — 28 wallet balances (all 0.0 APT)
multisig_probes  — 5 contracts (all healthy, 2 sigs)
mnx_snapshots    — 0 rows (service unavailable)
```

---

## Observations

1. **plurigrid/gorj** has 544 open issues — highest in plurigrid org.
2. **kubeflow/kubeflow** leads all repos at 15,720 stars.
3. **bmorphism** runs a prolific MCP server ecosystem (10+ servers across JS/OCaml/Python).
4. All 5 Hamming swarm multisig contracts operational with 2-of-N quorum.
5. All 28 Aptos addresses show 0 APT — likely FA-based accounts or uninitialized CoinStore.
6. MNX testnet is Vercel-protected — market data unavailable this sweep.
7. zubyul social graph: tight cluster around cognitive science (MIT/Yale), knowledge graphs, and ML vision.
