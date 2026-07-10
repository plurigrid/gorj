# World-Increment Sweep + Hamming Snapshot — 2026-07-10

## Sweep Metadata
- **Date:** 2026-07-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 389 |
| New Repo Snapshots This Run | 378 |
| Sources Covered | 3 orgs + 8 users (11 total) |
| Total Stars Indexed | 68,883 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (401) |

---

## GF(3) Color Chain Distribution

| GF3 Name | Color | Trit | Count (this run) |
|----------|-------|------|-----------------|
| PLUS | #b8bb26 | +1 | 130 |
| MINUS | #cc241d | -1 | 130 |
| ERGODIC | #d3869b | 0 | 129 |

GF(3) rule: `id%3==1 → PLUS (+1) · id%3==2 → MINUS (−1) · id%3==0 → ERGODIC (0)`

---

## JOB 1: GitHub Social Graph

### Repo Counts by Source

| Source | Type | Repos This Run | Total Stars |
|--------|------|----------------|-------------|
| plurigrid | org | 100 (103 total) | 80 |
| kubeflow | org | 49 | 67,723 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 (105 total) | 262 |
| zubyul | user | 49 | 26 |
| migalkin | user (social) | 19 | 554 |
| DJedamski | user (social) | 11 | 14 |
| wasita | user (social) | 11 | 6 |
| kristinezheng | user (social) | 5 | 0 |
| M1shaaa | user (social) | 16 | 0 |
| AustinCStone | user (social) | 40 | 216 |
| **TOTAL** | | **378** | **68,883** |

### Notable Repos
- **kubeflow/kubeflow** — 15,565+ stars, ML platform (pushed 2026-01-05)
- **kubeflow/pipelines** — 4,119 stars, Python ML pipelines (pushed 2026-04-10)
- **TeglonLabs/jank-crane** — newest push **2026-06-08**, GF3 convergence maps, C++
- **migalkin/NodePiece** — 143 stars, scalable KG embeddings
- **bmorphism/ocaml-mcp-sdk** — 60 stars, OCaml MCP SDK
- **wasita/wasita.github.io** — pushed **2026-07-06**, Svelte personal site (most recent social push)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01, HTML

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallet addresses (alice, bob, A–Z) probed on mainnet.
- **Account existence:** Confirmed — all accounts have non-zero sequence numbers (e.g. alice: seq=72, A: seq=58, Z: seq=2)
- **CoinStore status:** `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` not initialized on any address — returned HTTP 404 on resource endpoint
- **APT balance:** 0.0 for all (CoinStore uninitialized; accounts active but no native APT)

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 (no CoinStore) |
| bob | 0x0a3c...512d | 0.0 (no CoinStore) |
| A–Z | (26 addresses) | 0.0 (no CoinStore) |

### Multisig Contract Probes

All 5 multisig accounts are **healthy** (2-of-2 threshold):

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — HTTP 401 Unauthorized on all endpoints:
- `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/` — all 401
- Testnet requires authentication; no public market data accessible

---

## Schema (DuckDB)
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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=−1, color=#cc241d, name=MINUS
