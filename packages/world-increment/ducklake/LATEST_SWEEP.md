# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-06
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept (GF(3) Color Chain)

| Inc ID | Trit | Color | GF3 Name | Source | Repos |
|--------|------|-------|----------|--------|-------|
| 1 | +1 | #b8bb26 | PLUS | plurigrid (org) | 99 |
| 2 | -1 | #cc241d | MINUS | kubeflow (org) | 48 |
| 3 | 0 | #d3869b | ERGODIC | TeglonLabs (org) | 4 |
| 4 | +1 | #b8bb26 | PLUS | bmorphism (user) | 100 |
| 5 | -1 | #cc241d | MINUS | zubyul (user) | 49 |
| 6 | 0 | #d3869b | ERGODIC | migalkin (user) | 19 |
| 7 | +1 | #b8bb26 | PLUS | DJedamski (user) | 6 |
| 8 | -1 | #cc241d | MINUS | kristinezheng (user) | 5 |
| 9 | 0 | #d3869b | ERGODIC | M1shaaa (user) | 8 |
| 10 | +1 | #b8bb26 | PLUS | wasita (user) | 11 |
| 11 | -1 | #cc241d | MINUS | AustinCStone (user) | 40 |
| 12 | 0 | #d3869b | ERGODIC | aptos_hamming_swarm (event) | — |
| 13 | +1 | #b8bb26 | PLUS | multisig_probe (event) | — |
| 14 | -1 | #cc241d | MINUS | mnx_markets (event) | — |

**Total:** 389 repos snapshotted across 11 GitHub sources

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,706 | — |
| kubeflow/pipelines | 4,152 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,111 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 528 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| migalkin/NodePiece | 144 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |

### Notable Activity (2026-06-06)

- **plurigrid/gorj** (this repo): 391 open issues, pushed today — most active repo
- **bmorphism/Gay.jl**: 189 open issues, pushed today — highest open issue count
- **kubeflow/notebooks**: pushed today, 182 open issues
- **M1shaaa/M1shaaa**: profile repo pushed today

### Social Graph Highlights

- **bmorphism** (100 repos): MCP server ecosystem, category theory, Julia/OCaml/Zig/Clojure — ocaml-mcp-sdk (61★), Gay.jl, babashka-mcp-server (19★)
- **zubyul** (49 repos): Worlds/multiplayer experiments, Gay.jl color work, neuro bio-data analysis
- **plurigrid** (99 repos): Clojure/Zig/Rust, VCG auctions, Gay.jl derivatives, gorj (391 issues)
- **migalkin** (19 repos): KG research — NodePiece (144★), StarE (89★), NBFNet-MLX
- **TeglonLabs** (4 repos): mathpix-gem (Ruby), coin-flip-mcp, monad-mcp-server, topoi
- **wasita** (11 repos): WiNS network science site, Svelte apps, TypeScript tooling
- **kristinezheng** (5 repos): Cognitive science / MIT coursework
- **M1shaaa** (8 repos): Lookit cognitive experiments (Yale/Columbia)
- **DJedamski** (6 repos): Kaggle competitions, statistical modeling in R
- **AustinCStone** (40 repos): TextGAN (92★), StereoVisionMRF (11★), ML research

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

Queried 28 addresses (alice, bob, A–Z) against Aptos mainnet fullnode.

| Metric | Value |
|--------|-------|
| Wallets queried | 28 |
| Total APT | 0.0 |
| Min / Max balance | 0.0 / 0.0 APT |
| Status | All CoinStore resources return value=0 |

All Hamming swarm addresses hold **0.0 APT** — these are unfunded addresses on mainnet.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Contract Address (abbrev.) | Sigs Required | Status |
|------|--------------------------|--------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...e75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...c80eb6d | 2 | HEALTHY |

All 5 multisig accounts are **2-of-2** and responding. Hamming swarm multisig fabric is fully operational.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE**

`testnet.mnx.fi` is protected by Vercel deployment authentication. All API paths
(`/api/markets`, `/api/v1/markets`, `/api/tickers`) return 401 with instructions
to use `vercel curl`, Vercel MCP Server, or a Protection Bypass token.

`mnx_snapshots` table remains empty this sweep.

---

## DuckDB Schema Summary

```
world_increments  14 rows  GF(3) color-chained sweep increment records
repo_snapshots   389 rows  GitHub repo metadata (stars, forks, language, pushed_at)
aptos_snapshots   28 rows  Hamming swarm wallet balances (all 0.0 APT)
multisig_probes    5 rows  Multisig health probes (all 2-of-2 HEALTHY)
mnx_snapshots      0 rows  MNX market data (UNAVAILABLE - Vercel auth)
```

## GF(3) Color Chain

| id%3 | Trit | Name | Hex |
|------|------|------|-----|
| 1 | +1 | PLUS | #b8bb26 |
| 2 | -1 | MINUS | #cc241d |
| 0 | 0 | ERGODIC | #d3869b |
