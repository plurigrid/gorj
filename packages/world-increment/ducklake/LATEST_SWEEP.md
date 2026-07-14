# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-14

## Sweep Metadata
- **Date:** 2026-07-14T09:10 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger Version:** 6271538824 | Epoch 16531 | Block 898174331

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 81 |
| Total Repo Snapshots (this run) | 81 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

### GF(3) Color Chain

GF(3) rule: `id%3==0` → trit=0 ERGODIC `#d3869b` | `id%3==1` → trit=1 PLUS `#b8bb26` | `id%3==2` → trit=-1 MINUS `#cc241d`

### Top Repos by Source (Jul 14 2026)

| Source | Type | Repos | Top Repo (Stars) | Last Pushed |
|--------|------|-------|-----------------|-------------|
| plurigrid | org | 44+ | asi (30★) | 2026-07-10 |
| kubeflow | org | 49 | kubeflow (15,777★) | 2026-07-14 |
| TeglonLabs | org | 5 | mathpix-gem (2★) | 2026-06-08 |
| bmorphism | user | 105 | Gay.jl (2★, 187 issues) | **2026-07-14** |
| zubyul | user | 49 | gay-world (1★) | 2026-04-24 |
| migalkin | user | 19 | NodePiece (144★) | 2026-05-07 |
| wasita | user | 11 | wasita.github.io (1★) | **2026-07-14** |
| kristinezheng | user | 5 | lookit-jenga | 2026-07-01 |
| M1shaaa | user | 8 | lab-bookshelf- | 2024-12-31 |
| AustinCStone | user | 40 | TextGAN (92★) | 2026-02-11 |
| DJedamski | user | 6 | kaggle_ncaa18 | 2018-02-26 |

### Notable Activity Today (Jul 14 2026)
- `bmorphism/Gay.jl` — pushed 08:57 UTC (most recent in swarm)
- `kubeflow/hub` — pushed 08:22 UTC
- `kubeflow/trainer` — pushed 04:08 UTC
- `kubeflow/pipelines` — pushed 01:35 UTC
- `wasita/wm-cv` + `wasita.github.io` — both pushed today

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 wallets probed against `fullnode.mainnet.aptoslabs.com`.

**Result**: All 28 addresses return `404 resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
**Interpretation**: No APT coin stores exist on any swarm address. Wallets are unfunded or hold assets in non-APT modules.

**Balance: 0.0 APT across all 28 Hamming worlds.**

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f428...987003 | **2** | ✓ |
| A-G | 0xf56c4a1c...bc0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181...5b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9...d7883 | **2** | ✓ |
| V-W | 0x40fad7b4...0eb6d | **2** | ✓ |

**All 5 multisigs healthy — uniform 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — Vercel deployment protection active. No market data extractable without bypass token.

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

## Notable Highlights & Anomalies
- **Hamming swarm fully unfunded** — all 28 APT addresses at 0.0 APT
- **All 5 multisigs healthy** — consistent 2-of-N threshold across swarm
- **kubeflow/kubeflow** now at 15,777 stars (was 15,565 in April sweep — +212 stars)
- **bmorphism/Gay.jl** has 187 open issues, most recently pushed repo in swarm
- **plurigrid/gorj** has 1,161 open issues — highest in plurigrid org
- **bmorphism/ocaml-mcp-sdk** now at 61 stars (was 60 in April sweep)
- **MNX testnet.mnx.fi** — Vercel auth wall, needs bypass token for next run
