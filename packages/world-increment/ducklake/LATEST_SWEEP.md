# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-15  
**GF(3) Color Chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted |
|--------|------|-------------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 53 |
| zubyul | user | 38 |
| migalkin | user (social graph) | 19 |
| wasita | user (social graph) | 11 |
| AustinCStone | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| **TOTAL** | | **312** |

### Notable Activity (pushed since 2026-06-01)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| plurigrid/gorj | 0 | Clojure | 2026-06-15 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| plurigrid/place | 1 | TeX | 2026-06-10 |
| bmorphism/satreadout | 0 | Lean | 2026-06-10 |
| bmorphism/Gay.jl | 1 | Julia | 2026-06-10 |
| bmorphism/nanoclj-zig | 1 | Zig | 2026-06-10 |
| kubeflow/pipelines | 4154 | Python | 2026-06-15 |
| kubeflow/community | 194 | Jupyter | 2026-06-14 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |
| plurigrid/eirobri | 0 | Clojure | 2026-06-03 |
| bmorphism/flox-mcp-bb | 0 | Clojure | 2026-06-05 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2026-06-05 |

### GF(3) Distribution (this run)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 104 |
| 1 | PLUS | #b8bb26 | 104 |
| -1 | MINUS | #cc241d | 104 |

### DuckDB Ducklake Stats

- `world_increments`: 336 rows (cumulative across all sweeps)
- `repo_snapshots`: 1257 rows (cumulative)
- Database: `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...a9 | 0.0 |
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
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Note:** All 28 hamming-swarm addresses returned 0.0 APT. The `CoinStore` resource was not found for any address, indicating these wallets either hold no APT or have not been initialized on mainnet.

### Multisig Contract Probes

All 5 multisig contracts responded healthy with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...6d | 2 | ✓ |

**All multisigs: 2-of-N threshold, all healthy.**

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: Vercel deployment protection requires visitor password authentication. No market data could be retrieved.

---

## Summary

- **GitHub sweep:** 312 repos snapshotted across 11 sources (3 orgs + 8 users in social graph). Most active: plurigrid/gorj (pushed today), kubeflow/pipelines (4154 stars), bmorphism/ocaml-mcp-sdk (61 stars).
- **Aptos Hamming Swarm:** 28 addresses queried, all at 0.0 APT (wallets not holding APT on mainnet). 5 multisigs all healthy at 2-of-N threshold.
- **MNX:** Unavailable (auth-gated).
- **DuckDB:** `world-increments.duckdb` updated with this sweep.
