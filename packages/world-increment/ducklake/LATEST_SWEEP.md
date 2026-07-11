# Latest Sweep — 2026-07-11

## Summary

| Metric | Value |
|--------|-------|
| Sweep date | 2026-07-11 |
| World increments (total) | 25 |
| Repo snapshots (total) | 945 |
| Aptos wallet probes | 28 |
| Multisig probes | 5 |
| MNX Markets | Unavailable (401 Unauthorized) |

## GF(3) Color Chain — New Increments

- **id=12** trit=0 `#d3869b` **ERGODIC**
- **id=13** trit=1 `#b8bb26` **PLUS**

### GF(3) Legend
- trit=0 → ERGODIC `#d3869b`
- trit=1 → PLUS `#b8bb26`
- trit=-1 → MINUS `#cc241d`

## GitHub Social Graph Sweep

Direct GitHub REST API access was **blocked (HTTP 403)** by the network proxy for external orgs/users.
In-scope repo (plurigrid/gorj) was snapshotted via GitHub MCP.

| Source | Status |
|--------|--------|
| plurigrid org | 403 blocked |
| kubeflow org | 403 blocked |
| TeglonLabs org | 403 blocked |
| bmorphism user | 403 blocked |
| zubyul + social graph | 403 blocked |
| plurigrid/gorj (MCP) | Snapshotted ✓ |

**plurigrid/gorj** — last push 2026-05-08, language: Clojure.
Latest commit: `chore: ignore duckdb binary in repo root`

## Hamming Swarm — Aptos Wallet Snapshot (2026-07-11)

All 28 addresses probed. **All returned resource_not_found** — none hold a `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource at this ledger height.

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | `0xc793acde...24cc7b` | 0.00000000 |
| U | `0x75860da4...ef9956` | 0.00000000 |
| A | `0x8699edc0...be9d7a` | 0.00000000 |
| B | `0x3f892ebe...77cb13` | 0.00000000 |
| C | `0x38b99e63...91535e` | 0.00000000 |
| D | `0xf7765624...fcfdd1` | 0.00000000 |
| E | `0xdc1d9d53...958d36` | 0.00000000 |
| bob | `0x0a3c00c5...512d5d` | 0.00000000 |
| G | `0x69a394c0...cc7f32` | 0.00000000 |
| H | `0xce67c327...e5300f` | 0.00000000 |
| I | `0x070fe5d7...0c1fc9` | 0.00000000 |
| J | `0x4d964db8...e87f54` | 0.00000000 |
| K | `0xa732040a...425dc4` | 0.00000000 |
| L | `0x7c2eaeaf...37eba9` | 0.00000000 |
| M | `0x6fed37a7...b7f2e9` | 0.00000000 |
| N | `0xe7dde6da...551b2c` | 0.00000000 |
| O | `0x73252b60...25a89d` | 0.00000000 |
| P | `0x6218792d...1ec948` | 0.00000000 |
| Q | `0xac40fa50...5c89a9` | 0.00000000 |
| R | `0x7ce605cc...d76e10` | 0.00000000 |
| S | `0xb8753014...9d0386` | 0.00000000 |
| T | `0x35781dc0...3f4588` | 0.00000000 |
| Z | `0x7af0ef6e...4e197c` | 0.00000000 |
| V | `0xb59dd817...9af2c3` | 0.00000000 |
| W | `0x5f32aef7...ccc7b0` | 0.00000000 |
| X | `0xa95cbbd1...33047d` | 0.00000000 |
| Y | `0xd8e32848...2444c4` | 0.00000000 |
| F | `0x18a14b5b...c3cf71` | 0.00000000 |

## Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428...987003` | 2 | ✓ |
| A-G | `0xf56c4a1c...bc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe181...75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae9...ed7883` | 2 | ✓ |
| V-W | `0x40fad7b4...80eb6d` | 2 | ✓ |

## MNX Markets

`https://testnet.mnx.fi` and all probed API paths returned **401 Unauthorized**.
No market data available this sweep.

## DuckDB Schema

- `world_increments` — GF(3) color-chain sweep events
- `repo_snapshots` — GitHub org/user repo metadata
- `aptos_snapshots` — Hamming swarm wallet balances (APT)
- `multisig_probes` — Aptos multisig threshold queries
- `mnx_snapshots` — MNX market data (empty this sweep)
