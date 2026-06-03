# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-03  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Total Available |
|--------|------|-------------------|-----------------|
| plurigrid | org | 14 | 101 |
| kubeflow | org | 14 | 48 |
| TeglonLabs | org | 4 | 4 |
| bmorphism | user | 14 | 103 |
| zubyul | user | 8 | 49 |
| migalkin | social graph | 5 | 19 |
| DJedamski | social graph | 3 | 6 |
| wasita | social graph | 3 | 11 |
| kristinezheng | social graph | 2 | 6 |
| M1shaaa | social graph | 2 | 8 |
| AustinCStone | social graph | 5 | 40 |
| **TOTAL** | | **74 snapshots** | |

### DuckDB Tables

```
world_increments  74 rows   (GF3 color chain per repo)
repo_snapshots    74 rows   (full metadata)
```

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 25 |
| 1 | `#b8bb26` | PLUS | 25 |
| 2 (−1) | `#cc241d` | MINUS | 24 |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,704 | — |
| kubeflow/pipelines | 4,151 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,110 | Go |
| kubeflow/katib | 1,685 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/manifests | 1,020 | YAML |
| kubeflow/arena | 811 | Go |
| kubeflow/kale | 691 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 24 | HTML |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/risc0-cosmwasm-example | 23 | Rust |

### Top Repos by Open Issues

| Repo | Open Issues |
|------|------------|
| kubeflow/pipelines | 487 |
| plurigrid/gorj | 313 |
| bmorphism/Gay.jl | 189 |
| kubeflow/sdk | 133 |
| kubeflow/trainer | 126 |
| kubeflow/katib | 122 |
| kubeflow/examples | 111 |
| kubeflow/spark-operator | 103 |
| kubeflow/mpi-operator | 103 |
| kubeflow/dashboard | 83 |

### Notable Activity (Most Recent Pushes)

- `bmorphism/Gay.jl` — 2026-06-03 · wide-gamut SPI color sampling (189 open issues)
- `plurigrid/gorj` — 2026-06-03 · forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `plurigrid/eirobri` — 2026-05-26 · EiRoBri replay world
- `migalkin/RWL` — 2026-05-28 · Weisfeiler and Leman Go Relational (LOG 2022)
- `kubeflow/dashboard` — 2026-06-02 · Kubeflow Central Dashboard
- `wasita/wasita.github.io` — 2026-06-01 · personal website (Svelte)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Queried:** 2026-06-03 via `https://fullnode.mainnet.aptoslabs.com/v1`  
**Wallets probed:** 28 (alice, bob, A–Z)  
**Result:** All 28 wallets returned **0.0 APT**

Accounts not found or zero-balance on mainnet; these addresses are likely
testnet/staging addresses queried against mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N threshold confirmed):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status:** SPA (Next.js) — no REST API endpoints responded:
- `GET /api/markets` → empty
- `GET /api/v1/markets` → empty
- `GET /api/tickers` → empty
- `GET /markets` → Next.js HTML bundle only

`mnx_snapshots` table remains empty.

---

## Summary

| Component | Status | Records |
|-----------|--------|---------|
| GitHub orgs (plurigrid, kubeflow, TeglonLabs) | ✓ | 32 repos |
| GitHub users (bmorphism, zubyul) | ✓ | 22 repos |
| zubyul social graph (6 users) | ✓ | 20 repos |
| Aptos wallet balances | ✓ (all zero) | 28 wallets |
| Aptos multisig probes | ✓ all healthy | 5 contracts |
| MNX markets | unavailable | 0 records |

**Total world_increments:** 74  
**GF3 chain:** ERGODIC(0) → PLUS(1) → MINUS(2) cycling, balanced at 25/25/24

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

## GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id % 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id % 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS
