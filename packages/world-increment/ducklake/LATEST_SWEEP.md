# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-03T04:00:00Z  
**Branch:** world-increment/sweep-2026-06-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|----------------|
| plurigrid | org | 50 |
| kubeflow | org | 25 |
| TeglonLabs | org | 4 |
| bmorphism | user | 26 |
| zubyul | user | 23 |
| migalkin | social-graph | 7 |
| wasita | social-graph | 7 |
| AustinCStone | social-graph | 6 |
| kristinezheng | social-graph | 6 |
| M1shaaa | social-graph | 6 |
| DJedamski | social-graph | 6 |
| **Total** | | **165** |

### Top Repos by Stars

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,704 | — | 2026-05-24 |
| kubeflow/pipelines | 4,151 | Python | 2026-06-02 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-01 |
| kubeflow/trainer | 2,110 | Go | 2026-06-03 |
| kubeflow/katib | 1,685 | Python | 2026-05-29 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/arena | 811 | Go | 2026-05-07 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 24 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | 2022-10-20 |

### Most Active (by open issues)

| Repo | Open Issues |
|------|------------|
| kubeflow/pipelines | 487 |
| kubeflow/docs-agent | 154 |
| plurigrid/gorj | 315 |
| bmorphism/Gay.jl | 189 |
| plurigrid/eirobri | 28 |
| plurigrid/nanoclj-zig | 20 |

### GF(3) Color Chain Applied
- `id % 3 == 0` → trit=0 **ERGODIC** `#d3869b`
- `id % 3 == 1` → trit=1 **PLUS** `#b8bb26`
- `id % 3 == 2` → trit=-1 **MINUS** `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets: alice, bob, A–Z)

All 28 Hamming swarm wallets probed via Aptos mainnet fullnode
(`https://fullnode.mainnet.aptoslabs.com/v1`).

**Result:** All wallets returned 0.00000000 APT — no `CoinStore<AptosCoin>` resource  
found on mainnet (wallets unfunded or no coin store initialized).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B–Z | (25 addresses) | 0.00000000 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...3003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All multisigs require **2-of-N** signatures. All live and responsive.

### MNX Markets

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE**  
SPA endpoint returns no structured API data at common probe paths.

---

## DuckDB Schema Summary

```
world_increments  — 165 rows  (GF3-colored GitHub repo events)
repo_snapshots    — 165 rows  (org/user/repo metadata snapshot)
aptos_snapshots   —  28 rows  (Hamming swarm wallet balances)
multisig_probes   —   5 rows  (multisig sig-threshold probes)
mnx_snapshots     —   0 rows  (MNX unavailable)
```

## Example Queries

```sql
-- Top repos by stars
SELECT full_name, stars, language FROM repo_snapshots
ORDER BY stars DESC LIMIT 20;

-- GF3 trit distribution
SELECT gf3_name, gf3_color, COUNT(*) FROM world_increments
GROUP BY gf3_name, gf3_color;

-- Recently pushed plurigrid repos
SELECT repo_name, pushed_at FROM repo_snapshots
WHERE org_or_user = 'plurigrid'
ORDER BY pushed_at DESC LIMIT 10;

-- All healthy multisigs
SELECT pair, address, sigs_required FROM multisig_probes
WHERE healthy = true;

-- Aptos swarm summary
SELECT world, balance_apt FROM aptos_snapshots
ORDER BY world;
```
