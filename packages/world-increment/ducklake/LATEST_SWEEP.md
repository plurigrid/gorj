# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (2026-07-26 sweep)

| Metric | Value |
|--------|-------|
| World Increments (this sweep) | 10 |
| Repo Snapshots (this sweep) | 202 |
| Repo Snapshots (cumulative) | 1,146 |
| Sources Covered | 2 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Sweep's 10 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 2  | TeglonLabs | org | 1 | `#b8bb26` | **PLUS** |
| 3  | bmorphism | user | -1 | `#cc241d` | **MINUS** |
| 4  | zubyul | user | 0 | `#d3869b` | **ERGODIC** |
| 5  | migalkin | user | 1 | `#b8bb26` | **PLUS** |
| 6  | DJedamski | user | -1 | `#cc241d` | **MINUS** |
| 7  | wasita | user | 0 | `#d3869b` | **ERGODIC** |
| 8  | kristinezheng | user | 1 | `#b8bb26` | **PLUS** |
| 9  | M1shaaa | user | -1 | `#cc241d` | **MINUS** |
| 10 | AustinCStone | user | 0 | `#d3869b` | **ERGODIC** |

---

## Top Repos by Source (this sweep)

### plurigrid (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| ontology | JavaScript | 8 | 2025-05-27 |
| vcg-auction | Rust | 7 | 2023-03-16 |
| agent | Python | 5 | 2023-03-31 |
| StochFlow | Python | 4 | 2024-03-20 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| topoi | Python | 0 | 2025-01-24 |
| jank-crane | C++ | 0 | 2026-06-08 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |

### bmorphism (50 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| risc0-cosmwasm-example | Rust | 23 | 2022-10-20 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| say-mcp-server | JavaScript | 20 | 2025-01-07 |
| babashka-mcp-server | JavaScript | 19 | 2025-01-05 |

### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 24 |

### AustinCStone (8 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 50 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| AustinCStone | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| wasita | user | 5 |
| kristinezheng | user | 5 |
| M1shaaa | user | 5 |
| **TOTAL** | | **202** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-26)
All 28 addresses queried. **All returned 0 APT** — zero-balance accounts on mainnet.

| Address Label | Balance (APT) |
|--------------|---------------|
| alice, bob | 0 APT |
| A–Z (26 addresses) | 0 APT each |
| **Total swarm APT** | **0 APT** |

### Multisig Contract Health (2026-07-26)
All 5 contracts healthy with threshold = 2.

| Pair | Sigs Required | Status |
|------|---------------|--------|
| A-B (0x0da4f428...) | 2 | ✅ HEALTHY |
| A-G (0xf56c4a1c...) | 2 | ✅ HEALTHY |
| Y-Z (0xd3ffe181...) | 2 | ✅ HEALTHY |
| S-T (0x3b1c3ae9...) | 2 | ✅ HEALTHY |
| V-W (0x40fad7b4...) | 2 | ✅ HEALTHY |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — Next.js SPA returns HTML shell on all API paths (`/api/markets`, `/api/v1/markets`). No accessible REST endpoint found. Recorded as placeholder in `mnx_snapshots`.

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

## Notable Highlights (2026-07-26)
- **plurigrid/asi**: 31⭐ (up from 16⭐ in April) — topological chemputer, pushed 2026-07-10
- **TeglonLabs/jank-crane** (C++): "GF3 convergence maps" — this org references GF(3) directly
- **bmorphism/ocaml-mcp-sdk**: 61⭐ — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **migalkin/NodePiece**: 144⭐ — scalable KG embeddings, up 1 star since April
- **wasita/wasita.github.io**: pushed 2026-07-21 — most recently active social graph node
- **All 5 Aptos multisig contracts**: 2-of-N threshold, all healthy
- **Hamming swarm**: 28 addresses × 0 APT = no capital at risk on mainnet
