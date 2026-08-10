# World Increment Sweep — 2026-08-10

**Increment ID**: 13  
**GF(3) State**: trit=1 · PLUS · `#b8bb26`  
**Timestamp**: 2026-08-10T04:16 UTC  

---

## Job 1: GitHub Social Graph Sweep

**Scope note**: GitHub API access is proxy-restricted to `plurigrid/gorj` only in this environment. Cross-org endpoints (plurigrid org-wide, kubeflow, TeglonLabs) and user repos (bmorphism, zubyul, social graph) return 403. Only `plurigrid/gorj` was snapshotted via MCP.

### Repo Snapshot Added

| Repo | Language | Description |
|------|----------|-------------|
| `plurigrid/gorj` | Clojure | MCP server + hooks that give AI coding agents a Clojure REPL |

### Recent Activity (plurigrid/gorj — last 5 commits)

| SHA | Message | Date |
|-----|---------|------|
| `5b28fe0` | chore: ignore duckdb binary in repo root | 2026-05-08 |
| `ebf263f` | world-increment ducklake: sync world.duckdb sweep state | 2026-04-14 |
| `b434a43` | Merge sweep state into master | 2026-04-14 |
| `e76792f` | world-increments.duckdb: sync latest sweep state | 2026-04-14 |
| `631518b` | world-increment sweep 2026-04-12: insert id=12 ERGODIC | 2026-04-12 |

### DB State

| Table | Count |
|-------|-------|
| world_increments | 24 rows (ids 1–13) |
| repo_snapshots | 945 total |

---

## Job 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses probed)

All wallets queried against `fullnode.mainnet.aptoslabs.com`. No `CoinStore<AptosCoin>` resource found on any address — wallets hold 0 APT via this resource path (may hold other tokens or be unfunded on mainnet).

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...e9d7 | 0.0 |
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
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...af2c | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...444c | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — each requires **2-of-N signatures**.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets

`https://testnet.mnx.fi` returns a Next.js SPA with no JSON API exposed at `/api/markets` or `/api/v1/markets`. Market data is unavailable programmatically; recorded as `unavailable` in `mnx_snapshots`.

---

## GF(3) Color Chain Progress

| ID | Trit | Color | Name |
|----|------|-------|------|
| 12 | 0 | `#d3869b` | ERGODIC |
| **13** | **1** | **`#b8bb26`** | **PLUS** |
| 14 (next) | -1 | `#cc241d` | MINUS |
