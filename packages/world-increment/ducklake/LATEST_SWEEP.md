# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-17T16:30 UTC  
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Top Stars |
|--------|------|---------------|-----------|
| kubeflow | org | 22 | kubeflow/kubeflow (15,726 ⭐) |
| plurigrid | org | 44 | plurigrid/asi (26 ⭐) |
| bmorphism | user | 20 | bmorphism/ocaml-mcp-sdk (61 ⭐) |
| zubyul | user | 20 | zubyul/WGCNA (2 ⭐) |
| TeglonLabs | org | 5 | TeglonLabs/mathpix-gem (2 ⭐) |
| migalkin | social | 7 | migalkin/NodePiece (144 ⭐) |
| AustinCStone | social | 7 | AustinCStone/TextGAN (92 ⭐) |
| DJedamski | social | 6 | DJedamski/Getting-and-Cleaning-Data (1 ⭐) |
| wasita | social | 7 | wasita/magic-garden (2 ⭐) |
| kristinezheng | social | 5 | kristinezheng/Green-Machine (0 ⭐) |
| M1shaaa | social | 8 | M1shaaa/lab-bookshelf- (0 ⭐) |

**New world_increments added this sweep: 174**  
**Cumulative unique repos in DB: 517**

### Notable Activity (2026-06-17)

- **plurigrid/gorj** — pushed 2026-06-17 (637 open issues) — active today
- **kubeflow/kubeflow** — 15,726 stars, pushed 2026-06-17
- **kubeflow/pipelines-components** — pushed 2026-06-17T16:46
- **kubeflow/community** — pushed 2026-06-17T16:44
- **bmorphism/Gay.jl** — pushed 2026-06-17, 187 open issues (active)
- **M1shaaa/M1shaaa** — pushed 2026-06-17T15:17 (profile updated today)
- **wasita/wasita.github.io** — pushed 2026-06-15 (8 open issues)

### GF(3) Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 57 |
| +1 | PLUS | #b8bb26 | 59 |
| −1 | MINUS | #cc241d | 58 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets queried (alice, bob, A–Z). **All returned 0 APT** — no CoinStore resource registered on mainnet; accounts exist but APT coin store is not initialized.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...512d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C–Z | (see DB) | 0.00000000 each |

**Total APT across 28-world swarm: 0.00000000**

### Multisig Contract Probes

All 5 multisig contracts responded via `/v1/view`. **All require 2 signatures — all healthy.**

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N consensus intact**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection (visitor password required). No market data accessible without authentication bypass token. No rows inserted in `mnx_snapshots`.

---

## DuckDB State

```
world_increments:  174 new rows this sweep
repo_snapshots:   1095 total rows (517 unique full_names)
aptos_snapshots:    28 rows (all 0 APT)
multisig_probes:     5 rows (all healthy, 2-sig)
mnx_snapshots:       0 rows (auth-gated)
```

DB path: `packages/world-increment/ducklake/world-increments.duckdb`

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS

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
