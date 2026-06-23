# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-06-23)

| Metric | Value |
|--------|-------|
| Total World Increments | 391 |
| Total Repo Snapshots | 391 |
| Sources Covered | 3 orgs + 8 users |
| GF3 ERGODIC (#d3869b) | 130 |
| GF3 PLUS (#b8bb26) | 131 |
| GF3 MINUS (#cc241d) | 130 |

---

## JOB 1: GitHub Social Graph Sweep

### Repos by Source
| Source | Type | Repos | Stars | Notable |
|--------|------|-------|-------|---------|
| plurigrid | org | 100 | 77 | asi, ontology, vcg-auction, agent, StochFlow |
| bmorphism | user | 100 | 248 | ocaml-mcp-sdk, babashka-mcp-server, manifold-mcp-server, penrose-mcp |
| kubeflow | org | 48 | 34,246 | kubeflow (15,565★), pipelines, spark-operator, trainer, katib |
| zubyul | user | 49 | 14 | jonikas_lab_data_analysis_misc, WGCNA, gay-world, cascade-world |
| AustinCStone | user | 40 | 108 | TextGAN (92★), StereoVisionMRF, SpectralClustering |
| migalkin | user | 19 | 280 | NodePiece (143★), StarE (88★), kgcourse2021, NBFNet_mlx |
| wasita | user | 11 | 5 | magic-garden, wasita.github.io, send2kobo, proj-template |
| M1shaaa | user | 8 | 0 | M1shaaa profile (pushed 2026-06-22!) |
| DJedamski | user | 6 | 3 | kaggle_ncaa18, School, Getting-and-Cleaning-Data |
| TeglonLabs | org | 5 | 2 | jank-crane (GF3 hub, pushed 2026-06-08), mathpix-gem |
| kristinezheng | user | 5 | 0 | kristinezheng.github.io (pushed 2026-06-07) |
| **TOTAL** | | **391** | **34,983** | |

### Recently Active (pushed in 2026)
- `M1shaaa/M1shaaa` — pushed **2026-06-22** (profile config, yesterday!)
- `TeglonLabs/jank-crane` — pushed **2026-06-08** (C++, GF3 convergence maps + crane-jank IR hub)
- `kristinezheng/kristinezheng.github.io` — pushed **2026-06-07** (HTML portfolio)
- `wasita/proj-template` — pushed **2026-06-19**
- `TeglonLabs/mathpix-gem` — pushed **2026-01-01** (Ruby math OCR, 2★ + 11 open issues)

### Signal: bmorphism MCP Ecosystem
100 repos snapshotted — a dense cluster of MCP servers and agents:
`ocaml-mcp-sdk`, `babashka-mcp-server`, `manifold-mcp-server`, `penrose-mcp`,
`marginalia-mcp-server`, `nats-mcp-server`, `hypernym-mcp-server`, `penumbra-mcp`,
`slowtime-mcp-server`, `gists-mcp-server`, `graphistry-mcp`, `krep-mcp-server`,
`lumon-tui`, `infinity-topos`, `elevenlabs-mcp-enhanced`, `zk-haiku-nanogpt` — 
a swarm of composable AI-native tooling.

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 addresses
**All 28 wallets: 0 APT** — `CoinStore<AptosCoin>` resource not found on mainnet.
Addresses exist on-chain but have no APT deposited.

| Worlds | Count | APT |
|--------|-------|-----|
| alice, bob | 2 | 0.0 each |
| A through Z | 26 | 0.0 each |
| **Total swarm** | **28** | **0.0 APT** |

### Multisig Contracts — 5 probes
**All 5 healthy — 2-of-2 threshold.**

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4…3003 | 2 | ✓ healthy |
| A-G | 0xf56c…0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✓ healthy |
| S-T | 0x3b1c…7883 | 2 | ✓ healthy |
| V-W | 0x40fa…eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**UNAVAILABLE** — Vercel deployment protection (auth required). No market data extracted.

---

## Schema
```sql
world_increments  (391 rows) — GF3 color-tagged repo events
repo_snapshots    (391 rows) — org, name, language, stars, forks, issues, pushed_at
aptos_snapshots   (28 rows)  — world A-Z + alice/bob, all 0 APT
multisig_probes   (5 rows)   — all healthy, 2-of-2
mnx_snapshots     (0 rows)   — unavailable
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — ML pipelines (still actively pushed in 2026)
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings (Python)
- **bmorphism/ocaml-mcp-sdk**: 60★ — OCaml MCP SDK via Jane Street oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text GAN research
- **TeglonLabs/jank-crane**: GF3 convergence maps, pushed 2026-06-08 (most recently active in this sweep)
- **Hamming swarm**: 5/5 multisig contracts healthy at 2-of-2; all 28 wallet worlds at 0 APT
- **MNX**: testnet behind Vercel auth — probe deferred to future sweep with bypass token
