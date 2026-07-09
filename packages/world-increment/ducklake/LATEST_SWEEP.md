# LATEST_SWEEP — 2026-07-09T07:12:42Z

## Summary

- **Sweep type**: world-increment (GitHub) + hamming-swarm (Aptos)
- **DuckDB records**: 73 world_increments, 994 repo_snapshots, 28 aptos_snapshots, 5 multisig_probes

---

## JOB 1: GitHub Social Graph Sweep

### Data Sources
- **plurigrid** org: 50 repos captured via GitHub MCP API
- **kubeflow**, **TeglonLabs**: blocked by environment proxy (repo-scoped only)
- **bmorphism**, **zubyul** and social graph users: blocked by environment proxy

### GF(3) Color Chain Distribution

| Name | Color | Count |
|------|-------|-------|
| ERGODIC | `#d3869b` | 24 |
| MINUS | `#cc241d` | 24 |
| PLUS | `#b8bb26` | 25 |

### Top 10 Most Recently Pushed Repos

| Repo | Language | Stars | Pushed At | Description |
|------|----------|-------|-----------|-------------|
| plurigrid/gorj | Clojure | 1 | 2026-07-09 | forj + Rama topology nREPL routing + GF(3) gay trit coloring |
| plurigrid/place | TeX | 1 | 2026-07-07 |  |
| plurigrid/shrimp | - | 0 | 2026-07-03 | Jank worked example: shrimp |
| plurigrid/eirobri | Clojure | 0 | 2026-06-30 | EiRoBri replay world |
| plurigrid/asi | HTML | 30 | 2026-06-29 | everything is topological chemputer! |
| plurigrid/nash-portal | Rust | 2 | 2026-05-19 | NASH token TUI in the browser — ratzilla WASM + GeckoTermina |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 | High-performance Zig implementation of OCapN Syrup with CapT |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 | 69 skills with Galois Hole Type accessibility (Seven Sketche |
| plurigrid/bci-blue-share | JavaScript | 0 | 2026-04-26 | BCI signal infrastructure — bci.blue / bci.red / bci.horse |
| plurigrid/nanoclj-zig | Zig | 1 | 2026-04-25 | NaN-boxed Clojure interpreter in Zig 0.15 — interaction nets |

### Language Breakdown (plurigrid)

| Language | Repo Count |
|----------|-----------|
| Python | 157 |
| HTML | 39 |
| Go | 38 |
| Rust | 38 |
| JavaScript | 31 |
| Jupyter Notebook | 26 |
| TypeScript | 24 |
| Clojure | 22 |
| R | 16 |
| Jsonnet | 16 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses: alice, bob, A–Z)

All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.
This indicates the accounts have never received APT or the CoinStore resource has not been initialized.

**Total APT balance across all wallets: 0.0 APT**

### Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| V-W | `0x40fad7b423a843650f…` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49…` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622…` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f…` | 2 | ✓ |
| A-B | `0x0da4f428a0c007da0f…` | 2 | ✓ |

All 5 multisig contracts responded successfully: **2-of-N signatures required** on each.

### MNX Markets (testnet.mnx.fi)

Status: **401 Unauthorized** — testnet requires authentication. No market data available.

---

## Environment Notes

- GitHub API scope: repo-scoped only (`plurigrid/gorj`); org-level and cross-user queries blocked by proxy
- Aptos Mainnet Ledger version probed: ~6,192,549,516
- DuckDB Python module: 1.5.4
