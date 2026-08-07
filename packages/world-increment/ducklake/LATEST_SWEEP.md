# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-07  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| wasita | user (zubyul graph) | 14 |
| kristinezheng | user (zubyul graph) | 5 |
| M1shaaa | user (zubyul graph) | 8 |
| AustinCStone | user (zubyul graph) | 30 |
| DJedamski | user (zubyul graph) | 6 |

**Total unique repos:** 385  
**GF(3) distribution:** ERGODIC (#d3869b) 129, PLUS (#b8bb26) 129, MINUS (#cc241d) 127

### Notable Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | — | 2026-07-10 |
| kubeflow/pipelines | 4,181 | Python | 2026-08-07 |
| kubeflow/spark-operator | 3,145 | Python | 2026-08-06 |
| kubeflow/trainer | 2,173 | Go | 2026-08-07 |
| kubeflow/katib | 1,694 | Python | 2026-08-06 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

### Most Recently Active

- `kubeflow/pipelines` pushed 2026-08-07
- `kubeflow/trainer` pushed 2026-08-07
- `M1shaaa/M1shaaa` pushed 2026-08-07
- `wasita/xoxowasita-analysis` pushed 2026-08-06

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets)

All 28 wallets (`alice`, `bob`, `A`–`Z`) returned **0.0 APT** balance.  
The Aptos mainnet fullnode API responded successfully but the CoinStore resource value is `"0"` for all addresses. These accounts either hold no liquid APT or the coin resource is uninitialized.

**Total APT across swarm:** 0.000000

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

All 5 multisig contracts are live, healthy, and require **2-of-N** signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable (SPA only)**  
`testnet.mnx.fi` is a Next.js single-page application. REST API paths tried:
- `/api/markets` → returns SPA HTML
- `/api/v1/markets` → returns SPA HTML  
- `/api/tickers` → returns SPA HTML

No JSON market data accessible without browser execution. Noted as `unavailable` in `mnx_snapshots` table.

---

## DuckDB Tables Summary

| Table | Rows | Notes |
|-------|------|-------|
| `world_increments` | 385 | GF(3) color-coded repo events |
| `repo_snapshots` | 385 | Full repo metadata |
| `aptos_snapshots` | 28 | alice, bob, A–Z wallets |
| `multisig_probes` | 5 | A-B, A-G, Y-Z, S-T, V-W |
| `mnx_snapshots` | 1 | Placeholder (SPA unavailable) |
