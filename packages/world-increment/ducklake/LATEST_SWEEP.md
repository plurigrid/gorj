# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.2.1
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 140 |
| Total Repo Snapshots | 140 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Pairs Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found | Sampled |
|--------|------|-------------|---------|
| plurigrid | org | 100 | 100 |
| bmorphism | user | 106 | 10 |
| zubyul | user | 49 | 5 |
| kubeflow | org | 49 | 6 |
| TeglonLabs | org | 5 | 4 |
| migalkin | user | 19 | 3 |
| DJedamski | user | 6 | 2 |
| wasita | user | 13 | 3 |
| kristinezheng | user | 5 | 2 |
| M1shaaa | user | 8 | 2 |
| AustinCStone | user | 41 | 3 |

### GF(3) Color Chain Distribution

| Color | Name | Trit | Count |
|-------|------|------|-------|
| `#d3869b` | ERGODIC | 0 | 46 |
| `#b8bb26` | PLUS | +1 | 47 |
| `#cc241d` | MINUS | -1 | 47 |

### Top Repos by Stars

| Repo | Stars | Language | Source |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,805 | — | kubeflow org |
| kubeflow/pipelines | 4,175 | Python | kubeflow org |
| kubeflow/spark-operator | 3,143 | Python | kubeflow org |
| kubeflow/trainer | 2,167 | Go | kubeflow org |
| kubeflow/katib | 1,694 | Python | kubeflow org |
| migalkin/NodePiece | 144 | Python | social graph |
| AustinCStone/TextGAN | 92 | Python | social graph |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | bmorphism |
| plurigrid/asi | 58 | HTML | plurigrid |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | bmorphism |

### Recent Activity Highlights (2026-08-04)

- **wasita** created `joint-planning-lit` today (2026-08-04) — fresh commit
- **kubeflow** very active: trainer, pipelines, spark-operator all updated today
- **bmorphism** `anti-bullshit-mcp-server` active (2026-08-02) — 23 stars, 7 forks
- **plurigrid/gorj** (this repo) — most recently updated plurigrid project
- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Result:** All 28 accounts (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Interpretation:** These accounts are uninitialized on Aptos mainnet. Balances recorded as **0.0 APT** each.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ HEALTHY |

**5/5 healthy** — all multisig pairs require 2-of-N signatures and are responsive.

### MNX Markets (testnet.mnx.fi)

- `https://testnet.mnx.fi/api/markets` → **HTTP 404**
- `https://testnet.mnx.fi` → SPA shell only, no structured market data
- **Status: UNAVAILABLE** — `mnx_snapshots` table remains empty this sweep

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
