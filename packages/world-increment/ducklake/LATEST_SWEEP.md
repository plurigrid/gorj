# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-30  
**DuckDB:** `world-increments.duckdb` (v1.5.3 Variegata)  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 44 |
| zubyul | user | 21 |
| AustinCStone | user | 7 |
| migalkin | user | 6 |
| wasita | user | 6 |
| DJedamski | user | 4 |
| TeglonLabs | org | 4 |
| kristinezheng | user | 4 |
| M1shaaa | user | 3 |
| **TOTAL** | | **299** |

### Top Repos by Stars (all sources)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,687 | — |
| kubeflow/pipelines | 4,150 | Python |
| kubeflow/spark-operator | 3,124 | Python |
| kubeflow/trainer | 2,107 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,463 | Jsonnet |
| kubeflow/manifests | 1,019 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| kubeflow/mpi-operator | 527 | Go |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |
| plurigrid/asi | 23 | HTML |
| bmorphism/say-mcp-server | 20 | JavaScript |

### Notable Observations

- **plurigrid/gorj** (this repo): 261 open issues, last push 2026-05-30T05:12:06Z — most active plurigrid repo
- **bmorphism/Gay.jl**: 189 open issues — heaviest issue load in swarm
- **kubeflow/trainer** freshest kubeflow push (2026-05-30T03:14:50Z): Distributed AI Training on Kubernetes
- Social graph spans ML/KG research (migalkin), neuro/bioinformatics (zubyul, kristinezheng, M1shaaa, wasita), AI/systems (AustinCStone, DJedamski)
- bmorphism most active language: Zig (nanoclj-zig, zig-syrup, duck-rs, open-location-code-zig) + OCaml MCP toolchain
- plurigrid theme: GF(3) trit coloring, Gay.jl, OCapN Syrup, open games, Babashka/Clojure

### GF(3) Color Distribution

```
ERGODIC #d3869b (trit= 0):  99 increments
PLUS    #b8bb26 (trit=+1): 100 increments
MINUS   #cc241d (trit=-1): 100 increments
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `fullnode.mainnet.aptoslabs.com` → `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 addresses (alice, bob, A–Z) returned **0.0 APT**.  
Consistent with accounts that exist on-chain but have uninitialized CoinStore resources or zero balance.

### Multisig Contract Probes

Probed `0x1::multisig_account::num_signatures_required` for all 5 pairs:

| Pair | Contract (truncated) | Sigs Required | Status |
|------|----------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✅ HEALTHY |

All 5 contracts require **2-of-N signatures**. All probes responsive and healthy.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA with client-side rendering. `/api/markets` returns the HTML shell, not JSON. **Market data unavailable** at sweep time — `mnx_snapshots` table has 0 rows.

---

## DuckDB Schema

```sql
world_increments  -- GF(3) colored event log    (299 rows)
repo_snapshots    -- Full repo metadata          (299 rows)
aptos_snapshots   -- Hamming swarm balances      (28 rows)
multisig_probes   -- Aptos multisig health       (5 rows)
mnx_snapshots     -- MNX market data             (0 rows — SPA unavailable)
```

## Example Queries

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots ORDER BY stars DESC LIMIT 20;

-- GF(3) color breakdown
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY gf3_name, gf3_color;

-- Most active repos (most open issues)
SELECT full_name, open_issues, pushed_at FROM repo_snapshots ORDER BY open_issues DESC LIMIT 10;

-- All healthy multisig contracts
SELECT pair, address, sigs_required FROM multisig_probes WHERE healthy = true;

-- Aptos swarm balances
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
