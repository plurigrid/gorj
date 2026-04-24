# LATEST_SWEEP — 2026-04-24

## World Increment #13 · GF(3) PLUS · `#b8bb26`

| Field | Value |
|-------|-------|
| Increment ID | 13 |
| GF(3) trit | 1 (PLUS) |
| GF(3) color | `#b8bb26` |
| Cycle | 5th (id 13–15) |
| Timestamp | 2026-04-24 |
| Snapshot hash | `ebf263f516935cb93b64101666a01dc5a84b15aa` |

---

## JOB 1: GitHub Social Graph Sweep

### Data Source Status

| Source | Type | Status |
|--------|------|--------|
| plurigrid/gorj | org repo | ✓ captured via MCP |
| kubeflow | org | ✗ GitHub API rate limit exceeded (unauthenticated IP) |
| TeglonLabs | org | ✗ GitHub API rate limit exceeded |
| bmorphism | user | ✗ GitHub API rate limit exceeded |
| zubyul | user | ✗ GitHub API rate limit exceeded |
| zubyul social graph (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) | users | ✗ GitHub API rate limit exceeded |

> Unauthenticated GitHub API is capped at 60 req/hour per IP. MCP tools (restricted to plurigrid/gorj) provided gorj metadata.

### plurigrid/gorj Snapshot

- **Latest commit:** `ebf263f5` — "world-increment ducklake: sync world.duckdb sweep state" (2026-04-14)
- **Branches:** 50+ including `master`, `rama-gay-agent-o-rama`, and dense `world-increment/sweep-*` history from 2026-03-26 through 2026-03-29
- **Language:** Clojure
- **Description:** MCP server + hooks that give AI coding agents a Clojure REPL

### DuckDB State After Sweep

| Table | Rows |
|-------|------|
| world_increments | 24 |
| repo_snapshots | 949 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Balances (28 addresses)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1`. Every account returned no APT `CoinStore` resource — accounts not initialized or no APT held.

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | no CoinStore |
| bob | 0.0 | no CoinStore |
| A–Z (26) | 0.0 each | no CoinStore |

**Total swarm APT:** 0.0

### Multisig Contract Probes (5/5 healthy)

All 5 multisig contracts responded via `0x1::multisig_account::num_signatures_required` with value `2`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2 | ✓ |

### MNX Markets

`testnet.mnx.fi` — **DNS UNAVAILABLE** (503, DNS cache overflow at host IP). No market data captured this sweep.

---

## GF(3) Chain History

```
id  trit  name     color
1   0     ERGODIC  #d3869b
2   1     PLUS     #b8bb26
3   -1    MINUS    #cc241d
4   0     ERGODIC  #d3869b
5   1     PLUS     #b8bb26
6   -1    MINUS    #cc241d
7   0     ERGODIC  #d3869b
8   1     PLUS     #b8bb26
9   -1    MINUS    #cc241d
10  0     ERGODIC  #d3869b
11  1     PLUS     #b8bb26
12  -1    MINUS    #cc241d  ← previous sweep (2026-04-12)
13  1     PLUS     #b8bb26  ← THIS SWEEP (2026-04-24)
```

> id%3 mapping: 0→ERGODIC #d3869b, 1→PLUS #b8bb26, 2→MINUS #cc241d
> id=13 → 13%3=1 → PLUS
