# World-Increment Sweep + Hamming Snapshot — 2026-03-31

## Sweep Metadata
- **Date:** 2026-03-31
- **Agent:** world-increment-sweep (autonomous two-job sweep)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 324 |
| Total Repo Snapshots | 324 |
| Sources Covered | 3 orgs + 8 users (incl. social graph) |

### GF(3) Distribution

| GF(3) Name | Color | Hex | Trit | Count |
|-----------|-------|-----|------|-------|
| ERGODIC | Pink | `#d3869b` | 0 | 108 |
| PLUS | Yellow-Green | `#b8bb26` | +1 | 108 |
| MINUS | Red | `#cc241d` | -1 | 108 |

GF(3) assignment: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Repo Counts by Source

| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 33 |
| kubeflow | org | 46 | 33,792 |
| TeglonLabs | org | 53 | 6 |
| bmorphism | user | 100 | 132 |
| zubyul | user (social) | 5 | 1 |
| migalkin | user (social) | 5 | 273 |
| AustinCStone | user (social) | 4 | 102 |
| DJedamski | user (social) | 3 | 2 |
| wasita | user (social) | 3 | 1 |
| M1shaaa | user (social) | 3 | 0 |
| kristinezheng | user (social) | 2 | 0 |
| **TOTAL** | | **324** | **34,342** |

### Notable Repos (2026 activity)

- `plurigrid/gorj` — forj + Rama topology nREPL + GF(3) gay trit coloring (pushed 2026-03-30)
- `plurigrid/asi` — topological chemputer, 13 stars (pushed 2026-03-30)
- `zubyul/Gay.jl` — Wide-gamut color sampling with GF(3) trit classification, Julia (pushed 2026-03-28)
- `zubyul/kinesis-kb360pro` — Claude Code skill for Kinesis Advantage360 Pro with Gay.jl analysis (pushed 2026-03-26)
- `bmorphism/zig-syrup-1` — High-performance Zig OCapN Syrup with CapTP optimizations (pushed 2026-03-28)
- `migalkin/NodePiece` — 143 stars, ICLR'22 compositional KG representations
- `AustinCStone/TextGAN` — 92 stars, TF GAN for text generation
- `kubeflow/pipelines` — flagship ML pipeline platform (many stars)
- `TeglonLabs/Stahl` — Scheme interpreter in Rust ("xenoironic Rost")

### API Notes
- GitHub unauthenticated rate limit (60 req/hr) reached during sweep
- Events for bmorphism and zubyul skipped (rate limited); MCP github search used for social graph users

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

Queried via `0x1::coin::balance` view function (CoinStore resource absent on most accounts; fungible asset store used).

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | 0x0a3c00c5... |
| F | 1.960516 | 0x18a14b5b... |
| L | 1.927269 | 0x7c2eaeaf... |
| J | 1.895093 | 0x4d964db8... |
| alice | 0.436434 | 0xc793acde... |
| O | 0.210136 | 0x73252b60... |
| K | 0.161961 | 0xa732040a... |
| P | 0.140136 | 0x62187924... |
| M | 0.112285 | 0x6fed37a7... |
| N | 0.106121 | 0xe7dde6da... |
| Q | 0.103240 | 0xac40fa50... |
| S | 0.091788 | 0xb8753014... |
| R | 0.090217 | 0x7ce605cc... |
| T | 0.073713 | 0x35781dc0... |
| U | 0.055773 | 0x75860da4... |
| A | 0.051767 | 0x8699edc0... |
| V | 0.047833 | 0xb59dd817... |
| Y | 0.044449 | 0xd8e32848... |
| X | 0.042577 | 0xa95cbbd1... |
| W | 0.040705 | 0x5f32aef7... |
| B | 0.036256 | 0x3f892ebe... |
| Z | 0.023268 | 0x7af0ef6e... |
| E | 0.012561 | 0xdc1d9d53... |
| D | 0.011629 | 0xf7765624... |
| C | 0.010185 | 0x38b99e63... |
| G | 0.000681 | 0x69a394c0... |
| H | 0.000681 | 0xce67c327... |
| I | 0.000681 | 0x070fe5d7... |

**Total APT across 28 wallets: ~20.345 APT**  
**Dominant holders:** bob (12.66 APT), F/L/J cluster (~1.9 APT each)

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts return `num_signatures_required = 2` (2-of-N threshold):

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | HEALTHY |
| A-G | 0xf56c4a1c... | 2 | HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | HEALTHY |
| V-W | 0x40fad7b4... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

Status: **SPA_UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA. All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the full HTML shell. No machine-readable REST endpoints found. Recorded as `SPA_UNAVAILABLE` in `mnx_snapshots`.

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
