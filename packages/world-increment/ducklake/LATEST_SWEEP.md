# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-04

## Sweep Metadata
- **Date:** 2026-05-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 359 |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 47 | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 4 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | 10 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 6 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 10 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Source

#### kubeflow (47 repos)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,565 |
| pipelines | Python | 4,119 |
| spark-operator | Python | 3,111 |
| trainer | Go | 2,080 |
| katib | Python | 1,676 |

#### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

#### migalkin (19 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

#### AustinCStone (10 repos snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

#### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| topoi | Python | 0 |
| monad-mcp-server | — | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-05-04)

Method: `0x1::coin::balance` view function via `fullnode.mainnet.aptoslabs.com`

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | 0x0a3c00c5... | **12.657007** |
| F | 0x18a14b5b... | 1.960516 |
| L | 0x7c2eaeaf... | 1.927269 |
| J | 0x4d964db8... | 1.895093 |
| alice | 0xc793acde... | 0.436434 |
| O | 0x73252b60... | 0.210136 |
| K | 0xa732040a... | 0.161961 |
| P | 0x62187924... | 0.140136 |
| M | 0x6fed37a7... | 0.112285 |
| N | 0xe7dde6da... | 0.106121 |
| Q | 0xac40fa50... | 0.103240 |
| S | 0xb8753014... | 0.091788 |
| R | 0x7ce605cc... | 0.090217 |
| T | 0x35781dc0... | 0.073713 |
| U | 0x75860da4... | 0.055773 |
| A | 0x8699edc0... | 0.051767 |
| V | 0xb59dd817... | 0.048833 |
| Y | 0xd8e32848... | 0.044449 |
| X | 0xa95cbbd1... | 0.042577 |
| W | 0x5f32aef7... | 0.040705 |
| B | 0x3f892ebe... | 0.036256 |
| Z | 0x7af0ef6e... | 0.024268 |
| D | 0xf7765624... | 0.011629 |
| C | 0x38b99e63... | 0.010185 |
| E | 0xdc1d9d53... | 0.009372 |
| H | 0xce67c327... | 0.001681 |
| G | 0x69a394c0... | 0.000681 |
| I | 0x070fe5d7... | 0.000681 |

**Total APT across 28 wallets:** ~20.37 APT  
**Richest:** `bob` with 12.657 APT (~62% of total)

### Multisig Contract Probes (Aptos Mainnet)

All 5 probed multisig accounts are **healthy** — all require 2 signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets

`testnet.mnx.fi` — Next.js SPA with client-side rendering. No public REST/JSON API endpoints accessible via curl; all routes return the HTML shell. `mnx_snapshots` table remains empty this sweep.

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
