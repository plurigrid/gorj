# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 49 |
| Total Repo Snapshots | 49 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — Sample Increments
| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | gorj | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid | ontology | 0 | `#d3869b` | **ERGODIC** |
| 10 | kubeflow | kubeflow | -1 | `#cc241d` | **MINUS** |
| 20 | bmorphism | Gay.jl | -1 | `#cc241d` | **MINUS** |
| 30 | zubyul | voice-observatory | 0 | `#d3869b` | **ERGODIC** |
| 49 | M1shaaa | lab-bookshelf- | -1 | `#cc241d` | **MINUS** |

GF(3) rule: `id%3==0→ERGODIC #d3869b · id%3==1→PLUS #b8bb26 · id%3==2→MINUS #cc241d`

### Top Repos by Source (2026-07-27 snapshot)

#### plurigrid (103 total, 10 snapshotted)
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| asi | 51 | HTML | 2026-07-27 |
| gorj | 1 | Clojure | 2026-07-07 |
| ontology | 8 | JavaScript | 2026-05-09 |
| nash-portal | 2 | Rust | 2026-05-19 |
| zig-syrup | 2 | Zig | 2026-04-30 |

#### kubeflow (49 total, 10 snapshotted)
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow | 15,792 | — | 2026-07-27 |
| pipelines | 4,171 | Python | 2026-07-27 |
| spark-operator | 3,142 | Python | 2026-07-26 |
| trainer | 2,155 | Go | 2026-07-27 |
| katib | 1,692 | Python | 2026-07-20 |

#### TeglonLabs (5 total, all snapshotted)
| Repo | Stars | Language |
|------|-------|----------|
| mathpix-gem | 2 | Ruby |
| jank-crane | 0 | C++ |
| coin-flip-mcp | 0 | JavaScript |

#### bmorphism (106 total, 8 snapshotted)
| Repo | Stars | Language |
|------|-------|----------|
| ocaml-mcp-sdk | 61 | OCaml |
| anti-bullshit-mcp-server | 22 | JavaScript |
| shitcoin | 5 | Python |
| Gay.jl | 2 | Julia |

#### Zubyul social graph (migalkin/wasita/AustinCStone/DJedamski/kristinezheng/M1shaaa)
| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| migalkin/kgcourse2021 | 24 | HTML |

### Notable Activity (today, 2026-07-27)
- **plurigrid/asi** pushed today (51★, "everything is topological chemputer!")
- **kubeflow/pipelines** active today (4,171★, 465 open issues)
- **kubeflow/dashboard** pushed today
- **bmorphism/Gay.jl** most recent 2026-07-21 (188 open issues — GF3 color library very active)
- **wasita/wasita.github.io** pushed 2026-07-21

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Aptos mainnet status:** Reachable — ledger version **6,476,946,756**, epoch **16,689**, block height **929,194,982**

**Result:** All 28 addresses returned `resource_not_found` for `CoinStore<AptosCoin>`.  
All wallets are **uninitialized** (no CoinStore registered). Balance: `0.0 APT` for all.

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793... | 0.0 APT (uninitialized) |
| bob | 0x0a3c... | 0.0 APT (uninitialized) |
| A–Z (26) | 0x8699… 0x7af0… | 0.0 APT (uninitialized) |

### Multisig Contract Probes — ALL HEALTHY

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ healthy |
| A-G | 0xf56c4a... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✓ healthy |
| S-T | 0x3b1c3a... | 2 | ✓ healthy |
| V-W | 0x40fad7... | 2 | ✓ healthy |

All 5 multisig accounts respond correctly: **2-of-2** threshold, no degradation detected.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` → Next.js SPA (client-side rendered). No public REST `/api/markets` endpoint returned structured data. `mnx_snapshots` table: 0 rows.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 49 |
| repo_snapshots | 49 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA only) |

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
