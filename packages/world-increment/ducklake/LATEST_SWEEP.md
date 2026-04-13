# World-Increment Sweep + Hamming Snapshot — 2026-04-13

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.1 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) Color Chain:** id%3==0 → ERGODIC #d3869b | id%3==1 → PLUS #b8bb26 | id%3==2 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted This Run

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 99 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 47 |
| migalkin | social graph (zubyul) | 19 |
| DJedamski | social graph (zubyul) | 6 |
| wasita | social graph (zubyul) | 10 |
| kristinezheng | social graph (zubyul) | 6 |
| M1shaaa | social graph (zubyul) | 8 |
| AustinCStone | social graph (zubyul) | 40 |
| **New this sweep** | | **322** |
| **Cumulative total** | | **793** |

### Top Repos by Stars

**kubeflow:**
- kubeflow/kubeflow ★15,569
- kubeflow/pipelines ★4,119
- kubeflow/spark-operator ★3,114
- kubeflow/trainer ★2,080
- kubeflow/katib ★1,676

**migalkin (social graph):**
- migalkin/NodePiece ★143 (ICLR'22 knowledge graph embeddings)
- migalkin/StarE ★88 (EMNLP 2020 hyper-relational KGs)
- migalkin/kgcourse2021 ★25

**AustinCStone (social graph):**
- AustinCStone/TextGAN ★92 (TensorFlow text GAN)
- AustinCStone/StereoVisionMRF ★11

**bmorphism:**
- bmorphism/ocaml-mcp-sdk ★60 (OCaml MCP SDK w/ Jane Street oxcaml_effect)
- bmorphism/anti-bullshit-mcp-server ★23

**plurigrid:**
- plurigrid/asi ★16 (everything is topological chemputer!)
- plurigrid/gorj ★0 (this repo — forj + GF(3) trit coloring)
- plurigrid/zig-syrup ★2 (OCapN Syrup + CapTP in Zig 0.15)

**TeglonLabs:**
- TeglonLabs/mathpix-gem ★2 (Ruby math OCR gem)

### GF(3) Trit Distribution (322 new increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 108 |
| 1 | #b8bb26 | PLUS | 107 |
| -1 | #cc241d | MINUS | 107 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried via `0x1::coin::balance` view function (fullnode.mainnet.aptoslabs.com):

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.43643352 |
| bob | 0x0a3c...512d | 12.65700700 |
| A | 0x8699...e9d7 | 0.05176700 |
| B | 0x3f89...cb13 | 0.03625600 |
| C | 0x38b9...535e | 0.01018500 |
| D | 0xf776...fdd1 | 0.01162900 |
| E | 0xdc1d...8d36 | 0.00937200 |
| F | 0x18a1...cf71 | **1.96051600** |
| G | 0x69a3...7f32 | 0.00068100 |
| H | 0xce67...300f | 0.00168100 |
| I | 0x070f...1fc9 | 0.00068100 |
| J | 0x4d96...7f54 | **1.89509300** |
| K | 0xa732...5dc4 | 0.16196100 |
| L | 0x7c2e...eba9 | **1.92726900** |
| M | 0x6fed...f2e9 | 0.11228500 |
| N | 0xe7dd...1b2c | 0.10612100 |
| O | 0x7325...a89d | 0.21013600 |
| P | 0x6218...c948 | 0.14013600 |
| Q | 0xac40...c89a | 0.10324000 |
| R | 0x7ce6...6e10 | 0.09021700 |
| S | 0xb875...0386 | 0.09178800 |
| T | 0x3578...4588 | 0.07371300 |
| U | 0x7586...f956 | 0.05577300 |
| V | 0xb59d...f2c3 | 0.04883299 |
| W | 0x5f32...c7b0 | 0.04070500 |
| X | 0xa95c...047d | 0.04257700 |
| Y | 0xd8e3...44c4 | 0.04444900 |
| Z | 0x7af0...197c | 0.02426800 |

**Total swarm APT:** 20.34477251 APT  
**Richest:** bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)  
**Smallest balance:** G/I (0.000681 APT each)

### Multisig Contract Probes

All 5 multisig contracts respond healthy — **2-of-N signatures required** each:

| Pair | Address | Sigs | Healthy |
|------|---------|------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi is a client-side Next.js SPA. Probed `/api/markets`, `/api/tickers`, `/api/v1/markets`, `/api/v2/markets`, `/api/pairs` — all return 404. `/markets` route returns HTML shell only. No market data extractable without a headless browser. `mnx_snapshots` table remains empty for this sweep.

---

## Schema Reference

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
