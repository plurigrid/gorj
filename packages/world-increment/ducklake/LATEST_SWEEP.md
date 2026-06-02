# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-02

## Sweep Metadata
- **Date:** 2026-06-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph (zubyul) | 5 |
| DJedamski | social graph (zubyul) | 2 |
| wasita | social graph (zubyul) | 5 |
| kristinezheng | social graph (zubyul) | 2 |
| M1shaaa | social graph (zubyul) | 2 |
| AustinCStone | social graph (zubyul) | 4 |
| **Total** | | **321** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 107 |
| +1 | `#b8bb26` | PLUS | 107 |
| −1 | `#cc241d` | MINUS | 107 |

GF(3) conservation holds: 321 = 3 × 107, Σ trits ≡ 0 (mod 3).

### Top Repos by Stars

| Org/User | Repo | Stars | Language | Last Push |
|----------|------|-------|----------|-----------|
| kubeflow | kubeflow | 15702 | — | 2026-05-24 |
| kubeflow | pipelines | 4151 | Python | 2026-06-02 |
| kubeflow | spark-operator | 3125 | Python | 2026-06-01 |
| kubeflow | trainer | 2110 | Go | 2026-06-02 |
| kubeflow | katib | 1685 | Python | 2026-05-29 |
| migalkin | NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone | TextGAN | 92 | Python | 2025-03-03 |
| migalkin | StarE | 89 | Python | 2026-04-16 |
| migalkin | kgcourse2021 | 25 | HTML | 2026-02-16 |
| AustinCStone | StereoVisionMRF | 11 | Python | 2026-04-01 |

### Recent Activity Highlights (2026 YTD)

**bmorphism** (870+ commits since 2026-01-01):
- `plurigrid/nash-portal`: deterministic color sigil substitution via SplitMix64/HSL — NASH→◆ #E23C36, Plurigrid→⬡ #E25936
- `bmorphism/Gay.jl`: GF(3) Σ≡0 chirality color-discipline; positioned as "Camp C" (Smith et al. 2023 aperiodic monotile)
- `plurigrid/zig-syrup`: zigbjj 6-iteration loop — Zig 0.16.0 migration, OCapN parity harness, 1528/1528 tests
- `bmorphism/boxxy`: stellogen Go resolution engine, SplitMix64 SPI fuzzing, PLT layers (flix/gorard/stellogen/alea), GF(3) conservation across all layers
- `bmorphism/oxgame`: political legitimacy markers under `.topos/`, GF(3)/CE/entropy stack; OxCaml 5.2.0+ox CONTRIBUTING

**zubyul** (221+ commits since 2026-01-01):
- `plurigrid/place`: BCI Factory hardware — fNIRS ECU gerber fix (JLCPCB QA), copper zone fill, IRB device coverage matrix (28 devices, 4 risk tiers)
- `plurigrid/bci-blue-share`: ratzilla TUI-in-browser + oscilloscope native binary
- `plurigrid/nanoclj-zig`: Zig 0.16.0 pin + CI matrix (ubuntu+macos), ObjectMap unmanaged migration
- `plurigrid/asi`: 41 custom skills from 306-session provenance audit; 5 Pump SDK skills
- `zubyul/voice-observatory`: xfxfxf Pearl Level-2 do() intervention SCM viewer (11-node causal model)
- `plurigrid/nash-portal`: production deploy gating (2-of-2 admin review, environment approvals, tag rulesets)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com` with 1s sleep between calls.

**Result:** All 28 wallets returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~5,537,019,652. The addresses are registered on-chain but have not initialized APT coin stores (unfunded / no APT received).

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (26) | (see DB) | 0.0 each |

**Total Hamming Swarm APT: 0.0**

### Multisig Contract Probes (Mainnet)

All 5 probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts healthy — uniform 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `/api/markets` → HTTP 404; root serves a Next.js SPA requiring wallet authentication before market data renders. No static market data extractable.

---

## DuckDB Schema

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments   (321 rows) — GF(3)-colored increment log
├── repo_snapshots     (321 rows) — GitHub repo metadata
├── aptos_snapshots     (28 rows) — Hamming swarm wallet balances
├── multisig_probes      (5 rows) — Multisig contract health checks
└── mnx_snapshots        (1 row)  — MNX market probe (unavailable)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=−1, color=`#cc241d`, name=MINUS
