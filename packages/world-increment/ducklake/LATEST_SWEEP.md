# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-10T~14:00 UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC `#d3869b` | id%3==1 → trit=1 PLUS `#b8bb26` | id%3==2 → trit=-1 MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried

| Source | Type | Repos snapshotted |
|--------|------|-------------------|
| plurigrid | org | 13 |
| kubeflow | org | 11 |
| TeglonLabs | org | 7 |
| zubyul | user | 6 |
| migalkin | user (social graph) | 3 |
| wasita | user (social graph) | 3 |
| kristinezheng | user (social graph) | 2 |
| M1shaaa | user (social graph) | 2 |
| AustinCStone | user (social graph) | 2 |
| DJedamski | user (social graph) | 1 |

**Total:** 50 repo snapshots, 9 events → 59 world_increment rows

### Notable repos (by stars)

| Repo | Stars | Language | Last pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,565 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-06 |
| kubeflow/trainer | 2,079 | Go | 2026-04-10 |
| kubeflow/katib | 1,675 | Python | 2026-04-02 |
| kubeflow/arena | 808 | Go | 2026-03-19 |
| kubeflow/kale | 682 | Python | 2026-04-10 |
| kubeflow/mcp-apache-spark-history-server | 150 | Python | 2026-04-08 |
| kubeflow/model-registry | 172 | Go | 2026-04-10 |
| migalkin/NodePiece | 143 | Python | 2022-02-02 |
| migalkin/StarE | 88 | Python | 2023-12-01 |
| plurigrid/asi | 16 | HTML | 2026-04-10 |

### Recent events (bmorphism + zubyul)

**bmorphism** (as of 2026-04-10):
- `PushEvent` → `plurigrid/web-browser` (multiple pushes, active Rust browser dev)
- `PushEvent` → `plurigrid/graywall` (container-free AI agent sandbox)
- `ForkEvent` → `GreyhavenHQ/greywall` (forked upstream sandbox)
- `PushEvent` → `plurigrid/nanoclj-zig` (NaN-boxed Clojure/Zig interpreter)
- `WatchEvent` → `BlockScience/gds-core`

**zubyul** (as of 2026-04-10):
- `CreateEvent` × many → `plurigrid/gorj` (active branch creation in forj repo)
- `PullRequestEvent` × 2 → `plurigrid/gorj`
- `PushEvent` → `plurigrid/asi-skills`
- `CreateEvent` → `plurigrid/asi`

### GF(3) Distribution

| Trit | Color | Name | ~Count |
|------|-------|------|--------|
| 0 | `#d3869b` | ERGODIC | 20 |
| 1 | `#b8bb26` | PLUS | 20 |
| -1 | `#cc241d` | MINUS | 19 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.  
All addresses returned **0 APT** — no `0x1::coin::CoinStore<AptosCoin>` resource initialized on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0 |
| bob   | 0x0a3c...2d5d | 0 |
| A     | 0x8699...9d7a | 0 |
| B     | 0x3f89...b13  | 0 |
| C     | 0x38b9...35e  | 0 |
| D     | 0xf776...dd1  | 0 |
| E     | 0xdc1d...d36  | 0 |
| F     | 0x18a1...f71  | 0 |
| G     | 0x69a3...f32  | 0 |
| H     | 0xce67...30f  | 0 |
| I     | 0x070f...fc9  | 0 |
| J     | 0x4d96...f54  | 0 |
| K     | 0xa732...dc4  | 0 |
| L     | 0x7c2e...a9   | 0 |
| M     | 0x6fed...2e9  | 0 |
| N     | 0xe7dd...b2c  | 0 |
| O     | 0x7325...89d  | 0 |
| P     | 0x6218...948  | 0 |
| Q     | 0xac40...89a9 | 0 |
| R     | 0x7ce6...e10  | 0 |
| S     | 0xb875...386  | 0 |
| T     | 0x3578...588  | 0 |
| U     | 0x7586...956  | 0 |
| V     | 0xb59d...2b3  | 0 |
| W     | 0x5f32...b0   | 0 |
| X     | 0xa95c...47d  | 0 |
| Y     | 0xd8e3...4c4  | 0 |
| Z     | 0x7af0...97c  | 0 |

**Total APT across swarm: 0** (accounts not initialized on Aptos mainnet)

### Multisig Contract Probes

All 5 contracts probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed on each.**

### MNX Markets (testnet.mnx.fi)

- HTTP status: 200 (site reachable)
- Frontend: Next.js SPA
- API paths probed: `/api/markets`, `/api/v1/markets`, `/api/v2/markets`, `/api/tickers`, `/api/pairs`, `/markets`
- Result: All API paths return empty responses; `/markets` returns SPA shell HTML
- **Status: Market data unavailable** — no public JSON API found; recorded as `SPA_UNAVAILABLE`

---

## DuckDB Table Summary

```
world_increments : 59 rows  (50 repo_snapshot + 9 event increments)
repo_snapshots   : 50 rows  (10 sources, plurigrid/kubeflow/TeglonLabs/zubyul + social graph)
aptos_snapshots  : 28 rows  (alice, bob, A-Z; all 0 APT)
multisig_probes  :  5 rows  (A-B, A-G, Y-Z, S-T, V-W; all healthy, sigs=2)
mnx_snapshots    :  1 row   (SPA_UNAVAILABLE)
```

## GF(3) Color Semantics

Each `world_increment` is colored by `id % 3`:

- **ERGODIC** (`#d3869b`, trit=0): stable, identity-preserving increments
- **PLUS** (`#b8bb26`, trit=1): additive, growth increments
- **MINUS** (`#cc241d`, trit=-1): subtractive, contraction increments

The color chain provides compositional open-game coloring for REPL orchestration across the social graph topology.
