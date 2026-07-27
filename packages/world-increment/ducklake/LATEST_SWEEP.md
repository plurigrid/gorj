# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 73 |
| Total Repo Snapshots | 994 |
| Sources Covered | plurigrid org (MCP-scoped; external orgs/users restricted by env policy) |
| Aptos Wallets Probed | 28 |
| Multisig Pairs Probed | 5 |
| MNX Market Rows | 0 (SPA, no public API) |

---

## GF(3) Color Chain Distribution (this run: 50 new increments)

| Trit | Color | Name | Count (cumulative) |
|------|-------|------|-------------------|
| 0 | `#d3869b` | ERGODIC | 23 |
| +1 | `#b8bb26` | PLUS | 25 |
| -1 | `#cc241d` | MINUS | 25 |

GF(3) assignment: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## Top Repos by Source (this run: plurigrid, 50 repos)

### plurigrid (50 repos this run)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 51 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| Plurigraph | JavaScript | 3 | 2025-01-05 |
| act | Python | 3 | 2024-07-26 |
| nash-portal | Rust | 2 | 2026-05-19 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| gorj | Clojure | 1 | 2026-07-27 |
| place | TeX | 1 | 2026-07-14 |
| vivarium | Clojure | 1 | 2026-04-08 |

**Note:** kubeflow, TeglonLabs, bmorphism, zubyul and social graph users not accessible — GitHub API restricted to repository-scoped endpoints only in this environment.

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 wallets returned **0.0 APT** (CoinStore resource not initialized or unfunded on mainnet).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...987003 | 2 | ✅ |
| A-G | 0xf56c...bc0096 | 2 | ✅ |
| Y-Z | 0xd3ff...75b883 | 2 | ✅ |
| S-T | 0x3b1c...d7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — `num_signatures_required = 2` confirmed for all pairs.

### MNX Markets

`testnet.mnx.fi` is a Next.js SPA. API probed at `api.testnet.mnx.fi`:
- `/markets` → 404
- `/v1/markets` → 404
- WebSocket-based API (wss://api.testnet.mnx.fi) not queryable from CLI

**Status: unavailable** — no market data extractable without auth/WebSocket session.

---

## DuckDB Table State

| Table | Rows |
|-------|------|
| world_increments | 73 |
| repo_snapshots | 994 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

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

## Notable Highlights
- **plurigrid/asi**: 51 stars (up from 16 in April run) — topological chemputer, most starred plurigrid repo
- **plurigrid/gorj**: 1440 open issues, pushed today (2026-07-27) — active development
- **plurigrid/place**: TeX, pushed 2026-07-14
- **Multisig swarm**: all 5 pairs (A-B, A-G, Y-Z, S-T, V-W) healthy with sigs_required=2
- **Aptos wallets**: 28 addresses probed, all 0.0 APT on mainnet — likely not yet funded
- **MNX**: WebSocket-only API, not accessible without authenticated session
