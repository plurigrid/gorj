# World-Increment Sweep + Hamming Swarm Snapshot
**Run:** 2026-06-17 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **131 repos** snapshotted across 11 sources
- **GF(3) trit chain:** ERGODIC=43 (#d3869b), PLUS=44 (#b8bb26), MINUS=44 (#cc241d)

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 30 |
| kubeflow | org | 18 |
| TeglonLabs | org | 5 |
| bmorphism | user | 20 |
| zubyul | user | 14 |
| migalkin | social | 8 |
| wasita | social | 7 |
| DJedamski | social | 6 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 10 |

### Notable Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,728 | — | 2026-06-17 |
| kubeflow/pipelines | 4,154 | Python | 2026-06-17 |
| kubeflow/spark-operator | 3,127 | Python | 2026-06-17 |
| kubeflow/trainer | 2,115 | Go | 2026-06-17 |
| kubeflow/katib | 1,683 | Python | 2026-06-15 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/gorj | 0 | Clojure | 2026-06-17 (640 open issues) |

### Hot Repos (pushed today 2026-06-17)
- **plurigrid/gorj** — forj + Rama topology nREPL routing + GF(3) gay trit coloring (640 issues)
- **bmorphism/Gay.jl** — Wide-gamut color sampling with splittable determinism (187 issues)
- **kubeflow/hub**, **kubeflow/trainer**, **kubeflow/kale**, **kubeflow/community**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z)
All 28 addresses queried against Aptos mainnet fullnode.  
**Result:** All wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
This indicates the wallets have not registered the legacy CoinStore resource (may be uninitialized or use the newer Fungible Asset framework).  
**All balances recorded as 0.0 APT.**

### Multisig Contract Probes (5 pairs)
All probed via POST /v1/view -> 0x1::multisig_account::num_signatures_required

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...4987003 | 2 | healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | healthy |
| Y-Z | 0xd3ffe181...75b883 | 2 | healthy |
| S-T | 0x3b1c3ae9...ed7883 | 2 | healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | healthy |

**All 5 multisig contracts healthy, 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — All endpoints return HTTP 401 (Vercel Deployment Protection).  
No market data accessible without authentication token.

---

## DuckDB Tables
```
world_increments  : 131 rows  (GitHub repo events, GF3-colored)
repo_snapshots    : 131 rows  (full repo metadata)
aptos_snapshots   :  28 rows  (28 wallets, all 0.0 APT)
multisig_probes   :   5 rows  (5 pairs, all healthy)
mnx_snapshots     :   0 rows  (unavailable)
```

## GF(3) Chain Verification
```
id%3==0 => trit=0  ERGODIC #d3869b : 43 increments
id%3==1 => trit=1  PLUS    #b8bb26 : 44 increments
id%3==2 => trit=-1 MINUS   #cc241d : 44 increments
```
