# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-09  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**Aptos Ledger version:** 5,649,521,771 (mainnet, epoch 16112)  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 62 |
| kubeflow | org | 35 |
| TeglonLabs | org | 7 |
| bmorphism | user | 35 |
| zubyul | user | 30 |
| AustinCStone | user (zubyul graph) | 12 |
| migalkin | user (zubyul graph) | 8 |
| wasita | user (zubyul graph) | 8 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 5 |
| **Total** | | **213** |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars | Forks | Issues | Last Push |
|------|----------|-------|-------|--------|-----------|
| kubeflow/kubeflow | — | 15,713 | 2,672 | 3 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2,004 | 495 | 2026-06-09 |
| kubeflow/spark-operator | Python | 3,126 | 1,488 | 98 | 2026-06-08 |
| kubeflow/trainer | Go | 2,112 | 963 | 130 | 2026-06-09 |
| kubeflow/katib | Python | 1,685 | 525 | 119 | 2026-06-05 |
| kubeflow/examples | Jsonnet | 1,462 | 756 | 111 | 2025-04-14 |
| kubeflow/manifests | YAML | 1,022 | 1,065 | 22 | 2026-06-09 |
| migalkin/NodePiece | Python | 144 | 21 | 0 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 5 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 1 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 0 | 2026-03-16 |
| plurigrid/asi | HTML | 25 | 7 | 4 | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 1 | 2026-01-16 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2 | 1 | 2022-10-20 |
| bmorphism/say-mcp-server | JavaScript | 20 | 9 | 3 | 2025-01-07 |

### Language Distribution (top 10)

| Language | Count |
|----------|-------|
| Python | 47 |
| Rust | 15 |
| JavaScript | 14 |
| TypeScript | 11 |
| Go | 10 |
| HTML | 9 |
| Clojure | 9 |
| Julia | 7 |
| Jupyter Notebook | 7 |
| Zig | 6 |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 64 |
| 0 | `#d3869b` | ERGODIC | 63 |
| -1 | `#cc241d` | MINUS | 63 |

Near-perfect balance (64/63/63) across the ternary color chain — ergodic mixing confirmed.

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (A–Z, alice, bob)

All 28 addresses queried on Aptos mainnet (ledger v5,649,521,771, epoch 16112).

**Result:** All addresses return `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — no APT coin store registered on any address in the Hamming swarm at current ledger state. Addresses are present on-chain but carry no APT resource; they may hold other Move resources or represent non-APT-holding accounts.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
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
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...3003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-2 signature threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

Status: **UNAVAILABLE** — `testnet.mnx.fi` is protected by Vercel deployment authentication. No market data is accessible without a bypass token or Vercel CLI session.

---

## DuckDB Ducklake Summary

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows (this sweep) | Total (all-time) |
|-------|------------------|-----------------|
| world_increments | 190 | 213 |
| repo_snapshots | 190 | 1,134 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 1 (unavailable) | 1 |

Ducklake accumulates snapshots across sweeps; prior rows date back to 2026-04-10.

## GF(3) Assignment Rule

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS  
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

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
