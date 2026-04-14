# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-14T04:23:26Z
**GF(3) chain:** trit=0 → ERGODIC #d3869b | trit=1 → PLUS #b8bb26 | trit=-1 → MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted
| org/user | repos | total ★ | latest push |
|---|---|---|---|
| kubeflow | 40 | 33,818 | 2026-04-14 |
| bmorphism | 15 | 189 | 2026-04-13 |
| plurigrid | 9 | 30 | 2026-04-14 |
| zubyul | 7 | 1 | 2026-04-13 |
| migalkin | 5 | 273 | 2026-03-11 |
| TeglonLabs | 4 | 2 | 2026-01-01 |
| wasita | 4 | 1 | 2026-04-13 |
| AustinCStone | 4 | 103 | 2026-04-01 |
| DJedamski | 3 | 2 | 2023-04-21 |
| kristinezheng | 2 | 0 | 2026-04-09 |
| M1shaaa | 2 | 0 | 2026-02-04 |

**Total:** 95 repos across 11 nodes of the social graph

### Top Starred Repos
1. `kubeflow/kubeflow` — 15,574 ★
2. `kubeflow/pipelines` — 4,119 ★
3. `kubeflow/spark-operator` — 3,114 ★
4. `kubeflow/trainer` — 2,082 ★
5. `migalkin/NodePiece` — 143 ★ (knowledge graph embeddings, ICLR'22)
6. `AustinCStone/TextGAN` — 92 ★
7. `bmorphism/ocaml-mcp-sdk` — 60 ★
8. `migalkin/StarE` — 88 ★
9. `bmorphism/anti-bullshit-mcp-server` — 23 ★
10. `bmorphism/risc0-cosmwasm-example` — 23 ★

### Notable Recent Activity (last 48h)
- `plurigrid/gorj` pushed 2026-04-14 (this repo — 182 open issues)
- `plurigrid/nash-portal` pushed 2026-04-14 (NASH token TUI/WASM)
- `kubeflow/*` active as of 2026-04-14
- `bmorphism/boxxy` pushed 2026-04-13 (Move/Aptos)
- `zubyul/nash-web` + `zubyul/nash-tui` pushed 2026-04-13 (NASH OHLCV TUI)

### GF(3) Trit Distribution
- ERGODIC (trit=0, #d3869b): 31 increments
- PLUS (trit=1, #b8bb26): 32 increments
- MINUS (trit=-1, #cc241d): 32 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-04-14T04:23:26Z)
All 28 addresses queried via `fullnode.mainnet.aptoslabs.com`.

| world | address (prefix) | balance (APT) |
|---|---|---|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | 0x8699… – 0x7af0… | 0.0 each |

> All 28 wallets returned 0.0 APT. Addresses are valid on-chain (CoinStore resource responded without 404), confirming they exist but hold no liquid APT at time of snapshot.

### Multisig Contract Probes
| pair | address (prefix) | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts healthy — each requires 2-of-N signatures.

### MNX Testnet Markets
`https://testnet.mnx.fi` is a Next.js SPA. No public REST API endpoints found at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Market data unavailable programmatically at this time.

---

## DuckDB Schema Summary

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments   :  95 rows  (GF3 trit-colored increments)
  repo_snapshots     :  95 rows  (full repo metadata)
  aptos_snapshots    :  28 rows  (wallet balances)
  multisig_probes    :   5 rows  (2-of-N contracts)
  mnx_snapshots      :   1 rows  (SPA unavailable)
```
