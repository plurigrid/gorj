# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-27

## Sweep Metadata
- **Date:** 2026-06-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 404 |
| Total Repo Snapshots | 1325 |
| Sources Covered | 3 orgs + 8 users (social graph) |

### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
| ERGODIC | #d3869b | 134 |
| PLUS | #b8bb26 | 135 |
| MINUS | #cc241d | 135 |

**Rule:** `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

### Top Repos by Stars (this sweep)

| Org/User | Repo | Language | Stars | Pushed |
|----------|------|----------|-------|--------|
| kubeflow | kubeflow | — | 15,747 | 2026-06-18 |
| kubeflow | pipelines | Python | 4,156 | 2026-06-26 |
| kubeflow | spark-operator | Python | 3,129 | 2026-06-26 |
| kubeflow | trainer | Go | 2,124 | 2026-06-26 |
| migalkin | NodePiece | Python | 144 | — |
| AustinCStone | TextGAN | Python | 92 | — |
| TeglonLabs | jank-crane | C++ | 0 | 2026-06-08 |

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | social-graph | 30 |
| migalkin | social-graph | 19 |
| wasita | social-graph | 11 |
| M1shaaa | social-graph | 8 |
| DJedamski | social-graph | 6 |
| kristinezheng | social-graph | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **381** |

### Notable New Activity (zubyul social graph — pushed 2026-06)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-06-07
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (GF3 convergence maps, loopify pass spec)
- **M1shaaa/M1shaaa** — profile updated 2026-06-27 (today)

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (A–Z + alice/bob)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
Accounts exist on-chain but have never held APT (no coin store initialized).
All balances recorded as NULL.

### Multisig Contract Probes

All 5 contracts responsive and healthy. Each requires **2-of-N signatures**.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f42... | 2 | HEALTHY |
| A-G | 0xf56c4a1... | 2 | HEALTHY |
| Y-Z | 0xd3ffe18... | 2 | HEALTHY |
| S-T | 0x3b1c3ae... | 2 | HEALTHY |
| V-W | 0x40fad7b... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — behind Vercel deployment protection (visitor password required).
No market data extracted. mnx_snapshots table empty.

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
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
