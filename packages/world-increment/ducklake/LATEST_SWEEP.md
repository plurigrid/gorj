# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-23  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Notes |
|--------|------|-------|
| plurigrid | org | 100 repos total (40 key repos ingested) |
| kubeflow | org | 47 repos total (13 top repos ingested) |
| TeglonLabs | org | 5 repos (all) |
| bmorphism | user | 100 repos total (15 key repos ingested) |
| zubyul | user | 49 repos total (10 key repos ingested) |
| migalkin | user | 19 repos (5 top ingested) |
| DJedamski | user | 6 repos (2 ingested) |
| wasita | user | 11 repos (3 ingested) |
| kristinezheng | user | 5 repos (2 ingested) |
| M1shaaa | user | 8 repos (2 ingested) |
| AustinCStone | user | 40 repos (4 ingested) |

**Total world_increments inserted this run:** 102  
**GF3 color distribution:** ERGODIC #d3869b (34), PLUS #b8bb26 (34), MINUS #cc241d (34)

### Most Active Repos (Today, 2026-06-23)

| Repo | Pushed | Stars |
|------|--------|-------|
| kubeflow/pipelines | 2026-06-23T08:04Z | 4,157 |
| plurigrid/gorj | 2026-06-23T07:12Z | 0 (760 issues) |
| kubeflow/spark-operator | 2026-06-23T05:50Z | 3,128 |
| kubeflow/sdk | 2026-06-23T03:04Z | 120 |
| plurigrid/eirobri | 2026-06-23T02:23Z | 0 |
| bmorphism/Gay.jl | 2026-06-23T00:40Z | 2 (187 open issues) |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,739 | — |
| kubeflow/pipelines | 4,157 | Python |
| kubeflow/spark-operator | 3,128 | Python |
| kubeflow/katib | 1,685 | Python |
| kubeflow/trainer | 2,119 | Go |
| kubeflow/examples | 1,460 | Jsonnet |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 26 | HTML |

### Most Open Issues

| Repo | Issues |
|------|--------|
| plurigrid/gorj | 760 |
| kubeflow/pipelines | 448 |
| bmorphism/Gay.jl | 187 |
| kubeflow/sdk | 134 |
| kubeflow/trainer | 131 |
| kubeflow/katib | 116 |

### Notable Observations

- **plurigrid/gorj** (this repo): 760 open issues, pushed 07:12Z today — most active plurigrid repo
- **plurigrid/eirobri**: pushed 02:23Z today — EiRoBri replay world active
- **bmorphism/Gay.jl**: active today, 187 open issues — GF(3) color determinism under heavy development
- **kubeflow** ecosystem: pipelines, sdk, spark-operator, trainer all pushed within last 24h
- **TeglonLabs/jank-crane** (C++): latest push 2026-06-08, crane-jank converged-IR hub with GF3 convergence maps
- **AustinCStone** connection: `bmfork` + `bmforkupdate` repos indicate active cross-collaboration with bmorphism

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)

**Status: ALL 28 WALLETS UNFUNDED**

Aptos mainnet fullnode returns `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on all 28 swarm addresses. No APT coin stores initialized.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | unfunded |
| bob | 0x0a3c...512d | unfunded |
| A–Z (26 addrs) | 0x8699... – 0x7af0... | all unfunded |

### Multisig Contract Probes

**All 5 contracts healthy — 2-of-N threshold confirmed.**

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment auth. No market data accessible from this environment.

---

## DuckDB Schema

```
world_increments  -- GF3-colored repo snapshot events
repo_snapshots    -- cumulative repo snapshots (stars, forks, issues, pushed_at)
aptos_snapshots   -- Hamming swarm wallet balances (all null this run)
multisig_probes   -- 2-of-N multisig health checks
mnx_snapshots     -- MNX market tickers (empty, unavailable)
```

## GF(3) Color Chain (this run)

| id%3 | Trit | Color | Name |
|------|------|-------|------|
| 0 | 0 | #d3869b | ERGODIC |
| 1 | +1 | #b8bb26 | PLUS |
| 2 | -1 | #cc241d | MINUS |
