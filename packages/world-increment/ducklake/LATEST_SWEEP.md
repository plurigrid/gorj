# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-29T14:30:00Z  
**DuckDB:** `world-increments.duckdb` (v1.5.5 Variegata)  
**Sweep IDs:** wi=13–350, rs=474–1271 (this run added 327 increments)

---

## JOB 1: GitHub Social Graph Sweep

### Sources

| Source | Type | Repos | Stars | Open Issues | Latest Push |
|--------|------|------:|------:|------------:|-------------|
| kubeflow | org | 49 | 34,433 | 2,766 | 2026-07-29 |
| bmorphism | user | 100 | 246 | 244 | 2026-07-29 |
| plurigrid | org | 100 | 106 | 1,641 | 2026-07-29 |
| zubyul | user | 49 | 14 | 13 | 2026-07-18 |
| migalkin | user | 19 | 279 | 9 | 2025-08-04 |
| TeglonLabs | org | 5 | 2 | 13 | 2026-06-08 |
| wasita | user | 1 | 1 | 8 | 2026-07-21 |
| kristinezheng | user | 2 | 0 | 0 | 2026-07-01 |
| M1shaaa | user | 1 | 0 | 0 | 2026-07-29 |
| DJedamski | user | 1 | 0 | 0 | 2018-03-07 |
| **Total** | | **327** | **35,081** | **4,694** | |

### Notable Repos (most recently pushed)

- `plurigrid/gorj` — Clojure, 1 ⭐, 1,489 open issues, pushed 2026-07-29 (today!)
- `bmorphism/Gay.jl` — Julia, 2 ⭐, 188 issues, pushed 2026-07-29
- `kubeflow/website` — HTML, 184 ⭐, 21 issues, pushed 2026-07-29
- `kubeflow/community-distribution` — YAML, 1,029 ⭐, 1,070 issues, pushed 2026-07-29
- `M1shaaa/M1shaaa` — profile config, pushed 2026-07-29

### kubeflow Highlights

| Repo | Language | Stars | Issues | Pushed |
|------|----------|------:|-------:|--------|
| kubeflow/kubeflow | — | 15,795 | 0 | 2026-07-10 |
| kubeflow/pipelines | Python | 4,170 | 495 | 2026-07-29 |
| kubeflow/spark-operator | Python | 3,142 | 113 | 2026-07-25 |
| kubeflow/trainer | Go | 2,162 | 127 | 2026-07-27 |
| kubeflow/katib | Python | 1,694 | 107 | 2026-07-26 |
| kubeflow/mcp-server | Python | 31 | 36 | 2026-07-28 |

### bmorphism Highlights

| Repo | Language | Stars | Pushed |
|------|----------|------:|--------|
| bmorphism/Gay.jl | Julia | 2 | 2026-07-29 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 22 | 2026-01-16 |
| bmorphism/shitcoin | Python | 5 | 2026-04-08 |

### plurigrid Highlights

| Repo | Language | Stars | Pushed |
|------|----------|------:|--------|
| plurigrid/gorj | Clojure | 1 | 2026-07-29 |
| plurigrid/zig-syrup | Zig | 2 | 2026-07-28 |
| plurigrid/asi | HTML | 54 | 2026-07-10 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |

### TeglonLabs Repos

| Repo | Language | Stars | Description |
|------|----------|------:|-------------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps |
| mathpix-gem | Ruby | 2 | Mathematical image→LaTeX OCR |
| coin-flip-mcp | JavaScript | 0 | MCP server for randomness from random.org |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | |

### GF(3) Color Chain Distribution (this run)

| Trit | Color | Name | Count |
|------|-------|------|------:|
| 0 | #d3869b | ERGODIC | 109 |
| 1 | #b8bb26 | PLUS | 109 |
| 2 | #cc241d | MINUS | 109 |

GF(3) chain rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` for  
`0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger v6513306650.  
These accounts are uninitialized or use the Fungible Asset (FA) framework instead of the legacy CoinStore.

**All balances recorded as 0.0 APT.**

### Multisig Contract Probes (5 pairs)

| Pair | Address | Sigs Required | Healthy |
|------|---------|:-------------:|:-------:|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✅ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✅ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✅ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✅ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✅ |

All 5 multisig contracts responded and require 2-of-N signatures. **All healthy.**

### MNX Markets (testnet.mnx.fi)

testnet.mnx.fi is a Next.js SPA. No REST/JSON API endpoints found at:
- `/api/markets` → returns HTML SPA shell
- `/api/v1/markets` → returns HTML SPA shell
- `/markets` → returns HTML SPA shell

**Status: unavailable** — market data not extractable without browser execution.

---

## DuckDB Table Summary

| Table | Rows (total) | This Run |
|-------|-------------:|---------:|
| world_increments | 350 | +338 |
| repo_snapshots | 1,271 | +798 |
| aptos_snapshots | 28 | +28 |
| multisig_probes | 5 | +5 |
| mnx_snapshots | 1 | +1 |

---

## Schema Reference

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
