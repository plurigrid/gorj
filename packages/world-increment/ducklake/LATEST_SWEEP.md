# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-14  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 45 |
| kubeflow | org | 33 |
| TeglonLabs | org | 4 |
| bmorphism | user | 55 |
| zubyul | user | 27 |
| migalkin | user (social) | 7 |
| DJedamski | user (social) | 6 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 8 |
| wasita | user (social) | 10 |
| AustinCStone | user (social) | 9 |
| **TOTAL** | | **205** |

### GF(3) Trit Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 68 |
| 1 | `#b8bb26` | PLUS | 69 |
| -1 | `#cc241d` | MINUS | 68 |

### Top Repos by Stars

| Repo | Stars |
|------|-------|
| kubeflow/kubeflow | 15,629 |
| kubeflow/pipelines | 4,140 |
| kubeflow/spark-operator | 3,125 |
| kubeflow/trainer | 2,098 |
| kubeflow/katib | 1,682 |
| kubeflow/examples | 1,462 |
| kubeflow/manifests | 1,017 |
| kubeflow/arena | 810 |
| kubeflow/kale | 686 |
| kubeflow/mpi-operator | 526 |
| migalkin/NodePiece | 144 |
| bmorphism/Gay.jl | 1 (188 open issues) |
| plurigrid/gorj | 0 (185 open issues) |

### Notable Activity

- **bmorphism**: Dense MCP ecosystem (say-mcp, manifold-mcp, babashka-mcp, anti-bullshit-mcp, nats-mcp, marginalia-mcp), OCaml MCP SDK (61 stars), Gay.jl with 188 open issues; zig-syrup, postweb, vibesnipe-market Move contracts
- **zubyul**: NASH token TUIs (Rust/WASM), Gay.jl fork, tilelang GPU kernels for GF(3), OpenBCI visualizer in Zig; plurigrid-site active
- **plurigrid**: gorj (this repo) at top pushed_at, Gay.jl/GF(3) ecosystem (gay-rs, gay-go, gay-terminal, lazygay), nanoclj-zig NaN-boxed interpreter; spritely mirror repos
- **TeglonLabs**: mathpix-gem Ruby gem (security-first math OCR), monad-mcp-server, topoi (Python), coin-flip-mcp
- **migalkin**: KG ML research — NodePiece (144★), StarE (89★), NBFNet MLX, RWL
- **kubeflow**: Highly active ML platform; trainer (2098★), spark-operator (3125★), new mcp-apache-spark-history-server (168★)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All balances = 0.0 APT** — CoinStore resource not found (accounts uninitialized or migrated to FA standard post-v1.13).

### Multisig Contract Probes

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | HEALTHY |

All 5/5 multisig pairs are reachable on Aptos mainnet, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Next.js SPA — no REST API endpoints accessible. `/api/markets`, `/api/v1/markets`, `/api/status` all return no data. Status: **UNAVAILABLE**.

---

## DuckDB Schema Summary

```
world_increments   205 rows  GF3-colored increment log
repo_snapshots     205 rows  org/user -> repo metadata  
aptos_snapshots     28 rows  alice-Z APT wallet balances
multisig_probes      5 rows  A-B, A-G, Y-Z, S-T, V-W
mnx_snapshots        0 rows  API unavailable
```

## Example Queries

```sql
-- Repo counts by source
SELECT org_or_user, COUNT(*) FROM repo_snapshots GROUP BY org_or_user ORDER BY 2 DESC;

-- GF3 trit balance check
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments GROUP BY 1, 2;

-- Stars leaderboard
SELECT full_name, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 20;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Hamming swarm balances
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;
```
