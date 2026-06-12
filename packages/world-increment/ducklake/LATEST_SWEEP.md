# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-12

## Sweep Metadata
- **Date:** 2026-06-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos Mainnet:** epoch 16,144 · block 825,737,317 · ledger 5,693,971,996

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 71 |
| Repo Snapshots (this sweep) | 71 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain (first 12 new increments)

| ID | Repo | GF3 Trit | Color | Name |
|----|------|-----------|-------|------|
| 1  | plurigrid/asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid/place | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid/eirobri | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid/nash-portal | +1 | `#b8bb26` | **PLUS** |
| 5  | plurigrid/gorj | -1 | `#cc241d` | **MINUS** |
| 6  | plurigrid/zig-syrup | 0 | `#d3869b` | **ERGODIC** |
| 7  | plurigrid/asi-skills | +1 | `#b8bb26` | **PLUS** |
| 8  | plurigrid/nanoclj-zig | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid/ontology | 0 | `#d3869b` | **ERGODIC** |
| 10 | plurigrid/Plurigraph | +1 | `#b8bb26` | **PLUS** |
| 11 | plurigrid/StochFlow | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid/microworlds | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...`

### Top Repos by Stars (2026-06-12 snapshot)
| Repo | Language | Stars | Last Pushed |
|------|----------|-------|-------------|
| kubeflow/kubeflow | — | 15,714 | 2026-06-11 |
| kubeflow/pipelines | Python | 4,152 | 2026-06-11 |
| kubeflow/spark-operator | Python | 3,127 | 2026-06-09 |
| kubeflow/trainer | Go | 2,111 | 2026-06-12 |
| kubeflow/katib | Python | 1,683 | 2026-06-05 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2026-03-19 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| plurigrid/asi | HTML | 25 | 2026-06-10 |

### Most Active (≤7 days)
- `plurigrid/gorj` — 517 open issues, pushed 2026-06-12 (this repo)
- `kubeflow/sdk` — pushed 2026-06-12
- `kubeflow/trainer` — pushed 2026-06-12
- `kubeflow/community` + `website` — pushed 2026-06-12
- `bmorphism/satreadout` (Lean) — pushed 2026-06-10
- `bmorphism/Gay.jl` (Julia, 189 open issues) — pushed 2026-06-10
- `plurigrid/asi` — pushed 2026-06-10
- `TeglonLabs/jank-crane` (C++) — pushed 2026-06-08

### Repo Counts by Source
| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 101 |
| bmorphism | user | 104 |
| TeglonLabs | org | 5 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| zubyul | user | 49 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

**Status:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
These Hamming-swarm accounts have not been initialized with legacy APT CoinStore on mainnet.
Balance recorded as 0.0 APT for all entries. Accounts may exist with FA (fungible asset) balances.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793acd...4cc7b | 0.0 |
| bob | 0x0a3c00c...512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...7003 | **2** | ✓ |
| A-G | 0xf56c4a1c...0096 | **2** | ✓ |
| Y-Z | 0xd3ffe181...b883 | **2** | ✓ |
| S-T | 0x3b1c3ae9...7883 | **2** | ✓ |
| V-W | 0x40fad7b4...eb6d | **2** | ✓ |

All 5 multisig accounts healthy — 2-of-N threshold on Aptos mainnet.

### MNX Markets
**Status:** `testnet.mnx.fi` unreachable — API unavailable, `mnx_snapshots` empty.

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
