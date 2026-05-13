# World-Increment Sweep + Hamming Snapshot — 2026-05-13

## Sweep Metadata
- **Date:** 2026-05-13T19:13:56Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts (This Run)

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 100 | 72 |
| kubeflow | org | 48 | 34,047 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 248 |
| zubyul | user | 49 | 14 |
| migalkin | social | 6 | 278 |
| wasita | social | 5 | 3 |
| AustinCStone | social | 5 | 107 |
| DJedamski | social | 4 | 3 |
| kristinezheng | social | 3 | 0 |
| M1shaaa | social | 3 | 0 |
| **TOTAL** | | **327** | **34,774** |

### GF(3) Color Chain — This Sweep

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | all-sources | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3): `id%3==0 → trit=0 ERGODIC #d3869b`

### Notable Repos
- **kubeflow/pipelines** (Python, 4119★) — most active KF repo, pushed 2026-05-13
- **migalkin/NodePiece** (Python, 144★) — ICLR'22 parameter-efficient KG representations
- **migalkin/StarE** (Python, 89★) — EMNLP 2020 hyper-relational KGs
- **AustinCStone/TextGAN** (Python, 92★) — adversarial text generation in TensorFlow
- **bmorphism** — 100 repos, most recently pushed 2026-05-13
- **plurigrid** — 100 repos, most recently pushed 2026-05-13
- **wasita/wasita.github.io** (Svelte) — pushed today 2026-05-13T05:34:57Z

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallets (alice, bob, A–Z)

**Status: All 28 addresses returned null CoinStore**

Probed `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet. All 28 hamming-swarm addresses lack funded APT balances. Addresses span the space but none have registered coin stores.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...4cc7b | null |
| bob | 0x0a3c...512d5d | null |
| A–Z | (26 addresses) | null |

### Multisig Contract Probes

All 5 multisig pairs responded healthy: `num_signatures_required = 2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...87003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**5/5 multisig contracts healthy** — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: SPA unavailable** — `testnet.mnx.fi` serves a Next.js client-side app. No public API endpoints (`/api/markets`, `/api/v1/markets`) return structured market data. All data loads client-side. Recorded as `SPA_unavailable` in `mnx_snapshots`.

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
