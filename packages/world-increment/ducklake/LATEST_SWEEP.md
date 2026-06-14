# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep date:** 2026-06-14  
**GF(3) Increment:** #13 — trit=1 PLUS `#b8bb26`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| kubeflow | org | 48 | 34,208 | 2026-06-14 |
| migalkin | user (social) | 19 | 280 | 2026-05-28 |
| bmorphism | user | 100 | 247 | 2026-06-14 |
| AustinCStone | user (social) | 40 | 108 | 2026-04-01 |
| plurigrid | org | 100 | 77 | 2026-06-14 |
| zubyul | user | 49 | 14 | 2026-04-24 |
| wasita | user (social) | 11 | 5 | 2026-06-01 |
| DJedamski | user (social) | 6 | 3 | 2023-04-21 |
| TeglonLabs | org | 5 | 2 | 2026-06-08 |
| kristinezheng | user (social) | 5 | 0 | 2026-06-07 |
| M1shaaa | user (social) | 8 | 0 | 2026-02-04 |

**Total new repo snapshots this sweep: 391**  
**Cumulative repo_snapshots: 1,335**

### Notable Repos (Top by Stars)
- `kubeflow/kubeflow` — 15,721 ⭐
- `kubeflow/pipelines` — 4,154 ⭐ (Python)
- `kubeflow/spark-operator` — 3,127 ⭐ (Python)
- `kubeflow/trainer` — 2,115 ⭐ (Go)
- `kubeflow/katib` — 1,683 ⭐ (Python)
- `migalkin/NodePiece` — 144 ⭐ (Python, ICLR'22 knowledge graphs)
- `migalkin/StarE` — 89 ⭐ (Python, EMNLP 2020 hyper-relational KGs)
- `AustinCStone/TextGAN` — 92 ⭐ (Python, text GAN in TensorFlow)
- `TeglonLabs/jank-crane` — C++, crane-jank converged-IR hub with GF3 convergence maps (pushed 2026-06-08)

### Recent Activity (Active in Last 30 Days)
- **plurigrid**: pushed to `plurigrid/asi` (HTML, 26⭐) on 2026-06-14 — "everything is topological chemputer!"
- **bmorphism**: latest push 2026-06-14
- **kubeflow**: latest push 2026-06-14T11:54:36Z
- **TeglonLabs/jank-crane**: GF3 loopify pass spec, created 2026-06-08

### Events
- bmorphism public events: rate-limited (no GitHub auth token)
- zubyul public events: rate-limited (no GitHub auth token)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses returned `resource_not_found` from Aptos mainnet fullnode. The addresses do not have an initialized `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource — consistent with wallets that have never received APT on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…cc7b | not found |
| bob | 0x0a3c…2d5d | not found |
| A | 0x8699…9d7a | not found |
| B | 0x3f89…b13 | not found |
| C | 0x38b9…35e | not found |
| D | 0xf776…dd1 | not found |
| E | 0xdc1d…d36 | not found |
| F | 0x18a1…f71 | not found |
| G | 0x69a3…f32 | not found |
| H | 0xce67…00f | not found |
| I | 0x070f…c9 | not found |
| J | 0x4d96…f54 | not found |
| K | 0xa732…dc4 | not found |
| L | 0x7c2e…ba9 | not found |
| M | 0x6fed…e9 | not found |
| N | 0xe7dd…b2c | not found |
| O | 0x7325…89d | not found |
| P | 0x6218…948 | not found |
| Q | 0xac40…89a9 | not found |
| R | 0x7ce6…e10 | not found |
| S | 0xb875…386 | not found |
| T | 0x3578…588 | not found |
| U | 0x7586…956 | not found |
| V | 0xb59d…2c3 | not found |
| W | 0x5f32…b0 | not found |
| X | 0xa95c…47d | not found |
| Y | 0xd8e3…4c4 | not found |
| Z | 0x7af0…97c | not found |

### Multisig Contract Probes

All 5 multisig contracts are **HEALTHY** — all require 2-of-N signatures.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection requiring authentication. API paths `/api/markets` and `/api/v1/markets` return auth gates. No market data could be extracted.

---

## DuckDB Ducklake State

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 1,335 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

**GF(3) Color Chain:**
- trit=0 ERGODIC `#d3869b` (id%3==0)
- trit=1 PLUS `#b8bb26` (id%3==1) ← **this sweep (#13)**
- trit=-1 MINUS `#cc241d` (id%3==2)

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
