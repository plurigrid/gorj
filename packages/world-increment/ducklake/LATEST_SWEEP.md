# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-08T UTC  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 6 |
| M1shaaa | user (social) | 5 |
| AustinCStone | user (social) | 30 |
| **Total** | | **377** |

### Highlights by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15626 | — |
| kubeflow/pipelines | 4136 | Python |
| kubeflow/spark-operator | 3124 | Python |
| kubeflow/trainer | 2096 | Go |
| kubeflow/manifests | 1015 | YAML |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |
| AustinCStone/TextGAN | 92 | Python |
| plurigrid/ontology | 7 | JavaScript |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/babashka-mcp-server | 18 | JavaScript |
| plurigrid/nanoclj-zig | 1 | Zig (GF3 trit conservation!) |

### Notable Recent Activity (pushed 2026)

- `plurigrid/zig-syrup` (2026-04-30) — OCapN Syrup in Zig
- `plurigrid/nanoclj-zig` (2026-04-25) — NaN-boxed Clojure in Zig, GF(3) trit conservation
- `plurigrid/graded-optic` (2026-02-08) — Semiring-graded optics in Haskell
- `TeglonLabs/mathpix-gem` (2026-01-01) — Mathematical OCR in Ruby
- `bmorphism/Gay.jl` (2026-05-08) — Wide-gamut color sampling, 187 open issues!
- `M1shaaa/M1shaaa` (2026-05-08) — Profile updated today
- `kubeflow/trainer` (2026-05-08) — Distributed AI training on K8s
- `wasita/wasita.github.io` (2026-04-28) — Personal website (Svelte)
- `kristinezheng/kristinezheng.github.io` (2026-04-09) — Portfolio

### GF(3) Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 132 |
| +1 | #b8bb26 | PLUS | 134 |
| -1 | #cc241d | MINUS | 134 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 wallets probed via Aptos fullnode mainnet API.  
**Result: All wallets return 0.0 APT** — no `CoinStore<AptosCoin>` resource found.  
These addresses are registered in the swarm topology but have not received mainnet APT.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793ac...24cc7b | 0.0 |
| bob | 0x0a3c00...12d5d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-N threshold confirmed).

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4f4...87003 | 2 | ✓ |
| A-G | 0xf56c4a...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1...b883 | 2 | ✓ |
| S-T | 0x3b1c3a...7883 | 2 | ✓ |
| V-W | 0x40fad7...eb6d | 2 | ✓ |

All contracts require **2-of-N** signatures — standard 2-party multisig topology confirmed.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — `testnet.mnx.fi` serves a Next.js SPA with no public REST API endpoint.  
Paths probed: `/`, `/api/markets`, `/api/v1/markets` — all return HTML shell.  
No market data extractable without JavaScript execution.

---

## Database Summary

```
world_increments : 400 rows  (GF3 color-chained repo events)
repo_snapshots   : 1321 rows (org/user × repo metadata)
aptos_snapshots  :   28 rows (Hamming swarm wallet balances)
multisig_probes  :    5 rows (2-of-N contracts)
mnx_snapshots    :    1 row  (unavailable marker)
```

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
