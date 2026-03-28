# World-Increment Sweep + Hamming Swarm Snapshot — 2026-03-28

## Sweep Metadata
- **Date:** 2026-03-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 72 |
| Total Repo Snapshots | 508 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Queried | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (HTML-only) |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | bmorphism | IssuesEvent (gorj) | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism | IssuesEvent (asi) | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | PushEvent (lolita) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | PushEvent (asi) | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | PullRequestEvent (asi) | -1 | `#cc241d` | **MINUS** |
| 6  | bmorphism | PushEvent (gorj) | 0 | `#d3869b` | **ERGODIC** |
| 7  | bmorphism | CreateEvent (gorj) | +1 | `#b8bb26` | **PLUS** |
| 8  | bmorphism | WatchEvent (au-ts/sddf) | -1 | `#cc241d` | **MINUS** |
| 9  | bmorphism | PushEvent (asi) | 0 | `#d3869b` | **ERGODIC** |
| 10 | bmorphism | PullRequestEvent (asi) | +1 | `#b8bb26` | **PLUS** |
| 11 | bmorphism | CreateEvent (gtc2026-floxxy) | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism | PushEvent (zig-syrup) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (12 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi-skills | Julia | 1 | 2026-03-28 |
| zig-syrup | Zig | 1 | 2026-03-28 |
| asi | HTML | 13 | 2026-03-28 |
| gorj | Clojure | 0 | 2026-03-28 |
| lolita | Python | 0 | 2026-03-28 |

### kubeflow (9 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4112 | 2026-03-28 |
| mcp-apache-spark-history-server | Python | 144 | 2026-03-28 |
| spark-operator | Python | 3110 | 2026-03-27 |
| trainer | Go | 2068 | 2026-03-26 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| Stahl | Rust | 0 |

### bmorphism (6 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| shitcoin | HTML | 5 |
| flox-mcp-bb | Clojure | 0 |

---

## Event Summary (bmorphism + zubyul — 60 events captured)

| Event Type | Count |
|------------|-------|
| PushEvent | 34 |
| PullRequestEvent | 16 |
| CreateEvent | 10 |
| IssueCommentEvent | 5 |
| IssuesEvent | 4 |
| WatchEvent | 2 |
| ForkEvent | 1 |

---

## Repo Counts by Source (Full Sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 46 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 28 |
| zubyul | user | 23 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **468** |

---

## Aptos Wallet Balances (28 wallets)

All wallets queried via `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

All 28 addresses returned **0.0 APT** — CoinStore resource not found on any address. Accounts either have no native APT holding or do not exist on mainnet.

| Label | Balance (APT) |
|-------|---------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 wallets) | 0.0 each |

---

## Multisig Contract Probes

All 5 contracts probed via `POST https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f4...4987003 | 2 | YES |
| A-G | 0xf56c4a...fbc0096 | 2 | YES |
| Y-Z | 0xd3ffe1...e75b883 | 2 | YES |
| S-T | 0x3b1c3a...ded7883 | 2 | YES |
| V-W | 0x40fad7...c80eb6d | 2 | YES |

All contracts healthy — 2-of-N multisig, responding correctly.

---

## MNX Markets

**Status: UNAVAILABLE**

`https://testnet.mnx.fi/api/markets`, `/api/v1/markets`, and `/` all return HTML (Next.js SPA). No JSON market data API publicly accessible.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,537 stars — umbrella platform repo
- **kubeflow/pipelines**: 4,112 stars — ML pipeline for Kubernetes (pushed 2026-03-28)
- **kubeflow/spark-operator**: 3,110 stars — Kubernetes operator for Apache Spark
- **kubeflow/trainer**: 2,068 stars — distributed training
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **plurigrid/asi**: 13 stars — topological chemputer (pushed 2026-03-28)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Multisig status**: All 5 contracts (A-B, A-G, Y-Z, S-T, V-W) healthy with 2 sigs required
- **Aptos wallets**: All 28 wallets show 0 APT balance on mainnet
- **MNX testnet**: Frontend-only, no API data available
