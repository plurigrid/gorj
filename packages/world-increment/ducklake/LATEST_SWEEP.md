# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-14

## Sweep Metadata
- **Date:** 2026-04-14T11:15Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos mainnet ledger:** v4,869,955,367 · epoch 15435 · block 713,904,854

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 151 |
| Total Repo Snapshots (all time) | 1,072 |
| New Repos This Sweep | 128 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Total Swarm APT | ~20.12 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

### Sources Queried
| Source | Type | Repos This Sweep |
|--------|------|-----------------|
| plurigrid | org | 45 (top) |
| kubeflow | org | 20 (top) |
| TeglonLabs | org | 4 |
| bmorphism | user | 20 (top) |
| zubyul | user | 17 |
| migalkin | user (social) | 5 |
| DJedamski | user (social) | 3 |
| wasita | user (social) | 4 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 2 |
| AustinCStone | user (social) | 5 |
| **Total** | | **128** |

### Top Repos by Stars (this sweep)
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,575 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-14 |
| kubeflow/spark-operator | 3,114 | Python | 2026-04-13 |
| kubeflow/trainer | 2,082 | Go | 2026-04-14 |
| kubeflow/katib | 1,678 | Python | 2026-04-14 |
| migalkin/NodePiece | 143 | Python | 2026-03-02 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 88 | Python | 2026-02-22 |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | 2026-03-16 |
| plurigrid/asi | 16 | HTML | 2026-04-13 |

### Hot Recent Pushes (within 24h)
- `plurigrid/gorj` — Clojure, 187 open issues, **2026-04-14T10:19Z**
- `plurigrid/nash-portal` — Rust WASM TUI, **2026-04-14T05:48Z**
- `kubeflow/pipelines` — Python ML pipelines, **2026-04-14T09:47Z**
- `kubeflow/trainer` — Go distributed training, **2026-04-14T07:46Z**
- `kubeflow/dashboard` — TypeScript, **2026-04-14T05:09Z**
- `zubyul/nash-tui` — Rust, **2026-04-13T07:45Z**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-04-14)
*Method: `0x1::coin::balance` view function (FA-compatible)*

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c5… | **12.657007** |
| F | 0x18a14b5b… | 1.960516 |
| L | 0x7c2eaeaf… | 1.927269 |
| J | 0x4d964db8… | 1.895093 |
| alice | 0xc793acde… | 0.436434 |
| O | 0x73252b60… | 0.210136 |
| K | 0xa732040a… | 0.161961 |
| P | 0x62187929… | 0.140136 |
| M | 0x6fed37a7… | 0.112285 |
| N | 0xe7dde6da… | 0.106121 |
| Q | 0xac40fa50… | 0.103240 |
| S | 0xb8753014… | 0.091788 |
| R | 0x7ce605cc… | 0.090217 |
| T | 0x35781dc0… | 0.073713 |
| U | 0x75860da4… | 0.055773 |
| A | 0x8699edc0… | 0.051767 |
| V | 0xb59dd817… | 0.048833 |
| Y | 0xd8e32848… | 0.044449 |
| X | 0xa95cbbd1… | 0.042577 |
| W | 0x5f32aef7… | 0.040705 |
| B | 0x3f892ebe… | 0.036256 |
| Z | 0x7af0ef6e… | 0.024268 |
| D | 0xf7765624… | 0.011629 |
| C | 0x38b99e63… | 0.010185 |
| E | 0xdc1d9d53… | 0.009372 |
| H | 0xce67c327… | 0.001681 |
| G | 0x69a394c0… | 0.000681 |
| I | 0x070fe5d7… | 0.000681 |

**Total swarm APT:** ~20.12 APT

### Multisig Probes
*Function: `0x1::multisig_account::num_signatures_required`*

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

All 5/5 multisig contracts healthy — 2-of-N threshold confirmed.

### MNX Markets (testnet.mnx.fi)
**Status: SPA — wallet connection required.** `testnet.mnx.fi` serves a Next.js app titled "The AI Exchange" with nav: Home / Create / Trade. The `/api/markets` endpoint returns the SPA HTML rather than JSON. All market data is gated behind Petra/Martian wallet authentication. No public market rows insertable; `mnx_snapshots` table remains empty pending authenticated access.

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
- **kubeflow/kubeflow**: 15,575 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — pushed 2026-04-14 (today!)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP using Jane Street oxcaml_effect
- **plurigrid/gorj**: This very repo — forj + Rama + GF(3) gay trit coloring, 187 open issues
- **plurigrid/nash-portal + zubyul/nash-tui**: Dual Rust NASH TUI projects hot today
- **bob wallet**: Top swarm holder at 12.66 APT; G/I at floor (0.000681 APT each)
