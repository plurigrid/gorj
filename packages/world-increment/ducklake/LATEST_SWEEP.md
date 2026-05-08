# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-08  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 33 (10 added this sweep) |
| Total Repo Snapshots | 1,023 (79 added this sweep) |
| Aptos Addresses Probed | 28 |
| Multisig Pairs Probed | 5 |
| MNX Markets | unavailable (SPA/no public API) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — New Increments (IDs 12–21)

| ID | Source | Source Type | GF3 Trit | Color | Name |
|----|--------|-------------|----------|-------|------|
| 12 | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 13 | kubeflow | org | 1 | `#b8bb26` | **PLUS** |
| 14 | TeglonLabs | org | 2 | `#cc241d` | **MINUS** |
| 15 | zubyul | user | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 1 | `#b8bb26` | **PLUS** |
| 17 | migalkin | user | 2 | `#cc241d` | **MINUS** |
| 18 | DJedamski | user | 0 | `#d3869b` | **ERGODIC** |
| 19 | AustinCStone | user | 1 | `#b8bb26` | **PLUS** |
| 20 | aptos_mainnet | chain | 2 | `#cc241d` | **MINUS** |
| 21 | aptos_multisig | chain | 0 | `#d3869b` | **ERGODIC** |

### Repo Snapshots by Source (2026-05-08, 79 new rows)

| org/user | repos snapshotted | total stars |
|----------|-------------------|-------------|
| kubeflow | 20 | 30,658 |
| migalkin | 5 | 35 |
| plurigrid | 20 | 32 |
| TeglonLabs | 15 | 5 |
| zubyul | 11 | 2 |
| DJedamski | 4 | 2 |
| AustinCStone | 4 | 0 |

### Top Repos by Stars (2026-05-08 sweep)

| repo | stars | language | last pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,626 | — | 2026-05-07 |
| kubeflow/pipelines | 4,136 | Python | 2026-05-08 |
| kubeflow/spark-operator | 3,124 | Python | 2026-05-08 |
| kubeflow/trainer | 2,096 | Go | 2026-05-08 |
| kubeflow/katib | 1,683 | Python | 2026-05-08 |
| kubeflow/manifests | 1,015 | YAML | 2026-05-08 |
| kubeflow/arena | 810 | Go | 2026-05-07 |
| kubeflow/kale | 684 | Python | 2026-05-08 |
| kubeflow/mpi-operator | 524 | Go | 2026-05-05 |
| plurigrid/asi | 21 | HTML | 2026-04-26 |

### Social Graph Coverage

- **plurigrid** (org): 20 repos — gorj pushed `2026-05-08`, nanoclj-zig, zig-syrup active
- **kubeflow** (org): 20 repos — notebooks, trainer, pipelines, spark-operator all pushed today
- **TeglonLabs** (org): 15 repos — Stahl (Rust scheme interpreter), vibespace, duck-ui
- **bmorphism** (user): no public repos via unauthenticated GitHub API (private or rate-limited)
- **zubyul** (user): 11 repos — asi, voice-observatory, ghostel-emacs-worlds most recent
- **migalkin** (user): 5 repos — kgcourse2021 ★25, graph ML focus
- **DJedamski** (user): 4 repos — last activity 2018
- **wasita**, **kristinezheng**, **M1shaaa** (social graph): no public repos found

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 28 addresses)

All 28 addresses returned **0.0 APT** — `CoinStore<AptosCoin>` resource not found.  
These wallets exist on-chain but hold no native APT (may hold other tokens or be unfunded).

| world | address (truncated) | balance_apt |
|-------|---------------------|-------------|
| alice | 0xc793ac…cc7b | 0.0 |
| bob | 0x0a3c00…512d | 0.0 |
| A | 0x8699ed…b9d7a | 0.0 |
| B | 0x3f892e…b13 | 0.0 |
| C | 0x38b99e…535e | 0.0 |
| D | 0xf77656…fdd1 | 0.0 |
| E | 0xdc1d9d…d36 | 0.0 |
| F | 0x18a14b…f71 | 0.0 |
| G | 0x69a394…f32 | 0.0 |
| H | 0xce67c3…300f | 0.0 |
| I–Z (18) | various | 0.0 each |

**Total APT across Hamming swarm:** 0.0  
**API:** `fullnode.mainnet.aptoslabs.com/v1` (1s sleep between calls)

### Multisig Contract Probes — ALL HEALTHY ✓

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4f4…7003 | 2 | ✓ |
| A-G | 0xf56c4a…0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1…b883 | 2 | ✓ |
| S-T | 0x3b1c3a…7883 | 2 | ✓ |
| V-W | 0x40fad7…eb6d | 2 | ✓ |

**Function:** `0x1::multisig_account::num_signatures_required`  
**Result:** All 5 pairs require exactly **2 signatures** — 2-of-2 multisig, all contracts live.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE — no public REST API**  
`testnet.mnx.fi` is a Next.js SPA (Vercel). Frontend loads (HTTP 200) but all probed REST paths (`/api/markets`, `/api/tickers`, `/api/v1/markets`) on both `testnet.mnx.fi` and `api.testnet.mnx.fi` returned no data. Market data requires WebSocket or authenticated session.  
**mnx_snapshots rows inserted:** 0

---

## DuckDB State (post-sweep)

| table | total rows |
|-------|-----------|
| world_increments | 33 |
| repo_snapshots | 1,023 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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
- `id % 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id % 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id % 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,626 stars — flagship ML platform for Kubernetes, +61 stars since April sweep
- **kubeflow/pipelines**: 4,136 stars — +17 since April; pushed 2026-05-08
- **kubeflow/spark-operator**: 3,124 stars — +13 since April
- **plurigrid/gorj**: 117 open issues — active forj+Rama+GF(3) REPL orchestration work
- **plurigrid/nanoclj-zig**: NaN-boxed Clojure interpreter in Zig 0.15 with GF(3) trit conservation
- **zubyul/voice-observatory**: New — passive macOS TUI for voice-download pathway observation
- **All 5 multisig contracts**: Healthy 2-of-2 (A-B, A-G, Y-Z, S-T, V-W)
- **Hamming swarm (A–Z + alice/bob)**: 28 addresses probed — zero APT balances on mainnet
