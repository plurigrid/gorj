# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| New World Increments (this run) | 53 |
| Total World Increments (cumulative) | 76 |
| Total Repo Snapshots (cumulative) | 997 |
| Sources Covered (this run) | 3 orgs + 4 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain (this run — 53 increments)

| GF3 Name | GF3 Color | Trit | Count |
|----------|-----------|------|-------|
| ERGODIC | `#d3869b` | 0 | 24 |
| PLUS | `#b8bb26` | +1 | 26 |
| MINUS | `#cc241d` | -1 | 26 |

GF(3) assignment: `id mod 3 == 0 → ERGODIC, id mod 3 == 1 → PLUS, id mod 3 == 2 → MINUS`

---

## Top Repos by Source (this run)

### plurigrid (13 repos, org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-08-04 |
| eirobri | Clojure | 0 | 2026-08-04 |
| place | TeX | 1 | 2026-08-02 |
| asi | HTML | 58 | 2026-07-10 |
| zig-syrup | Zig | 2 | 2026-07-28 |

### kubeflow (13 repos, org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15805 | 2026-07-10 |
| pipelines | Python | 4175 | 2026-08-04 |
| spark-operator | Python | 3143 | 2026-08-03 |
| trainer | Go | 2167 | 2026-08-04 |
| katib | Python | 1694 | 2026-08-04 |
| kale | Python | 699 | 2026-08-04 |

### TeglonLabs (5 repos, org)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (12 repos, user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-08-04 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| shitcoin | Python | 5 | 2026-04-08 |
| open-location-code-zig | Zig | 3 | 2025-12-30 |

### zubyul (10 repos, user)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| Gay.jl | Julia | 0 | 2026-03-28 |
| kinesis-kb360pro | Python | 0 | 2026-03-26 |

### migalkin (10 repos, social graph)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |
| RWL | Python | 8 | 2026-05-28 |

### AustinCStone (5 repos, social graph)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| byteruckus | HTML | 0 | 2026-07-15 |
| EpsteinSearch | Python | 0 | 2026-02-11 |
| bmforkupdate | Python | 0 | 2025-05-09 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-08-04)

**Total addresses probed:** 28 (alice, bob, A–Z)  
**All balances:** 0.000000 APT  
**Reason:** No `0x1::coin::CoinStore<AptosCoin>` resource initialized on mainnet for any address.

All wallets in the Hamming swarm show zero APT on Aptos mainnet — these appear to be testnet or uninitialized accounts.

### Multisig Contract Probes (Mainnet)

All 5 multisig contracts **healthy** — all require 2-of-N signatures:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...c0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...eb6d` | 2 | ✓ healthy |

**Consistent 2-of-N multisig threshold across all probed pairs.**

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable via server-side fetch  
**Reason:** `testnet.mnx.fi` is a Next.js SPA (HTTP 200 with JS shell only). No `/api/markets` or `/api/v1/markets` endpoint returned data. Recorded as unavailable in `mnx_snapshots`.

---

## DuckDB Table State

| Table | Rows |
|-------|------|
| world_increments | 76 |
| repo_snapshots | 997 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,805 stars (↑240 vs Apr 2026) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,175 stars (↑56 vs Apr 2026) — pushed 2026-08-04
- **kubeflow/kale**: 699 stars — new capture in this run
- **plurigrid/gorj**: 1625 open issues — this repo — GF(3) trit coloring active
- **plurigrid/asi**: 58 stars (↑42 vs Apr 2026) — topological chemputer growing fast
- **bmorphism/Gay.jl**: 188 open issues — active development
- **TeglonLabs/jank-crane**: C++ crane-jank IR hub with GF3 convergence maps
- **All 5 multisig contracts**: 2-of-N threshold, healthy
- **Hamming swarm wallets**: 28 addresses, all 0 APT on mainnet
