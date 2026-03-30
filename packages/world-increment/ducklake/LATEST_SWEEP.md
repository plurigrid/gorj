# World-Increment Sweep — 2026-03-30

## Sweep Metadata
- **Date:** 2026-03-30
- **Agent:** world-increment-sweep v2 (GitHub Social Graph + Hamming Swarm)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 (one per source) |
| Total Repo Snapshots | 678 rows (538 unique) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA — no API |

---

## GitHub Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 93 |
| kubeflow | org | 46 |
| TeglonLabs | org | 3 |
| bmorphism | user | 97 (10 sampled in detail) |
| zubyul | user | 44 (5 public sampled) |
| migalkin | user | 19 |
| DJedamski | user | 6 |
| wasita | user | 9 |
| kristinezheng | user | 6 |
| M1shaaa | user | 8 |
| AustinCStone | user | 40 |

---

## Top 5 Most Recently Pushed Repos

| Repo | Pushed At | Stars |
|------|-----------|-------|
| plurigrid/gorj | 2026-03-30T10:22:55Z | 0 |
| plurigrid/horse | 2026-03-30T10:12:23Z | 0 |
| kubeflow/pipelines | 2026-03-30T04:01:09Z | 4113 |
| kubeflow/dashboard | 2026-03-30T03:22:52Z | 16 |
| kubeflow/mcp-apache-spark-history-server | 2026-03-29T04:29:55Z | 0 |

---

## Aptos Wallet Balances

All 28 addresses queried against Aptos mainnet fullnode (`fullnode.mainnet.aptoslabs.com`).
All returned 0.0 APT (accounts not found on mainnet CoinStore resource, or zero balance).

| Label | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

---

## Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.
All healthy, all require **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | YES |
| A-G | 0xf56c...096 | 2 | YES |
| Y-Z | 0xd3ff...883 | 2 | YES |
| S-T | 0x3b1c...883 | 2 | YES |
| V-W | 0x40fa...b6d | 2 | YES |

---

## MNX Markets Status

**Status: SPA / API Unavailable**

All three endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) on `testnet.mnx.fi`
returned an HTML Next.js single-page application response (HTTP 200, Content-Type: text/html).
No JSON API is publicly accessible. No market data was captured.

---

## GF(3) Color Chain Summary

11 world_increment rows, one per GitHub source, cycling through GF(3) trit color chain:

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1 | plurigrid | 1 | #b8bb26 | PLUS |
| 2 | kubeflow | 2 | #cc241d | MINUS |
| 3 | TeglonLabs | 0 | #d3869b | ERGODIC |
| 4 | bmorphism | 1 | #b8bb26 | PLUS |
| 5 | zubyul | 2 | #cc241d | MINUS |
| 6 | migalkin | 0 | #d3869b | ERGODIC |
| 7 | DJedamski | 1 | #b8bb26 | PLUS |
| 8 | wasita | 2 | #cc241d | MINUS |
| 9 | kristinezheng | 0 | #d3869b | ERGODIC |
| 10 | M1shaaa | 1 | #b8bb26 | PLUS |
| 11 | AustinCStone | 2 | #cc241d | MINUS |

Pattern: `PLUS(+1) → MINUS(-1) → ERGODIC(0) → PLUS → MINUS → ERGODIC → ...`

Assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Notable Highlights
- **kubeflow/pipelines**: 4,113 stars — most active ML pipeline (pushed 2026-03-30)
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — top bmorphism MCP repo
- **bmorphism/say-mcp-server**: 20 stars — macOS TTS via MCP
- **migalkin/NodePiece**: 143 stars — top social graph user repo
- **AustinCStone/TextGAN**: 92 stars — GAN for text generation in TensorFlow
- **plurigrid/gorj**: This very repo — active as of 2026-03-30T10:22:55Z
