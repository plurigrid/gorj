# World Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-06-14  
**GF(3) color chain:** trit=0 ERGODIC #d3869b | trit=1 PLUS #b8bb26 | trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos captured |
|--------|------|----------------|
| plurigrid | org | 20 |
| kubeflow | org | 20 |
| TeglonLabs | org | 5 |
| bmorphism | user | 19 |
| zubyul | user | 10 |
| migalkin | social | 5 |
| wasita | social | 5 |
| AustinCStone | social | 5 |
| DJedamski | social | 3 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| **Total** | | **98** |

### Notable repos (most recently pushed)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/gorj | 0 | Clojure | 2026-06-14 |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-14 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| bmorphism/satreadout | 0 | Lean | 2026-06-10 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |
| kubeflow/website | 184 | HTML | 2026-06-13 |
| kubeflow/pipelines | 4153 | Python | 2026-06-13 |
| kubeflow/trainer | 2114 | Go | 2026-06-13 |

### Top repos by stars (cross-network)
| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15720 |
| kubeflow/pipelines | 4153 |
| kubeflow/spark-operator | 3127 |
| kubeflow/trainer | 2114 |
| kubeflow/katib | 1683 |
| kubeflow/examples | 1461 |
| migalkin/NodePiece | 144 |
| AustinCStone/TextGAN | 92 |
| migalkin/StarE | 89 |
| bmorphism/ocaml-mcp-sdk | 61 |
| plurigrid/asi | 26 |
| bmorphism/risc0-cosmwasm-example | 23 |
| bmorphism/anti-bullshit-mcp-server | 23 |

### GF(3) increment distribution
- ERGODIC (trit=0, #d3869b): 33 increments (ids 3,6,9,...)
- PLUS (trit=1, #b8bb26): 33 increments (ids 1,4,7,...)
- MINUS (trit=-1, #cc241d): 32 increments (ids 2,5,8,...)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses: alice, bob, A-Z)
All 28 addresses returned **0.0 APT** — no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource found. These accounts are either dormant or have not registered an APT CoinStore on mainnet.

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z | 0x8699ed...–0x7af0ef... | 0.0 each |

**Total swarm APT:** 0.0

### Multisig Probes (5 contracts)
All 5 multisig contracts responded successfully. Every contract requires **2-of-N signatures** and is marked **healthy**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | YES |
| A-G | 0xf56c4a... | 2 | YES |
| Y-Z | 0xd3ffe1... | 2 | YES |
| S-T | 0x3b1c3a... | 2 | YES |
| V-W | 0x40fad7... | 2 | YES |

**All 5 multisigs healthy — uniform 2-of-N threshold.**

### MNX Markets
`testnet.mnx.fi` is **unavailable** — protected by Vercel deployment authentication. All API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) returned HTML auth challenge rather than JSON data.

---

## DuckDB Schema Summary
```
world_increments: 98 rows (GF3-tagged repo push events)
repo_snapshots:   98 rows (org/user/social repo metadata)
aptos_snapshots:  28 rows (all 0.0 APT)
multisig_probes:   5 rows (all healthy, sigs_required=2)
mnx_snapshots:     0 rows (unavailable)
```

## Observations
1. **plurigrid/gorj** was pushed just hours before this sweep (2026-06-14 07:17 UTC) — active development.
2. **bmorphism/Gay.jl** has 189 open issues and was pushed today (2026-06-14) — high activity.
3. **plurigrid/gorj** has 566 open issues — largest issue count in the network.
4. The Hamming swarm (A-Z + alice + bob) has **zero on-chain APT** — all wallets dormant on mainnet CoinStore.
5. All 5 multisig contracts are structurally sound with consistent 2-of-N threshold.
6. **kubeflow** remains the most starred org in the sweep (15k+ stars on main repo, active in June 2026).
7. **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) is the newest TeglonLabs repo, focused on GF3 convergence maps.
