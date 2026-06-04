# World-Increment Sweep + Hamming Snapshot

**Swept:** 2026-05-03T23:31:17Z  
**GF(3) color chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 100 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 10 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 42 |
| **TOTAL** | | **391** |

### Top Repos by Stars

| Org/User | Repo | Stars | Language | Last Pushed |
|----------|------|-------|----------|-------------|
| kubeflow | kubeflow | 15,619 | — | 2026-04-29 |
| kubeflow | pipelines | 4,131 | Python | 2026-05-01 |
| kubeflow | spark-operator | 3,111 | Python | 2026-04-10 |
| kubeflow | trainer | 2,096 | Go | 2026-05-01 |
| kubeflow | katib | 1,678 | Python | 2026-04-14 |
| kubeflow | examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow | manifests | 1,014 | YAML | 2026-04-30 |
| kubeflow | arena | 810 | Go | 2026-04-28 |
| kubeflow | kale | 683 | Python | 2026-04-13 |
| TeglonLabs | mathpix-gem | 2 | Ruby | 2026-01-01 |

### TeglonLabs Repos

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| mathpix-gem | Ruby | 2 | Mathematical image-to-LaTeX OCR |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | — |
| coin-flip-mcp | JavaScript | 0 | Coin flip via random.org |

### DuckDB ducklake

- **File:** `packages/world-increment/ducklake/world-increments.duckdb`
- **world_increments:** 389 rows (GF3-tagged)
- **repo_snapshots:** 389 deduplicated snapshots

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet.  
**Result:** All addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — balance = **0 APT** for each.  
This indicates these are unfunded or non-existent accounts on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0 |
| bob | 0x0a3c...2d5d | 0 |
| A–Z | (26 addrs) | 0 each |

### Multisig Contract Probes (Aptos mainnet)

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✅ |
| A-G | 0xf56c...0096 | 2 | ✅ |
| Y-Z | 0xd3ff...b883 | 2 | ✅ |
| S-T | 0x3b1c...7883 | 2 | ✅ |
| V-W | 0x40fa...eb6d | 2 | ✅ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable via API** — `testnet.mnx.fi` is a Next.js SPA. The `/api/markets` and `/api/tickers` endpoints returned no JSON data; the site renders client-side. No market data extractable without browser execution.

---

## GF(3) Chain Summary

```
id%3==0 → trit=0  ERGODIC  #d3869b  (136 increments)
id%3==1 → trit=1  PLUS     #b8bb26  (138 increments)
id%3==2 → trit=-1 MINUS    #cc241d  (138 increments)
```

Total world-increment events: **412** (389 repo snapshots + 28 Aptos + 5 multisig)
