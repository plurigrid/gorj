# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-14  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 101 (100 fetched) |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 104 (100 fetched) |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 11 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 40 |

### Notable repos by stars
| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,720 | 2,673 |
| kubeflow/pipelines | Python | 4,153 | 2,007 |
| kubeflow/spark-operator | Python | 3,128 | 1,490 |
| kubeflow/trainer | Go | 2,114 | 969 |
| kubeflow/katib | Python | 1,683 | 527 |
| kubeflow/examples | Jsonnet | 1,461 | 756 |
| migalkin/NodePiece | Python | 144 | 21 |
| migalkin/StarE | Python | 89 | 16 |
| plurigrid/asi | HTML | 26 | 8 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 |

### Recently active (plurigrid ecosystem)
- `plurigrid/gorj` — 563 open issues, last pushed 2026-06-14 (this repo)
- `plurigrid/eirobri` — 29 open issues, Clojure, pushed 2026-06-03
- `plurigrid/asi` — 26 stars, HTML, pushed 2026-06-10
- `bmorphism/Gay.jl` — Julia, 189 open issues, pushed 2026-06-14
- `TeglonLabs/jank-crane` — C++, pushed 2026-06-08 (GF3 convergence maps)
- `kubeflow/website` — HTML, pushed 2026-06-13

### DuckDB ducklake state
```
world_increments:  90 rows (cumulative)
repo_snapshots:  1011 rows (cumulative, includes prior sweep)
aptos_snapshots:   28 rows (this sweep)
multisig_probes:    5 rows (this sweep)
mnx_snapshots:      0 rows (auth required)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A-Z) returned **null** for the
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource. Accounts either
do not exist on-chain or have not initialized an APT coin store.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793acd... | null |
| bob | 0x0a3c00c... | null |
| A | 0x8699edc... | null |
| B | 0x3f892eb... | null |
| C | 0x38b99e6... | null |
| D | 0xf776562... | null |
| E | 0xdc1d9d5... | null |
| F | 0x18a14b5... | null |
| G | 0x69a394c... | null |
| H | 0xce67c32... | null |
| I | 0x070fe5d... | null |
| J | 0x4d964db... | null |
| K | 0xa732040... | null |
| L | 0x7c2eaea... | null |
| M | 0x6fed37a... | null |
| N | 0xe7dde6d... | null |
| O | 0x73252b6... | null |
| P | 0x6218792... | null |
| Q | 0xac40fa5... | null |
| R | 0x7ce605c... | null |
| S | 0xb875301... | null |
| T | 0x35781dc... | null |
| U | 0x75860da... | null |
| V | 0xb59dd81... | null |
| W | 0x5f32aef... | null |
| X | 0xa95cbbd... | null |
| Y | 0xd8e3284... | null |
| Z | 0x7af0ef6... | null |

### Multisig Contract Probes

All 5 multisig contracts responded healthy with **2 signatures required**:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

All API paths return **401 Authentication Required**. The testnet SPA requires
authenticated access — no public market data retrievable. `mnx_snapshots` table
is empty this sweep.

---

## GF(3) World Increment Distribution (this sweep)

| GF(3) | Color | Hex | Increments |
|-------|-------|-----|------------|
| +1 (PLUS) | green | #b8bb26 | 31 |
| -1 (MINUS) | red | #cc241d | 30 |
| 0 (ERGODIC) | pink | #d3869b | 29 |

Total world increments this sweep: **90**

---

## Summary

- **GitHub sweep:** 356+ repos indexed across 11 org/user sources
  - kubeflow/kubeflow leads at 15,720 stars; very active (pushed 2026-06-11)
  - plurigrid/gorj most active in ecosystem: 563 open issues, pushed today
  - bmorphism/Gay.jl most issue-active: 189 open issues
  - New: TeglonLabs/jank-crane (GF3 convergence maps, C++, 2026-06-08)
- **Aptos Hamming swarm:** 28/28 addresses have no APT CoinStore resource
- **Multisig health:** 5/5 contracts healthy, all require 2-of-N threshold (n=2)
- **MNX:** testnet.mnx.fi requires authentication; market data unavailable

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
