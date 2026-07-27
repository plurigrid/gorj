# World-Increment Sweep + Hamming Snapshot — 2026-07-27

## Sweep Metadata
- **Date:** 2026-07-27 08:11 UTC
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) Increment:** id≈12 (next) · trit=1 · color=`#b8bb26` · name=**PLUS**

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 945 |
| Sources Covered | 11 orgs/users (historical) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

**Session constraint:** GitHub direct API (`api.github.com`) returned 403 via proxy.  
MCP tools scoped to `plurigrid/gorj` only. Historical data (945 repo snapshots across 11 orgs/users) preserved from prior sweeps.

**plurigrid/gorj live state:**
- Master HEAD: `5b28fe0` — chore: ignore duckdb binary (2026-05-08)
- 50+ active `world-increment/sweep-*` branches
- Latest sweep branch: `world-increment/sweep-2026-05-02-1318`

**Historical repo highlights (from prior sweeps):**

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | asi (16★), ontology (7★) |
| bmorphism | user | 100 | ocaml-mcp-sdk (60★), anti-bullshit-mcp-server (23★) |
| TeglonLabs | org | 53 | vibespace, mcp-terminal |
| kubeflow | org | 47 | kubeflow (15565★), pipelines (4119★) |
| AustinCStone | user | 43 | TextGAN (92★) |
| migalkin | user | 30 | NodePiece (143★), StarE (88★) |
| wasita | user | 29 | — |
| zubyul | user | 24 | — |
| kristinezheng | user | 18 | — |
| M1shaaa | user | 16 | — |
| DJedamski | user | 11 | — |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets probed via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
**No CoinStore resource found on any wallet — all balances: 0.00 APT.**

| World | Address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793…cc7b | 0.00 |
| bob   | 0x0a3c…2d5d | 0.00 |
| A–Z   | (26 addresses)      | 0.00 each |

**Total APT across all 28 wallets: 0.00 APT**

---

### Multisig Contract Probes (Aptos Mainnet)

Probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B  | 0x0da4…7003 | 2 | HEALTHY |
| A-G  | 0xf56c…0096 | 2 | HEALTHY |
| Y-Z  | 0xd3ff…b883 | 2 | HEALTHY |
| S-T  | 0x3b1c…7883 | 2 | HEALTHY |
| V-W  | 0x40fa…eb6d | 2 | HEALTHY |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed.**

---

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA (dark theme). API endpoints (`/api/markets`,  
`/api/v1/markets`, `/api/tickers`) return the HTML shell, not JSON.  
**Status: UNAVAILABLE** — no public REST API surface accessible.

---

## GF(3) Color Chain

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

Current increment: **PLUS** `#b8bb26`

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
