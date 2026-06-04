# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-04

## Sweep Metadata
- **Date:** 2026-06-04 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 49 |
| zubyul | user | 100 |
| migalkin | social graph | 19 |
| DJedamski | social graph | 6 |
| wasita | social graph | 11 |
| kristinezheng | social graph | 6 |
| M1shaaa | social graph | 8 |
| AustinCStone | social graph | 30 |
| **TOTAL** | | **381** |

### DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 381 |
| repo_snapshots | 381 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

### GF(3) Color Chain

Color cycle over all 381 repo increments:
- `id%3==0` → trit=0, **ERGODIC** `#d3869b` (rose)
- `id%3==1` → trit=1, **PLUS** `#b8bb26` (yellow-green)
- `id%3==2` → trit=-1, **MINUS** `#cc241d` (red)

Distribution: 127 ERGODIC / 127 PLUS / 127 MINUS (chain closes at id=381, MINUS; next sweep begins at 382, ERGODIC).

### Top Repos by Stars

| Repo | Language | ★ Stars | Last Pushed |
|------|----------|---------|-------------|
| kubeflow/kubeflow | — | 15,705 | 2026-06-01 |
| kubeflow/pipelines | Python | 4,152 | 2026-06-03 |
| kubeflow/spark-operator | Python | 3,124 | 2026-05-28 |
| kubeflow/trainer | Go | 2,110 | 2026-05-30 |
| kubeflow/katib | Python | 1,685 | 2026-05-27 |
| kubeflow/examples | Jsonnet | 1,462 | 2025-12-18 |
| kubeflow/manifests | YAML | 1,020 | 2026-06-02 |
| migalkin/NodePiece | Python | 144 | 2022-02-02 |
| AustinCStone/TextGAN | Python | 92 | 2016-10-04 |
| migalkin/StarE | Python | 89 | 2023-12-01 |
| plurigrid/asi | HTML | 25 | 2026-04-26 |
| migalkin/kgcourse2021 | HTML | 25 | 2025-08-04 |
| migalkin/NBFNet_mlx | Python | 10 | 2024-03-02 |

### Notable Plurigrid Repos (current activity)

| Repo | Language | Description | Last Pushed |
|------|----------|-------------|-------------|
| place | TeX | — | 2026-06-04 |
| gorj | Clojure | forj + Rama topology nREPL routing + GF(3) | 2026-06-04 |
| eirobri | Clojure | EiRoBri replay world | 2026-06-03 |
| nash-portal | Rust | NASH token TUI, ratzilla WASM + OHLCV | 2026-05-19 |
| zig-syrup | Zig | OCapN Syrup / CapTP Zig implementation | 2026-04-30 |
| asi | HTML | topological chemputer | 2026-04-26 |
| nanoclj-zig | Zig | NaN-boxed Clojure interpreter in Zig 0.15 | 2026-04-25 |
| asi-skills | Julia | 69 skills with Galois Hole Type accessibility | 2026-04-26 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (alice, bob, A–Z)

All 28 addresses queried against `fullnode.mainnet.aptoslabs.com`.
`CoinStore<AptosCoin>` resource not present on any address — all return 0.00 APT.
These addresses are either unfunded or have not initialized the APT coin store.

| Range | Balance | Status |
|-------|---------|--------|
| alice | 0.00 APT | no CoinStore |
| bob | 0.00 APT | no CoinStore |
| A–Z (26 addrs) | 0.00 APT each | no CoinStore |

### Multisig Contract Probes

All 5 accounts probed via `0x1::multisig_account::num_signatures_required`.
All returned `2` — all healthy.

| Pair | Contract Address | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | ✓ |
| A-G | 0xf56c4a1c090621... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✓ |
| V-W | 0x40fad7b423a843... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` serves a Next.js SPA — the `/api/markets` path returns HTML,
not JSON. No market data was extractable. `mnx_snapshots` table is empty.
Status: **unavailable (SPA-only, no public REST API)**.

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

## GF(3) Rule
- `id mod 3 == 0` → trit=0, `#d3869b`, ERGODIC
- `id mod 3 == 1` → trit=1, `#b8bb26`, PLUS
- `id mod 3 == 2` → trit=-1, `#cc241d`, MINUS
