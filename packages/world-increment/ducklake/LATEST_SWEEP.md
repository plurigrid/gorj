# World-Increment Sweep + Hamming Snapshot

**Generated:** 2026-07-27T22:12Z  
**Branch:** `world-increment/sweep-2026-07-27-2212`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Status |
|--------|------|--------|
| plurigrid | org | ✅ 50 repos captured |
| kubeflow | org | ⚠️ scope-restricted (prior run data in DB) |
| TeglonLabs | org | ⚠️ scope-restricted |
| bmorphism | user | ⚠️ scope-restricted |
| zubyul | user | ⚠️ scope-restricted |
| Social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) | users | ⚠️ scope-restricted |

*Note: GitHub API in this session is scoped to `plurigrid/gorj`. Direct API calls for other orgs/users were denied. Data for kubeflow and others visible in DB is from prior sweeps.*

### Plurigrid Repos — Most Recently Pushed

| Repo | Language | Stars | Pushed |
|------|----------|-------|--------|
| plurigrid/gorj | Clojure | 1 | 2026-07-27 |
| plurigrid/asi | HTML | 52 | 2026-07-10 |
| plurigrid/place | TeX | 1 | 2026-07-14 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| plurigrid/shrimp | — | 0 | 2026-07-03 |

### Plurigrid — Top by Stars

| Repo | Language | Stars | Description |
|------|----------|-------|-------------|
| plurigrid/asi | HTML | 52 | everything is topological chemputer! |
| plurigrid/asi-skills | Julia | 3 | 69 skills w/ Galois Hole Type accessibility |
| plurigrid/nash-portal | Rust | 2 | NASH token TUI in the browser |
| plurigrid/zig-syrup | Zig | 2 | High-performance Zig OCapN Syrup |
| plurigrid/gorj | Clojure | 1 | forj + Rama topology nREPL routing |

### GF(3) Color Chain Distribution

| Trit | Color | Name | Increments This Run |
|------|-------|------|---------------------|
| 0 | #d3869b | ERGODIC | 24 |
| 1 | #b8bb26 | PLUS | 25 |
| -1 | #cc241d | MINUS | 24 |

### DuckDB Cumulative Totals

| Table | Rows |
|-------|------|
| world_increments | 73 |
| repo_snapshots | 994 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com` (1s sleep between calls).

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|----------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B | 0x3f892e... | 0.0 |
| C | 0x38b99e... | 0.0 |
| D | 0xf77656... | 0.0 |
| E | 0xdc1d9d... | 0.0 |
| F | 0x18a14b... | 0.0 |
| G | 0x69a394... | 0.0 |
| H | 0xce67c3... | 0.0 |
| I | 0x070fe5... | 0.0 |
| J | 0x4d964d... | 0.0 |
| K | 0xa73204... | 0.0 |
| L | 0x7c2eae... | 0.0 |
| M | 0x6fed37... | 0.0 |
| N | 0xe7dde6... | 0.0 |
| O | 0x73252b... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa... | 0.0 |
| R | 0x7ce605... | 0.0 |
| S | 0xb87530... | 0.0 |
| T | 0x35781d... | 0.0 |
| U | 0x75860d... | 0.0 |
| V | 0xb59dd8... | 0.0 |
| W | 0x5f32ae... | 0.0 |
| X | 0xa95cbb... | 0.0 |
| Y | 0xd8e328... | 0.0 |
| Z | 0x7af0ef... | 0.0 |

*All addresses return 0 APT — CoinStore<AptosCoin> resource uninitialized or zero balance on mainnet.*

### Multisig Contract Probes

All 5 probes successful via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`.

| Pair | Contract Address (prefix) | Sigs Required | Status |
|------|--------------------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ healthy |
| A-G | 0xf56c4a... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✅ healthy |
| S-T | 0x3b1c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7... | 2 | ✅ healthy |

**All 5 multisig contracts healthy — 2-of-N threshold confirmed across the entire swarm.**

### MNX Testnet Markets

`https://testnet.mnx.fi` is a Next.js SPA. All API paths (`/api/markets`, `/api/tickers`, `/api/v1/tickers`, `/api/orderbook`, `/api/stats`, `/api/v2/markets`, `/v1/markets`) return the HTML shell — no REST endpoint is publicly accessible without browser JS execution. **Status: UNAVAILABLE** — no data inserted into `mnx_snapshots`.

---

## Notes

- DuckDB: `packages/world-increment/ducklake/world-increments.duckdb`
- GF(3) chain: `id%3` → 0=ERGODIC(#d3869b), 1=PLUS(#b8bb26), 2=MINUS(#cc241d)
- Aptos RPC: `https://fullnode.mainnet.aptoslabs.com/v1`
- GitHub session scope: restricted to `plurigrid/gorj`; other org/user queries blocked by proxy
