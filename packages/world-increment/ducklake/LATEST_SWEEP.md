# World-Increment Sweep — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 67 |
| Total Repo Snapshots (cumulative) | 988 |
| New Increments This Sweep | 44 |
| New Repos This Sweep | 44 |
| Sources Covered This Sweep | plurigrid, bmorphism, zubyul, TeglonLabs, migalkin |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Sweep (44 new increments, IDs 1–44)

First and last few entries:

| ID | Source | Repo | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | plurigrid/asi | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | plurigrid/gorj | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid | plurigrid/shrimp | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid | plurigrid/place | +1 | `#b8bb26` | **PLUS** |
| … | … | … | … | … | … |
| 18 | bmorphism | bmorphism/Gay.jl | 0 | `#d3869b` | **ERGODIC** |
| 19 | bmorphism | bmorphism/ocaml-mcp-sdk | +1 | `#b8bb26` | **PLUS** |
| … | … | … | … | … | … |
| 42 | migalkin | migalkin/NBFNet_mlx | 0 | `#d3869b` | **ERGODIC** |
| 43 | migalkin | migalkin/RWL | +1 | `#b8bb26` | **PLUS** |
| 44 | migalkin | migalkin/rambo | -1 | `#cc241d` | **MINUS** |

---

## Top Repos by Source (this sweep)

### plurigrid (17 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 30 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| gorj | Clojure | 1 | 2026-07-11 (1114 open issues) |

### bmorphism (12 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 23 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| Gay.jl | Julia | 2 | 2026-07-11 (187 open issues) |

### migalkin (6 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

---

## Job 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Ledger version at probe:** 6,222,929,710 · Epoch: 16,492 · Block height: 890,744,240

### Wallet Balances — All 28 addresses: 0.0 APT

All wallets exist on-chain but `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource not initialized.

### Multisig Probes — All 5 healthy (2-of-2)

| Pair | Address | Sigs Required |
|------|---------|---------------|
| A-B | 0x0da4f428... | 2 |
| A-G | 0xf56c4a1c... | 2 |
| Y-Z | 0xd3ffe181... | 2 |
| S-T | 0x3b1c3ae9... | 2 |
| V-W | 0x40fad7b4... | 2 |

### MNX Markets

`https://testnet.mnx.fi` — Vercel deployment protection active (visitor password required). Data unavailable this sweep.

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

## Notable Highlights (2026-07-11)
- **plurigrid/gorj** pushed 04:14 UTC today — most recently active, 1114 open issues
- **bmorphism/Gay.jl** pushed 00:28 UTC today — 187 open issues, 2 stars
- **migalkin/NodePiece**: 144 stars (ICLR'22) — top starred repo in this sweep
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP (Jane Street oxcaml_effect)
- **All 5 multisig contracts** probed as 2-of-2: A-B, A-G, Y-Z, S-T, V-W — all healthy
- **All 28 Hamming swarm wallets** at 0.0 APT (CoinStore uninitialized)
