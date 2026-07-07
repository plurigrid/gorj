# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-07 (automated sweep)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`
**GF(3) Color Chain:** ERGODIC=#d3869b (trit=0) · PLUS=#b8bb26 (trit=1) · MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### World-Increment Chain (11 increments)

| id | GF3 | color | source | type | repos |
|----|-----|-------|--------|------|-------|
| 1 | PLUS | #b8bb26 | plurigrid | org | 100 (103 total) |
| 2 | MINUS | #cc241d | kubeflow | org | 49 |
| 3 | ERGODIC | #d3869b | bmorphism | user | 100 (105 total) |
| 4 | PLUS | #b8bb26 | zubyul | user | 49 |
| 5 | MINUS | #cc241d | TeglonLabs | org | 5 |
| 6 | ERGODIC | #d3869b | migalkin | social | 19 (5 sampled) |
| 7 | PLUS | #b8bb26 | DJedamski | social | 6 (2 sampled) |
| 8 | MINUS | #cc241d | wasita | social | 11 (3 sampled) |
| 9 | ERGODIC | #d3869b | kristinezheng | social | 5 (2 sampled) |
| 10 | PLUS | #b8bb26 | M1shaaa | social | 8 (2 sampled) |
| 11 | MINUS | #cc241d | AustinCStone | social | 40 (3 sampled) |

**Total repo_snapshots stored:** 320

### Top Repositories by Stars

| repo | language | stars | forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | Python | 15,769 | 2,760 |
| kubeflow/pipelines | Python | 4,169 | 1,800 |
| kubeflow/spark-operator | Go | 3,133 | 770 |
| kubeflow/trainer | Go | 2,130 | 600 |
| kubeflow/katib | Go | 1,690 | 480 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/NodePiece | Python | 144 | 21 |
| migalkin/StarE | Python | 89 | 16 |

### Notable Recent Activity

- **bmorphism** (1,237 total commits indexed): Most recent = `bmorphism/open-location-code-zig` — Zig implementation of Open Location Codes, Claude Code-assisted, 35 tests passing (2025-12-30)
- **wasita/wasita.github.io**: Updated 2026-07-06 (yesterday!) — Svelte personal site actively maintained
- **TeglonLabs/jank-crane**: C++ crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- **kristinezheng/kristinezheng.github.io**: Updated 2026-07-01

### TeglonLabs Repos (5 total)

| repo | language | stars | description |
|------|----------|-------|-------------|
| jank-crane | C++ | 0 | crane-jank converged-IR hub, GF3 convergence maps |
| mathpix-gem | Ruby | 2 | Math images → LaTeX (11 open issues) |
| coin-flip-mcp | JavaScript | 0 | MCP server coin flip (2 forks) |
| monad-mcp-server | — | 0 | Monad MCP Server |
| topoi | Python | 0 | Topoi |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, ledger v6,162,673,026)

All 28 wallets (alice, bob, A–Z) queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All wallets returned `resource_not_found` → 0.00000000 APT**

These addresses do not have an initialized AptosCoin store at this ledger version. The Aptos mainnet node confirmed healthy: chain_id=1, block_height=882,807,543, epoch=16,451.

| world | address (truncated) | balance_apt |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...af2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...3047d | 0.0 |
| Y | 0xd8e3...444c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5/5 healthy)

| pair | address (truncated) | sigs_required | status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

All 5 multisig accounts require 2-of-N signatures. All probed successfully via `0x1::multisig_account::num_signatures_required`.

### MNX Markets

`https://testnet.mnx.fi` — SPA frontend only; no JSON API exposed at `/api/markets` or `/api/v1/markets`. **Status: unavailable / no market data extracted.**

---

## Database Schema Summary

```
world_increments  : 11 rows  (GF3 chain across orgs/users)
repo_snapshots    : 320 rows (GitHub repos with lang/stars/forks/issues)
aptos_snapshots   : 28 rows  (Hamming swarm wallets, all 0 APT)
multisig_probes   : 5 rows   (all healthy, 2 sigs required)
mnx_snapshots     : 0 rows   (API unavailable)
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
