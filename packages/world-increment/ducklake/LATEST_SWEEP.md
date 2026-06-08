# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-08T00:00:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
| trit | name | hex | count |
|------|------|-----|-------|
| 0 | ERGODIC | #d3869b | 73 |
| 1 | PLUS | #b8bb26 | 74 |
| -1 | MINUS | #cc241d | 74 |

### Sources Snapshotted

| org/user | repos | total_stars | notes |
|----------|-------|-------------|-------|
| kubeflow | 48 | 100,005 | ML infra org; pipelines(4.1k⭐), spark-operator(3.1k⭐), trainer(2.1k⭐) |
| migalkin | 19 | 833 | KG/GNN researcher; NodePiece(144⭐), StarE(89⭐) |
| bmorphism | 103 | 453 | plurigrid dev; Gay.jl(active), ocaml-mcp-sdk(61⭐), anti-bullshit-mcp(23⭐) |
| AustinCStone | 40 | 323 | TextGAN(92⭐), StereoVisionMRF(11⭐) |
| plurigrid | 101 | 156 | asi(25⭐), ontology(8⭐), vcg-auction(7⭐), gorj(active, 430 open issues) |
| zubyul | 49 | 32 | plurigrid collab; nash-tui, Gay.jl fork, kinesis-kb360pro |
| DJedamski | 6 | 17 | data science / Kaggle; older activity |
| TeglonLabs | 4 | 14 | mathpix-gem(2⭐), coin-flip-mcp, monad-mcp-server |
| wasita | 11 | 10 | Svelte dev; wasita.github.io active 2026-06-01 |
| M1shaaa | 8 | 0 | Yale dev; lab bookshelf, Lookit experiments |
| kristinezheng | 5 | 0 | MIT/neuroscience; website active 2026-06-07 |

### Most Recently Pushed (top 10)
| repo | pushed_at | language |
|------|-----------|----------|
| kubeflow/dashboard | 2026-06-08 | TypeScript |
| bmorphism/Gay.jl | 2026-06-08 | Julia |
| plurigrid/gorj | 2026-06-08 | Clojure |
| kubeflow/notebooks | 2026-06-06 | — |
| kubeflow/pipelines | 2026-06-06 | Python |
| kubeflow/community | 2026-06-05 | Jupyter |
| kubeflow/katib | 2026-06-05 | Python |
| kubeflow/trainer | 2026-06-05 | Go |
| plurigrid/place | 2026-06-04 | TeX |
| kubeflow/spark-operator | 2026-06-04 | Python |

### Notable Repos
- **plurigrid/gorj**: This very repo — `forj + Rama topology nREPL routing + GF(3) gay trit coloring` — 430 open issues, active today
- **bmorphism/Gay.jl**: Wide-gamut color sampling with splittable determinism (189 open issues, pushed today)
- **plurigrid/asi**: `everything is topological chemputer!` — 25 stars, HTML
- **kubeflow/kubeflow**: 15,706 stars flagship ML toolkit for Kubernetes
- **TeglonLabs/mathpix-gem**: `Transform mathematical images to LaTeX` — Ruby, MIT license, pushed 2026-01-01
- **migalkin/NodePiece**: Compositional KG representations ICLR'22 — 144 stars

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets)

All 28 Hamming swarm wallets returned **0.0 APT** — accounts have no CoinStore resource initialized (on-chain accounts holding no APT in the standard coin module).

| world | address (truncated) | balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A–Z   | 0x8699...–0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (responsive, 2-of-N threshold):

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

All contracts require **2 signatures** — standard 2-of-2 multisig configuration for each named pair.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Vercel-deployed SPA behind authentication. All endpoints (`/`, `/api/markets`, `/api/v1/markets`) return HTTP 200 with a Vercel auth-wall page. No market data extractable without bypass token or Vercel MCP server access.

---

## DuckDB Schema Summary

| table | rows | description |
|-------|------|-------------|
| world_increments | 198 | GF(3)-tagged increment events per repo snapshot |
| repo_snapshots | 198 | Full repo metadata (stars, forks, language, pushed_at) |
| aptos_snapshots | 28 | APT balance for each Hamming swarm wallet |
| multisig_probes | 5 | Multisig threshold probes (A-B, A-G, Y-Z, S-T, V-W) |
| mnx_snapshots | 1 | Placeholder — MNX unavailable (auth required) |

**Total sources swept:** 11 GitHub orgs/users  
**Total repos captured:** 198 (representative sample across all sources)  
**GF(3) distribution:** ERGODIC(#d3869b)=73 · PLUS(#b8bb26)=74 · MINUS(#cc241d)=74  
**Aptos wallets probed:** 28 (alice, bob, A-Z)  
**Multisig contracts healthy:** 5/5  
