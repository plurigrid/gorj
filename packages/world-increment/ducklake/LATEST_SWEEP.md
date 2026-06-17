# World Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-06-17
**Run type:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Total Available |
|--------|------|---------------|-----------------|
| plurigrid | org | 50 | 101 |
| kubeflow | org | 48 | 48 |
| bmorphism | user | 50 | 104 |
| zubyul | user | 49 | 49 |
| TeglonLabs | org | 5 | 5 |
| migalkin | social | 4 | 19 |
| DJedamski | social | 2 | 6 |
| wasita | social | 3 | 11 |
| kristinezheng | social | 2 | 5 |
| M1shaaa | social | 2 | 8 |
| AustinCStone | social | 3 | 40 |
| **Total** | | **218** | **396** |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count |
|----------|-------|------|-------|
| ERGODIC | `#d3869b` | 0 | 72 |
| PLUS | `#b8bb26` | 1 | 73 |
| MINUS | `#cc241d` | -1 | 73 |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,725 | — | 2026-06-17 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-17 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-15 |
| kubeflow/trainer | 2,115 | Go | 2026-06-17 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,024 | YAML | 2026-06-17 |
| migalkin/NodePiece | 144 | Python | — |
| migalkin/StarE | 89 | Python | — |
| AustinCStone/TextGAN | 92 | Python | — |

### Notable Plurigrid Activity

- `plurigrid/gorj` — 629 open issues, last push **2026-06-17** (this repo)
- `plurigrid/asi` — 26 stars, HTML, "everything is topological chemputer!"
- `plurigrid/Gay.jl` (via bmorphism) — 187 open issues, pushed 2026-06-17
- `plurigrid/eirobri` — 29 open issues, EiRoBri replay world

### Notable bmorphism Activity

- `bmorphism/Gay.jl` — Julia, wide-gamut color sampling SPI, pushed 2026-06-17
- `bmorphism/ocaml-mcp-sdk` — 61 stars, OCaml MCP SDK with Jane Street oxcaml_effect
- `bmorphism/anti-bullshit-mcp-server` — 23 stars, JS claim analysis MCP

### TeglonLabs Repos

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub, GF3 convergence maps |
| mathpix-gem | Ruby | 2 | Mathematical image-to-LaTeX OCR |
| coin-flip-mcp | JavaScript | 0 | MCP server for random.org coin flips |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | — |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming swarm addresses (alice, bob, A-Z) queried against Aptos mainnet fullnode.

**Result: All wallets return 0.0 APT** — CoinStore resource not initialized on mainnet for these addresses. Accounts likely exist on devnet/testnet or have zero APT balance.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...5b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...d7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...0eb6d | 2 | HEALTHY |

**All 5/5 multisigs healthy — 2-of-N signatures required, contracts live on mainnet.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment authentication (auth challenge page). No market data extracted this run.

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 218 | GF(3)-colored increment log |
| `repo_snapshots` | 218 | Repo metadata per increment |
| `aptos_snapshots` | 28 | Hamming swarm APT balances |
| `multisig_probes` | 5 | Multisig contract health |
| `mnx_snapshots` | 0 | MNX markets (unavailable) |

GF(3) color chain: `id%3==0` ERGODIC `#d3869b` | `id%3==1` PLUS `#b8bb26` | `id%3==2` MINUS `#cc241d`
