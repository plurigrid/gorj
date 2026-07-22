# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-22

## Sweep Metadata
- **Date:** 2026-07-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 132 |
| Total Repo Snapshots | 132 |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph

### Sources Snapshotted

| Source | Type | Discovered | Stored |
|--------|------|-----------|--------|
| plurigrid | org | 100 | 100 |
| kubeflow | org | 49 | 8 (top by stars/activity) |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 7 |
| zubyul | user | 49 | 3 |
| migalkin | social | 19 | 2 |
| DJedamski | social | 6 | 1 |
| wasita | social | 12 | 2 |
| kristinezheng | social | 5 | 1 |
| M1shaaa | social | 8 | 1 |
| AustinCStone | social | 41 | 2 |

### Top Repos by Stars (2026-07-22)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,789 | — | 2026-07-21 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-21 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-22 |
| kubeflow/trainer | 2,152 | Go | 2026-07-21 |
| AustinCStone/TextGAN | 92 | Python | — |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 31 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript | 2026-07-12 |
| bmorphism/risc0-cosmwasm-example | 23 | Rust | — |

### Notable Recent Activity
- `plurigrid/gorj` — pushed 2026-07-22 (this repo)
- `bmorphism/Gay.jl` — pushed 2026-07-21 — 187 open issues, wide-gamut color sampling
- `bmorphism/gay-chat` — pushed 2026-07-14 — gay://chat over Spritely Brassica
- `wasita/wasita.github.io` — pushed 2026-07-21 — Svelte personal site (active)
- `wasita/pnas-typst-template` — pushed 2026-07-16 — new Typst template
- `TeglonLabs/jank-crane` — pushed 2026-06-08 — crane-jank converged-IR + GF3 maps

### GF(3) Color Distribution (132 increments)
- trit=1 PLUS #b8bb26: 44 increments
- trit=-1 MINUS #cc241d: 44 increments
- trit=0 ERGODIC #d3869b: 44 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet APT)

**Method:** `POST /v1/view` → `0x1::coin::balance<AptosCoin>` (legacy CoinStore was migrated to FA)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| alice | 0.43643352 | 0xc793ac… |
| bob | **12.65700700** | 0x0a3c00… |
| A | 0.05176700 | 0x8699ed… |
| B | 0.03625600 | 0x3f892e… |
| C | 0.01018500 | 0x38b99e… |
| D | 0.01162900 | 0xf77656… |
| E | 0.00937200 | 0xdc1d9d… |
| F | 1.96051600 | 0x18a14b… |
| G | 0.00068100 | 0x69a394… |
| H | 0.00168100 | 0xce67c3… |
| I | 0.00068100 | 0x070fe5… |
| J | 1.89509300 | 0x4d964d… |
| K | 0.16196100 | 0xa73204… |
| L | 1.92726900 | 0x7c2eae… |
| M | 0.11228500 | 0x6fed37… |
| N | 0.10612100 | 0xe7dde6… |
| O | 0.21013600 | 0x73252b… |
| P | 0.14013600 | 0x621879… |
| Q | 0.10324000 | 0xac40fa… |
| R | 0.09021700 | 0x7ce605… |
| S | 0.09178800 | 0xb87530… |
| T | 0.07371300 | 0x35781d… |
| U | 0.05577300 | 0x75860d… |
| V | 0.04883299 | 0xb59dd8… |
| W | 0.04070500 | 0x5f32ae… |
| X | 0.04257700 | 0xa95cbb… |
| Y | 0.04444900 | 0xd8e328… |
| Z | 0.02426800 | 0x7af0ef… |

**Total swarm: 20.34477251 APT**  
`bob` holds 62.2% of total. `F`, `J`, `L` each ~1.9 APT. `G`, `I` at dust (0.00068 APT).

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required`:

| Pair | sigs_required | Healthy |
|------|--------------|---------|
| A-B | 2 | ✓ |
| A-G | 2 | ✓ |
| Y-Z | 2 | ✓ |
| S-T | 2 | ✓ |
| V-W | 2 | ✓ |

All contracts require 2-of-N. All respond healthy.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Next.js SPA, no public `/api/markets` REST endpoint. `mnx_snapshots` table has 0 rows.

---

## Database Tables

| Table | Rows |
|-------|------|
| world_increments | 132 |
| repo_snapshots | 132 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
