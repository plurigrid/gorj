# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-15

## Sweep Metadata
- **Date:** 2026-06-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (new) | 33 (cumulative, incl. prior runs) |
| Total Repo Snapshots (new) | 380 unique repos this sweep |
| Sources Covered (new) | 3 orgs + 8 users (+ 11-source social graph) |
| Aptos Wallets Probed | 28 (alice/bob + A–Z) |
| Multisig Contracts Probed | 5 (all healthy, 2-of-2) |
| MNX Markets | UNAVAILABLE (Vercel auth required) |

---

## GF(3) Color Chain — This Sweep (10 new increments)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| +1 | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| +2 | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| +3 | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| +4 | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| +5 | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| +6 | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| +7 | AustinCStone (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| +8 | DJedamski (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| +9 | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| +10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Top Repos by Source (2026-06-15 Sweep)

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565+ | 2026-01-05 |
| pipelines | Python | 4119+ | 2026-04-10 |
| spark-operator | Python | 3111+ | 2026-04-10 |
| trainer | Go | 2080+ | 2026-04-10 |

### TeglonLabs (5 repos this sweep)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 (newest!) |
| mathpix-gem | Ruby | 2 | 2026-01-01 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143+ |
| StarE | Python | 88+ |

### AustinCStone (40 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92+ |
| StereoVisionMRF | Python | 11+ |

### Zubyul Social Graph
| User | Repos | Most Recent Push |
|------|-------|-----------------|
| wasita | 11 | 2026-06-15 (wasita.github.io — today!) |
| M1shaaa | 8 | 2026-06-15 (M1shaaa profile — today!) |
| kristinezheng | 5 | 2026-06-07 |
| DJedamski | 6 | 2018-03-07 |

---

## Repo Counts by Source (2026-06-15)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | zubyul social | 11 |
| M1shaaa | zubyul social | 8 |
| DJedamski | zubyul social | 6 |
| kristinezheng | zubyul social | 5 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All queried addresses use the **Aptos Fungible Asset (FA) standard** or are smart contract accounts. The legacy `0x1::coin::CoinStore<AptosCoin>` resource is absent. Accounts confirmed on-chain (alice seq=72, has lending_pool::UserPosition resource). Balance shown NULL pending FA-compatible query.

| Range | Status |
|-------|--------|
| alice, bob | NULL — contract/FA accounts |
| A – Z (26) | NULL — contract/FA accounts |

### Multisig Probes — ALL HEALTHY ✅

| Pair | Address | Sigs Required |
|------|---------|---------------|
| A-B | 0x0da4f4...7003 | **2** |
| A-G | 0xf56c4a...0096 | **2** |
| Y-Z | 0xd3ffe1...b883 | **2** |
| S-T | 0x3b1c3a...7883 | **2** |
| V-W | 0x40fad7...eb6d | **2** |

**5/5 multisig contracts healthy — 2-of-2 threshold confirmed on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — All endpoints gated by Vercel deployment auth. No market data accessible.

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

## Notable Highlights (2026-06-15)
- **wasita/wasita.github.io** & **M1shaaa/M1shaaa**: pushed **today** (2026-06-15) — social graph live
- **TeglonLabs/jank-crane**: newest repo (2026-06-08) — crane-jank IR hub with GF(3) convergence maps
- **bmorphism/ocaml-mcp-sdk**: 61 stars (↑1 from Apr sweep) — OCaml MCP SDK growing
- **plurigrid/asi**: 26 stars (↑10 from Apr) — significant growth since last sweep
- **plurigrid/nanoclj-zig**: Zig Clojure interpreter with GF(3) trit conservation (our own orbit)
- **kubeflow/kubeflow**: 15,565+ stars — flagship ML platform for Kubernetes
- **migalkin/NodePiece**: 143+ stars — scalable KG embeddings
- **All 5 Hamming multisigs**: 2-of-2 healthy on Aptos mainnet
- **MNX testnet**: Vercel-gated, inaccessible without credentials
