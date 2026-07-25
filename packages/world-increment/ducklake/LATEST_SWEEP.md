# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-07-25 run)

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 220 |
| Total World Increments (cumulative) | 243 |
| New Repo Snapshots (this run) | 220 |
| Total Repo Snapshots (cumulative) | 1,164 |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Repos by Source (this run)

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 34,410 |
| migalkin | social | 5 | 275 |
| bmorphism | user | 50 | 115 |
| AustinCStone | social | 3 | 103 |
| plurigrid | org | 50 | 58 |
| zubyul | user | 49 | 14 |
| wasita | social | 4 | 4 |
| TeglonLabs | org | 5 | 2 |
| M1shaaa | social | 2 | 0 |
| kristinezheng | social | 2 | 0 |
| DJedamski | social | 1 | 0 |
| **TOTAL** | | **220** | **34,981** |

### GF(3) Color Chain Distribution

| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 80 |
| PLUS | #b8bb26 | 82 |
| MINUS | #cc241d | 81 |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Top Repos by Stars (this run)

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,793 |
| kubeflow/pipelines | Python | 4,169 |
| kubeflow/spark-operator | Python | 3,143 |
| kubeflow/trainer | Go | 2,153 |
| kubeflow/katib | Python | 1,692 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| AustinCStone/StereoVisionMRF | Python | 11 |
| migalkin/NBFNet_mlx | Python | 10 |

### Notable Recent Pushes

| Repo | Pushed | Notable |
|------|--------|---------|
| wasita/wasita.github.io | 2026-07-21 | Most recent push in social graph |
| AustinCStone/byteruckus | 2026-07-15 | Newest AustinCStone repo (HTML) |
| migalkin/kgcourse2021 | 2026-07-10 | Knowledge Graphs course — recently touched |
| TeglonLabs/jank-crane | 2026-06-08 | C++ converged-IR hub with GF3 convergence maps |
| migalkin/RWL | 2026-05-28 | Weisfeiler-Leman Go Relational (Python) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

**Result:** All 28 addresses returned HTTP 404 `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

Queried at ledger version **6,447,952,295** (mainnet, epoch 16665, block height 924,495,049).

Addresses with no APT CoinStore (all 28):

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...b3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 probes returned `num_signatures_required = 2` — all **healthy**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...7003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `/api/markets` returned HTTP 404. Root page is a JavaScript SPA rendering only the text "MNX" — no market data extractable via static fetch. `mnx_snapshots` table has 0 rows.

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
