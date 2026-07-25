# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-25

## Sweep Metadata
- **Date:** 2026-07-25
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 174 |
| Total Repo Snapshots | 174 |
| Sources Covered | 3 orgs + 3 users + 6 social graph |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Distribution (174 increments = 3 × 58)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 58 |
| +1 | `#b8bb26` | PLUS | 58 |
| -1 | `#cc241d` | MINUS | 58 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| social_graph (migalkin/DJedamski/wasita/kristinezheng/M1shaaa/AustinCStone) | users | 24 |
| bmorphism | user | 20 |
| zubyul | user | 13 |
| kubeflow | org | 12 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **174** |

### Top Repos by Stars (2026-07-25 snapshot)

| Repo | Language | Stars | Updated |
|------|----------|-------|---------|
| kubeflow/kubeflow | — | 15,792 | 2026-07-24 |
| kubeflow/pipelines | Python | 4,169 | 2026-07-24 |
| kubeflow/spark-operator | Python | 3,143 | 2026-07-23 |
| kubeflow/trainer | Go | 2,153 | 2026-07-24 |
| kubeflow/katib | Python | 1,692 | 2026-07-20 |
| kubeflow/community-distribution | YAML | 1,029 | 2026-07-23 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| bmorphism/anti-bullshit-mcp-server | JS | 22 | 2026-07-12 |
| plurigrid/asi | HTML | 31 | 2026-07-17 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-21 |

### plurigrid Most Recently Active
- `plurigrid/asi` — HTML, 31 ⭐ (pushed 2026-07-17)
- `plurigrid/gorj` — Clojure, 1 ⭐ (this repo, pushed 2026-07-07)
- `plurigrid/shrimp` — (pushed 2026-07-03)
- `plurigrid/place` — TeX, 1 ⭐ (pushed 2026-06-27)

### bmorphism Most Recently Active
- `bmorphism/Gay.jl` — Julia (wide-gamut color sampling, SPI pattern, 2026-07-21)
- `bmorphism/gay-chat` — Scheme (gay://chat Spritely Brassica, 2026-07-14)
- `bmorphism/anti-bullshit-mcp-server` — JS (epistemic validation MCP, 2026-07-12)

### TeglonLabs Repos (5 captured)
- `TeglonLabs/jank-crane` — C++ (crane-jank converged-IR hub, GF3 convergence maps, loopify pass spec)
- `TeglonLabs/mathpix-gem` — Ruby, 2 ⭐ (mathematical OCR)
- `TeglonLabs/coin-flip-mcp` — JavaScript (MCP coin flip with random.org)
- `TeglonLabs/monad-mcp-server` — Monad MCP Server
- `TeglonLabs/topoi` — Python

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

All 28 Hamming swarm addresses (alice, bob, A–Z) returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,442,697,603. Accounts have not been initialized with an APT CoinStore on mainnet.

**Total swarm APT:** 0.00000000 across all 28 worlds

### Multisig Contract Probes (5 pairs)

All 5 contracts responded via `0x1::multisig_account::num_signatures_required`. **All healthy.**

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2-of-2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2-of-2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2-of-2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2-of-2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2-of-2 | ✓ |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA — no public REST API found at `/api/markets` or `/api/v1/markets`. All paths return the HTML shell only. **MNX market data unavailable** (requires browser-side execution; no accessible JSON endpoint).

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
