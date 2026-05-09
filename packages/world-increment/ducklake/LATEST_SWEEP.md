# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-09

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repo Snapshot Summary

| org_or_user    | repos | total_stars | latest_push          |
|----------------|------:|------------:|----------------------|
| kubeflow       |   114 |      98,388 | 2026-05-09T02:47:57Z |
| migalkin       |    80 |         832 | 2025-08-04T03:01:46Z |
| bmorphism      |   220 |         330 | 2026-05-09T00:33:36Z |
| AustinCStone   |   106 |         323 | 2026-02-11T01:10:54Z |
| plurigrid      |   220 |         112 | 2026-05-09T10:17:16Z |
| zubyul         |    68 |          29 | 2026-04-30T15:43:58Z |
| DJedamski      |    33 |          21 | 2018-03-07T12:36:09Z |
| TeglonLabs     |   126 |          18 | 2026-01-16T01:42:16Z |
| wasita         |    80 |          10 | 2026-05-06T05:14:00Z |
| kristinezheng  |    54 |           0 | 2026-04-09T17:09:42Z |
| M1shaaa        |    48 |           0 | 2026-05-09T02:35:21Z |

**Total repo_snapshots:** 1,149 rows (across all sources)
**Total world_increments:** 228 (GF(3) colored)

### GF(3) Color Chain Distribution

| trit | color   | name    | count |
|-----:|---------|---------|------:|
|    0 | #d3869b | ERGODIC |    75 |
|    1 | #b8bb26 | PLUS    |    77 |
|   -1 | #cc241d | MINUS   |    76 |

GF(3) coloring applied: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

### Notable Repos (plurigrid, most recently pushed)

- `plurigrid/gorj` — Clojure, 0★, forj + Rama topology nREPL routing + GF(3) gay trit coloring
- `plurigrid/horse` — TeX, 1★
- `plurigrid/zig-syrup` — Zig, 2★, OCapN Syrup with CapTP optimizations
- `plurigrid/asi` — HTML, 21★, topological chemputer
- `plurigrid/nash-portal` — Rust, 2★, NASH token TUI in browser (ratzilla WASM + GeckoTerminal)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 Hamming-swarm addresses queried via `fullnode.mainnet.aptoslabs.com`.

| world | address (truncated)   | balance (APT) |
|-------|-----------------------|--------------:|
| alice | 0xc793...4cc7b        |           0.0 |
| bob   | 0x0a3c...512d5d       |           0.0 |
| A     | 0x8699...ebe9d7a      |           0.0 |
| B     | 0x3f89...577cb13      |           0.0 |
| C     | 0x38b9...91535e       |           0.0 |
| D     | 0xf776...fcfdd1       |           0.0 |
| E     | 0xdc1d...958d36       |           0.0 |
| F     | 0x18a1...4c3cf71      |           0.0 |
| G     | 0x69a3...bcc7f32      |           0.0 |
| H     | 0xce67...4e5300f      |           0.0 |
| I     | 0x070f...c00c1fc9     |           0.0 |
| J     | 0x4d96...93e87f54     |           0.0 |
| K     | 0xa732...7425dc4      |           0.0 |
| L     | 0x7c2e...6337eba9     |           0.0 |
| M     | 0x6fed...4b7f2e9      |           0.0 |
| N     | 0xe7dd...11551b2c     |           0.0 |
| O     | 0x7325...525a89d      |           0.0 |
| P     | 0x6218...621ec948     |           0.0 |
| Q     | 0xac40...5e5c89a9     |           0.0 |
| R     | 0x7ce6...36d76e10     |           0.0 |
| S     | 0xb875...f99d0386     |           0.0 |
| T     | 0x3578...2d3f4588     |           0.0 |
| U     | 0x7586...5ef9956      |           0.0 |
| V     | 0xb59d...a89af2c3     |           0.0 |
| W     | 0x5f32...a6ccc7b0     |           0.0 |
| X     | 0xa95c...cbe33047d    |           0.0 |
| Y     | 0xd8e3...fa2444c4     |           0.0 |
| Z     | 0x7af0...6e4e197c     |           0.0 |

All balances are 0.0 APT — addresses are registered in schema but unfunded on mainnet.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| pair | address (truncated)  | sigs_required | healthy |
|------|----------------------|:-------------:|:-------:|
| A-B  | 0x0da4...987003      |             2 | yes     |
| A-G  | 0xf56c...c0096       |             2 | yes     |
| Y-Z  | 0xd3ff...75b883      |             2 | yes     |
| S-T  | 0x3b1c...ed7883      |             2 | yes     |
| V-W  | 0x40fa...80eb6d      |             2 | yes     |

All 5/5 multisig contracts healthy. Each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status: unavailable** — `testnet.mnx.fi` is a Next.js SPA. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the SPA HTML shell rather than JSON. No market data could be extracted without a headless browser. `mnx_snapshots` table remains empty.

---

## DuckDB Tables

```
world-increments.duckdb
├── world_increments   (228 rows) — GF(3) colored increment log
├── repo_snapshots    (1149 rows) — GitHub repo metadata across 11 sources
├── aptos_snapshots     (28 rows) — Hamming swarm APT balances
├── multisig_probes      (5 rows) — Aptos multisig health probes
└── mnx_snapshots        (0 rows) — MNX market data (SPA, unavailable)
```
