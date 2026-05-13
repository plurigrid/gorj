# World-Increment Sweep + Hamming Snapshot

**Timestamp:** 2026-05-13T00:00:00Z  
**Branch:** world-increment/sweep  
**GF(3) Color Chain:** ERGODIC `#d3869b` · PLUS `#b8bb26` · MINUS `#cc241d`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 37 |
| kubeflow | org | 16 |
| TeglonLabs | org | 4 |
| bmorphism | user | 14 |
| zubyul | user | 10 |
| migalkin | user (zubyul social) | 6 |
| DJedamski | user (zubyul social) | 3 |
| wasita | user (zubyul social) | 4 |
| kristinezheng | user (zubyul social) | 3 |
| M1shaaa | user (zubyul social) | 3 |
| AustinCStone | user (zubyul social) | 5 |
| **TOTAL** | | **105 repos** |

### Top Repos by Stars

| Org/User | Repo | Stars | Language |
|----------|------|-------|----------|
| kubeflow | kubeflow | 15,628 | — |
| kubeflow | pipelines | 4,140 | Python |
| kubeflow | spark-operator | 3,126 | Python |
| kubeflow | trainer | 2,098 | Go |
| kubeflow | katib | 1,683 | Python |
| kubeflow | examples | 1,462 | Jsonnet |
| kubeflow | manifests | 1,017 | YAML |
| kubeflow | arena | 810 | Go |
| kubeflow | kale | 686 | Python |
| migalkin | NodePiece | 144 | Python |
| AustinCStone | TextGAN | 92 | Python |
| bmorphism | ocaml-mcp-sdk | 61 | OCaml |
| plurigrid | asi | 21 | HTML |
| bmorphism | anti-bullshit-mcp-server | 23 | JavaScript |

### Most Active Recent Repos (plurigrid ecosystem)

- `plurigrid/gorj` — Clojure, pushed 2026-05-12, 169 open issues
- `plurigrid/zig-syrup` — Zig OCapN Syrup, pushed 2026-04-30
- `plurigrid/asi` — topological chemputer, pushed 2026-04-26
- `plurigrid/nanoclj-zig` — NaN-boxed Clojure in Zig, pushed 2026-04-25
- `bmorphism/ocaml-mcp-sdk` — OCaml MCP SDK, 61 stars, pushed 2026-05-08
- `wasita/wasita.github.io` — personal site (Svelte), pushed 2026-05-13
- `zubyul/voice-observatory` — macOS voice TUI, pushed 2026-04-24

### GF(3) Color Chain Distribution

| Trit | Color | Hex | Count |
|------|-------|-----|-------|
| 0 | ERGODIC | `#d3869b` | 35 |
| 1 | PLUS | `#b8bb26` | 35 |
| −1 | MINUS | `#cc241d` | 35 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|--------------------:|--------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

> All wallets returned 0.0 APT — addresses either hold no APT native coin or the `CoinStore<AptosCoin>` resource has not been initialized.

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|--------------------:|:------------:|:-------:|
| A-B | 0x0da4...003 | 2 | ✅ |
| A-G | 0xf56c...096 | 2 | ✅ |
| Y-Z | 0xd3ff...883 | 2 | ✅ |
| S-T | 0x3b1c...883 | 2 | ✅ |
| V-W | 0x40fa...b6d | 2 | ✅ |

**All 5 multisig contracts are healthy with 2-of-N signature requirements.**

### MNX Markets (testnet.mnx.fi)

The testnet endpoint returns a Next.js SPA with no public REST API exposed at standard paths (`/api/markets`, `/api/v1/markets`). Market data is loaded client-side from JavaScript bundles. **Status: unavailable via headless API probe.**

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 105 | GF(3)-colored increment log |
| `repo_snapshots` | 105 | GitHub repo metadata snapshots |
| `aptos_snapshots` | 28 | Aptos wallet balance snapshot |
| `multisig_probes` | 5 | Multisig contract health probes |
| `mnx_snapshots` | 0 | MNX market data (API unavailable) |

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
