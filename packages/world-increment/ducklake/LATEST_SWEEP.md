# World-Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-08-04T21:11 UTC  
**Increment ID:** 1 (this run) | **GF(3):** trit=+1 · color=#b8bb26 · name=**PLUS**

---

## JOB 1: GitHub Social Graph Sweep

### Scope Note
GitHub API access in this session is proxy-scoped to `plurigrid/gorj` only. External orgs (kubeflow, TeglonLabs), users (bmorphism, zubyul), and social-graph users (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) were blocked by proxy with 403. Only `plurigrid` org repos were snapshotted via the GitHub MCP server.

### Plurigrid Org — 100 Repos Snapshotted

**Top by stars (this sweep):**

| Repo | Language | Stars | Forks | Issues | Last Pushed |
|------|----------|-------|-------|--------|-------------|
| plurigrid/asi | HTML | 58 | 13 | 4 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |
| plurigrid/act | Python | 3 | 1 | 4 | 2024-07-26 |
| plurigrid/asi-skills | Julia | 3 | 0 | 0 | 2026-04-26 |
| plurigrid/Plurigraph | JavaScript | 3 | 5 | 4 | 2025-01-05 |
| plurigrid/zig-syrup | Zig | 2 | 2 | 0 | 2026-07-28 |
| plurigrid/nash-portal | Rust | 2 | 2 | 1 | 2026-05-19 |
| plurigrid/gorj | Clojure | 1 | 0 | 1632 | 2026-08-04 |
| *(92 more in repo_snapshots table)* | | | | | |

**Most recently pushed:** `gorj` (2026-08-04) · `eirobri` (2026-08-04) · `zig-syrup` (2026-07-28)  
**Highest open issues:** `gorj` (1632) · `eirobri` (31) · `nanoclj-zig` (20) · `ontology` (16) · `place` (15)

### DuckDB Tables Updated
- `world_increments` — 1 sweep record (id=1, GF3 PLUS #b8bb26)
- `repo_snapshots` — 100 rows inserted (cumulative total: 1044)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger v~6.6B)

All 28 addresses queried. All returned `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>`. These accounts likely use the Fungible Asset (FA) standard post-migration rather than the legacy CoinStore module.

| Label | Address prefix | Balance APT (CoinStore) |
|-------|---------------|-------------------------|
| alice | 0xc793acde... | 0.0 (resource_not_found) |
| bob   | 0x0a3c00c5... | 0.0 (resource_not_found) |
| A     | 0x8699edc0... | 0.0 (resource_not_found) |
| B     | 0x3f892ebe... | 0.0 (resource_not_found) |
| C     | 0x38b99e63... | 0.0 (resource_not_found) |
| D     | 0xf7765624... | 0.0 (resource_not_found) |
| E     | 0xdc1d9d53... | 0.0 (resource_not_found) |
| F     | 0x18a14b5b... | 0.0 (resource_not_found) |
| G     | 0x69a394c0... | 0.0 (resource_not_found) |
| H     | 0xce67c327... | 0.0 (resource_not_found) |
| I     | 0x070fe5d7... | 0.0 (resource_not_found) |
| J     | 0x4d964db8... | 0.0 (resource_not_found) |
| K     | 0xa732040a... | 0.0 (resource_not_found) |
| L     | 0x7c2eaeaf... | 0.0 (resource_not_found) |
| M     | 0x6fed37a7... | 0.0 (resource_not_found) |
| N     | 0xe7dde6da... | 0.0 (resource_not_found) |
| O     | 0x73252b60... | 0.0 (resource_not_found) |
| P     | 0x62187920... | 0.0 (resource_not_found) |
| Q     | 0xac40fa50... | 0.0 (resource_not_found) |
| R     | 0x7ce605cc... | 0.0 (resource_not_found) |
| S     | 0xb8753014... | 0.0 (resource_not_found) |
| T     | 0x35781dc0... | 0.0 (resource_not_found) |
| U     | 0x75860da4... | 0.0 (resource_not_found) |
| V     | 0xb59dd817... | 0.0 (resource_not_found) |
| W     | 0x5f32aef7... | 0.0 (resource_not_found) |
| X     | 0xa95cbbd1... | 0.0 (resource_not_found) |
| Y     | 0xd8e32848... | 0.0 (resource_not_found) |
| Z     | 0x7af0ef6e... | 0.0 (resource_not_found) |

> **Note:** CoinStore queries return 0 for accounts using the FA standard. Consider querying `0x1::fungible_asset::FungibleStore` to check actual balances.

### Multisig Contract Health — 5/5 HEALTHY

All 5 multisig contracts responded via `0x1::multisig_account::num_signatures_required`. All require 2-of-N signatures.

| Pair | Address prefix | Sigs Required | Status |
|------|---------------|---------------|--------|
| A-B  | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G  | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z  | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T  | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W  | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` responds HTTP 200 with HTML (SPA). No JSON REST API endpoints found at: `/api/markets`, `/api/v1/markets`, `/api/tickers`. Market data requires JS execution; marked **unavailable** in `mnx_snapshots`.

---

## Cumulative DuckDB State

```
world_increments:  1 rows  (this run)
repo_snapshots:    1044 rows  (cumulative)
aptos_snapshots:   28 rows  (this run)
multisig_probes:   5 rows  (this run, all healthy)
mnx_snapshots:     1 rows  (unavailable marker)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Flags / Anomalies

1. **GitHub scope restriction** — proxy blocks API beyond `plurigrid/gorj`; kubeflow, TeglonLabs, bmorphism, zubyul social graph not snapshotted this run.
2. **Aptos CoinStore 0 balances** — all 28 addresses return `resource_not_found`; likely FA-standard post-migration. Consider `0x1::fungible_asset::FungibleStore` queries next run.
3. **MNX testnet SPA** — no machine-readable API; would need headless browser to extract market data.
4. **All multisigs healthy** — 2-of-N confirmed on all 5 contracts (A-B, A-G, Y-Z, S-T, V-W).
