# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-10T10:06 UTC  
**Branch:** world-increment/sweep-2026-06-10-1006  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 20 |
| kubeflow | org | 18 |
| TeglonLabs | org | 5 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| migalkin | user | 7 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| AustinCStone | user | 7 |
| **Total** | | **112** |

### Top Repos by Stars (GF3 Color-Coded)

| Repo | Stars | Language | GF3 | Color |
|------|-------|----------|-----|-------|
| kubeflow/kubeflow | 15,714 | — | ERGODIC | #d3869b |
| kubeflow/pipelines | 4,153 | Python | PLUS | #b8bb26 |
| kubeflow/spark-operator | 3,126 | Python | MINUS | #cc241d |
| kubeflow/trainer | 2,112 | Go | ERGODIC | #d3869b |
| kubeflow/katib | 1,685 | Python | PLUS | #b8bb26 |
| kubeflow/examples | 1,462 | Jsonnet | MINUS | #cc241d |
| migalkin/NodePiece | 144 | Python | PLUS | #b8bb26 |
| migalkin/StarE | 89 | Python | PLUS | #b8bb26 |
| AustinCStone/TextGAN | 92 | Python | MINUS | #cc241d |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | ERGODIC | #d3869b |
| plurigrid/asi | 25 | HTML | PLUS | #b8bb26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MINUS | #cc241d |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | MINUS | #cc241d |

### Most Active (pushed June 2026)

- `plurigrid/gorj` — 475 open issues, pushed 2026-06-10 (this repo!)
- `bmorphism/Gay.jl` — 189 open issues, pushed 2026-06-10
- `kubeflow/trainer` / `kubeflow/dashboard` — pushed 2026-06-10
- `M1shaaa/M1shaaa` — pushed 2026-06-10
- `TeglonLabs/jank-crane` — crane-jank converged-IR hub, pushed 2026-06-08
- `kristinezheng/kristinezheng.github.io` — pushed 2026-06-07

### GF3 Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 37 |
| 1 | PLUS | #b8bb26 | 38 |
| -1 | MINUS | #cc241d | 37 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

All 28 hamming-swarm wallets (alice, bob, A-Z) probed via Aptos mainnet fullnode.  
**Result: All balances = 0.0 APT** — no APT held in CoinStore resources.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A-Z (26) | various | 0.0 each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts: `num_signatures_required = 2`. All **healthy**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | yes |
| A-G | 0xf56c4a... | 2 | yes |
| Y-Z | 0xd3ffe1... | 2 | yes |
| S-T | 0x3b1c3a... | 2 | yes |
| V-W | 0x40fad7... | 2 | yes |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — HTTP 401 Unauthorized on both `/api/markets` and root.
`mnx_snapshots` table is empty (0 rows).

---

## DuckDB Schema Summary

```
world_increments  112 rows  GF3-colored repo-push events
repo_snapshots    112 rows  org/user/repo metadata
aptos_snapshots    28 rows  hamming swarm wallet balances
multisig_probes     5 rows  sigs_required probe results
mnx_snapshots       0 rows  unavailable (401)
```

## Query Examples

```sql
-- Top repos by stars with GF3 color
SELECT rs.full_name, rs.stars, rs.language, wi.gf3_color, wi.gf3_name
FROM repo_snapshots rs JOIN world_increments wi ON rs.increment_id = wi.id
ORDER BY rs.stars DESC LIMIT 20;

-- All PLUS-trit repos (id%3==1)
SELECT full_name, stars FROM repo_snapshots rs
JOIN world_increments wi ON rs.increment_id = wi.id
WHERE wi.gf3_trit = 1 ORDER BY stars DESC;

-- Multisig health check
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos swarm balances
SELECT world, address, balance_apt FROM aptos_snapshots ORDER BY world;
```
