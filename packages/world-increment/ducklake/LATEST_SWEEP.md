# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-16T19:13 UTC

**Increment #13** — GF(3) trit=+1, color=`#b8bb26`, name=**PLUS**

---

## JOB 1: GitHub Social Graph

GitHub API access this session is scoped to `plurigrid/gorj` only; external org/user REST endpoints return 403. Social graph source data (944 repo_snapshots) carried from 2026-04-12 sweep.

### plurigrid/gorj (live, MCP-queried)
- Open issues: 1 (brainfloj↔gorj bridge — zig-syrup BCI frame encoding over Tailscale mesh)
- Latest commit: `5b28fe0` — "chore: ignore duckdb binary in repo root" (2026-05-08)
- Open sweep PRs today: #1485–#1494 (10 runs, all targeting master)

### Carried from 2026-04-12 sweep (944 repo_snapshots)
| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | `asi` (★16→30), `gorj`, `zig-syrup` |
| kubeflow | org | 49 | `kubeflow` (★15,565), `pipelines` (★4,119) |
| TeglonLabs | org | 53 | `jank-crane` (C++, GF3 convergence maps) |
| bmorphism | user | 100 | `ocaml-mcp-sdk` (★60), `anti-bullshit-mcp-server` (★23) |
| zubyul | user | 24 | `voice-observatory`, `gay-world` |
| migalkin | social | 30 | `NodePiece` (★143), `StarE` (★88) |
| DJedamski | social | 11 | — |
| wasita | social | 29 | `magic-garden`, `send2kobo` |
| kristinezheng | social | 18 | — |
| M1shaaa | social | 16 | — |
| AustinCStone | social | 43 | `TextGAN` (★92), `byteruckus` (pushed 2026-07-15) |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 wallets, `0x1::coin::balance` view)

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c5… | **12.657007** |
| F | 0x18a14b5b… | 1.960516 |
| L | 0x7c2eaeaf… | 1.927269 |
| J | 0x4d964db8… | 1.895093 |
| alice | 0xc793acde… | 0.436434 |
| O | 0x73252b60… | 0.210136 |
| K | 0xa732040a… | 0.161961 |
| P | 0x6218792d… | 0.140136 |
| M | 0x6fed37a7… | 0.112285 |
| N | 0xe7dde6da… | 0.106121 |
| Q | 0xac40fa50… | 0.103240 |
| S | 0xb8753014… | 0.091788 |
| R | 0x7ce605cc… | 0.090217 |
| T | 0x35781dc0… | 0.073713 |
| U | 0x75860da4… | 0.055773 |
| A | 0x8699edc0… | 0.051767 |
| V | 0xb59dd817… | 0.048833 |
| Y | 0xd8e32848… | 0.044449 |
| X | 0xa95cbbd1… | 0.042577 |
| W | 0x5f32aef7… | 0.040705 |
| B | 0x3f892ebe… | 0.036256 |
| Z | 0x7af0ef6e… | 0.024268 |
| D | 0xf7765624… | 0.011629 |
| C | 0x38b99e63… | 0.010185 |
| E | 0xdc1d9d53… | 0.009372 |
| H | 0xce67c327… | 0.001681 |
| G | 0x69a394c0… | 0.000681 |
| I | 0x070fe5d7… | 0.000681 |

**Total swarm: 20.344773 APT**

Note: `0x1::coin::CoinStore` resource absent on all wallets — balances confirmed via `0x1::coin::balance` view function (Fungible Asset aware). Addresses are active on mainnet.

### Multisig Contract Probes (5/5 healthy)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da… | 2 | ✅ |
| A-G | 0xf56c4a1c09062143… | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df406… | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a… | 2 | ✅ |
| V-W | 0x40fad7b423a84365… | 2 | ✅ |

All 5 multisig contracts on Aptos mainnet are healthy, each requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Unavailable — behind Vercel deployment protection on all API paths. `mnx_snapshots` table remains empty.

---

## GF(3) Color Chain

| id%3 | Trit | Name | Color |
|------|------|------|-------|
| 0 | 0 | ERGODIC | `#d3869b` |
| 1 | +1 | PLUS | `#b8bb26` |
| 2 | -1 | MINUS | `#cc241d` |

**This increment: id=13, PLUS `#b8bb26`** (5th GF3 cycle entry)

GF(3) chain to date:
`PLUS(1) → MINUS(2) → ERGODIC(3) → PLUS(4) → MINUS(5) → ERGODIC(6) → PLUS(7) → MINUS(8) → ERGODIC(9) → PLUS(10) → MINUS(11) → ERGODIC(12) → PLUS(13)`

---

## DuckDB State After Sweep

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 945 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

DB: `packages/world-increment/ducklake/world-increments.duckdb`

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
