# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04T03:20Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 247 |
| Total Repo Snapshots | 247 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 37 |
| zubyul | user | 22 |
| migalkin | user (zubyul social) | 8 |
| AustinCStone | user (zubyul social) | 8 |
| DJedamski | user (zubyul social) | 4 |
| wasita | user (zubyul social) | 7 |
| kristinezheng | user (zubyul social) | 4 |
| M1shaaa | user (zubyul social) | 5 |
| **TOTAL** | | **247** |

### GF(3) Color Chain — Distribution Across 247 Increments

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 82 |
| +1 | #b8bb26 | PLUS | 83 |
| -1 | #cc241d | MINUS | 82 |

GF(3) chain cycles through: `PLUS → MINUS → ERGODIC → ...` (82-83 cycles completed)

---

## Top Repos by Stars (2026-06-04 snapshot)

| Org/User | Repo | Language | Stars | Forks | Last Push |
|----------|------|----------|-------|-------|-----------|
| kubeflow | kubeflow | — | 15,704 | 2,668 | 2026-05-24 |
| kubeflow | pipelines | Python | 4,151 | 2,004 | 2026-06-03 |
| kubeflow | spark-operator | Python | 3,124 | 1,488 | 2026-06-03 |
| kubeflow | trainer | Go | 2,110 | 964 | 2026-06-03 |
| kubeflow | katib | Python | 1,685 | 525 | 2026-06-04 |
| kubeflow | examples | Jsonnet | 1,462 | 756 | 2025-04-14 |
| kubeflow | manifests | YAML | 1,020 | 1,065 | 2026-06-02 |
| kubeflow | arena | Go | 811 | 191 | 2026-05-07 |
| kubeflow | kale | Python | 690 | 155 | 2026-06-01 |
| kubeflow | mpi-operator | Go | 528 | 235 | 2026-06-02 |
| migalkin | NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone | TextGAN | Python | 92 | 30 | 2025-03-03 |
| bmorphism | ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-05-08 |
| plurigrid | asi | HTML | 24 | 6 | 2026-04-26 |
| bmorphism | anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-02-05 |
| migalkin | StarE | Python | 89 | 16 | 2026-04-16 |
| plurigrid | ontology | JavaScript | 8 | 9 | 2025-05-27 |
| plurigrid | gorj | Clojure | 0 | 0 | 2026-06-04 (338 issues!) |

## Most Recently Active Repos

- `plurigrid/gorj` — 2026-06-04T02:21Z (338 open issues, most active tracker)
- `kubeflow/dashboard` — 2026-06-04T02:16Z
- `kubeflow/katib` — 2026-06-04T01:14Z
- `kubeflow/notebooks` — 2026-06-04T02:11Z
- `kubeflow/hub` — 2026-06-04T00:19Z
- `plurigrid/eirobri` — 2026-06-03T20:43Z

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Ledger v5,558,526,808)

All 28 addresses (alice, bob, A–Z) queried on Aptos mainnet.

**Result: All 28 wallets returned `resource_not_found`**

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793... | 0.0 |
| bob | 0x0a3c... | 0.0 |
| A | 0x8699... | 0.0 |
| B–Z (24 wallets) | various | 0.0 each |

**Note:** `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource not found for any address. These accounts exist on-chain but have not initialized a CoinStore for APT — valid Aptos behavior for accounts that use `0x1::fungible_asset` module instead, or have zero balance.

### Multisig Contract Probes

Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...7003 | **2** | ✓ |
| A-G | 0xf56c4a1c...0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181...b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9...7883 | **2** | ✓ |
| V-W | 0x40fad7b4...eb6d | **2** | ✓ |

**All 5 multisig contracts live and healthy — unanimous 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

- HTTP status: **200 OK** — site is live
- Technology: Next.js SPA (dark theme, React)
- API endpoints probed: `/api/markets`, `/api/v1/markets`, `/api/ticker`
- All return HTML shell — data fetched client-side via WebSocket or browser JS
- **No market data extractable via curl** — mnx_snapshots table empty

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

### Row Counts

| Table | Rows |
|-------|------|
| world_increments | 247 |
| repo_snapshots | 247 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,704 ⭐ — flagship ML platform for Kubernetes (up from 15,565 in April sweep)
- **plurigrid/gorj**: 338 open issues — most active issue tracker in the entire sweep
- **bmorphism/Gay.jl**: 189 open issues — intense GF(3) color library activity
- **bmorphism/ocaml-mcp-sdk**: 61 ⭐ — OCaml SDK using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144 ⭐ — parameter-efficient knowledge graph representations (ICLR'22)
- **All 5 Hamming swarm multisigs**: healthy with 2-of-N unanimous threshold
- **MNX testnet**: live (HTTP 200) but API is SPA-only, no REST endpoint
- **GF(3) sweep**: 247 increments across 82-83 full trit cycles
