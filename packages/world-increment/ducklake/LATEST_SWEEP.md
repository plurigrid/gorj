# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-10

## Sweep Metadata
- **Date:** 2026-06-10
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 326 |
| Total Repo Snapshots | 326 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 108 |
| +1 | `#b8bb26` | PLUS | 109 |
| -1 | `#cc241d` | MINUS | 109 |

GF(3) rule: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## Top Repos by Stars

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,715 | 2,672 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,153 | 2,004 | 2026-06-10 |
| kubeflow/spark-operator | Python | 3,126 | 1,488 | 2026-06-09 |
| kubeflow/trainer | Go | 2,112 | 964 | 2026-06-10 |
| kubeflow/katib | Python | 1,685 | 525 | 2026-06-05 |
| kubeflow/arena | Go | 812 | 190 | 2026-05-07 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| plurigrid/gorj | Clojure | 0 | 0 | 2026-06-10 (482 issues) |

---

## Repo Counts by Source (2026-06-10)

| Source | Type | Repos (deduplicated) |
|--------|------|---------------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 48 |
| migalkin | user (social) | 6 |
| wasita | user (social) | 5 |
| TeglonLabs | org | 5 |
| AustinCStone | user (social) | 4 |
| DJedamski | user (social) | 3 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| **TOTAL** | | **326** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>`.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| bob | `0x0a3c00c5...05512d5d` | **12.657007** |
| F | `0x18a14b5b...74c3cf71` | 1.960516 |
| L | `0x7c2eaeaf...6337eba9` | 1.927269 |
| J | `0x4d964db8...93e87f54` | 1.895093 |
| alice | `0xc793acde...624cc7b` | 0.436434 |
| O | `0x73252b60...525a89d` | 0.210136 |
| K | `0xa732040a...a425dc4` | 0.161961 |
| P | `0x62187929...1ec948` | 0.140136 |
| M | `0x6fed37a7...4b7f2e9` | 0.112285 |
| N | `0xe7dde6da...1551b2c` | 0.106121 |
| Q | `0xac40fa50...5c89a9` | 0.103240 |
| S | `0xb8753014...99d0386` | 0.091788 |
| R | `0x7ce605cc...d76e10` | 0.090217 |
| T | `0x35781dc0...d3f4588` | 0.073713 |
| U | `0x75860da4...5ef9956` | 0.055773 |
| A | `0x8699edc0...ebe9d7a` | 0.051767 |
| V | `0xb59dd817...89af2c3` | 0.048833 |
| Y | `0xd8e32848...2444c4` | 0.044449 |
| X | `0xa95cbbd1...e33047d` | 0.042577 |
| W | `0x5f32aef7...cc7b0` | 0.040705 |
| B | `0x3f892ebe...577cb13` | 0.036256 |
| Z | `0x7af0ef6e...4e197c` | 0.024268 |
| D | `0xf7765624...fcfdd1` | 0.011629 |
| C | `0x38b99e63...691535e` | 0.010185 |
| E | `0xdc1d9d53...0958d36` | 0.009372 |
| H | `0xce67c327...4e5300f` | 0.001681 |
| G | `0x69a394c0...bcc7f32` | 0.000681 |
| I | `0x070fe5d7...c00c1fc9` | 0.000681 |

**Total tracked APT: 20.344773 APT**

Notable: `bob` holds 62% of all tracked APT (12.66 APT). `F`, `L`, `J` each hold ~1.9 APT. `G`, `H`, `I` are near-empty dust wallets.

### Multisig Contract Probes

All 5 pairs use `0x1::multisig_account::num_signatures_required`.

| Pair | Contract | Sigs Required | Status |
|------|----------|---------------|--------|
| A-B | `0x0da4f428...987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ healthy |

All 5 multisig accounts are 2-of-N and responding on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel authentication gate blocks API access without credentials. No market data captured in `mnx_snapshots`.

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

## Notable Highlights (2026-06-10)
- **plurigrid/gorj** pushed today: forj + Rama topology nREPL + GF(3) orchestration (482 open issues)
- **plurigrid/asi** pushed today: "everything is topological chemputer!" (25 stars)
- **bmorphism/Gay.jl** pushed today: wide-gamut SPI color sampling with Pigeons.jl (189 open issues)
- **kubeflow/kubeflow**: 15,715 stars — ML platform for Kubernetes (▲150 since April sweep)
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK with Jane Street oxcaml_effect
- **Hamming swarm**: bob dominates at 12.66 APT; all 5 multisigs healthy at 2-of-N
