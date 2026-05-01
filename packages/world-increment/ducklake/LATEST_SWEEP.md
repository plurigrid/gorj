# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-01

## Sweep Metadata
- **Date:** 2026-05-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 536 |
| Total Repo Snapshots | 476 |
| Sources Covered | 3 orgs + 8 users |
| Events Captured | 60 (bmorphism + zubyul) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 |

---

## GF(3) Color Chain Distribution

GF(3) trit coloring applied per `id mod 3` across all 536 increments:

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 178 |
| +1 | PLUS | `#b8bb26` | 179 |
| -1 | MINUS | `#cc241d` | 179 |

---

## GitHub Social Graph — Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user (zubyul-graph) | 43 |
| wasita | user (zubyul-graph) | 31 |
| migalkin | user (zubyul-graph) | 30 |
| zubyul | user | 27 |
| kristinezheng | user (zubyul-graph) | 18 |
| M1shaaa | user (zubyul-graph) | 16 |
| DJedamski | user (zubyul-graph) | 11 |
| **TOTAL** | | **476** |

### Top Repos by Stars

| Repo | Language | Stars | Forks | Open Issues |
|------|----------|-------|-------|-------------|
| kubeflow/kubeflow | — | 15,609 | 2,646 | 0 |
| kubeflow/pipelines | Python | 4,130 | 1,986 | 488 |
| kubeflow/spark-operator | Python | 3,121 | 1,483 | 90 |
| kubeflow/trainer | Go | 2,095 | 947 | 122 |
| kubeflow/katib | Python | 1,681 | 521 | 121 |
| kubeflow/examples | Jsonnet | 1,460 | 757 | 111 |
| kubeflow/manifests | YAML | 1,013 | 1,065 | 29 |
| migalkin/NodePiece | Python | 143 | — | — |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | — | — |
| plurigrid/gorj | Clojure | 0 | 0 | 27 |

### Most Recently Pushed

| Repo | Language | Pushed At |
|------|----------|-----------|
| bmorphism/Gay.jl | Julia | 2026-05-01T00:34:17Z |
| plurigrid/gorj | Clojure | 2026-04-30T22:09:57Z |
| kubeflow/notebooks | — | 2026-04-30T20:03:02Z |
| kubeflow/kale | Python | 2026-04-30T18:03:46Z |
| zubyul/asi | Python | 2026-04-30T15:43:58Z |

### Recent Events (bmorphism + zubyul, 60 total)

| Event Type | Count |
|------------|-------|
| DeleteEvent | 17 |
| PullRequestEvent | 15 |
| CreateEvent | 14 |
| PushEvent | 12 |
| WatchEvent | 1 |
| ForkEvent | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 28 wallets)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1` with 1s sleep between calls.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z (24) | various | 0.0 each |

**Note:** All wallets returned zero balance for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. Accounts may hold other fungible asset types or be unfunded on mainnet.

### Multisig Contract Probes (5 pairs)

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig accounts **healthy** — 2-of-N threshold confirmed on all pairs.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA ("The AI Exchange") requiring wallet connection to render market data. Static HTML fetch returns "Connect Wallet to View Account". No market data extractable without browser/wallet execution context. **Status: unavailable via headless fetch.** `mnx_snapshots` table populated with 0 rows.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| world_increments | 536 |
| repo_snapshots | 476 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA wall) |

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
