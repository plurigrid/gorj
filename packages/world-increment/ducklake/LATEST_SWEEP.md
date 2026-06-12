# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-06-12  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Total ★ |
|--------|------|------:|--------:|
| kubeflow | org | 48 | 34,196 |
| migalkin | user (social) | 6 | 279 |
| bmorphism | user | 100 | 247 |
| AustinCStone | user (social) | 5 | 106 |
| plurigrid | org | 100 | 77 |
| zubyul | user | 49 | 14 |
| wasita | user (social) | 5 | 4 |
| TeglonLabs | org | 5 | 2 |
| DJedamski | user (social) | 4 | 2 |
| kristinezheng | user (social) | 3 | 0 |
| M1shaaa | user (social) | 3 | 0 |
| **Total** | | **328** | **34,927** |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | `#d3869b` | ERGODIC | 109 |
| +1 | `#b8bb26` | PLUS | 110 |
| -1 | `#cc241d` | MINUS | 109 |

### Notable Repos

- **kubeflow/kubeflow** — ML platform (kubeflow org dominates with 34k+ stars)
- **migalkin/NodePiece** — 144 stars; Knowledge Graph representations (ICLR'22)
- **migalkin/StarE** — 89 stars; Hyper-relational KG message passing (EMNLP'20)
- **AustinCStone/TextGAN** — 92 stars; TF text generation GAN
- **TeglonLabs/jank-crane** — GF3 convergence maps, simonw workflow (C++, pushed 2026-06-08)
- **TeglonLabs/mathpix-gem** — Ruby mathpix gem (2 stars, 11 open issues)
- **plurigrid** — 100 repos; active AI/infra org
- **bmorphism** — 100 repos; active contributor

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com`.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|-------------:|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
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
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...b2c | 0.0 |
| O | 0x7325...89d | 0.0 |
| P | 0x6218...948 | 0.0 |
| Q | 0xac40...a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...386 | 0.0 |
| T | 0x3578...588 | 0.0 |
| U | 0x7586...956 | 0.0 |
| V | 0xb59d...2c3 | 0.0 |
| W | 0x5f32...7b0 | 0.0 |
| X | 0xa95c...47d | 0.0 |
| Y | 0xd8e3...4c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

**Result:** All 28 addresses returned 0 APT. These addresses have no registered
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on mainnet (unregistered/unfunded).

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|:-------------:|:-------:|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

**Result:** All 5 multisig contracts are healthy 2-of-2 multisigs.

### MNX Markets

`https://testnet.mnx.fi` returned **HTTP 401** on all probed paths. The testnet SPA requires
authentication. **Status: unavailable** — no market data captured; `mnx_snapshots` table is empty.

---

## DuckDB Tables

```
world_increments   328 rows  — GF3-tagged repo events
repo_snapshots     328 rows  — full repo metadata per source
aptos_snapshots     28 rows  — wallet balance snapshot (all 0 APT)
multisig_probes      5 rows  — 2-of-2 healthy contracts
mnx_snapshots        0 rows  — unavailable (auth required)
```

### Sample Queries

```sql
-- Top repos by stars
SELECT full_name, language, stars FROM repo_snapshots ORDER BY stars DESC LIMIT 10;

-- GF3 chain view
SELECT gf3_color, gf3_name, repo_name, source_name FROM world_increments ORDER BY id LIMIT 10;

-- Aptos balances
SELECT world, balance_apt FROM aptos_snapshots ORDER BY world;

-- Multisig health
SELECT pair, sigs_required, healthy FROM multisig_probes;
```
