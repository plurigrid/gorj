# World-Increment Sweep + Hamming Snapshot — 2026-06-23

## Sweep Metadata
- **Date:** 2026-06-23
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept (this run)

| Source | Type | Repos This Run |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| AustinCStone | social graph | 30 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **TOTAL** | | **381** |

### GF(3) Color Chain Distribution (this run: 381 increments)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 127 |
| +1 | PLUS | #b8bb26 | 127 |
| -1 | MINUS | #cc241d | 127 |

GF(3) chain: `PLUS → MINUS → ERGODIC → ...` cycling 127 complete triples.

### Notable Repos

- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08): crane-jank converged-IR hub — loopify pass spec, GF3 convergence maps, simonw workflow
- **TeglonLabs/mathpix-gem** (Ruby, ★2, pushed 2026-01-01): LaTeX/SMILES/markdown mathematical OCR gem
- **kristinezheng/kristinezheng.github.io** (HTML, pushed 2026-06-07): personal site active
- **M1shaaa/M1shaaa** (GitHub profile, pushed 2026-06-23 — today): active today
- **wasita/wasita.github.io** (Svelte, pushed 2026-06-15): personal website at wasita.space

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | social graph | 30 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 11 |
| M1shaaa | social graph | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | social graph | 5 |
| DJedamski | social graph | 6 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 wallets queried against Aptos mainnet (`fullnode.mainnet.aptoslabs.com`).

| World | Balance (APT) | Note |
|-------|--------------|------|
| alice | 0.0 | CoinStore absent or zero |
| bob | 0.0 | CoinStore absent or zero |
| A–Z (26) | 0.0 each | CoinStore absent or zero |

**Summary:** All 28 Hamming swarm addresses report 0 APT balance on Aptos mainnet. The CoinStore resource is either absent (address never initialized) or holds zero balance.

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✅ healthy |
| A-G | 0xf56c4a1c...bc0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ffe181...75b883 | 2 | ✅ healthy |
| S-T | 0x3b1c3ae9...ed7883 | 2 | ✅ healthy |
| V-W | 0x40fad7b4...80eb6d | 2 | ✅ healthy |

**All 5 multisig accounts are live 2-of-2 on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

**Status:** UNAVAILABLE — Vercel deployment protection active on testnet.mnx.fi. Authentication token required (see Vercel bypass docs). No market data extractable without credentials.

---

## DuckDB Tables (cumulative including prior runs)

| Table | Total Rows |
|-------|-----------|
| world_increments | 404+ |
| repo_snapshots | 1325+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (N/A placeholder) |

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
