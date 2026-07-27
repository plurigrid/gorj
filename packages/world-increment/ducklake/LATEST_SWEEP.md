# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 318 |
| Total Repo Snapshots | 318 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA — no API data available |

---

## GF(3) Color Chain — 318 Increments (per-repo)

Each of the 318 repo snapshots is assigned a GF(3) trit by `id % 3`:

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 106 |
| 1 | `#b8bb26` | PLUS | 106 |
| 2 (−1) | `#cc241d` | MINUS | 106 |

Cycle: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → …` (106 full GF(3) cycles)

---

## Top Repos by Stars (2026-07-27 snapshot)

| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,792 | 2,685 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | 2,064 | Python | 2026-07-26 |
| kubeflow/spark-operator | 3,142 | 1,506 | Python | 2026-07-25 |
| kubeflow/trainer | 2,154 | 997 | Go | 2026-07-26 |
| migalkin/NodePiece | 144 | 21 | Python | 2021-06-14 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2016-09-19 |
| migalkin/StarE | 89 | 16 | Python | 2020-09-17 |
| bmorphism/anti-bullshit-mcp-server | 22 | 7 | JavaScript | 2026-01-16 |
| migalkin/kgcourse2021 | 24 | 8 | HTML | 2020-09-01 |
| bmorphism/manifold-mcp-server | 14 | 9 | JavaScript | 2025-01-11 |

## Recently Active (last 30 days)
- **bmorphism/Gay.jl** — pushed 2026-07-26: Wide-gamut color sampling with splittable determinism (Pigeon 0.6)
- **bmorphism/world** — pushed 2026-06-02: Local worlds launcher for SA3, jank, world proofs
- **TeglonLabs/jank-crane** — pushed 2026-06-08: crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user (social graph) | 4 |
| TeglonLabs | org | 5 |
| migalkin | user (social graph) | 5 |
| wasita | user (social graph) | 3 |
| DJedamski | user (social graph) | 1 |
| kristinezheng | user (social graph) | 1 |
| M1shaaa | user (social graph) | 1 |
| **TOTAL** | | **318** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-27)

All 28 wallets probed — **all returned 0.0 APT**. CoinStore resource absent on all accounts (wallets unfunded or uninitialized on mainnet).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A | 0x8699... | 0.0 |
| B–Z | 0x3f89...–0x7af0... | 0.0 each |

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`. All **require 2 signatures** → **HEALTHY** ✓

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a Next.js SPA. The `/api/markets` endpoint returned no structured data from a server-side HTTP probe. **Market data unavailable** — requires browser execution of JS bundles. `mnx_snapshots` table has 0 rows.

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

---

## DuckDB Table Summary

```
world_increments  — 318 rows  (per-repo GF3-colored increment events)
repo_snapshots    — 318 rows  (full repo metadata: lang, stars, forks, issues, push date)
aptos_snapshots   — 28 rows   (wallet balance probe, all 0.0 APT)
multisig_probes   — 5 rows    (all healthy, 2-of-N threshold)
mnx_snapshots     — 0 rows    (SPA, no server-accessible API)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
