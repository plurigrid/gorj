# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-03

## Sweep Metadata
- **Date:** 2026-08-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 83 |
| Total Repo Snapshots | 83 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 27 |
| +1 | #b8bb26 | PLUS | 28 |
| -1 | #cc241d | MINUS | 28 |

### Repo Counts by Source

| Source | Type | Total Found | Sampled |
|--------|------|------------|---------|
| plurigrid | org | 103 | 24 |
| kubeflow | org | 49 | 12 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 14 |
| zubyul | user | 49 | 8 |
| migalkin | social | 19 | 5 |
| DJedamski | social | 6 | 2 |
| wasita | social | 12 | 4 |
| kristinezheng | social | 5 | 2 |
| M1shaaa | social | 8 | 2 |
| AustinCStone | social | 41 | 5 |

### Notable Recent Activity (top by stars or freshness)

| Repo | Stars | Pushed At | Language |
|------|-------|-----------|----------|
| kubeflow/kubeflow | 15,804 | 2026-08-03 | — |
| kubeflow/pipelines | 4,173 | 2026-08-03 | Python |
| kubeflow/spark-operator | 3,143 | 2026-08-03 | Python |
| kubeflow/trainer | 2,165 | 2026-07-31 | Go |
| migalkin/NodePiece | 144 | 2026-05-07 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | 2026-05-08 | OCaml |
| AustinCStone/TextGAN | 92 | 2025-03-03 | Python |
| migalkin/StarE | 89 | 2026-04-16 | Python |
| plurigrid/asi | 58 | 2026-08-01 | HTML |
| plurigrid/microworlds | 4 | 2026-08-02 | Rust |
| plurigrid/gorj | 1 | 2026-07-29 | Clojure |
| bmorphism/Gay.jl | 2 | 2026-07-21 | Julia (188 issues) |
| bmorphism/anti-bullshit-mcp-server | 23 | 2026-08-02 | JavaScript |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming-swarm addresses queried against Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).

**Result:** All 28 wallets returned 0 APT. The CoinStore resource was not found (returned null) for each address — these wallets exist on-chain but have no APT CoinStore initialized or hold 0 APT.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.00 |
| bob | 0x0a3c...2d5d | 0.00 |
| A | 0x8699...9d7a | 0.00 |
| B | 0x3f89...b13 | 0.00 |
| C | 0x38b9...35e | 0.00 |
| D | 0xf776...dd1 | 0.00 |
| E | 0xdc1d...d36 | 0.00 |
| F | 0x18a1...f71 | 0.00 |
| G | 0x69a3...f32 | 0.00 |
| H | 0xce67...00f | 0.00 |
| I | 0x070f...c9 | 0.00 |
| J | 0x4d96...f54 | 0.00 |
| K | 0xa732...dc4 | 0.00 |
| L | 0x7c2e...ba9 | 0.00 |
| M | 0x6fed...f2e9 | 0.00 |
| N | 0xe7dd...b2c | 0.00 |
| O | 0x7325...89d | 0.00 |
| P | 0x6218...948 | 0.00 |
| Q | 0xac40...89a9 | 0.00 |
| R | 0x7ce6...e10 | 0.00 |
| S | 0xb875...386 | 0.00 |
| T | 0x3578...588 | 0.00 |
| U | 0x7586...956 | 0.00 |
| V | 0xb59d...2c3 | 0.00 |
| W | 0x5f32...b0 | 0.00 |
| X | 0xa95c...47d | 0.00 |
| Y | 0xd8e3...4c4 | 0.00 |
| Z | 0x7af0...97c | 0.00 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | ✅ healthy |
| A-G | 0xf56c...0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✅ healthy |
| S-T | 0x3b1c...7883 | 2 | ✅ healthy |
| V-W | 0x40fa...eb6d | 2 | ✅ healthy |

**All 5 contracts online: 2-of-2 multisig, fully operational.**

### MNX Markets (testnet.mnx.fi)

Probed `/api/markets`, `/api/v1/markets`, and root. Returns a Next.js SPA shell (HTML) — no machine-readable market data available via static HTTP probe.  
**Status: SPA — data unavailable via direct API probe.**

---

## DuckDB Ducklake Schema

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
