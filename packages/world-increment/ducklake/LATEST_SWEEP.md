# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-24

## Sweep Metadata
- **Date:** 2026-04-24T12:16:23Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 198 |
| Total Repo Snapshots | 1,119 |
| Sources Covered | 3 orgs + 8 users |

### Sources by Star Count

| Source | Type | Snapshots | Total Stars | Last Push |
|--------|------|-----------|-------------|-----------|
| kubeflow | org | 141 | 101,660 | 2026-04-24 |
| migalkin | social-graph | 65 | 828 | 2026-04-16 |
| AustinCStone | social-graph | 89 | 319 | 2026-04-01 |
| bmorphism | user | 205 | 268 | 2026-04-24 |
| plurigrid | org | 300 | 145 | 2026-04-24 |
| zubyul | user | 51 | 26 | 2026-04-24 |
| DJedamski | social-graph | 24 | 15 | 2023-04-21 |
| TeglonLabs | org | 110 | 14 | 2026-01-16 |
| wasita | social-graph | 63 | 9 | 2026-04-22 |
| kristinezheng | social-graph | 37 | 0 | 2026-04-09 |
| M1shaaa | social-graph | 34 | 0 | 2026-04-13 |

### GF(3) Trit Conservation

| Trit | Name | Color | Count |
|------|------|-------|-------|
| +1 | PLUS | `#b8bb26` | 67 |
| -1 | MINUS | `#cc241d` | 66 |
| 0 | ERGODIC | `#d3869b` | 65 |

GF(3) chain: `PLUS → MINUS → ERGODIC → …` repeating. Δ(PLUS−MINUS) = +1 (balanced within ±1).

Assignment rule:
- `id mod 3 == 0` → trit=0, `#d3869b`, ERGODIC
- `id mod 3 == 1` → trit=+1, `#b8bb26`, PLUS
- `id mod 3 == 2` → trit=−1, `#cc241d`, MINUS

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,599 | — | 2026-01-05 |
| kubeflow/pipelines | 4,125 | Python | 2026-04-23 |
| kubeflow/spark-operator | 3,120 | Python | 2026-04-21 |
| kubeflow/trainer | 2,090 | Go | 2026-04-23 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2026-04-01 |
| migalkin/NBFNet_mlx | 10 | Python | 2026-03-11 |
| migalkin/kgcourse2021 | 25 | HTML | 2026-02-16 |

### Notable Active Repos (plurigrid/bmorphism/zubyul, pushed 2026-04-24)

- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig 0.15, interaction nets, GF(3) trit conservation
- `plurigrid/asi` — everything is topological chemputer! (17★)
- `plurigrid/gorj` — forj + Rama nREPL + GF(3) gay trit coloring
- `plurigrid/zig-syrup` — OCapN Syrup with CapTP optimizations
- `bmorphism/Gay.jl` — wide-gamut color sampling, splittable determinism (Julia)
- `zubyul/voice-observatory` — passive macOS TUI, bmorphism/say-mcp-server companion

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried `https://fullnode.mainnet.aptoslabs.com` for 28 wallets (alice, bob, A–Z).

| Result | Count |
|--------|-------|
| 0.0 APT (unfunded / no CoinStore) | 28 |
| Non-zero balance | 0 |

All 28 Hamming swarm wallets returned 0.0 APT on mainnet. These are Aptos accounts with no funded `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource.

### Multisig Contract Probes — 5/5 Healthy

All probed multisig accounts require **2-of-2 signatures** and responded correctly to `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428…4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c…bc0096` | 2 | ✓ |
| S-T | `0x3b1c3ae9…d7883` | 2 | ✓ |
| V-W | `0x40fad7b4…80eb6d` | 2 | ✓ |
| Y-Z | `0xd3ffe181…75b883` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — DNS resolution failure for `testnet.mnx.fi`. `mnx_snapshots` table has 0 rows.

---

## DuckDB Table Summary

```sql
world_increments  198 rows  -- GF3-colored sweep events
repo_snapshots   1119 rows  -- org/user × repo snapshots (multi-snapshot cumulative)
aptos_snapshots    28 rows  -- Hamming swarm wallet balances
multisig_probes     5 rows  -- 2-of-2 multisig contracts, all healthy
mnx_snapshots       0 rows  -- DNS unavailable
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
