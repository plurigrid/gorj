# World-Increment Sweep + Hamming Snapshot — 2026-04-11

## Sweep Metadata
- **Date:** 2026-04-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| ID | GF(3) | Color | Source | Type | Repos | Status |
|----|-------|-------|--------|------|-------|--------|
| 1 | PLUS (+1) | `#b8bb26` | plurigrid | org | 100 | ✓ |
| 2 | MINUS (-1) | `#cc241d` | kubeflow | org | 47 | ✓ |
| 3 | ERGODIC (0) | `#d3869b` | TeglonLabs | org | 53 | ✓ |
| 4 | PLUS (+1) | `#b8bb26` | bmorphism | user | 100 | ✓ |
| 5 | MINUS (-1) | `#cc241d` | zubyul | user | 24 | ✓ |
| 6 | ERGODIC (0) | `#d3869b` | migalkin | user (zubyul-graph) | 30 | ✓ |
| 7 | PLUS (+1) | `#b8bb26` | DJedamski | user (zubyul-graph) | 0 | rate-limited |
| 8 | MINUS (-1) | `#cc241d` | wasita | user (zubyul-graph) | 29 | ✓ |
| 9 | ERGODIC (0) | `#d3869b` | kristinezheng | user (zubyul-graph) | 18 | ✓ |
| 10 | PLUS (+1) | `#b8bb26` | M1shaaa | user (zubyul-graph) | 0 | rate-limited |
| 11 | MINUS (-1) | `#cc241d` | AustinCStone | user (zubyul-graph) | 43 | ✓ |
| 12–16 | ERGODIC (0) | `#d3869b` | bmorphism | events | 5 | ✓ |
| 17–21 | MINUS (-1) | `#cc241d` | zubyul | events | 5 | ✓ |

**Total world_increments:** 21  
**Total repo_snapshots:** 444

### Org/User Stats

| Org/User | Repos | Total Stars | Latest Push |
|----------|-------|-------------|-------------|
| kubeflow | 47 | 33,851 | 2026-04-11 |
| migalkin | 30 | 277 | 2025-08-04 |
| bmorphism | 100 | 131 | 2026-04-09 |
| AustinCStone | 43 | 108 | 2026-02-11 |
| plurigrid | 100 | 40 | 2026-04-11 |
| zubyul | 24 | 13 | 2026-04-09 |
| TeglonLabs | 53 | 6 | 2026-01-16 |
| wasita | 29 | 3 | 2026-04-08 |
| kristinezheng | 18 | 0 | 2026-04-09 |

### Top Repos by Stars

| Repo | Org | Stars | Language | Last Push |
|------|-----|-------|----------|-----------|
| kubeflow/kubeflow | kubeflow | 15,565 | — | 2026-01-05 |
| kubeflow/pipelines | kubeflow | 4,119 | Python | 2026-04-11 |
| kubeflow/spark-operator | kubeflow | 3,111 | Python | 2026-04-10 |
| kubeflow/trainer | kubeflow | 2,080 | Go | 2026-04-10 |
| kubeflow/katib | kubeflow | 1,676 | Python | 2026-04-02 |
| migalkin/NodePiece | migalkin | 143 | Python | 2022-02-02 |
| bmorphism/ocaml-mcp-sdk | bmorphism | 60 | OCaml | 2026-03-16 |
| plurigrid/asi | plurigrid | 16 | HTML | 2026-04-10 |

### Recent plurigrid Activity (Top 5)

| Repo | Language | Stars | Last Push | Description |
|------|----------|-------|-----------|-------------|
| gorj | Clojure | 0 | 2026-04-11 | forj + Rama topology nREPL routing + GF(3) trit coloring |
| horse | TeX | 1 | 2026-04-10 | — |
| web-browser | Rust | 0 | 2026-04-10 | from prepostweb lineage (monaduck1069) |
| asi | HTML | 16 | 2026-04-10 | everything is topological chemputer! |
| nanoclj-zig | Zig | 0 | 2026-04-09 | NaN-boxed Clojure in Zig 0.15, GF(3) trit conservation |

### Recent Events

| Actor | Event Type | Count |
|-------|-----------|-------|
| bmorphism | PushEvent | 5 |
| zubyul | PullRequestEvent | 3 |
| zubyul | CreateEvent | 2 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

28 addresses queried. Accounts exist on mainnet but `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource not found — accounts have migrated to fungible asset standard. Balances recorded as 0 APT via legacy endpoint.

Note: `alice` account confirmed active (sequence_number: 72). Resources moved to fungible asset store.

| World | Address | APT (CoinStore) |
|-------|---------|-----------------|
| alice | 0xc793...cc7b | 0 (FA migrated) |
| bob | 0x0a3c...2d5d | 0 (FA migrated) |
| A | 0x8699...9d7a | 0 (FA migrated) |
| B | 0x3f89...b13 | 0 (FA migrated) |
| C | 0x38b9...535e | 0 (FA migrated) |
| D | 0xf776...fdd1 | 0 (FA migrated) |
| E | 0xdc1d...8d36 | 0 (FA migrated) |
| F | 0x18a1...f71 | 0 (FA migrated) |
| G | 0x69a3...f32 | 0 (FA migrated) |
| H | 0xce67...300f | 0 (FA migrated) |
| I | 0x070f...fc9 | 0 (FA migrated) |
| J | 0x4d96...f54 | 0 (FA migrated) |
| K | 0xa732...dc4 | 0 (FA migrated) |
| L | 0x7c2e...ba9 | 0 (FA migrated) |
| M | 0x6fed...2e9 | 0 (FA migrated) |
| N | 0xe7dd...b2c | 0 (FA migrated) |
| O | 0x7325...89d | 0 (FA migrated) |
| P | 0x6218...948 | 0 (FA migrated) |
| Q | 0xac40...a9 | 0 (FA migrated) |
| R | 0x7ce6...e10 | 0 (FA migrated) |
| S | 0xb875...386 | 0 (FA migrated) |
| T | 0x3578...588 | 0 (FA migrated) |
| U | 0x7586...956 | 0 (FA migrated) |
| V | 0xb59d...f2c3 | 0 (FA migrated) |
| W | 0x5f32...b0 | 0 (FA migrated) |
| X | 0xa95c...47d | 0 (FA migrated) |
| Y | 0xd8e3...44c4 | 0 (FA migrated) |
| Z | 0x7af0...97c | 0 (FA migrated) |

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

**All multisig contracts: 2-of-N, all HEALTHY.**

### MNX Markets (testnet.mnx.fi)

Next.js SPA — API routes return HTML shell, not JSON. Market data not extractable via curl.  
**Status: SPA unavailable; 0 mnx_snapshots recorded.**

---

## DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 21 |
| repo_snapshots | 444 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## GF(3) Color Chain

| Trit | Value | Color | Hex |
|------|-------|-------|-----|
| ERGODIC | 0 | Pink-rose | `#d3869b` |
| PLUS | +1 | Yellow-green | `#b8bb26` |
| MINUS | -1 | Red | `#cc241d` |

- `id % 3 == 0` → ERGODIC (#d3869b)
- `id % 3 == 1` → PLUS (#b8bb26)
- `id % 3 == 2` → MINUS (#cc241d)
