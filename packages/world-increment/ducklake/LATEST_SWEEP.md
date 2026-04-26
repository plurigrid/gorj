# World-Increment Sweep + Hamming Swarm Snapshot

**Generated:** 2026-04-26 00:41 UTC  
**Branch:** world-increment/sweep-2026-04-26-0041  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary
- **World increments recorded:** 44
- **Repo snapshots:** 1244
- **Sources scanned:** orgs (plurigrid, kubeflow, TeglonLabs) + users (bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone)
- **Events captured:** bmorphism (30 recent public), zubyul (30 recent public)

### GF(3) Color Chain Distribution
```
┌──────────┬───────────┬───────┐
│ gf3_name │ gf3_color │ count │
│ varchar  │  varchar  │ int64 │
├──────────┼───────────┼───────┤
│ ERGODIC  │ #d3869b   │    14 │
│ MINUS    │ #cc241d   │    15 │
│ PLUS     │ #b8bb26   │    15 │
└──────────┴───────────┴───────┘
```
- **ERGODIC** (#d3869b): id%3==0, trit=0
- **PLUS** (#b8bb26): id%3==1, trit=+1
- **MINUS** (#cc241d): id%3==2, trit=-1

### Repos by Source
```
┌───────────────┬───────┐
│  org_or_user  │ repos │
│    varchar    │ int64 │
├───────────────┼───────┤
│ plurigrid     │   300 │
│ bmorphism     │   200 │
│ TeglonLabs    │   159 │
│ kubeflow      │   141 │
│ AustinCStone  │   129 │
│ migalkin      │    90 │
│ wasita        │    60 │
│ zubyul        │    48 │
│ M1shaaa       │    48 │
│ kristinezheng │    36 │
│ DJedamski     │    33 │
└───────────────┴───────┘
  11 rows     2 columns
```

### Top Languages
```
┌──────────────────┬───────┐
│     language     │   n   │
│     varchar      │ int64 │
├──────────────────┼───────┤
│ Python           │   214 │
│ Go               │    51 │
│ HTML             │    49 │
│ Rust             │    43 │
│ JavaScript       │    36 │
│ Jupyter Notebook │    32 │
│ TypeScript       │    32 │
│ Jsonnet          │    24 │
└──────────────────┴───────┘
```

### Event Activity
- **bmorphism:** 30 recent events — all `PullRequestEvent` on plurigrid/gorj
- **zubyul:** 30 recent events — mix of `CreateEvent`, `PullRequestEvent`, `PushEvent` on plurigrid/gorj

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets)

All 28 addresses (alice, bob, A–Z) queried via `fullnode.mainnet.aptoslabs.com`.  
**Result:** All wallets have 0 APT — `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.  
These are uninitialized Hamming swarm wallets on mainnet (no APT deposited yet).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z | 0x86...→0x7af0... | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts are **healthy** — 2-of-N signatures required.

```
┌─────────┬────────────────────────────────────────────────────────────────────┬───────────────┬─────────┐
│  pair   │                              address                               │ sigs_required │ healthy │
│ varchar │                              varchar                               │     int32     │ boolean │
├─────────┼────────────────────────────────────────────────────────────────────┼───────────────┼─────────┤
│ A-B     │ 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 │             2 │ true    │
│ A-G     │ 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 │             2 │ true    │
│ Y-Z     │ 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 │             2 │ true    │
│ S-T     │ 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 │             2 │ true    │
│ V-W     │ 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d │             2 │ true    │
└─────────┴────────────────────────────────────────────────────────────────────┴───────────────┴─────────┘
```

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c...0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c...7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa...eb6d | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — All API paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/pairs`) return 404.  
The site is a Next.js SPA; market data not exposed via REST API on testnet. Recorded as `N/A` in `mnx_snapshots`.

---

## DuckDB Schema

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 44 | GF(3) color-coded event log |
| repo_snapshots | 1244 | GitHub repo metadata |
| aptos_snapshots | 28 | Wallet balances (APT) |
| multisig_probes | 5 | Multisig contract health |
| mnx_snapshots | 1 | MNX market data (unavailable) |

---

*Sweep automation: world-increment-sweep + hamming-swarm-snapshot agent*
