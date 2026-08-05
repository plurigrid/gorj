# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-05

## Sweep Metadata
- **Date:** 2026-08-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos ledger version:** 6,615,856,795

---

## Summary Counts

| Table | Rows |
|-------|------|
| world_increments | 11 |
| repo_snapshots | 320 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA — unavailable) |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 49 |
| zubyul | user | 49 |
| AustinCStone | user (social) | 29 |
| migalkin | user (social) | 19 |
| wasita | user (social) | 14 |
| M1shaaa | user (social) | 8 |
| DJedamski | user (social) | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user (social) | 5 |
| **TOTAL** | | **384 queried / 320 stored** |

### GF(3) Color Chain — All 11 World Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | AustinCStone | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 2  | DJedamski | repo_sweep | 1 | `#b8bb26` | **PLUS** |
| 3  | M1shaaa | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 4  | bmorphism | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 5  | kristinezheng | repo_sweep | 1 | `#b8bb26` | **PLUS** |
| 6  | kubeflow | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 7  | migalkin | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 8  | plurigrid | repo_sweep | 1 | `#b8bb26` | **PLUS** |
| 9  | TeglonLabs | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 10 | wasita | repo_sweep | 0 | `#d3869b` | **ERGODIC** |
| 11 | zubyul | repo_sweep | 1 | `#b8bb26` | **PLUS** |

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | — | 2026-07-10 |
| kubeflow/pipelines | 4,175 | Python | 2026-08-04 |
| kubeflow/spark-operator | 3,143 | Python | 2026-08-04 |
| kubeflow/trainer | 2,169 | Go | 2026-08-04 |
| kubeflow/katib | 1,694 | Python | 2026-08-04 |
| migalkin/NodePiece | 144 | Python | 2021-06-14 |
| AustinCStone/TextGAN | 92 | Python | 2016-09-19 |
| migalkin/StarE | 89 | Python | 2020-09-17 |
| AustinCStone/StereoVisionMRF | 11 | Python | 2016-01-10 |
| migalkin/NBFNet_mlx | 10 | Python | 2024-03-01 |

### Notable Activity (pushed recently)

- **wasita/xoxowasita-analysis**: pushed 2026-08-04 (yesterday)
- **wasita/joint-planning-lit**: pushed 2026-08-04
- **kubeflow/pipelines**: pushed 2026-08-04 (active ML infra)
- **kubeflow/spark-operator**: pushed 2026-08-04
- **TeglonLabs/jank-crane**: C++ GF3 convergence hub, pushed 2026-06-08

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, alice + bob + A–Z)

All addresses queried against Aptos mainnet. All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version 6,615,856,795. Accounts exist but have no registered APT CoinStore (may hold other resources, be multisig controllers, or have never received APT directly).

**All 28 balances: 0.0 APT**

### Multisig Contract Probes — All 5 Healthy

All probes via `0x1::multisig_account::num_signatures_required` — **all require 2-of-N signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable via REST API.** The endpoint is a Next.js SPA — `https://testnet.mnx.fi/api/markets` returns an HTML shell requiring client-side JS rendering. No market data extractable without a headless browser. Zero rows stored in `mnx_snapshots`.

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
