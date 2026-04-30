# World-Increment Sweep — 2026-04-30

## Sweep Metadata
- **Date:** 2026-04-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** installed from latest (duckdb_cli-linux-amd64)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | count_star()
389 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Next.js SPA) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1 | plurigrid (org) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 2 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4 | bmorphism (user) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 5 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7 | DJedamski (user) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 8 | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | 1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | — | 100 |
| bmorphism | — | 100 |
| zubyul | — | 49 |
| kubeflow | — | 47 |
| AustinCStone | — | 40 |
| migalkin | — | 19 |
| wasita | — | 10 |
| M1shaaa | — | 8 |
| kristinezheng | — | 6 |
| DJedamski | — | 6 |
| TeglonLabs | — | 4 |
| **TOTAL** | | **389** |

---

## Top Repos by Stars

| Source | Repo | Language | Stars | Last Pushed |
|--------|------|----------|-------|-------------|
| kubeflow | kubeflow |  | 15610 | 2026-04-29 |
| kubeflow | pipelines | Python | 4130 | 2026-04-30 |
| kubeflow | spark-operator | Python | 3121 | 2026-04-28 |
| kubeflow | trainer | Go | 2095 | 2026-04-30 |
| kubeflow | katib | Python | 1681 | 2026-04-14 |
| kubeflow | examples | Jsonnet | 1460 | 2025-04-14 |
| kubeflow | manifests | YAML | 1013 | 2026-04-30 |
| kubeflow | arena | Go | 810 | 2026-04-28 |
| kubeflow | kale | Python | 684 | 2026-04-30 |
| kubeflow | mpi-operator | Go | 524 | 2026-04-14 |
| kubeflow | fairing | Jsonnet | 337 | 2022-04-11 |
| kubeflow | pytorch-operator | Jsonnet | 310 | 2021-12-01 |
| kubeflow | community | Jsonnet | 195 | 2026-04-29 |
| kubeflow | website | HTML | 184 | 2026-04-28 |
| kubeflow | kfp-tekton | TypeScript | 182 | 2024-11-19 |
| kubeflow | kfctl | Go | 182 | 2023-08-15 |
| kubeflow | hub | Go | 174 | 2026-04-29 |
| kubeflow | example-seldon | Jupyter Notebook | 172 | 2021-12-01 |
| kubeflow | mcp-apache-spark-history-server | Python | 161 | 2026-04-28 |
| migalkin | NodePiece | Python | 143 | 2022-02-02 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses probed against Aptos mainnet fullnode.
**Result:** All addresses returned `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These wallets have no APT CoinStore resource — they are either unfunded, use FA (Fungible Asset) standard, or do not exist on-chain.

| World | Address | Balance APT |
|-------|---------|-------------|
| A | `0x8699edc0960dd5b916...` | unfunded/no-CoinStore |
| B | `0x3f892ebe6e45164e63...` | unfunded/no-CoinStore |
| C | `0x38b99e63ada9b6fef1...` | unfunded/no-CoinStore |
| D | `0xf77656248f64d5dd00...` | unfunded/no-CoinStore |
| E | `0xdc1d9d533bac3507f9...` | unfunded/no-CoinStore |
| F | `0x18a14b5b4bec118c1c...` | unfunded/no-CoinStore |
| G | `0x69a394c0b0ac842127...` | unfunded/no-CoinStore |
| H | `0xce67c327a7844e5488...` | unfunded/no-CoinStore |
| I | `0x070fe5d74e4eda30e2...` | unfunded/no-CoinStore |
| J | `0x4d964db8f538374034...` | unfunded/no-CoinStore |
| K | `0xa732040a6b0d559041...` | unfunded/no-CoinStore |
| L | `0x7c2eaeafad9725492e...` | unfunded/no-CoinStore |
| M | `0x6fed37a7553ef16b2a...` | unfunded/no-CoinStore |
| N | `0xe7dde6da0a65f51062...` | unfunded/no-CoinStore |
| O | `0x73252b6011a75115a2...` | unfunded/no-CoinStore |
| P | `0x6218792de4a9bc3891...` | unfunded/no-CoinStore |
| Q | `0xac40fa50b81b4ca6b1...` | unfunded/no-CoinStore |
| R | `0x7ce605cc8fda4f8e4a...` | unfunded/no-CoinStore |
| S | `0xb8753014e4888ea48a...` | unfunded/no-CoinStore |
| T | `0x35781dc0e42fef3f25...` | unfunded/no-CoinStore |
| U | `0x75860da47565f6509b...` | unfunded/no-CoinStore |
| V | `0xb59dd8170321dfab5a...` | unfunded/no-CoinStore |
| W | `0x5f32aef70f5ba530d3...` | unfunded/no-CoinStore |
| X | `0xa95cbbd116548ac990...` | unfunded/no-CoinStore |
| Y | `0xd8e32848f1dffa811b...` | unfunded/no-CoinStore |
| Z | `0x7af0ef6e1bd706f4b3...` | unfunded/no-CoinStore |
| alice | `0xc793acdec12b4a6371...` | unfunded/no-CoinStore |
| bob | `0x0a3c00c58fdf9020b2...` | unfunded/no-CoinStore |

---

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

---

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi is a Next.js SPA with client-side rendering. No REST API endpoints (`/api/markets`, `/api/v1/markets`) returned JSON data. The SPA loads but market data is populated dynamically via JavaScript. Recorded as placeholder in `mnx_snapshots` table.

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
- **kubeflow/kubeflow**: 15,610 stars — flagship ML platform for Kubernetes (pushed 2026-04-29)
- **kubeflow/pipelines**: 4,130 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-30)
- **kubeflow/spark-operator**: 3,121 stars — Kubernetes operator for Apache Spark
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring (pushed 2026-04-30)
- **plurigrid/zig-syrup**: Zig/OCapN implementation pushed 2026-04-30 (most recent plurigrid activity)
- **plurigrid/asi**: 17 stars — topological chemputer
- **Multisigs A-B, A-G, Y-Z, S-T, V-W**: All healthy, all require 2-of-N signatures
- **Aptos wallets (alice/bob/A-Z)**: 28 addresses probed; all unfunded (no APT CoinStore resource on mainnet at ledger version ~5,065,337,000)
- **MNX testnet**: Next.js SPA — no REST API available in server-rendered HTML
