# LATEST_SWEEP — 2026-07-11T13:12:40Z

## World-Increment Social Graph Sweep + Hamming Swarm Snapshot

Generated: 2026-07-11T13:12:40Z  
GF(3) color chain: trit=0 ERGODIC #d3869b | trit=1 PLUS #b8bb26 | trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

**Total repos snapshotted this run: 292**

| Source | Repos | Stars |
|--------|-------|-------|
| plurigrid | 300 | 162 |
| bmorphism | 200 | 262 |
| kubeflow | 143 | 102064 |
| AustinCStone | 126 | 324 |
| TeglonLabs | 111 | 14 |
| zubyul | 97 | 40 |
| migalkin | 79 | 833 |
| wasita | 71 | 11 |
| kristinezheng | 41 | 0 |
| M1shaaa | 40 | 0 |
| DJedamski | 28 | 17 |

### Notable Activity
- **kubeflow** (org): 143 repos, 102064 total stars
- **bmorphism** (user): 200 repos, 262 total stars  
- **plurigrid** (org): 300 repos, 162 total stars
- **TeglonLabs** (org): jank-crane (C++, GF3 IR hub, pushed 2026-06-08), mathpix-gem (Ruby, 2 stars)
- **M1shaaa** (user): M1shaaa profile repo pushed 2026-07-11 (today)
- **wasita** (user): wasita.github.io (Svelte, pushed 2026-07-06)
- **kristinezheng** (user): kristinezheng.github.io (HTML, pushed 2026-07-01)

### DuckDB Tables
- `world_increments` — GF(3) tagged event chain
- `repo_snapshots` — full repo metadata per push event

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, ledger ~6.2B)

**Total APT across 28 wallets: 20.3448 APT**

> Note: Wallets use fungible_asset model (coin::CoinStore not registered); queried via `0x1::coin::balance` view function.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c58fdf9020b2... | 12.6570 |
| F | 0x18a14b5b4bec118c1c... | 1.9605 |
| L | 0x7c2eaeafad9725492e... | 1.9273 |
| J | 0x4d964db8f538374034... | 1.8951 |
| alice | 0xc793acdec12b4a6371... | 0.4364 |
| O | 0x73252b6011a75115a2... | 0.2101 |
| K | 0xa732040a6b0d559041... | 0.1620 |
| P | 0x6218792de4a9bc3891... | 0.1401 |
| M | 0x6fed37a7553ef16b2a... | 0.1123 |
| N | 0xe7dde6da0a65f51062... | 0.1061 |
| Q | 0xac40fa50b81b4ca6b1... | 0.1032 |
| S | 0xb8753014e4888ea48a... | 0.0918 |
| R | 0x7ce605cc8fda4f8e4a... | 0.0902 |
| T | 0x35781dc0e42fef3f25... | 0.0737 |
| U | 0x75860da47565f6509b... | 0.0558 |
| A | 0x8699edc0960dd5b916... | 0.0518 |
| V | 0xb59dd8170321dfab5a... | 0.0488 |
| Y | 0xd8e32848f1dffa811b... | 0.0444 |
| X | 0xa95cbbd116548ac990... | 0.0426 |
| W | 0x5f32aef70f5ba530d3... | 0.0407 |
| B | 0x3f892ebe6e45164e63... | 0.0363 |
| Z | 0x7af0ef6e1bd706f4b3... | 0.0243 |
| D | 0xf77656248f64d5dd00... | 0.0116 |
| C | 0x38b99e63ada9b6fef1... | 0.0102 |
| E | 0xdc1d9d533bac3507f9... | 0.0094 |
| H | 0xce67c327a7844e5488... | 0.0017 |
| G | 0x69a394c0b0ac842127... | 0.0007 |
| I | 0x070fe5d74e4eda30e2... | 0.0007 |

### Top 5 by Balance
- **bob**: 12.6570 APT (0x0a3c00c58fdf9020b27854...)
- **F**: 1.9605 APT (0x18a14b5b4bec118c1cc029...)
- **L**: 1.9273 APT (0x7c2eaeafad9725492e4f46...)
- **J**: 1.8951 APT (0x4d964db8f5383740341946...)
- **alice**: 0.4364 APT (0xc793acdec12b4a63717b00...)

### Multisig Contract Probes

All 5 multisig pairs probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f... | 2 | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f... | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df40622... | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49... | 2 | HEALTHY |
| V-W | 0x40fad7b423a843650f... | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — testnet.mnx.fi returns HTTP 401 (Vercel authentication required). No market data retrievable without auth credentials.

---

## DuckDB Schema Summary

```
packages/world-increment/ducklake/world-increments.duckdb
├── world_increments   — GF(3) trit/color/name per repo event
├── repo_snapshots     — org, name, language, stars, forks, pushed_at
├── aptos_snapshots    — world label, address, balance_apt
├── multisig_probes    — pair, address, sigs_required, healthy
└── mnx_snapshots      — unavailable this run
```

---
*Sweep agent: world-increment-sweep + hamming-swarm-snapshot*  
*Timestamp: 2026-07-11T13:12:40Z*
