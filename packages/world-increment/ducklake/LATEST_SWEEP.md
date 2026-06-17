# World-Increment Sweep — 2026-06-17

DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain — World Increments

| id | source | type | trit | color | name | snapshot_hash |
|----|--------|------|------|-------|------|---------------|
| 1 | TeglonLabs | org | +1 | #b8bb26 | PLUS | 54efcfc1ed630530 |
| 2 | DJedamski | user | -1 | #cc241d | MINUS | 42500f75e7906266 |
| 3 | wasita | user | 0 | #d3869b | ERGODIC | 152894ba26ce5669 |
| 4 | kristinezheng | user | +1 | #b8bb26 | PLUS | 75309c56ff75a8f4 |
| 5 | M1shaaa | user | -1 | #cc241d | MINUS | 39f884d7df7d7a58 |
| 6 | migalkin | user | 0 | #d3869b | ERGODIC | d933cf1f8c548845 |
| 7 | AustinCStone | user | +1 | #b8bb26 | PLUS | 0ec12000210231f3 |
| 8 | plurigrid | org | -1 | #cc241d | MINUS | 9472ce68c0750b5a |
| 9 | kubeflow | org | 0 | #d3869b | ERGODIC | 1213045d87643ce8 |
| 10 | bmorphism | user | +1 | #b8bb26 | PLUS | ffb406b4f6ac4f91 |
| 11 | zubyul | user | -1 | #cc241d | MINUS | dbd577d6fa9863a2 |

GF(3) legend: ERGODIC (#d3869b, trit=0), PLUS (#b8bb26, trit=+1), MINUS (#cc241d, trit=-1)

---

## GitHub Social Graph Sweep

**Total repo snapshots:** 107 across 11 sources  
(orgs: plurigrid, kubeflow, TeglonLabs; users: bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)

| source | repos | total_stars | last_pushed |
|--------|-------|-------------|-------------|
| kubeflow | 10 | 30,121 | 2026-06-17 |
| migalkin | 19 | 280 | 2025-08-04 |
| bmorphism | 10 | 176 | 2026-06-17 |
| AustinCStone | 6 | 104 | 2026-02-11 |
| plurigrid | 15 | 81 | 2026-06-17 |
| zubyul | 12 | 5 | 2026-04-24 |
| wasita | 11 | 5 | 2026-06-15 |
| DJedamski | 6 | 3 | 2018-03-07 |
| TeglonLabs | 5 | 2 | 2026-06-08 |
| kristinezheng | 5 | 0 | 2026-06-07 |
| M1shaaa | 8 | 0 | 2026-06-17 |

Notable repos:
- `kubeflow/kubeflow` — 15,726 stars, ML platform
- `migalkin/NodePiece` — 144 stars, relational graph rep learning (ICLR'22)
- `bmorphism/ocaml-mcp-sdk` — 61 stars, OCaml MCP SDK
- `AustinCStone/TextGAN` — 92 stars, text generation GAN
- `plurigrid/gorj` — MCP server + REPL hooks for AI coding agents (active 2026-06-17)
- `TeglonLabs/jank-crane` — C++ converged-IR hub (active 2026-06-08)

---

## Hamming Swarm Snapshot — Aptos Mainnet

**Wallet balances queried:** 28 addresses (alice, bob, A–Z)  
**All balances:** 0.0 APT (CoinStore resource absent — unfunded accounts)

| world | address (truncated) | APT |
|-------|---------------------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...12d5 | 0.0 |
| A–Z | (26 addresses) | 0.0 |

### Multisig Probes (Aptos mainnet)

| pair | address (truncated) | sigs_required | healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...883 | 2 | true |
| S-T | 0x3b1c...883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

All 5 multisig contracts report `num_signatures_required = 2`.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active.  
Both `/api/markets` and `/api/v1/markets` returned authentication walls. No market data captured.

---

## DuckDB Schema

```sql
world_increments  (id, timestamp, gf3_trit, gf3_color, gf3_name, source_type,
                   source_name, event_type, repo_name, actor, snapshot_hash)
repo_snapshots    (id, timestamp, increment_id, org_or_user, repo_name, full_name,
                   language, stars, forks, open_issues, pushed_at, description)
aptos_snapshots   (timestamp, world, address, balance_apt)
multisig_probes   (timestamp, pair, address, sigs_required, healthy)
mnx_snapshots     (timestamp, ticker, name, category, price, change_pct)
```

---

*Sweep generated: 2026-06-17 | Branch: world-increment/sweep-2026-06-17*
