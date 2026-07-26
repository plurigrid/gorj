# World Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-07-26 UTC  
**GF(3) color chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources queried
| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| kubeflow | org | 49 | 34,414 |
| migalkin | user (social) | 5 | 275 |
| bmorphism | user | 100 | 246 |
| AustinCStone | user (social) | 4 | 106 |
| plurigrid | org | 100 | 84 |
| zubyul | user | 49 | 14 |
| wasita | user (social) | 4 | 3 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user (social) | 3 | 2 |
| M1shaaa | user (social) | 3 | 0 |
| kristinezheng | user (social) | 3 | 0 |
| **Total** | | **325** | **35,146** |

### Notable repos (this sweep)
- **TeglonLabs/jank-crane** (C++, pushed 2026-06-08) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **migalkin/NodePiece** (Python, 144 stars) — Compositional KG representations (ICLR'22)
- **AustinCStone/TextGAN** (Python, 92 stars) — GAN for text generation in TensorFlow
- **wasita/wasita.github.io** (Svelte, pushed 2026-07-21) — personal website, active
- **wasita/pnas-typst-template** (pushed 2026-07-16) — newest repo in social graph
- **AustinCStone/byteruckus** (HTML, pushed 2026-07-15) — newest AustinCStone repo

### DuckDB state after this sweep
- `world_increments`: 348 rows (325 new + 23 prior)
- `repo_snapshots`: 1,269 rows (325 new + 944 prior)
- GF(3) distribution this sweep: ERGODIC=116, PLUS=116, MINUS=116 (perfectly balanced)

### GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger v6461665451)

All 28 wallets (alice, bob, A–Z) returned **resource_not_found** for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. These accounts do not hold APT via the legacy Coin module — they are either unfunded or use the Fungible Asset (FA) standard.

All 28 rows stored with `balance_apt = 0.0`.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B–Z | (25 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** — `num_signatures_required = 2` for each.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

### MNX Markets (testnet.mnx.fi)

**Unavailable** — `testnet.mnx.fi` is a Next.js SPA. No JSON API endpoint is exposed; market data must be fetched client-side via JavaScript. `mnx_snapshots` table remains empty (0 rows).

---

## DuckDB Schema Reference

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

## Full DuckDB Table Row Counts

| Table | Rows |
|-------|------|
| world_increments | 348 |
| repo_snapshots | 1,269 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |
