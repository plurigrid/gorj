# World-Increment Sweep + Hamming Swarm Snapshot

**Run:** 2026-07-23T15:10:30Z  
**DuckDB:** `world-increments.duckdb`  
**GF(3) Chain:**  
- Increment 12 → trit=0 `#d3869b` **ERGODIC** (GitHub sweep)  
- Increment 13 → trit=1 `#b8bb26` **PLUS** (Aptos snapshot)

---

## Job 1: GitHub Social Graph Sweep

**Scope note:** GH MCP access for this session is restricted to `plurigrid/gorj`. Broad org/user repo queries are outside the authorized scope. All 11 targets are recorded in `repo_snapshots` as metadata entries.

| Source Type | Name | Status |
|------------|------|--------|
| org | plurigrid | scope-limited |
| org | kubeflow | scope-limited |
| org | TeglonLabs | scope-limited |
| user | bmorphism | scope-limited |
| user | zubyul | scope-limited |
| user | migalkin | scope-limited |
| user | DJedamski | scope-limited |
| user | wasita | scope-limited |
| user | kristinezheng | scope-limited |
| user | M1shaaa | scope-limited |
| user | AustinCStone | scope-limited |

> **Action needed:** Extend GH MCP scope to include these orgs/users to enable full crawl.

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on **mainnet**. None of the Hamming swarm wallets hold a funded APT coin store on Aptos mainnet.

**Possible causes:**
- Wallets are on testnet/devnet but queried against mainnet
- Addresses were never funded / coin store not initialized

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts are live. Every pair requires **2 signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f4... | 2 | yes |
| A-G | 0xf56c4a... | 2 | yes |
| Y-Z | 0xd3ffe1... | 2 | yes |
| S-T | 0x3b1c3a... | 2 | yes |
| V-W | 0x40fad7... | 2 | yes |

### MNX Markets (testnet.mnx.fi)

All probed API paths return a 46 KB HTML SPA shell — no REST endpoints exposed.  
Status: **unavailable / SPA-only** (paths tried: `/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v1/tickers`)

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 2 |
| repo_snapshots | 11 |
| aptos_snapshots | 0 (no funded wallets) |
| multisig_probes | 5 |
| mnx_snapshots | 1 (unavailable marker) |

---

## Action Items

1. **Aptos wallets**: Verify network (mainnet vs testnet) for Hamming swarm addresses
2. **GitHub sweep**: Widen MCP scope to enable full social-graph crawl
3. **MNX Markets**: Obtain internal API docs or WebSocket endpoint for market data
