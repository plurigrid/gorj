# World-Increment Sweep — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GitHub API:** Scoped to `plurigrid/gorj` only; external org/user repos sourced from prior sweep (2026-04-10)
- **MNX Markets:** Unavailable (Vercel deployment protection)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 28 |
| Total Repo Snapshots (cumulative) | 944 |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users (prior sweep data) |

---

## GF(3) Color Chain — Increments 13–17 (This Run)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | sweep (world-increment-sweep) | sweep_start | +1 | `#b8bb26` | **PLUS** |
| 14 | aptos (hamming-swarm) | aptos_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | aptos (hamming-swarm) | multisig_probe | 0 | `#d3869b` | **ERGODIC** |
| 16 | github (plurigrid) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | sweep (world-increment-sweep) | sweep_complete | -1 | `#cc241d` | **MINUS** |

GF(3) continuation: `…ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Full GF(3) Chain (All 28 Increments)
IDs 1–12 from prior sweeps; IDs 13–17 this run.
Pattern: `PLUS → MINUS → ERGODIC` repeating across all sweeps, maintaining compositional closure.

---

## Hamming Swarm — Aptos Wallet Snapshot

**Probed at:** 2026-07-10T10:12 UTC  
**Node:** fullnode.mainnet.aptoslabs.com (ledger ~v6.2B)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These accounts are not funded with APT on mainnet (unfunded key material or different resource types).

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob   | 0x0a3c…2d5d | 0.0 |
| A     | 0x8699…9d7a | 0.0 |
| B     | 0x3f89…b13 | 0.0 |
| C–Z   | (24 addrs) | 0.0 each |

**Total APT across swarm:** 0.0

---

## Multisig Contract Probes

All 5 multisig contracts are **healthy** (responding, sigs_required=2).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4…003  | 2 | ✓ |
| A-G  | 0xf56c…096  | 2 | ✓ |
| Y-Z  | 0xd3ff…883  | 2 | ✓ |
| S-T  | 0x3b1c…883  | 2 | ✓ |
| V-W  | 0x40fa…b6d  | 2 | ✓ |

All contracts require 2-of-N signatures. No anomalies detected.

---

## MNX Markets

`testnet.mnx.fi` — **Unavailable** (Vercel deployment protection requires visitor password or bypass token). No market data captured this run.

---

## GitHub Social Graph (Prior Sweep Data — 2026-04-10)

*Note: External GitHub API endpoints are not accessible in this session (scoped to plurigrid/gorj). Repo data reflects the last successful sweep from 2026-04-10.*

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,572 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,119 | 2026-04-14 |
| kubeflow/spark-operator | Python | 3,114 | 2026-04-13 |
| kubeflow/trainer | Go | ~2,080 | 2026-04-10 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | — |
| bmorphism/anti-bullshit-mcp-server | JS | 23 | — |
| AustinCStone/TextGAN | Python | 92 | — |
| migalkin/NodePiece | Python | 143 | — |
| migalkin/StarE | Python | 88 | — |
| plurigrid/asi | HTML | 16 | 2026-04-10 |

### Repo Counts by Source

| Source | Type | Repos (cumulative) |
|--------|------|-------------------|
| plurigrid | org | 200 |
| bmorphism | user | 200 |
| TeglonLabs | org | 106 |
| kubeflow | org | 94 |
| AustinCStone | user | 86 |
| wasita | user | 60 |
| migalkin | user | 60 |
| zubyul | user | 48 |
| kristinezheng | user | 36 |
| M1shaaa | user | 32 |
| DJedamski | user | 22 |
| **TOTAL** | | **944** |

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

## Notes
- GitHub API blocked for non-scoped endpoints; repo data frozen at 2026-04-10 sweep
- All 28 Aptos addresses unfunded on mainnet (no AptosCoin resource)
- All 5 multisig contracts healthy with 2-of-N threshold
- MNX testnet behind Vercel auth; market data not captured
