# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

## Sweep Metadata
- **Date:** 2026-07-21
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Increment:** 13 · trit=1 · PLUS · #b8bb26

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried (2026-07-21)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 12 |
| AustinCStone | social graph | 41 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **394** |

**Cumulative repo_snapshots in DuckDB:** 1,277

### Notable Repos (active in 2026)

- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub, GF3 convergence maps; pushed 2026-06-08
- **TeglonLabs/mathpix-gem** (Ruby, ★2) — math OCR to LaTeX/SMILES; updated 2026-01-01
- **migalkin/NodePiece** (Python, ★144) — Compositional KG representations (ICLR'22)
- **migalkin/StarE** (Python, ★89) — Message Passing for Hyper-Relational KGs
- **wasita/wasita.github.io** (Svelte) — personal site; pushed 2026-07-20 (most recent across all users)
- **AustinCStone/byteruckus** (HTML) — pushed 2026-07-15
- **AustinCStone/TextGAN** (Python, ★92) — GAN for text generation

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (coin::balance view, 2026-07-21)

| World | Address | Balance (APT) |
|-------|---------|--------------|
| alice | 0xc793...4cc7b | 0.43643352 |
| bob | 0x0a3c...512d5d | **12.65700700** |
| A | 0x8699...e9d7a | 0.05176700 |
| B | 0x3f89...cb13 | 0.03625600 |
| C | 0x38b9...535e | 0.01018500 |
| D | 0xf776...fdd1 | 0.01162900 |
| E | 0xdc1d...d36 | 0.00937200 |
| F | 0x18a1...cf71 | **1.96051600** |
| G | 0x69a3...f32 | 0.00068100 |
| H | 0xce67...300f | 0.00168100 |
| I | 0x070f...fc9 | 0.00068100 |
| J | 0x4d96...f54 | **1.89509300** |
| K | 0xa732...dc4 | 0.16196100 |
| L | 0x7c2e...ba9 | **1.92726900** |
| M | 0x6fed...2e9 | 0.11228500 |
| N | 0xe7dd...b2c | 0.10612100 |
| O | 0x7325...89d | 0.21013600 |
| P | 0x6218...948 | 0.14013600 |
| Q | 0xac40...a9 | 0.10324000 |
| R | 0x7ce6...e10 | 0.09021700 |
| S | 0xb875...386 | 0.09178800 |
| T | 0x3578...588 | 0.07371300 |
| U | 0x7586...956 | 0.05577300 |
| V | 0xb59d...c3 | 0.04883299 |
| W | 0x5f32...b0 | 0.04070500 |
| X | 0xa95c...47d | 0.04257700 |
| Y | 0xd8e3...c4 | 0.04444900 |
| Z | 0x7af0...97c | 0.02426800 |

**Swarm Total: 20.34477251 APT**

Top holders: bob (12.66 APT), F (1.96 APT), L (1.93 APT), J (1.90 APT)

### Multisig Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...003 | 2 | ✅ HEALTHY |
| A-G | 0xf56c...096 | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ff...883 | 2 | ✅ HEALTHY |
| S-T | 0x3b1c...883 | 2 | ✅ HEALTHY |
| V-W | 0x40fa...6d | 2 | ✅ HEALTHY |

All 5 multisig contracts are 2-of-2 and responding healthy.

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** (Vercel deployment protection requires auth). No market data extracted; mnx_snapshots table empty.

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 13+ |
| repo_snapshots | 1,277 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

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
