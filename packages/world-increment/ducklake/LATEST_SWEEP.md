# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-05

## Sweep Metadata
- **Date:** 2026-05-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 141 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | Event | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | social_graph | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | social_graph | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | social_graph | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | social_graph | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | social_graph | -1 | `#cc241d` | **MINUS** |

GF(3) trit conservation: PLUS×4, MINUS×4, ERGODIC×3.  
Rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS.

### Repo Snapshots by Source

| Source | Repos | Total Stars | Notable |
|--------|-------|-------------|---------|
| kubeflow | 20 | 32,181 | kubeflow ★15,622; pipelines ★4,132; spark-operator ★3,123; trainer ★2,096 |
| migalkin | 7 | 277 | NodePiece ★143 (ICLR'22); StarE ★89 (EMNLP'20); NBFNet_mlx ★10 |
| bmorphism | 29 | 215 | ocaml-mcp-sdk ★60; TextGAN-adjacent; anti-bullshit-mcp ★23; risc0-cosmwasm ★23 |
| AustinCStone | 11 | 107 | TextGAN ★92; StereoVisionMRF ★11 |
| plurigrid | 30 | 46 | gorj (this repo) 74 open issues; asi ★18; ontology ★7 |
| zubyul | 15 | 9 | gay-world ★1; WGCNA ★2 |
| wasita | 8 | 4 | magic-garden ★2 |
| DJedamski | 6 | 3 | grad school data science |
| TeglonLabs | 4 | 2 | mathpix-gem ★2 |
| kristinezheng | 6 | 0 | MIT neuroscience / HackMIT |
| M1shaaa | 5 | 0 | Yale ML coursework, Lookit studies |
| **TOTAL** | **141** | **32,844** | |

### Signal: What Changed Since 2026-04-12

- **plurigrid/gorj** open issues: 0 → 74 (active sprint)
- **plurigrid/asi** stars: 16 → 18
- **kubeflow/kubeflow** stars: 15,565 → 15,622 (+57)
- **kubeflow/pipelines** stars: 4,119 → 4,132 (+13)
- **kubeflow/spark-operator** stars: 3,111 → 3,123 (+12)
- **bmorphism/Gay.jl**: 187 open issues (experimental project with heavy issue tracking)
- New repos: `plurigrid/reafference`, `zubyul/tilelang-kernels`, `zubyul/kinesis-kb360pro`, `bmorphism/nanoclj-zig`, `bmorphism/postweb`

### Social Graph Topology (zubyul neighbors)

| User | Domain | Language Mix |
|------|--------|-------------|
| migalkin | KG ML research | Python, Rust, R |
| DJedamski | Data science | R, Jupyter |
| wasita | Network science / Svelte | Svelte, TypeScript, Typst |
| kristinezheng | MIT neuroscience | Python, CSS, Jupyter |
| M1shaaa | Yale ML / Lookit | TypeScript, Python |
| AustinCStone | CV/ML/GPU | Python, C++, Haskell |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (2026-05-05)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`.  
**Result: 0.00000000 APT for all addresses** — wallets may hold non-APT assets or be unfunded on mainnet.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (24 more) | 0.0 each |

### Multisig Contract Health (5/5 HEALTHY)

All probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

All 5 contracts require **2-of-N signatures**. Network responsive and contract state intact.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Next.js SPA, no public REST API. `/api/markets` and `/api/v1/markets` return HTML only. `mnx_snapshots` table is empty pending websocket/API key access.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Useful Queries
```sql
-- Top repos by stars
SELECT full_name, language, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF(3) trit balance
SELECT gf3_name, gf3_color, count(*) FROM world_increments GROUP BY 1,2 ORDER BY 2;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;

-- Aptos swarm
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;

-- Active repos (push in last 30 days from sweep date)
SELECT full_name, pushed_at FROM repo_snapshots
WHERE pushed_at > '2026-04-05' ORDER BY pushed_at DESC LIMIT 20;
```
