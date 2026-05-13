# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-13

## Sweep Metadata
- **Date:** 2026-05-13T21:30:00Z (UTC)
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 34 |
| Total Repo Snapshots | 1293 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GitHub Social Graph Sweep

### Sources Scanned

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 6 (top active) |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 6 |
| **TOTAL** | | **349** |

### GF(3) Color Chain (per source sweep)
- `id % 3 == 0` → trit=0, name=ERGODIC, color=#d3869b
- `id % 3 == 1` → trit=1, name=PLUS, color=#b8bb26
- `id % 3 == 2` → trit=-1, name=MINUS, color=#cc241d

### Top 15 Most Recently Pushed Repos

| Pushed At | Repo | Language | Stars |
|-----------|------|----------|-------|
| 2026-05-13T21:20:35Z | plurigrid/gorj | Clojure | 0 |
| 2026-05-13T20:18:40Z | kubeflow/website | HTML | 184 |
| 2026-05-13T19:15:35Z | kubeflow/mcp-apache-spark-history-server | Python | 168 |
| 2026-05-13T18:44:27Z | kubeflow/manifests | YAML | 1017 |
| 2026-05-13T14:25:04Z | M1shaaa/M1shaaa | — | 0 |
| 2026-05-13T13:05:37Z | kubeflow/trainer | Go | 2098 |
| 2026-05-13T05:35:31Z | wasita/wasita.github.io | Svelte | 1 |
| 2026-05-13T05:29:04Z | wasita/wm-cv | Svelte | 0 |
| 2026-05-13T00:35:31Z | bmorphism/Gay.jl | Julia | 1 |
| 2026-05-12T22:53:36Z | kubeflow/pipelines | Python | 4140 |
| 2026-05-07T20:12:15Z | bmorphism/nanoclj-zig | Zig | 0 |
| 2026-05-07T19:49:05Z | bmorphism/zig-syrup | Zig | 0 |
| 2026-05-07T13:46:41Z | kubeflow/kubeflow | — | 15630 |
| 2026-05-07T04:35:12Z | plurigrid/horse | TeX | 1 |
| 2026-05-06T05:14:00Z | wasita/vocoder | JavaScript | 0 |

---

## Aptos Hamming Swarm Snapshot

Balances queried via `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` view function on Aptos Mainnet.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.436434 |
| bob | 0x0a3c...512d5d | **12.657007** |
| A | 0x8699...be9d7a | 0.051767 |
| B | 0x3f89...cb13 | 0.036256 |
| C | 0x38b9...535e | 0.010185 |
| D | 0xf776...cfdd1 | 0.011629 |
| E | 0xdc1d...8d36 | 0.009372 |
| F | 0x18a1...cf71 | **1.960516** |
| G | 0x69a3...c7f32 | 0.000681 |
| H | 0xce67...5300f | 0.001681 |
| I | 0x070f...1fc9 | 0.000681 |
| J | 0x4d96...7f54 | **1.895093** |
| K | 0xa732...25dc4 | 0.161961 |
| L | 0x7c2e...eba9 | **1.927269** |
| M | 0x6fed...7f2e9 | 0.112285 |
| N | 0xe7dd...51b2c | 0.106121 |
| O | 0x7325...5a89d | 0.210136 |
| P | 0x6218...ec948 | 0.140136 |
| Q | 0xac40...c89a9 | 0.103240 |
| R | 0x7ce6...76e10 | 0.090217 |
| S | 0xb875...d0386 | 0.091788 |
| T | 0x3578...4588 | 0.073713 |
| U | 0x7586...f9956 | 0.055773 |
| V | 0xb59d...af2c3 | 0.048833 |
| W | 0x5f32...c7b0 | 0.040705 |
| X | 0xa95c...047d | 0.042577 |
| Y | 0xd8e3...444c4 | 0.044449 |
| Z | 0x7af0...197c | 0.024268 |

**Notable:** bob holds the largest balance at **12.657 APT**. F, J, L hold ~1.9 APT each (likely gas reserves for multisig ops). G, H, I are near-empty.

---

## Multisig Contract Probes

All probed via `0x1::multisig_account::num_signatures_required` view function (POST /v1/view).

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | YES |
| A-G | 0xf56c...0096 | 2 | YES |
| Y-Z | 0xd3ff...b883 | 2 | YES |
| S-T | 0x3b1c...7883 | 2 | YES |
| V-W | 0x40fa...eb6d | 2 | YES |

All 5 multisig contracts healthy — all require 2 signatures (2-of-N threshold).

---

## MNX Markets Status

All three endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) at `https://testnet.mnx.fi` return HTML (Next.js SPA), not JSON market data. **MNX Markets API: UNAVAILABLE** — no machine-readable ticker or price data accessible.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,630 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,140 stars — ML pipelines for Kubernetes (pushed 2026-05-12)
- **kubeflow/trainer**: 2,098 stars — distributed AI training (pushed 2026-05-13, most recently active kubeflow repo)
- **plurigrid/gorj**: 0 stars but 181 open issues — this very repo, most recently pushed of all sources
- **bob (0x0a3c...)**: 12.657 APT — dominant holder in the Hamming swarm
- **All multisigs**: 2-of-N healthy across all 5 probed contract pairs
