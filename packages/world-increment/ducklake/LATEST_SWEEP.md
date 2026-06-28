# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-28

## Sweep Metadata
- **Date:** 2026-06-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 323 |
| Total Repo Snapshots | 323 |
| Sources Covered | 3 orgs + 8 users (11 sources) |
| Aptos wallets probed | 28 (alice–Z) |
| Multisig pairs probed | 5 |
| MNX markets | unavailable (Vercel auth) |

---

## GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 107 |
| PLUS | +1 | `#b8bb26` | 108 |
| MINUS | -1 | `#cc241d` | 108 |

Assignment rule: `id%3==0` → ERGODIC #d3869b, `id%3==1` → PLUS #b8bb26, `id%3==2` → MINUS #cc241d

---

## Top Repos by Stars (Top 15)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,749 | — | 2026-06-18 |
| kubeflow/pipelines | 4,158 | Python | 2026-06-27 |
| kubeflow/spark-operator | 3,129 | Python | 2026-06-26 |
| kubeflow/trainer | 2,125 | Go | 2026-06-26 |
| kubeflow/katib | 1,687 | Python | 2026-06-23 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-06-25 |
| kubeflow/arena | 814 | Go | 2026-06-26 |
| kubeflow/kale | 694 | Python | 2026-06-25 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-25 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |

## Repo Counts by Source (2026-06-28 snapshot)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| migalkin | social-graph | 5 |
| wasita | social-graph | 4 |
| AustinCStone | social-graph | 3 |
| DJedamski | social-graph | 3 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| **TOTAL** | | **323** |

## Most Recent Activity (2026-06-28)

| Repo | Pushed |
|------|--------|
| plurigrid/gorj | 2026-06-28T02:11 UTC |
| plurigrid/asi (26 stars) | 2026-06-28T00:42 UTC |
| bmorphism/Gay.jl | 2026-06-28T00:39 UTC |
| plurigrid/place | 2026-06-27T22:03 UTC |
| kubeflow/hub | 2026-06-27T17:16 UTC |
| kubeflow/pipelines | 2026-06-27T15:18 UTC |
| wasita/wasita.github.io | 2026-06-25T16:23 UTC |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice–Z, 28 addresses)

**Aptos ledger:** version 5,972,510,454 | epoch 16,335 | block height 861,214,940  
**Result:** All 28 hamming-swarm addresses return HTTP 404 `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. No APT has ever been deposited to any of these addresses on mainnet.

**Total APT across swarm:** 0.0 APT

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

All 5 pairs are online, responsive, and require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection is active on `testnet.mnx.fi`. All paths (`/`, `/api/markets`, `/api/v1/markets`) return HTTP 200 with an auth-required page. No bypass token is available. Market data cannot be retrieved.

---

## DuckDB Tables

```
world_increments  : 323 rows (one per repo, GF3-colored)
repo_snapshots    : 323 rows (full repo metadata)
aptos_snapshots   :  28 rows (hamming swarm wallets A–Z + alice + bob)
multisig_probes   :   5 rows (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     :   0 rows (site unavailable)
```

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

## Key Findings

1. **plurigrid/gorj** (this repo!) pushed 2026-06-28T02:11 UTC — most recently active in sweep.
2. **plurigrid/asi** now at 26 stars (up from 16 in April 2026 sweep), pushed today.
3. **bmorphism/Gay.jl** active today; **bmorphism/ocaml-mcp-sdk** at 61 stars (up from 60).
4. **kubeflow** dominates stars: flagship at 15,749 stars, pipelines at 4,158, spark-operator at 3,129.
5. **Hamming swarm (alice–Z):** All 28 Aptos addresses unfunded (0 APT). No CoinStore resource on-chain.
6. **Multisig contracts:** All 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy, all require exactly 2 sigs.
7. **MNX testnet:** Behind Vercel auth gate — market data inaccessible without bypass token.
