# World-Increment Sweep — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 14 |
| Total Repo Snapshots (all time) | 945 |
| Aptos Wallets Probed (this sweep) | 28 |
| Multisig Contracts Probed (this sweep) | 5 |
| MNX Markets | unavailable (Vercel auth required) |

---

## This Sweep: New Increments (id=13, id=14)

### GF(3) Color Chain — Current Sweep

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos-mainnet | hamming_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) position: continuing from id=12 (ERGODIC) → **PLUS → MINUS**

---

## JOB 1: GitHub Social Graph Sweep

**Note:** This session's GitHub access is scoped to `plurigrid/gorj` only. Direct API calls to other orgs (kubeflow, TeglonLabs) and users (bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) are blocked by the proxy policy. Social graph data from prior sweeps (id=1–12) remains in the DB with 944 historical snapshots.

### plurigrid/gorj — Latest State
| Field | Value |
|-------|-------|
| Language | Clojure |
| Latest Commit | `5b28fe0` — chore: ignore duckdb binary (2026-05-08) |
| Prior Sweep Commit | `ebf263f` — world-increment ducklake: sync world.duckdb sweep state (2026-04-14) |
| Active Sweep Branches | 50+ `world-increment/sweep-*` branches on remote |
| Last Increment Before Today | id=12 ERGODIC sweep_complete (2026-04-12) |

### Recent Commits (last 5)
| SHA | Message | Date |
|-----|---------|------|
| `5b28fe0` | chore: ignore duckdb binary in repo root | 2026-05-08 |
| `ebf263f` | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| `b434a43` | Merge sweep state into master | 2026-04-14 |
| `e76792f` | world-increments.duckdb: sync latest sweep state | 2026-04-14 |
| `631518b` | world-increment sweep 2026-04-12: insert id=12 ERGODIC | 2026-04-12 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned `resource_not_found` from the Aptos mainnet CoinStore. This indicates none of these accounts hold a funded APT CoinStore at ledger version ~6,280,133,572.

| World | Balance (APT) | Status |
|-------|---------------|--------|
| alice | 0.0 | no CoinStore |
| bob | 0.0 | no CoinStore |
| A–Z (26 wallets) | 0.0 each | no CoinStore |
| **Total** | **0.0 APT** | |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are healthy, each requiring 2-of-N signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...` | 2 | ✓ |
| A-G | `0xf56c4a1c...` | 2 | ✓ |
| Y-Z | `0xd3ffe181...` | 2 | ✓ |
| S-T | `0x3b1c3ae9...` | 2 | ✓ |
| V-W | `0x40fad7b4...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
- **Status:** Unavailable — site requires Vercel visitor password authentication
- No market data extracted this sweep

---

## Historical GF(3) Chain (All 14 Increments)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid | +1 | `#b8bb26` | PLUS |
| 2  | kubeflow | -1 | `#cc241d` | MINUS |
| 3  | TeglonLabs | 0 | `#d3869b` | ERGODIC |
| 4  | bmorphism | +1 | `#b8bb26` | PLUS |
| 5  | zubyul | -1 | `#cc241d` | MINUS |
| 6  | migalkin | 0 | `#d3869b` | ERGODIC |
| 7  | DJedamski | +1 | `#b8bb26` | PLUS |
| 8  | wasita | -1 | `#cc241d` | MINUS |
| 9  | kristinezheng | 0 | `#d3869b` | ERGODIC |
| 10 | M1shaaa | +1 | `#b8bb26` | PLUS |
| 11 | AustinCStone | -1 | `#cc241d` | MINUS |
| 12 | bmorphism/sweep_complete | 0 | `#d3869b` | ERGODIC |
| **13** | **plurigrid/gorj** | **+1** | **`#b8bb26`** | **PLUS** |
| **14** | **aptos-mainnet** | **-1** | **`#cc241d`** | **MINUS** |

Full GF(3) cycle count: 4 complete cycles (ids 1–12) + 2/3 of cycle 5 (ids 13–14)

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
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Access Constraints Observed
- GitHub REST API: blocked by proxy for non-scoped repos; only `plurigrid/gorj` accessible via MCP tools
- Aptos mainnet: all 28 Hamming swarm wallets show 0 APT (no funded CoinStore at current ledger)
- MNX testnet.mnx.fi: Vercel password-protected, no market data available
- Multisig contracts: all 5 pairs live on mainnet and responsive (2-of-N threshold confirmed)
