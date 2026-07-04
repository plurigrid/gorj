# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-04

## Sweep Metadata
- **Date:** 2026-07-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** v1.5.4 (Python) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social-graph (zubyul) | 5 |
| DJedamski | social-graph (zubyul) | 3 |
| wasita | social-graph (zubyul) | 3 |
| kristinezheng | social-graph (zubyul) | 3 |
| M1shaaa | social-graph (zubyul) | 2 |
| AustinCStone | social-graph (zubyul) | 3 |
| **TOTAL** | | **321** |

### Top Repos by Stars

| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,761 | 2026-01-05 |
| kubeflow/pipelines | Python | 4,169 | 2026-04-10 |
| kubeflow/spark-operator | Python | 3,132 | 2026-04-10 |
| kubeflow/trainer | Go | 2,129 | 2026-04-10 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| migalkin/kgcourse2021 | HTML | 25 | 2026-02-16 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |

### Notable Recent Activity
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-02) — most recently active repo
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-07-01)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) — crane-jank converged-IR hub with GF3 convergence maps
- **migalkin/RWL** (Python, pushed 2026-05-28) — Weisfeiler and Leman Go Relational

### GF(3) Color Chain Summary
- **ERGODIC #d3869b** (trit=0, id%3==0): 114 increments
- **PLUS #b8bb26** (trit=1, id%3==1): 115 increments
- **MINUS #cc241d** (trit=2, id%3==2): 115 increments
- **Total world_increments this run:** 321

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c… | **12.65700700** |
| F | 0x18a1… | 1.96051600 |
| L | 0x7c2e… | 1.92726900 |
| J | 0x4d96… | 1.89509300 |
| alice | 0xc793… | 0.43643352 |
| O | 0x7325… | 0.21013600 |
| K | 0xa732… | 0.16196100 |
| P | 0x6218… | 0.14013600 |
| M | 0x6fed… | 0.11228500 |
| N | 0xe7dd… | 0.10612100 |
| Q | 0xac40… | 0.10324000 |
| S | 0xb875… | 0.09178800 |
| R | 0x7ce6… | 0.09021700 |
| T | 0x3578… | 0.07371300 |
| U | 0x7586… | 0.05577300 |
| A | 0x8699… | 0.05176700 |
| Y | 0xd8e3… | 0.04444900 |
| V | 0xb59d… | 0.04883299 |
| X | 0xa95c… | 0.04257700 |
| W | 0x5f32… | 0.04070500 |
| B | 0x3f89… | 0.03625600 |
| Z | 0x7af0… | 0.02426800 |
| D | 0xf776… | 0.01162900 |
| C | 0x38b9… | 0.01018500 |
| E | 0xdc1d… | 0.00937200 |
| H | 0xce67… | 0.00168100 |
| G | 0x69a3… | 0.00068100 |
| I | 0x070f… | 0.00068100 |

**Total Swarm: ~20.74 APT**  
Method: `0x1::coin::balance` view function (CoinStore 404 → FA model absent, falling back to legacy coin module).

### Multisig Contract Probes (5/5 healthy)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4… | 2 | ✅ |
| A-G | 0xf56c… | 2 | ✅ |
| Y-Z | 0xd3ff… | 2 | ✅ |
| S-T | 0x3b1c… | 2 | ✅ |
| V-W | 0x40fa… | 2 | ✅ |

All 5 multisig contracts are live with 2-of-N threshold.

### MNX Markets
`testnet.mnx.fi` is behind **Vercel deployment protection** (password required). Market data unavailable without auth token. Row inserted in `mnx_snapshots` with `category='unavailable'`.

---

## DuckDB Tables

```
world-increments.duckdb
├── world_increments   (344 rows) — GF(3)-tagged increment chain
├── repo_snapshots    (1265 rows) — GitHub repo metadata (cumulative)
├── aptos_snapshots    (28 rows)  — Hamming wallet balances
├── multisig_probes     (5 rows)  — Contract sigs_required checks
└── mnx_snapshots       (1 row)   — MNX unavailable (Vercel auth)
```

## GF(3) Assignment Rule
- `id % 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id % 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id % 3 == 2` → trit=2, color=#cc241d, name=**MINUS**
