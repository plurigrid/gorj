# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-20

## Sweep Metadata
- **Date:** 2026-07-20
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Orgs + Users Scanned

| Source | Type | Repos Found | Most Recent Push |
|--------|------|-------------|-----------------|
| plurigrid | org | 50+ | 2026-07-17 (asi) |
| bmorphism | user | 50+ | 2026-07-20 (Gay.jl) — **TODAY** |
| zubyul | user | 49 | 2026-04-24 (voice-observatory) |
| kubeflow | org | 30+ | 2026-07-20 (kubeflow/kubeflow) — **TODAY** |
| TeglonLabs | org | 5 | 2026-06-08 (jank-crane) |
| migalkin | user | 19 | 2026-07-10 (kgcourse2021) |
| AustinCStone | user | 20 | 2026-07-15 (byteruckus) |
| DJedamski | user | 6 | 2018-02-26 (kaggle_ncaa18) — inactive |
| M1shaaa | user | 8 | 2026-02-04 |
| wasita | user | 12 | 2026-07-16 (pnas-typst-template) |
| kristinezheng | user | 5 | 2026-07-01 |

### Noteworthy Activity

- **bmorphism/Gay.jl** — updated today, 187 open issues, Julia GF(3) color library, 2 stars
- **plurigrid/asi** — "everything is topological chemputer!", 31 stars, updated 2026-07-17
- **plurigrid/gorj** — this repo, 1272 open issues, updated 2026-07-07
- **kubeflow/kubeflow** — 15,784 stars, updated today
- **kubeflow/spark-operator** — 3,140 stars, updated today
- **bmorphism/anti-bullshit-mcp-server** — 22 stars, updated 2026-07-12
- **bmorphism/gay-chat** — new Spritely Brassica Chat impl, 2026-07-14
- **wasita/pnas-typst-template** — new typst template, 2026-07-16
- **AustinCStone/byteruckus** — brand new repo 2026-07-15
- **wasita/wasita.github.io** — active personal Svelte site, 2026-07-16

### New World-Increment Entries (GF3 chain, IDs 24–34)

| ID | Source | Event Type | GF3 | Color | Name |
|----|--------|------------|-----|-------|------|
| 24 | plurigrid (org) | repo_snapshot | 0 | #d3869b | ERGODIC |
| 25 | bmorphism (user) | repo_snapshot | 1 | #b8bb26 | PLUS |
| 26 | zubyul (user) | repo_snapshot | 2 | #cc241d | MINUS |
| 27 | kubeflow (org) | repo_snapshot | 0 | #d3869b | ERGODIC |
| 28 | TeglonLabs (org) | repo_snapshot | 1 | #b8bb26 | PLUS |
| 29 | migalkin (user) | repo_snapshot | 2 | #cc241d | MINUS |
| 30 | AustinCStone (user) | repo_snapshot | 0 | #d3869b | ERGODIC |
| 31 | DJedamski (user) | repo_snapshot | 1 | #b8bb26 | PLUS |
| 32 | M1shaaa (user) | repo_snapshot | 2 | #cc241d | MINUS |
| 33 | aptos_mainnet | hamming_swarm_snapshot | 0 | #d3869b | ERGODIC |
| 34 | aptos_mainnet | multisig_probe | 1 | #b8bb26 | PLUS |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

**Snapshot ledger version:** ~6,366,760,112  
**Method:** `0x1::coin::balance` view function (legacy CoinStore resource unavailable on these accounts)

### Wallet Balances — All 28 Worlds

| World | Balance (APT) |
|-------|--------------|
| bob | 12.657007 |
| F | 1.960516 |
| L | 1.927269 |
| J | 1.895093 |
| O | 0.210136 |
| alice | 0.436434 |
| P | 0.140136 |
| K | 0.161961 |
| M | 0.112285 |
| N | 0.106121 |
| Q | 0.103240 |
| R | 0.090217 |
| S | 0.091788 |
| T | 0.073713 |
| U | 0.055773 |
| A | 0.051767 |
| V | 0.048833 |
| Y | 0.044449 |
| X | 0.042577 |
| W | 0.040705 |
| B | 0.036256 |
| Z | 0.024268 |
| D | 0.011629 |
| C | 0.010185 |
| E | 0.009372 |
| H | 0.001681 |
| G | 0.000681 |
| I | 0.000681 |

**Total Swarm APT: 20.344773 APT**  
**Top 3:** bob (12.657), F (1.961), L (1.927)

### Multisig Probes — All 5 Healthy

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c00... | 2 | ✅ |
| A-G | 0xf56c4a1c09062... | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df... | 2 | ✅ |
| S-T | 0x3b1c3ae905d44... | 2 | ✅ |
| V-W | 0x40fad7b423a84... | 2 | ✅ |

All 5 multisig contracts respond healthy with 2-of-N threshold. No anomalies.

### MNX Markets

`testnet.mnx.fi` — **Authentication Required** (Vercel-protected). No public API. Market data unavailable this sweep.

---

## DuckDB State After Sweep

| Table | Rows |
|-------|------|
| world_increments | 34 |
| repo_snapshots | 944 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
