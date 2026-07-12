# World-Increment Sweep + Hamming Snapshot — 2026-07-12

## Sweep Metadata
- **Date:** 2026-07-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Found | Total Stars |
|--------|------|-------------|-------------|
| kubeflow | org | 49 | 98,252 |
| migalkin | user (social) | 19 | 829 |
| bmorphism | user | 50 | 368 |
| AustinCStone | user (social) | 40 | 308 |
| plurigrid | org | 50 | 134 |
| zubyul | user | 49 | 33 |
| TeglonLabs | org | 5 | 14 |
| DJedamski | user (social) | 6 | 14 |
| wasita | user (social) | 11 | 10 |
| M1shaaa | user (social) | 8 | 0 |
| kristinezheng | user (social) | 5 | 0 |

### Notable Active Repos (pushed last 30d)

- **plurigrid/gorj** — Clojure, 1134 open issues, pushed 2026-07-12 (today)
- **plurigrid/asi** — HTML, 30⭐, pushed 2026-07-10
- **kubeflow/kubeflow** — 15771⭐, pushed 2026-07-12
- **kubeflow/mcp-server** — Python MCP tooling for Kubeflow, pushed 2026-07-12
- **kubeflow/pipelines** — 4169⭐, pushed 2026-07-11
- **kubeflow/trainer** — 2136⭐ distributed AI training, pushed 2026-07-11
- **bmorphism/Gay.jl** — Julia, 187 open issues, pushed 2026-06-20
- **migalkin/kgcourse2021** — HTML, 24⭐, pushed 2026-07-10
- **wasita/wasita.github.io** — Svelte personal site, pushed 2026-07-06
- **TeglonLabs/jank-crane** — C++, crane-jank converged-IR hub, pushed 2026-06-08

### GF(3) Color Chain Distribution (this sweep, 73 new increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 31 |
| +1 | `#b8bb26` | PLUS | 33 |
| -1 | `#cc241d` | MINUS | 32 |

GF(3) assignment rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
Accounts may exist on-chain but have no APT CoinStore registered.

| World | Address (prefix) | Balance (APT) | Status |
|-------|------------------|---------------|--------|
| alice | `0xc793...cc7b` | 0 | no CoinStore |
| bob | `0x0a3c...512d` | 0 | no CoinStore |
| A–Z (26) | various | 0 each | no CoinStore |

### Multisig Contract Probes — All 5 Healthy

All contracts require **2 signatures** (`num_signatures_required = 2`).

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | `0x0da4f4...` | 2 | ✓ |
| A-G | `0xf56c4a...` | 2 | ✓ |
| Y-Z | `0xd3ffe1...` | 2 | ✓ |
| S-T | `0x3b1c3a...` | 2 | ✓ |
| V-W | `0x40fad7...` | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no API data extractable.**
All probed paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`)
return the same HTML shell. The site is a client-side SPA; no server-rendered market
data is available via HTTP. Recorded as `unavailable` in `mnx_snapshots`.

---

## Database State

| Table | Rows (cumulative) |
|-------|-------------------|
| world_increments | 1017+ |
| repo_snapshots | 1017+ |
| aptos_snapshots | 28 (this sweep) |
| multisig_probes | 5 (this sweep) |
| mnx_snapshots | unavailable marker |

## Schema Reference
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
