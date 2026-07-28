# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 1004 |
| Total Repo Snapshots | 1004 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| +1 | PLUS | #b8bb26 | 335 |
| -1 | MINUS | #cc241d | 335 |
| 0 | ERGODIC | #d3869b | 334 |

### Top Repos by Source (2026-07-28 snapshot)

#### plurigrid (103 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| zig-syrup | Zig | 2 | 2026-07-28 |
| asi | HTML | 52 | 2026-07-27 |
| gorj | Clojure | 1 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| Plurigraph | JavaScript | 3 | 2026-05-12 |

#### kubeflow (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,794 | 2026-07-28 |
| pipelines | Python | 4,171 | 2026-07-28 |
| spark-operator | Python | 3,142 | 2026-07-26 |
| trainer | Go | 2,157 | 2026-07-28 |
| katib | Python | 1,693 | 2026-07-28 |

#### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |

#### bmorphism (106 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| Gay.jl | Julia | 2 | 2026-07-21 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

#### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| gay-world | Python | 1 | 2026-04-05 |
| tilelang-kernels | Python | 0 | 2026-03-16 |

#### migalkin (19 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |

#### AustinCStone (41 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets, via `0x1::coin::balance` view function)

**Total APT across swarm: 20.3448 APT**

| World | Balance (APT) | Rank |
|-------|--------------|------|
| bob | 12.6570 | 1 |
| F | 1.9605 | 2 |
| L | 1.9273 | 3 |
| J | 1.8951 | 4 |
| alice | 0.4364 | 5 |
| O | 0.2101 | 6 |
| K | 0.1620 | 7 |
| P | 0.1401 | 8 |
| M | 0.1123 | 9 |
| N | 0.1061 | 10 |
| Q | 0.1032 | 11 |
| S | 0.0918 | 12 |
| R | 0.0902 | 13 |
| T | 0.0737 | 14 |
| A | 0.0518 | 15 |
| U | 0.0558 | 16 |
| B | 0.0363 | 17 |
| V | 0.0488 | 18 |
| Y | 0.0444 | 19 |
| X | 0.0426 | 20 |
| W | 0.0407 | 21 |
| C | 0.0102 | 22 |
| D | 0.0116 | 23 |
| E | 0.0094 | 24 |
| Z | 0.0243 | 25 |
| H | 0.0017 | 26 |
| G | 0.0007 | 27 |
| I | 0.0007 | 28 |

**bob holds 62.2% of total swarm APT. F, L, J together hold another 28.2%.**

### Multisig Contract Probes

All 5 contracts **healthy** — each requires exactly **2-of-N signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — SPA, no public JSON API.**  
`testnet.mnx.fi` serves a Next.js SPA that loads market data client-side. Neither `/api/markets` nor `/api/v1/markets` return JSON. No rows inserted to `mnx_snapshots`.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,794 stars — flagship ML platform for Kubernetes (active 2026-07-28)
- **plurigrid/gorj**: 1,469 open issues — most active ticket tracker in the social graph
- **bmorphism/Gay.jl**: 188 open issues — color sampling library under heavy development
- **bmorphism/anti-bullshit-mcp-server**: 22 stars — epistemological MCP tool
- **migalkin/NodePiece**: 144 stars — ICLR'22 KG embedding, still receiving activity
- **AustinCStone/TextGAN**: 92 stars — TF text generation still popular
- **bob wallet**: 12.66 APT — dominant Hamming swarm holder (62.2% of total)
- **All multisig contracts**: 2-of-N, all healthy at time of sweep
