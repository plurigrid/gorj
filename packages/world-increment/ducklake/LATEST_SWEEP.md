# World-Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-06-14  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Snapshotted | Total Stars | GF(3) |
|--------|------|:-----------------:|:-----------:|-------|
| plurigrid | org | 100 | 138 | #b8bb26 PLUS (trit=1) |
| kubeflow | org | 48 | 98,693 | #cc241d MINUS (trit=-1) |
| TeglonLabs | org | 5 | 14 | #d3869b ERGODIC (trit=0) |
| bmorphism | user | 104 | 444 | #b8bb26 PLUS (trit=1) |
| zubyul | user | 49 | 29 | #cc241d MINUS (trit=-1) |
| migalkin | user | 19 | 830 | #d3869b ERGODIC (trit=0) |
| DJedamski | user | 6 | 2 | #b8bb26 PLUS (trit=1) |
| wasita | user | 11 | 5 | #cc241d MINUS (trit=-1) |
| kristinezheng | user | 5 | 0 | #d3869b ERGODIC (trit=0) |
| M1shaaa | user | 8 | 0 | #b8bb26 PLUS (trit=1) |
| AustinCStone | user | 40 | 323 | #cc241d MINUS (trit=-1) |

**Total repos in DB:** 1,003 (cumulative across runs)

### Notable Repos (by stars)

**kubeflow:**
- `kubeflow/kubeflow` — 15,720 stars — Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — 4,153 stars — Machine Learning Pipelines
- `kubeflow/spark-operator` — 3,127 stars — Kubernetes Spark operator
- `kubeflow/trainer` — 2,114 stars — Distributed AI Model Training

**plurigrid:**
- `plurigrid/gorj` — 565 open issues, pushed 2026-06-14 (today, very active)
- `plurigrid/asi` — 26 stars — "everything is topological chemputer!"
- `plurigrid/vcg-auction` — 7 stars — CosmWasm VCG auction
- `plurigrid/ontology` — 8 stars — "autopoietic ergodicity and embodied gradualism"

**bmorphism:**
- `bmorphism/ocaml-mcp-sdk` — 61 stars — OCaml SDK for MCP
- `bmorphism/anti-bullshit-mcp-server` — 23 stars
- `bmorphism/Gay.jl` — 189 open issues, pushed today
- `bmorphism/say-mcp-server` — 20 stars
- `bmorphism/babashka-mcp-server` — 19 stars

**migalkin (social graph):**
- `migalkin/NodePiece` — 144 stars — Knowledge graph embeddings (ICLR'22)
- `migalkin/StarE` — 89 stars — Hyper-Relational Knowledge Graphs (EMNLP 2020)

**AustinCStone (social graph):**
- `AustinCStone/TextGAN` — 92 stars — Text GAN in TensorFlow

### GF(3) Color Chain (world_increments sequence)

```
id=1  trit=1  PLUS     #b8bb26  plurigrid
id=2  trit=-1 MINUS    #cc241d  kubeflow
id=3  trit=0  ERGODIC  #d3869b  TeglonLabs
id=4  trit=1  PLUS     #b8bb26  bmorphism
id=5  trit=-1 MINUS    #cc241d  zubyul
id=6  trit=0  ERGODIC  #d3869b  migalkin
id=7  trit=1  PLUS     #b8bb26  DJedamski
id=8  trit=-1 MINUS    #cc241d  wasita
id=9  trit=0  ERGODIC  #d3869b  kristinezheng
id=10 trit=1  PLUS     #b8bb26  M1shaaa
id=11 trit=-1 MINUS    #cc241d  AustinCStone
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance` view function at ledger version ~5.73B.

| World | APT Balance |
|-------|-------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| alice | 0.436434 |
| O | 0.210136 |
| K | 0.161961 |
| P | 0.140136 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| S | 0.091788 |
| R | 0.090217 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

**Total APT across swarm:** ~22.37 APT  
**Note:** Accounts use FungibleAsset standard; balances fetched via `0x1::coin::balance` view function.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4f428... | 2 | YES |
| A-G | 0xf56c4a1c... | 2 | YES |
| Y-Z | 0xd3ffe181... | 2 | YES |
| S-T | 0x3b1c3ae9... | 2 | YES |
| V-W | 0x40fad7b4... | 2 | YES |

**All multisig contracts healthy: 2-of-N threshold on all pairs.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` requires Vercel authentication. No market data extractable without credentials.

---

## DuckDB Schema Summary

```
world_increments  34 rows (cumulative)
repo_snapshots    1,003 rows (cumulative)
aptos_snapshots   28 rows (this run)
multisig_probes   5 rows (this run)
mnx_snapshots     0 rows (auth unavailable)
```

*Sweep completed: 2026-06-14 UTC*
