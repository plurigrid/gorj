# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 12 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 30 |
| **TOTAL** | | **383** |

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,798 | — | 2026-07-10 |
| kubeflow/pipelines | 4,171 | Python | 2026-07-29 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-31 |
| kubeflow/trainer | 2,165 | Go | 2026-07-31 |
| plurigrid/asi | 56 | HTML | 2026-07-10 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |

### Most Recently Active

- **plurigrid/gorj** — 2026-07-31 (Clojure)
- **M1shaaa/M1shaaa** — 2026-07-31 (profile config pushed today)
- **kubeflow/spark-operator** — 2026-07-31
- **kubeflow/trainer** — 2026-07-31
- **wasita/wasita.github.io** — 2026-07-21 (Svelte)
- **kristinezheng/kristinezheng.github.io** — 2026-07-01 (HTML)
- **TeglonLabs/jank-crane** — 2026-06-08 (C++, GF3 convergence maps)

### Notable Highlights

- **kubeflow/kubeflow**: 15,798 stars — flagship ML platform for Kubernetes (up from 15,565 in April)
- **kubeflow/pipelines**: 4,171 stars — ML pipelines (up from 4,119)
- **plurigrid/asi**: 56 stars — topological chemputer (up from 16 in April — significant growth!)
- **TeglonLabs/jank-crane**: C++ repo with GF3 convergence maps — directly relevant to this sweep
- **plurigrid/zig-syrup**: pushed 2026-07-28

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count (this run) |
|------|-------|------|-----------------|
| 0 | `#d3869b` | ERGODIC | 128 |
| 1 | `#b8bb26` | PLUS | 128 |
| −1 | `#cc241d` | MINUS | 127 |

**Total world_increments in DB (all runs):** 406  
**Total repo_snapshots in DB (all runs):** 1,327

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.

| World | Address (first 8 chars) | Balance (APT) |
|-------|------------------------|---------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B–Z | (25 more) | 0.0 each |

**Note:** All 28 wallets returned 0 APT. The `0x1::coin::CoinStore<AptosCoin>` resource was not found or has zero balance on mainnet — these wallets may be uninitialized or testnet-only accounts.

### Multisig Contract Probes (5 contracts)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (first 8 chars) | Sigs Required | Healthy |
|------|------------------------|---------------|---------|
| A-B | 0x0da4f4… | 2 | ✅ |
| A-G | 0xf56c4a… | 2 | ✅ |
| Y-Z | 0xd3ffe1… | 2 | ✅ |
| S-T | 0x3b1c3a… | 2 | ✅ |
| V-W | 0x40fad7… | 2 | ✅ |

**All 5 multisig contracts healthy** — each enforces 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

Status: **SPA only — REST/JSON API unavailable from server-side**

The site loads a Next.js SPA. REST probes to `/api/markets`, `/api/v1/markets`, and the backend `https://api.testnet.mnx.fi/markets` returned no JSON. The CSP header reveals the live data endpoint is `wss://api.testnet.mnx.fi` (WebSocket — requires browser/JS client). No market data extractable this run.

---

## DuckDB Counts

| Table | Rows Added (this run) | Total in DB |
|-------|----------------------|-------------|
| world_increments | 383 | 406 |
| repo_snapshots | 383 | 1,327 |
| aptos_snapshots | 28 | 28 |
| multisig_probes | 5 | 5 |
| mnx_snapshots | 1 | 1 |

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS
