# World Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-07-29

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 50 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 43 |
| migalkin | social | 5 |
| DJedamski | social | 3 |
| wasita | social | 5 |
| kristinezheng | social | 3 |
| M1shaaa | social | 3 |
| AustinCStone | social | 5 |
| **TOTAL** | | **322** |

### Notable Repos

**plurigrid** (most active): `gorj` (Clojure, pushed 2026-07-29, 1475 open issues), `zig-syrup` (Zig, OCapN Syrup impl), `asi` (HTML, 52★), `nanoclj-zig` (Zig, NaN-boxed Clojure)

**kubeflow** (most starred): `kubeflow/kubeflow` (15794★), `pipelines` (4171★), `spark-operator` (3142★), `trainer` (2159★, 1000 forks)

**bmorphism** (most active): `Gay.jl` (Julia, 188 open issues, pushed 2026-07-28), `ocaml-mcp-sdk` (OCaml, 61★), `anti-bullshit-mcp-server` (JS, 22★), `say-mcp-server` (JS, 20★), `babashka-mcp-server` (JS, 19★)

**TeglonLabs**: `jank-crane` (C++, GF3 convergence maps, pushed 2026-06-08), `mathpix-gem` (Ruby, 2★), `coin-flip-mcp` (JS, 2 forks)

**zubyul** (recent): `from-possible-worlds` (TeX, pushed 2026-07-18), `voice-observatory` (Python, passive macOS TUI), `nash-tui` (Rust, NASH token candlesticks)

**Social graph highlights**: `migalkin/NodePiece` (144★, KG ICLR'22), `AustinCStone/TextGAN` (92★), `migalkin/StarE` (89★, EMNLP 2020)

### GF(3) Color Chain Distribution (327 world increments)

| Color | Trit | Name | Count |
|-------|------|------|-------|
| #d3869b | 0 | ERGODIC | 109 |
| #b8bb26 | 1 | PLUS | 109 |
| #cc241d | -1 | MINUS | 109 |

GF(3) rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.

**Result:** All wallets returned **0.0 APT** — no `CoinStore<AptosCoin>` resources found. Wallets are unfunded/inactive on mainnet at snapshot time.

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

**All 5 multisig contracts healthy — 2-of-N signatures required across all pairs.**

### MNX Markets

`https://testnet.mnx.fi/api/markets` — **UNAVAILABLE** (SPA endpoints returned no data).

---

## DuckDB Schema Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 327 |
| repo_snapshots | 327 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

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
