# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 157 |
| Total Repo Snapshots | 157 |
| Sources Covered | 3 orgs + 5 users + social graph |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 (A-B, A-G, Y-Z, S-T, V-W) |
| MNX Markets | N/A (SPA, no public API) |

---

## GF(3) Color Chain Rule

- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured | Last Active |
|--------|------|---------------|-------------|
| plurigrid | org | 50 (of 103) | 2026-07-25 (gorj) |
| kubeflow | org | 30 (of 49) | 2026-07-25 (pipelines, trainer) |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| bmorphism | user | 30 (of 106) | 2026-07-25 (Gay.jl) |
| zubyul | user | 30 (of 49) | 2026-07-18 (from-possible-worlds) |
| social graph | mixed | 12 | 2026-07-21 (wasita) |

### Top Repos by Source

#### plurigrid (103 total, 50 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-25 |
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-26 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |

#### kubeflow (49 total, 30 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,793 | 2026-07-10 |
| pipelines | Python | 4,170 | 2026-07-25 |
| spark-operator | Python | 3,143 | 2026-07-25 |
| trainer | Go | 2,153 | 2026-07-25 |
| katib | Python | 1,692 | 2026-07-22 |
| mcp-server | Python | 29 | 2026-07-24 |

#### TeglonLabs (5 total)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

#### bmorphism (106 total, 30 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-07-25 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| shitcoin | Python | 5 | 2026-04-08 |

#### zubyul (49 total, 30 captured)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gay-world | Python | 1 | 2026-03-26 |
| from-possible-worlds | TeX | 0 | 2026-07-18 |
| voice-observatory | Python | 0 | 2026-04-24 |

#### Social Graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
| Repo | Owner | Language | Stars |
|------|-------|----------|-------|
| NodePiece | migalkin | Python | 144 |
| StarE | migalkin | Python | 89 |
| kgcourse2021 | migalkin | HTML | 24 |
| wasita.github.io | wasita | Svelte | 1 |
| byteruckus | AustinCStone | HTML | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm addresses returned `Resource not found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet (ledger version ~6,454,491,993). These accounts have not initialized an APT CoinStore — balances recorded as NULL.

| World | Address | Balance |
|-------|---------|---------|
| alice | 0xc793...4cc7b | NULL |
| bob | 0x0a3c...512d5d | NULL |
| A–Z (26 addrs) | 0x8699...–0x7af0... | NULL (all uninitialized) |

### Multisig Contract Probes

All 5 contracts are live and require **2 signatures** — all healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a deployed Next.js SPA (HTTP 200). No public JSON API endpoints accessible (`/api/markets`, `/api/v1/markets` return HTML). Market data **unavailable** — SPA requires client-side rendering. No rows in `mnx_snapshots`.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,793★ — flagship ML platform for Kubernetes (up from 15,565 in April sweep)
- **plurigrid/gorj**: 1,402 open issues — most active plurigrid repo right now
- **bmorphism/Gay.jl**: 188 open issues, active 2026-07-25
- **migalkin/NodePiece**: 144★ (ICLR'22), **StarE**: 89★ (EMNLP'20)
- **All 5 multisig contracts healthy** (2-of-N, all on Aptos mainnet)
- **28 Hamming swarm wallets**: uninitialized CoinStore — no APT balances on mainnet
