# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-16

## Sweep Metadata
- **Date:** 2026-06-16 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 291 |
| Total Repo Snapshots (raw) | 1,211 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Market Snapshots | 0 (unavailable) |
| Sources Covered | 3 orgs + 8 users (social graph) |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 97 |
| +1 | `#b8bb26` | PLUS | 97 |
| -1 | `#cc241d` | MINUS | 97 |

GF(3) chain rule: `id mod 3 == 0` → ERGODIC · `id mod 3 == 1` → PLUS · `id mod 3 == 2` → MINUS

---

## JOB 1: GitHub Social Graph Sweep

### Sources Crawled

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph (zubyul) | 19 |
| DJedamski | social-graph (zubyul) | 6 |
| wasita | social-graph (zubyul) | 11 |
| kristinezheng | social-graph (zubyul) | 5 |
| M1shaaa | social-graph (zubyul) | 8 |
| AustinCStone | social-graph (zubyul) | 40 |
| **TOTAL** | | **~391** |

### Most Recently Active Repos (as of 2026-06-16)

| Org/User | Repo | Pushed | Language |
|----------|------|--------|----------|
| plurigrid | gorj | 2026-06-16 01:11 | Clojure |
| bmorphism | Gay.jl | 2026-06-16 00:49 | Julia |
| kubeflow | trainer | 2026-06-15 23:34 | Go |
| kubeflow | sdk | 2026-06-15 23:09 | Python |
| plurigrid | place | 2026-06-15 23:04 | TeX |
| bmorphism | satreadout | 2026-06-15 21:20 | Lean |
| wasita | wasita.github.io | 2026-06-15 20:14 | Svelte |
| kubeflow | katib | 2026-06-15 20:07 | Python |
| kubeflow | hub | 2026-06-15 19:56 | Go |
| kubeflow | pipelines | 2026-06-15 19:49 | Python |

### Top Repos by Stars

| Org/User | Repo | Stars | Forks | Language |
|----------|------|-------|-------|----------|
| kubeflow | kubeflow | 15,726 | 2,673 | — |
| kubeflow | pipelines | 4,154 | 2,008 | Python |
| kubeflow | spark-operator | 3,127 | 1,490 | Python |
| kubeflow | trainer | 2,115 | 969 | Go |
| kubeflow | katib | 1,683 | 527 | Python |
| kubeflow | examples | 1,461 | 756 | Jsonnet |
| migalkin | NodePiece | 144 | 21 | Python |
| AustinCStone | TextGAN | 92 | 30 | Python |
| migalkin | StarE | 89 | 16 | Python |

### Notable Signals
- **plurigrid/gorj** pushed today (2026-06-16) — this repo is live and active
- **bmorphism/satreadout** (Lean) and **Gay.jl** (Julia) — active formal verification + research stream
- **TeglonLabs/jank-crane** (C++, 2026-06-08): description explicitly references "GF3 convergence maps"
- **kubeflow** shows sustained activity across 10+ repos, all pushed 2026-06-15

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-16)

All 28 wallets (alice, bob, A–Z) were probed via `fullnode.mainnet.aptoslabs.com`.

**Result: 0.0 APT across all 28 addresses**

All accounts returned no `CoinStore<AptosCoin>` resource — accounts are registered on-chain but hold no liquid APT. Consistent with unfunded or swept wallets.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...cc7b | 0.0 APT |
| bob | 0x0a3c...512d | 0.0 APT |
| A | 0x8699...d7a | 0.0 APT |
| B | 0x3f89...b13 | 0.0 APT |
| C | 0x38b9...35e | 0.0 APT |
| D | 0xf776...dd1 | 0.0 APT |
| E | 0xdc1d...d36 | 0.0 APT |
| F | 0x18a1...f71 | 0.0 APT |
| G | 0x69a3...f32 | 0.0 APT |
| H | 0xce67...00f | 0.0 APT |
| I | 0x070f...fc9 | 0.0 APT |
| J | 0x4d96...f54 | 0.0 APT |
| K | 0xa732...dc4 | 0.0 APT |
| L | 0x7c2e...ba9 | 0.0 APT |
| M | 0x6fed...2e9 | 0.0 APT |
| N | 0xe7dd...b2c | 0.0 APT |
| O | 0x7325...89d | 0.0 APT |
| P | 0x6218...948 | 0.0 APT |
| Q | 0xac40...89a9 | 0.0 APT |
| R | 0x7ce6...e10 | 0.0 APT |
| S | 0xb875...386 | 0.0 APT |
| T | 0x3578...588 | 0.0 APT |
| U | 0x7586...956 | 0.0 APT |
| V | 0xb59d...f2c3 | 0.0 APT |
| W | 0x5f32...7b0 | 0.0 APT |
| X | 0xa95c...47d | 0.0 APT |
| Y | 0xd8e3...44c4 | 0.0 APT |
| Z | 0x7af0...97c | 0.0 APT |

### Multisig Contract Probes

All 5 multisig accounts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig accounts healthy — 2-of-N threshold confirmed across all pairs.**

### MNX Markets (`testnet.mnx.fi`)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi` and `/api/markets`, `/api/v1/markets` all return Vercel authentication gate (`Authentication Required`). No market data extractable without credentials. `mnx_snapshots` table remains empty this sweep.

---

## DuckDB Schema

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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent — 2026-06-16*
