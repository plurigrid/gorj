# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-11

## Sweep Metadata
- **Date:** 2026-05-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 48 | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 4 | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 6 | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita | user | 4 | +1 | `#b8bb26` | **PLUS** |
| 8  | kristinezheng | user | 4 | -1 | `#cc241d` | **MINUS** |
| 9  | AustinCStone | user | 4 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 3 | +1 | `#b8bb26` | **PLUS** |
| 11 | DJedamski | user | 3 | -1 | `#cc241d` | **MINUS** |

**Total: 325 repo snapshots across 3 orgs + 8 users**

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Top Repos by Stars

| Repo | Language | Stars | Forks | Pushed |
|------|----------|-------|-------|--------|
| kubeflow/kubeflow | — | 15,630 | 2,648 | 2026-05-07 |
| kubeflow/pipelines | Python | 4,138 | 1,990 | 2026-05-11 |
| kubeflow/spark-operator | Python | 3,125 | 1,480 | 2026-05-08 |
| kubeflow/trainer | Go | 2,097 | 948 | 2026-05-09 |
| kubeflow/katib | Python | 1,683 | 522 | 2026-05-09 |
| kubeflow/arena | Go | 810 | 190 | 2026-05-07 |
| kubeflow/kale | Python | 684 | 156 | 2026-05-11 |
| migalkin/NodePiece | Python | 144 | 21 | 2026-05-07 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2025-03-03 |
| migalkin/StarE | Python | 89 | 16 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 7 | 2026-01-16 |
| plurigrid/asi | HTML | 21 | 5 | 2026-04-26 |

### Notable Activity (2026-05-11)
- **plurigrid/gorj** (Clojure) — 152 open issues, pushed today — this very repo
- **kubeflow/kale** + **kubeflow/blog** + **kubeflow/hub** — pushed today (active ML ecosystem)
- **bmorphism/Gay.jl** — 188 open issues, Julia, pushed 2026-05-11
- **zubyul/voice-observatory** — macOS TUI for voice-download pathways, 2026-04-24
- **plurigrid/zig-syrup** + **bmorphism/zig-syrup** — OCapN Syrup pair, pushed 2026-04-30

### Note on GitHub API Access
Unauthenticated REST API rate-limited (60 req/hour). All org/user queries
routed through authenticated GitHub MCP server. Social graph user repos
(migalkin, wasita, kristinezheng, AustinCStone, M1shaaa, DJedamski) captured
via MCP search (top N per user shown; inline sample stored for social graph nodes).

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Wallets (alice, bob, A–Z)

Queried `fullnode.mainnet.aptoslabs.com/v1` for
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` with 1s sleep between calls.

**All 28 wallets: 0.00000000 APT**

Accounts exist on mainnet (no 404 errors) but hold zero APT balance.
These appear to be freshly provisioned addresses awaiting funding.

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...35e | 0.0 |
| D | 0xf776...dd1 | 0.0 |
| E | 0xdc1d...d36 | 0.0 |
| F | 0x18a1...f71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...00f | 0.0 |
| I | 0x070f...c9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...a9 | 0.0 |
| M | 0x6fed...e9 | 0.0 |
| N | 0xe7dd...c2 | 0.0 |
| O | 0x7325...9d | 0.0 |
| P | 0x6218...48 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...10 | 0.0 |
| S | 0xb875...86 | 0.0 |
| T | 0x3578...88 | 0.0 |
| U | 0x7586...56 | 0.0 |
| V | 0xb59d...c3 | 0.0 |
| W | 0x5f32...b0 | 0.0 |
| X | 0xa95c...7d | 0.0 |
| Y | 0xd8e3...c4 | 0.0 |
| Z | 0x7af0...7c | 0.0 |

### Multisig Contract Probes — 5 Pairs

All probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | **2** | ✓ |
| A-G | 0xf56c...0096 | **2** | ✓ |
| Y-Z | 0xd3ff...b883 | **2** | ✓ |
| S-T | 0x3b1c...7883 | **2** | ✓ |
| V-W | 0x40fa...eb6d | **2** | ✓ |

**All 5 multisig contracts healthy — uniform 2-of-N threshold.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA ("The AI Exchange"). CSP header reveals
backend at `api.testnet.mnx.fi` + `wss://api.testnet.mnx.fi`.
All REST paths probed (`/markets`, `/tickers`, `/api/markets`, `/v1/markets`, etc.)
return `Cannot GET /path` — Express server with no public REST surface.
Market data requires WebSocket subscription or authenticated session.

**Status: UNAVAILABLE — `mnx_snapshots` table empty.**

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 11 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)            -- 325 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy) -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS
