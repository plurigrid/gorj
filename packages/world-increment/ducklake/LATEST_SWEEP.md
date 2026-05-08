# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-05-08  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources & GF(3) Color Chain

| # | Source | Type | GF(3) | Color | Repos |
|---|--------|------|-------|-------|-------|
| 1 | plurigrid | org | PLUS (trit=1) | `#b8bb26` | 100 |
| 2 | kubeflow | org | MINUS (trit=2) | `#cc241d` | 48 |
| 3 | TeglonLabs | org | ERGODIC (trit=0) | `#d3869b` | 4 |
| 4 | bmorphism | user | PLUS (trit=1) | `#b8bb26` | 100 |
| 5 | zubyul | user | MINUS (trit=2) | `#cc241d` | 49 |
| 6 | migalkin | social | ERGODIC (trit=0) | `#d3869b` | 5 |
| 7 | DJedamski | social | PLUS (trit=1) | `#b8bb26` | 3 |
| 8 | wasita | social | MINUS (trit=2) | `#cc241d` | 7 |
| 9 | kristinezheng | social | ERGODIC (trit=0) | `#d3869b` | 4 |
| 10 | M1shaaa | social | PLUS (trit=1) | `#b8bb26` | 4 |
| 11 | AustinCStone | social | MINUS (trit=2) | `#cc241d` | 6 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

**Total repos snapshotted:** 330

### Stars / Forks by Source

| Source | Stars | Forks | Repos |
|--------|-------|-------|-------|
| kubeflow | 34,023 | 13,402 | 48 |
| migalkin | 275 | 48 | 5 |
| bmorphism | 248 | 73 | 100 |
| AustinCStone | 106 | 36 | 6 |
| plurigrid | 70 | 43 | 100 |
| zubyul | 14 | 2 | 49 |
| wasita | 4 | 1 | 7 |
| TeglonLabs | 2 | 2 | 4 |
| DJedamski | 2 | 1 | 3 |
| kristinezheng | 0 | 0 | 4 |
| M1shaaa | 0 | 0 | 4 |

### Notable Repos

- **kubeflow/kubeflow** — MLOps flagship (~15k★)
- **migalkin/NodePiece** — Knowledge graph embeddings, ICLR'22 (144★)
- **migalkin/StarE** — Hyper-relational KGs, EMNLP'20 (89★)
- **AustinCStone/TextGAN** — Text generation with GANs in TensorFlow (92★)
- **bmorphism** — 100 repos: Move, Zig, Julia, Clojure, OCaml (active polyglot)
- **plurigrid/gorj** — This repo: Clojure MCP REPL server
- **TeglonLabs/mathpix-gem** — LaTeX/chemistry OCR Ruby gem (2★, 11 open issues)
- **wasita/vocoder** — Latest push: 2026-05-06

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A-Z) queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All addresses return `resource_not_found` — no APT CoinStore registered.  
Balance: **0.0 APT** for all 28 wallets.

*Ledger height at query: ~755,145,639 · epoch 15729 · 2026-05-08T20:05 UTC*

| Wallet | Address | APT |
|--------|---------|-----|
| alice | `0xc793...cc7b` | 0.0 |
| bob | `0x0a3c...2d5d` | 0.0 |
| A-Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4...7003` | 2 | HEALTHY |
| A-G | `0xf56c...0096` | 2 | HEALTHY |
| Y-Z | `0xd3ff...b883` | 2 | HEALTHY |
| S-T | `0x3b1c...7883` | 2 | HEALTHY |
| V-W | `0x40fa...eb6d` | 2 | HEALTHY |

All 5 multisig contracts live and responsive with **2-of-N** threshold.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no market data extractable**  
The endpoint returns ~293 KB HTML bundle (client-side rendered). No ticker, price, or name fields present in static payload. JavaScript execution required for data.

---

## DuckDB Schema

```sql
world_increments  : 11 rows  (GF3 color-chained source registry)
repo_snapshots    : 330 rows (per-repo: stars, forks, language, pushed_at)
aptos_snapshots   :  28 rows (alice + bob + A-Z wallet balances)
multisig_probes   :   5 rows (A-B, A-G, Y-Z, S-T, V-W)
mnx_snapshots     :   1 row  (unavailability record)
```

## GF(3) Assignment Rule

```
id % 3 == 0  =>  trit=0,  color=#d3869b,  name=ERGODIC
id % 3 == 1  =>  trit=1,  color=#b8bb26,  name=PLUS
id % 3 == 2  =>  trit=-1, color=#cc241d,  name=MINUS
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent · 2026-05-08*
