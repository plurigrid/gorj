# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-06-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshot

| Source | Type | Repos Captured |
|---|---|---|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| wasita | user (social) | 11 |
| migalkin | user (social) | 10 |
| AustinCStone | user (social) | 10 |
| M1shaaa | user (social) | 8 |
| kristinezheng | user (social) | 6 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 4 |
| **Total** | | **352** |

### GF(3) Color Distribution

| GF(3) Name | Color | Trit | Count |
|---|---|---|---|
| ERGODIC | #d3869b (pink) | 0 | 117 |
| PLUS | #b8bb26 (yellow-green) | +1 | 118 |
| MINUS | #cc241d (red) | -1 | 117 |

### Top Starred Repos

| Repo | Language | Stars | Forks | Last Push |
|---|---|---|---|---|
| kubeflow/kubeflow | — | 15,705 | 2,668 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,151 | 2,004 | 2026-06-03 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 | 2026-06-03 |
| kubeflow/trainer | Go | 2,110 | 963 | 2026-06-03 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-05-29 |
| kubeflow/examples | Jsonnet | 1,462 | 755 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,020 | 1,065 | 2026-06-02 |
| kubeflow/arena | Go | 811 | 191 | 2026-05-07 |
| kubeflow/kale | Python | 691 | 155 | 2026-06-01 |
| kubeflow/mpi-operator | Go | 528 | 235 | 2026-06-02 |
| kubeflow/mcp-apache-spark-history-server | Python | 173 | 61 | 2026-06-01 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| plurigrid/asi | HTML | 24 | 6 | 2026-04-26 |

### Most Recently Pushed (since 2026-05-01)

| Repo | Last Push |
|---|---|
| kubeflow/trainer | 2026-06-03T17:02Z |
| kubeflow/spark-operator | 2026-06-03T17:01Z |
| plurigrid/gorj | 2026-06-03T16:16Z |
| kubeflow/hub | 2026-06-03T15:29Z |
| kubeflow/sdk | 2026-06-03T15:18Z |
| kubeflow/pipelines | 2026-06-03T07:21Z |
| plurigrid/place | 2026-06-03T07:12Z |
| bmorphism/Gay.jl | 2026-06-03T00:48Z |
| plurigrid/eirobri | 2026-05-26T07:23Z |
| plurigrid/nash-portal | 2026-05-19T01:49Z |

### Notable Plurigrid Repos

| Repo | Language | Stars | Description |
|---|---|---|---|
| plurigrid/asi | HTML | 24 | everything is topological chemputer |
| plurigrid/ontology | JavaScript | 8 | autopoietic ergodicity and embodied gradualism |
| plurigrid/vcg-auction | Rust | 7 | VCG auction CosmWasm contract |
| plurigrid/agent | Python | 5 | Agency amplification framework |
| plurigrid/StochFlow | Python | 4 | stochastic interpolant models |
| plurigrid/asi-skills | Julia | 3 | 69 skills w/ Galois Hole Type accessibility |
| plurigrid/gorj | Clojure | 0 | forj + Rama topology nREPL (328 open issues!) |
| plurigrid/zig-syrup | Zig | 2 | OCapN Syrup high-perf Zig impl |
| plurigrid/nanoclj-zig | Zig | 1 | NaN-boxed Clojure interpreter in Zig 0.15 |

### Notable bmorphism Repos

| Repo | Language | Stars | Description |
|---|---|---|---|
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | OCaml SDK for MCP using Jane Street oxcaml_effect |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | Claim validation + manipulation detection |
| bmorphism/say-mcp-server | JavaScript | 20 | macOS TTS MCP server |
| bmorphism/babashka-mcp-server | JavaScript | 18 | Babashka/Clojure MCP server |
| bmorphism/Gay.jl | Julia | 1 | Wide-gamut color sampling w/ splittable determinism |

### Notable zubyul Repos

| Repo | Language | Stars | Description |
|---|---|---|---|
| zubyul/gay-world | Python | 1 | Goblin world builder w/ MLX task decomposition |
| zubyul/WGCNA | HTML | 2 | weighted gene correlation network analysis |
| zubyul/Nikolova_lab_data_analysis | R | 2 | HCP connectome study |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

All 28 Hamming-swarm addresses probed against Aptos mainnet.  
Endpoint: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | APT Balance |
|---|---|---|
| alice | 0xc793…cc7b | 0.00 APT |
| bob | 0x0a3c…2d5d | 0.00 APT |
| A | 0x8699…9d7a | 0.00 APT |
| B | 0x3f89…b13 | 0.00 APT |
| C | 0x38b9…35e | 0.00 APT |
| D–Z (24 wallets) | … | 0.00 APT each |

**Status:** All 28 accounts return 0 APT (CoinStore not initialized / unfunded on mainnet at sweep time).

### Multisig Account Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4…7003 | 2 | YES |
| A-G | 0xf56c…0096 | 2 | YES |
| S-T | 0x3b1c…7883 | 2 | YES |
| V-W | 0x40fa…eb6d | 2 | YES |
| Y-Z | 0xd3ff…b883 | 2 | YES |

All 5 multisig contracts respond with `num_signatures_required = 2`. **All healthy.**

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` serves a Next.js SPA. No public REST API endpoints responding at `/api/markets` or `/api/v1/markets`. Market data is client-side rendered — **unavailable via static probe**.

---

## DuckDB Schema Summary

```sql
world_increments  -- 352 rows  (GF3-colored repo push events)
repo_snapshots    -- 352 rows  (full repo metadata per increment)
aptos_snapshots   --  28 rows  (Hamming swarm wallet balances)
multisig_probes   --   5 rows  (multisig sig-threshold probes)
mnx_snapshots     --   0 rows  (SPA - no API data available)
```

## GF(3) Color Chain Key

```
id % 3 == 0  →  trit= 0  ERGODIC  #d3869b  (pink)
id % 3 == 1  →  trit=+1  PLUS     #b8bb26  (yellow-green)
id % 3 == 2  →  trit=-1  MINUS    #cc241d  (red)
```

Balanced distribution: ERGODIC=117, PLUS=118, MINUS=117 across 352 repo increments.
