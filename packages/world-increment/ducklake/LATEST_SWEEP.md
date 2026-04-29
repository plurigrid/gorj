# World-Increment Sweep — 2026-04-29

## Sweep Metadata
- **Date:** 2026-04-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

### GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (gorj) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

### Top Repos by Stars

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,565 | — | 2026-01-05 |
| kubeflow/pipelines | 4,119 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-10 |
| kubeflow/trainer | 2,080 | Go | 2026-04-10 |
| kubeflow/katib | 1,676 | Python | 2026-04-02 |
| migalkin/NodePiece | 143 | Python | — |
| migalkin/StarE | 88 | Python | — |
| AustinCStone/TextGAN | 92 | Python | — |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml | — |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | — |
| plurigrid/asi | 16 | HTML | 2026-04-10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-04-29)

**Total swarm APT:** 20.34477251 APT

| World | Address (short) | APT Balance |
|-------|----------------|-------------|
| bob | 0x0a3c…512d | **12.65700700** |
| F | 0x18a1…cf71 | 1.96051600 |
| L | 0x7c2e…eba9 | 1.92726900 |
| J | 0x4d96…7f54 | 1.89509300 |
| alice | 0xc793…cc7b | 0.43643352 |
| K | 0xa732…dc4 | 0.16196100 |
| O | 0x7325…89d | 0.21013600 |
| P | 0x6218…948 | 0.14013600 |
| M | 0x6fed…f2e9 | 0.11228500 |
| N | 0xe7dd…1b2c | 0.10612100 |
| Q | 0xac40…89a9 | 0.10324000 |
| S | 0xb875…386 | 0.09178800 |
| R | 0x7ce6…6e10 | 0.09021700 |
| T | 0x3578…588 | 0.07371300 |
| U | 0x7586…956 | 0.05577300 |
| A | 0x8699…9d7a | 0.05176700 |
| X | 0xa95c…047d | 0.04257700 |
| Y | 0xd8e3…44c4 | 0.04444900 |
| V | 0xb59d…f2c3 | 0.04883299 |
| W | 0x5f32…c7b0 | 0.04070500 |
| B | 0x3f89…cb13 | 0.03625600 |
| Z | 0x7af0…97c | 0.02426800 |
| D | 0xf776…fdd1 | 0.01162900 |
| C | 0x38b9…535e | 0.01018500 |
| E | 0xdc1d…8d36 | 0.00937200 |
| H | 0xce67…300f | 0.00168100 |
| G | 0x69a3…f32 | 0.00068100 |
| I | 0x070f…1fc9 | 0.00068100 |

### Multisig Probes (5/5 healthy)

| Pair | Address (short) | Sigs Required | Healthy |
|------|----------------|---------------|---------|
| A-B | 0x0da4…7003 | 2/2 | ✓ |
| A-G | 0xf56c…0096 | 2/2 | ✓ |
| Y-Z | 0xd3ff…883 | 2/2 | ✓ |
| S-T | 0x3b1c…883 | 2/2 | ✓ |
| V-W | 0x40fa…eb6d | 2/2 | ✓ |

All 5 multisig accounts require 2-of-N signatures. All respond healthy.

### MNX Markets (testnet.mnx.fi)

**Status: SPA only — REST API unavailable.**

The site serves a Next.js SPA. The backend at `api.testnet.mnx.fi` does not expose REST market endpoints at `/markets`, `/v1/markets`, or `/api/markets`. Data is served via WebSocket (`wss://api.testnet.mnx.fi`) which requires browser auth (Privy/WalletConnect). No market data captured.

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
