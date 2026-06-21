# World-Increment Sweep + Hamming Snapshot — 2026-06-21

## Sweep Metadata
- **Date:** 2026-06-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 354 |
| Total Repo Snapshots | 1,275 |
| Sources Covered | 3 orgs + 8 users + 6 social graph |

### Repo Counts by Source (2026-06-21)

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 157 |
| kubeflow | org | 48 | 101,959 |
| TeglonLabs | org | 5 | 14 |
| bmorphism | user | 100 | 510 |
| zubyul | user | 49 | 40 |
| migalkin | social graph | 19 | 833 |
| AustinCStone | social graph | 40 | 319 |
| wasita | social graph | 11 | 10 |
| DJedamski | social graph | 6 | 17 |
| kristinezheng | social graph | 5 | 0 |
| M1shaaa | social graph | 8 | 0 |
| **TOTAL** | | **391** | **103,849** |

### Notable Repos (2026-06-21 push dates)

- `TeglonLabs/jank-crane` — C++ crane-jank converged-IR hub, GF3 convergence maps (pushed 2026-06-08)
- `wasita/proj-template` — most recently active social graph repo (pushed 2026-06-19)
- `wasita/wasita.github.io` — Svelte personal site (pushed 2026-06-15)
- `migalkin/RWL` — Weisfeiler & Leman Go Relational, 8★ (pushed 2026-05-28)
- `migalkin/NodePiece` — ICLR'22 KG paper, 144★ (pushed 2026-05-07)
- `AustinCStone/StereoVisionMRF` — MRF depth inference, 11★ (pushed 2026-04-01)
- `AustinCStone/TextGAN` — TF text GAN, 92★

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 117 |
| +1 | `#b8bb26` | PLUS | 119 |
| -1 | `#cc241d` | MINUS | 118 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — Mainnet (28 addresses, 2026-06-21)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned
`resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`.
This indicates uninitialized APT coin stores — wallets have not yet
received on-chain APT deposits on mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | uninitialized |
| bob | 0x0a3c...2d5d | uninitialized |
| A–Z | 26 addresses | uninitialized |

### Multisig Contract Probes (5 pairs) — All Healthy ✓

All 5 multisig contracts respond with **2-of-2 signatures required**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` is behind Vercel deployment protection (authentication required).
Market data unavailable without bypass token. `mnx_snapshots` table: 0 rows.

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
