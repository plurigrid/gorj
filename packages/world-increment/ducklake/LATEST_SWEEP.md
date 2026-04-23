# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-23

## Sweep Metadata
- **Date:** 2026-04-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Source Coverage

| Source | Type | Live Fetch | Repos in DB |
|--------|------|-----------|-------------|
| plurigrid | org | ✅ 100 repos live | 300 |
| kubeflow | org | ⚠️ rate-limited (historical) | 94 |
| TeglonLabs | org | ⚠️ rate-limited (historical) | 106 |
| bmorphism | user | ⚠️ rate-limited (historical) | 200 |
| zubyul | user | ⚠️ rate-limited (historical) | 48 |
| kristinezheng | user | ✅ 18 repos live | 54 |
| migalkin | user | ⚠️ rate-limited (historical) | 60 |
| DJedamski | user | ⚠️ rate-limited (historical) | 22 |
| wasita | user | ⚠️ rate-limited (historical) | 60 |
| M1shaaa | user | ⚠️ rate-limited (historical) | 32 |
| AustinCStone | user | ⚠️ rate-limited (historical) | 86 |

> Anonymous GitHub API (60 req/hr limit) was exhausted after plurigrid and kristinezheng. All other sources reflect historical DB data from the 2026-04-12 sweep.

### Stars by Source (Cumulative DB)

| Source | Total Stars | Total Forks | Repos |
|--------|-------------|-------------|-------|
| kubeflow | 67,723 | 26,703 | 94 |
| migalkin | 554 | 98 | 60 |
| bmorphism | 262 | 26 | 200 |
| AustinCStone | 216 | 76 | 86 |
| plurigrid | 123 | 58 | 300 |
| zubyul | 26 | 2 | 48 |
| DJedamski | 14 | 4 | 22 |
| TeglonLabs | 12 | 6 | 106 |
| wasita | 6 | 2 | 60 |
| M1shaaa | 0 | 0 | 32 |
| kristinezheng | 0 | 0 | 54 |

### plurigrid Top Repos (live as of 2026-04-23)

| Repo | Language | Stars | Forks | Last Push |
|------|----------|-------|-------|-----------|
| plurigrid/asi | HTML | 17 | 5 | 2026-04-20 |
| plurigrid/ontology | JavaScript | 7 | 9 | 2025-05-27 |
| plurigrid/asi-skills | Julia | 3 | 1 | 2026-04-09 |
| plurigrid/zig-syrup | Zig | 2 | 2 | 2026-04-21 |
| plurigrid/horse | TeX | 1 | 1 | 2026-04-10 |
| plurigrid/vivarium | Clojure | 1 | 0 | 2026-04-08 |

> `plurigrid/asi` gained 1 star since the 2026-04-12 sweep (16 → 17).

### Language Distribution (DB-wide, top 15)

| Language | Repos |
|----------|-------|
| Python | 163 |
| HTML | 41 |
| Rust | 40 |
| Go | 39 |
| JavaScript | 31 |
| Jupyter Notebook | 27 |
| TypeScript | 24 |
| Clojure | 21 |
| R | 16 |
| Jsonnet | 16 |
| C | 13 |
| Scheme | 12 |
| Java | 12 |
| TeX | 12 |
| Julia | 11 |

### GF(3) Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 46 |
| +1 | `#b8bb26` | PLUS | 48 |
| -1 | `#cc241d` | MINUS | 47 |

Chain: `…ERGODIC→PLUS→MINUS→ERGODIC→PLUS→MINUS…` (141 increments total, ids 1–118)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 addresses returned `resource_not_found` — wallets have not been funded with APT via the standard coin module, or have not been registered on-chain.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...512d` | 0.0 |
| A | `0x8699...9d7a` | 0.0 |
| B | `0x3f89...b13` | 0.0 |
| C | `0x38b9...535e` | 0.0 |
| D | `0xf776...cfd1` | 0.0 |
| E | `0xdc1d...8d36` | 0.0 |
| F | `0x18a1...3cf71` | 0.0 |
| G | `0x69a3...cf32` | 0.0 |
| H | `0xce67...300f` | 0.0 |
| I | `0x070f...c1fc9` | 0.0 |
| J | `0x4d96...7f54` | 0.0 |
| K | `0xa732...25dc4` | 0.0 |
| L | `0x7c2e...7eba9` | 0.0 |
| M | `0x6fed...b7f2e9` | 0.0 |
| N | `0xe7dd...51b2c` | 0.0 |
| O | `0x7325...5a89d` | 0.0 |
| P | `0x6218...ec948` | 0.0 |
| Q | `0xac40...c89a9` | 0.0 |
| R | `0x7ce6...76e10` | 0.0 |
| S | `0xb875...9d0386` | 0.0 |
| T | `0x3578...f4588` | 0.0 |
| U | `0x7586...f9956` | 0.0 |
| V | `0xb59d...89af2c3` | 0.0 |
| W | `0x5f32...cc7b0` | 0.0 |
| X | `0xa95c...e33047d` | 0.0 |
| Y | `0xd8e3...f2444c4` | 0.0 |
| Z | `0x7af0...e4e197c` | 0.0 |

### Multisig Contract Probes

`0x1::multisig_account::num_signatures_required` called for 5 pairs.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...87003` | 2 | ✅ healthy |
| A-G | `0xf56c...c0096` | 2 | ✅ healthy |
| Y-Z | `0xd3ff...b883` | 2 | ✅ healthy |
| S-T | `0x3b1c...d7883` | 2 | ✅ healthy |
| V-W | `0x40fa...0eb6d` | 2 | ✅ healthy |

**5/5 multisig contracts healthy — 2-of-N threshold on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

**Status: SPA unavailable.** `testnet.mnx.fi` serves a Next.js client-side app. Neither `/api/markets` nor `/api/v1/markets` returns structured data via `curl`. Market data requires JavaScript execution. Recorded as sentinel row in `mnx_snapshots`.

---

## DuckDB Table Counts

```
world_increments    141 rows  (GF3 color chain, per-repo increments)
repo_snapshots     1062 rows  (cumulative repo metadata, 11 sources)
aptos_snapshots      28 rows  (Hamming swarm alice + bob + A–Z)
multisig_probes       5 rows  (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots         1 row   (SPA-unavailable sentinel)
```

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow** dominates with 67,723 cumulative stars across 94 repos
- **plurigrid/asi** hit 17 stars (up from 16 on 2026-04-12) — HTML topological chemputer
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- All 5 Hamming multisig pairs report **2 signatures required** and are healthy on mainnet
- Hamming swarm wallets (A–Z + alice + bob): all unfunded, **0 APT** total
