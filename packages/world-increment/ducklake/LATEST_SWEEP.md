# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-09

## Sweep Metadata
- **Date:** 2026-06-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Ledger:** 5,648,774,455 (epoch 16111, block 819,603,196)

---

## JOB 1: GitHub Social Graph Sweep

### Coverage — 2026-06-09
| Source | Type | Repos Snapshotted |
|---|---|---|
| plurigrid | org | 21 |
| kubeflow | org | 15 |
| TeglonLabs | org | 5 |
| bmorphism | user | 15 |
| zubyul | user | 10 |
| migalkin | social (zubyul graph) | 5 |
| wasita | social (zubyul graph) | 5 |
| AustinCStone | social (zubyul graph) | 4 |
| DJedamski | social (zubyul graph) | 3 |
| kristinezheng | social (zubyul graph) | 2 |
| M1shaaa | social (zubyul graph) | 2 |
| **Total** | | **87** |

### GF(3) Color Chain Distribution (this sweep)
| GF3 Color | Name | Trit | Count |
|---|---|---|---|
| #b8bb26 | PLUS | +1 | 37 |
| #cc241d | MINUS | -1 | 37 |
| #d3869b | ERGODIC | 0 | 36 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (87 increments)

### Notable Repos by Stars (2026-06-09 snapshot)
| Repo | Stars | Language | Last Push |
|---|---|---|---|
| kubeflow/kubeflow | 15,712 | — | 2026-05-24 |
| kubeflow/pipelines | 4,153 | Python | 2026-06-09 |
| kubeflow/spark-operator | 3,126 | Python | 2026-06-08 |
| kubeflow/trainer | 2,112 | Go | 2026-06-09 |
| kubeflow/katib | 1,685 | Python | 2026-06-05 |
| kubeflow/examples | 1,462 | Jsonnet | 2025-04-14 |
| kubeflow/manifests | 1,022 | YAML | 2026-06-09 |
| kubeflow/arena | 812 | Go | 2026-05-07 |
| kubeflow/mpi-operator | 528 | Go | 2026-06-02 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### TeglonLabs Org (5 repos)
| Repo | Language | Stars | Last Push |
|---|---|---|---|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### plurigrid Hot Repos
| Repo | Stars | Language | Last Push |
|---|---|---|---|
| gorj | 0 | Clojure | 2026-06-09 (458 open issues) |
| eirobri | 0 | Clojure | 2026-06-03 (29 open issues) |
| asi | 25 | HTML | 2026-04-26 |
| nanoclj-zig | 1 | Zig | 2026-04-25 |
| asi-skills | 3 | Julia | 2026-04-26 |

### bmorphism Hot Repos
| Repo | Stars | Language | Last Push |
|---|---|---|---|
| Gay.jl | 1 | Julia | 2026-06-09 (189 open issues) |
| world | 0 | Python | 2026-06-02 |
| oxgame | 0 | OCaml | 2026-05-15 |
| ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)
**Query method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

All 28 Hamming-swarm wallets returned **404 resource_not_found**. Wallets have zero APT balance in the standard coin resource (unfunded or holding assets in non-standard resource slots).

| World | Address (first 10 chars) | Balance (APT) |
|---|---|---|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A–Z (26 wallets) | 0x8699edc...→0x7af0ef6... | 0.0 (all) |

### Multisig Contract Probes (5 contracts)
**Method:** `POST /v1/view` with `0x1::multisig_account::num_signatures_required`

All 5 multisig contracts are **healthy** with 2-of-N threshold.

| Pair | Address (truncated) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428...003 | 2 | ✓ |
| A-G | 0xf56c4a1c...096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...883 | 2 | ✓ |
| V-W | 0x40fad7b4...b6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `https://testnet.mnx.fi` is protected by Vercel Authentication (HTTP 401). Both `/api/markets` and `/api/v1/markets` redirect to a password-protected auth wall. A Vercel bypass token or authenticated session is required.

---

## DuckDB Ducklake State (cumulative)

| Table | Total Rows | Notes |
|---|---|---|
| world_increments | 110 | 87 new this sweep |
| repo_snapshots | 1,031 | 87 new this sweep |
| aptos_snapshots | 28 | 28 new this sweep |
| multisig_probes | 5 | 5 new this sweep |
| mnx_snapshots | 1 | unavailable marker |

Database is append-only; earlier sweeps (from 2026-04-10) preserved.

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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
