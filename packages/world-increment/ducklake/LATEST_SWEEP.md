# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-06  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.3 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) → PLUS #b8bb26 (trit=1) → MINUS #cc241d (trit=2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Distinct Repos |
|--------|------|---------------|
| plurigrid | org | 168 |
| bmorphism | user | 165 |
| zubyul | user | 59 |
| TeglonLabs | org | 53 |
| kubeflow | org | 49 |
| AustinCStone | social/zubyul | 43 |
| wasita | social/zubyul | 32 |
| migalkin | social/zubyul | 30 |
| kristinezheng | social/zubyul | 18 |
| M1shaaa | social/zubyul | 16 |
| DJedamski | social/zubyul | 11 |
| **TOTAL** | | **644 distinct repos** |

**World increment records created: 346**

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,706 | — | 2026-05-24 |
| kubeflow/pipelines | 4,152 | Python | 2026-06-05 |
| kubeflow/spark-operator | 3,125 | Python | 2026-06-04 |
| kubeflow/trainer | 2,111 | Go | 2026-06-05 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,020 | YAML | 2026-06-05 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |

### Notable plurigrid Activity (recent pushes)

- `plurigrid/gorj` — Clojure (forj + Rama topology nREPL + GF(3)) — **pushed 2026-06-06**
- `plurigrid/place` — TeX — pushed 2026-06-04
- `plurigrid/eirobri` — Clojure (EiRoBri replay world) — pushed 2026-06-03
- `plurigrid/nash-portal` — Rust (NASH token TUI, WASM + GeckoTerminal) — pushed 2026-05-19
- `plurigrid/zig-syrup` — Zig (OCapN Syrup + CapTP) — pushed 2026-04-30
- `plurigrid/asi` — HTML (25★ everything is topological chemputer) — pushed 2026-04-26

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 addresses (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**Result: all balances = 0.0 APT** — accounts exist on-chain but hold no liquid APT in the coin store at time of snapshot.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (see DB) | 0.0 each |

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisigs healthy — 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is deployed on Vercel with deployment protection (password wall). All API paths (`/api/markets`, `/api/v1/markets`) return authentication-required HTML. No market data extractable without a visitor bypass token.

---

## DuckDB Ducklake Summary

**File:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows |
|-------|------|
| world_increments | 346 |
| repo_snapshots | 1,267 (644 distinct repos) |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

GF(3) color distribution across increments:
- **ERGODIC #d3869b** (trit=0): 107 increments
- **PLUS #b8bb26** (trit=1): 108 increments
- **MINUS #cc241d** (trit=2): 108 increments

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
