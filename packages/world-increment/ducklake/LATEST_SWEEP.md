# World-Increment Sweep + Hamming Snapshot — 2026-06-18

## Sweep Metadata
- **Date:** 2026-06-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (cumulative) | 34 |
| Repo Snapshots (cumulative) | 1276 |
| Aptos Snapshots (this run) | 28 |
| Multisig Probes (this run) | 5 |
| MNX Snapshots | 0 (auth-blocked) |
| Sources Covered | 3 orgs + 8 users + zubyul social graph |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this run)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| TeglonLabs | org | 5 |
| AustinCStone | social-graph | 40 |
| wasita | social-graph | 11 |
| migalkin | social-graph | 19 |
| M1shaaa | social-graph | 8 |
| kristinezheng | social-graph | 5 |
| DJedamski | social-graph | 6 |
| **TOTAL** | | **391** |

### GF(3) Color Chain — New Increments (IDs 2–12, this run)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 2  | plurigrid | +1 | `#b8bb26` | **PLUS** |
| 3  | kubeflow | -1 | `#cc241d` | **MINUS** |
| 4  | TeglonLabs | 0 | `#d3869b` | **ERGODIC** |
| 5  | bmorphism | +1 | `#b8bb26` | **PLUS** |
| 6  | zubyul | -1 | `#cc241d` | **MINUS** |
| 7  | migalkin | 0 | `#d3869b` | **ERGODIC** |
| 8  | DJedamski | +1 | `#b8bb26` | **PLUS** |
| 9  | wasita | -1 | `#cc241d` | **MINUS** |
| 10 | kristinezheng | 0 | `#d3869b` | **ERGODIC** |
| 11 | M1shaaa | +1 | `#b8bb26` | **PLUS** |
| 12 | AustinCStone | -1 | `#cc241d` | **MINUS** |

### Notable Repos (by stars, this run)

| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| migalkin/NodePiece | 144 | Python | migalkin |
| AustinCStone/TextGAN | 92 | Python | AustinCStone |
| migalkin/StarE | 89 | Python | migalkin |
| migalkin/kgcourse2021 | 25 | HTML | migalkin |
| migalkin/NBFNet_mlx | 10 | Python | migalkin |
| AustinCStone/StereoVisionMRF | 11 | Python | AustinCStone |
| TeglonLabs/jank-crane | 0 | C++ | TeglonLabs (newest: pushed 2026-06-08) |

### TeglonLabs — New: jank-crane (pushed 2026-06-08)
`crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

**Result: All 28 addresses returned `Resource not found`**

The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was absent on every
queried address. These wallets are uninitialised / have no APT on Aptos mainnet.

| Worlds | Status |
|--------|--------|
| alice, bob | Inactive (no CoinStore) |
| A–Z (26 addresses) | Inactive (no CoinStore) |

All 28 rows recorded in `aptos_snapshots` with `balance_apt = NULL`.

### Multisig Contract Probes — ALL HEALTHY

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401, Vercel deployment protection active.  
Requires Vercel bypass token or Trusted Source OIDC to access.  
No `mnx_snapshots` rows inserted.

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
