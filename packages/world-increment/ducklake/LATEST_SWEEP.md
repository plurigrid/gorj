# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-15

## Sweep Metadata
- **Date:** 2026-04-15
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all time) | 323 |
| New Increments This Sweep | 300 |
| Total Repo Snapshots (all time) | 1,244 |
| New Repos This Sweep | 300 |
| Sources Covered (this sweep) | 4 (rate limit after that) |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (client-side SPA) |

---

## GF(3) Color Chain — New Increments This Sweep (first 12 shown)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid | repo_push | +1 | `#b8bb26` | **PLUS** |
| 2  | plurigrid | repo_push | -1 | `#cc241d` | **MINUS** |
| 3  | plurigrid | repo_push | 0 | `#d3869b` | **ERGODIC** |
| 4  | plurigrid | repo_push | +1 | `#b8bb26` | **PLUS** |
| ... | ... | ... | ... | ... | ... |
| 101 | kubeflow | repo_push | +1 | `#b8bb26` | **PLUS** |
| 102 | kubeflow | repo_push | -1 | `#cc241d` | **MINUS** |
| ... | ... | ... | ... | ... | ... |
| 148 | TeglonLabs | repo_push | +1 | `#b8bb26` | **PLUS** |
| ... | ... | ... | ... | ... | ... |
| 201 | bmorphism | repo_push | +1 | `#b8bb26` | **PLUS** |
| ... | ... | ... | ... | ... | ... |
| 300 | bmorphism | repo_push | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain this sweep: 100 × (PLUS → MINUS → ERGODIC) repeated across 300 repo increments

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source (All Time in DB)

| Source | Type | Repos (all time) | New This Sweep |
|--------|------|-----------------|----------------|
| plurigrid | org | 300 | 100 |
| bmorphism | user | 300 | 100 |
| TeglonLabs | org | 159 | 53 |
| kubeflow | org | 141 | 47 |
| AustinCStone | user | 86 | 0 (rate-limited) |
| migalkin | user | 60 | 0 (rate-limited) |
| wasita | user | 60 | 0 (rate-limited) |
| zubyul | user | 48 | 0 (rate-limited) |
| kristinezheng | user | 36 | 0 (rate-limited) |
| M1shaaa | user | 32 | 0 (rate-limited) |
| DJedamski | user | 22 | 0 (rate-limited) |
| **TOTAL** | | **1,244** | **300** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Snapshot time:** 2026-04-15  
**Endpoint:** `POST https://fullnode.mainnet.aptoslabs.com/v1/view` → `0x1::coin::balance`  
**Note:** Legacy `CoinStore` resources are absent on these accounts (Move V2 FA model); used the coin view function instead.

| World | Address (truncated) | Balance (APT) |
|-------|-------------------|--------------|
| bob | 0x0a3c00c5... | **12.6570** |
| F | 0x18a14b5b... | 1.9605 |
| L | 0x7c2eaeaf... | 1.9273 |
| J | 0x4d964db8... | 1.8951 |
| alice | 0xc793acde... | 0.4364 |
| O | 0x73252b60... | 0.2101 |
| K | 0xa732040a... | 0.1620 |
| P | 0x62187920... | 0.1401 |
| M | 0x6fed37a7... | 0.1123 |
| N | 0xe7dde6da... | 0.1061 |
| Q | 0xac40fa50... | 0.1032 |
| S | 0xb8753014... | 0.0918 |
| R | 0x7ce605cc... | 0.0902 |
| T | 0x35781dc0... | 0.0737 |
| U | 0x75860da4... | 0.0558 |
| A | 0x8699edc0... | 0.0518 |
| V | 0xb59dd817... | 0.0488 |
| Y | 0xd8e32848... | 0.0444 |
| X | 0xa95cbbd1... | 0.0426 |
| W | 0x5f32aef7... | 0.0407 |
| B | 0x3f892ebe... | 0.0363 |
| Z | 0x7af0ef6e... | 0.0243 |
| D | 0xf7765624... | 0.0116 |
| C | 0x38b99e63... | 0.0102 |
| E | 0xdc1d9d53... | 0.0094 |
| H | 0xce67c327... | 0.0017 |
| I | 0x070fe5d7... | 0.0007 |
| G | 0x69a394c0... | 0.0007 |
| **TOTAL** | 28 wallets | **20.3448 APT** |

### Multisig Contract Probes

All 5 multisig accounts healthy — all require **2-of-N** signatures.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428...987003 | 2 | ✓ |
| A-G | 0xf56c4a1c...c0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a client-side Next.js SPA. `/api/markets` returns 404. No HTML-embedded market data found. `mnx_snapshots` table has 0 rows.

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

## Notable Highlights (2026-04-15 Sweep)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform (33,888 stars across 47 repos)
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-15)
- **plurigrid/gorj**: This very repo — forj + GF(3) trit coloring (pushed 2026-04-15)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bob**: Richest Aptos wallet at 12.66 APT (62% of total swarm holdings)
- **F, L, J**: Second tier ~1.9 APT each
- **All 5 multisigs**: 2-of-N healthy — A-B, A-G, Y-Z, S-T, V-W
