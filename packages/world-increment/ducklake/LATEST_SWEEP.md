# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-18

## Sweep Metadata
- **Date:** 2026-07-18
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (via pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| World Increments (this run) | 91 |
| Repo Snapshots (this run) | 91 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A-Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (SPA) |

---

## GF(3) Color Chain — 2026-07-18 Run (91 increments)

GF(3) assignment: `id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d`

| Trit | Name | Color | Count (this run) |
|------|------|-------|-----------------|
| 0 | ERGODIC | `#d3869b` | 37 |
| 1 | PLUS | `#b8bb26` | 39 |
| -1 | MINUS | `#cc241d` | 38 |

Chain: 91 increments spanning 30 complete GF(3) cycles + 1 remainder.

---

## Top Repos by Source (2026-07-18)

### plurigrid (100 repos total, 30 snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| gorj | Clojure | 1 | 2026-07-18 ← active today |
| asi | HTML | 31 | 2026-07-10 |
| place | TeX | 1 | 2026-07-14 |
| eirobri | Clojure | 0 | 2026-07-14 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |

### kubeflow (49 repos, 15 snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,781 | 2026-07-18 ← active today |
| mcp-server | Python | 26 | 2026-07-18 ← active today |
| pipelines | Python | 4,168 | 2026-07-17 |
| spark-operator | Python | 3,138 | 2026-07-18 |
| trainer | Go | 2,151 | 2026-07-18 |

### TeglonLabs (5 repos, all snapshotted)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |

### bmorphism (106 total, 15 snapshotted)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| gay-chat | Scheme | 0 | 2026-07-14 |

### Social Graph (migalkin / DJedamski / wasita / kristinezheng / M1shaaa / AustinCStone)
| Repo | Stars | Recently Active |
|------|-------|----------------|
| migalkin/NodePiece | 144 | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 2025-03-03 |
| migalkin/StarE | 89 | 2026-04-16 |
| wasita/wasita.github.io | 1 | 2026-07-16 ← active |
| AustinCStone/byteruckus | 0 | 2026-07-15 ← new repo |

---

## Repo Counts by Source (GitHub totals per 2026-07-18 query)

| Source | Type | Total Repos | Snapshotted |
|--------|------|-------------|------------|
| plurigrid | org | 100+ | 30 |
| kubeflow | org | 49 | 15 |
| bmorphism | user | 106 | 15 |
| TeglonLabs | org | 5 | 5 |
| zubyul | user | 49 | 8 |
| AustinCStone | user | 41 | 4 |
| migalkin | user | 19 | 4 |
| wasita | user | 12 | 4 |
| kristinezheng | user | 5 | 2 |
| M1shaaa | user | 8 | 2 |
| DJedamski | user | 6 | 2 |
| **TOTAL** | | | **91** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A-Z — 28 addresses)

**All 28 addresses returned HTTP 404 — `resource_not_found`**

The Aptos mainnet fullnode confirms none of these addresses have an active
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource at ledger version ~6,340,247,588.
Likely interpretation: addresses may hold balances in FA (fungible asset) format, or were never funded with APT on mainnet.

All 28 entries recorded in `aptos_snapshots` with `balance_apt = -1.0` (sentinel for "not found").

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | not found |
| bob | 0x0a3c00... | not found |
| A–Z | 0x8699ed... – 0x7af0ef... | not found (all 26) |

### Multisig Contract Probes

All 5 probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | **2** | ✓ healthy |
| A-G | 0xf56c4a1c... | **2** | ✓ healthy |
| Y-Z | 0xd3ffe181... | **2** | ✓ healthy |
| S-T | 0x3b1c3ae9... | **2** | ✓ healthy |
| V-W | 0x40fad7b4... | **2** | ✓ healthy |

All 5/5 multisig contracts healthy — all require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — pure React SPA, no accessible REST endpoints.  
Paths probed: `/api/markets`, `/api/v1/markets`, `/api/tickers` — all returned empty.  
No `mnx_snapshots` rows inserted.

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

## Notable Highlights (2026-07-18)

### GitHub
- **kubeflow/kubeflow**: 15,781 stars (+216 vs Apr sweep) — active today
- **kubeflow/mcp-server**: newly appeared repo (pushed 14:32 UTC today) — AI-assisted dev with Kubeflow Tools
- **plurigrid/gorj**: 1,242 open issues — most active plurigrid repo, pushed today
- **bmorphism/Gay.jl**: 187 open issues — broad color-SPI library activity
- **AustinCStone/byteruckus**: new repo created 2026-07-15
- **wasita/pnas-typst-template**: new repo created 2026-07-16

### Hamming Swarm
- **All 28 Aptos wallets (alice, bob, A-Z)**: no APT coin store on mainnet — zero APT recorded
- **All 5 multisig contracts (A-B, A-G, Y-Z, S-T, V-W)**: healthy, 2-of-N signatures required
- **MNX testnet**: SPA-only, no API data extractable

### GF(3) Cumulative DB State
- `world_increments`: 114 total rows (91 new this run)
- `repo_snapshots`: 1,035 total rows (91 new this run)
- `aptos_snapshots`: 28 rows (28 new this run)
- `multisig_probes`: 5 rows (5 new this run)

*Generated 2026-07-18 by world-increment-sweep + hamming-swarm-snapshot agent*
