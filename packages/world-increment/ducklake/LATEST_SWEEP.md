# World Increment Sweep + Hamming Swarm Snapshot

**Run timestamp:** 2026-08-06T03:17-08:00 (UTC)
**DuckDB version:** v1.5.5 (Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Scope Note
GitHub API access in this environment is scoped to `plurigrid/gorj` only.
Cross-org queries (`kubeflow`, `TeglonLabs`, user repos for `bmorphism`, `zubyul`,
social graph contacts) were blocked by the proxy — sessions are bound to their
configured repository. 50 plurigrid org repos were successfully snapshotted via
the GitHub MCP search API.

### Plurigrid Org — Top Repos by Stars

| repo | lang | ★ | forks | issues | last push |
|------|------|---|-------|--------|-----------|
| plurigrid/asi | HTML | 59 | 13 | 4 | 2026-07-10 |
| plurigrid/ontology | JavaScript | 8 | 9 | 16 | 2025-05-27 |
| plurigrid/zig-syrup | Zig | 2 | 2 | 0 | 2026-07-28 |
| plurigrid/nash-portal | Rust | 2 | 2 | 1 | 2026-05-19 |
| plurigrid/asi-skills | Julia | 3 | 0 | 0 | 2026-04-26 |

### Recently Active Repos (by push date)

| repo | lang | last push |
|------|------|-----------|
| plurigrid/gorj | Clojure | 2026-08-06 |
| plurigrid/place | TeX | 2026-08-02 |
| plurigrid/eirobri | Clojure | 2026-08-04 |
| plurigrid/zig-syrup | Zig | 2026-07-28 |
| plurigrid/asi | HTML | 2026-07-10 |

### GF(3) Color Chain Distribution

| trit | color | name | count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 25 |
| -1 | `#cc241d` | MINUS | 25 |
|  0 | `#d3869b` | ERGODIC | 23 |

**50 repos inserted** as world_increments with GF(3) trit coloring (id%3 chain).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet fullnode.

| world | balance APT |
|-------|------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z (26 addresses) | 0.0 each |

All balances returned 0.0 APT. Accounts may be unfunded or the coin store
resource may not be initialized on mainnet.

### Multisig Contract Probes

| pair | address | sigs_required | healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✅ |
| A-G | 0xf56c4a1c... | 2 | ✅ |
| Y-Z | 0xd3ffe181... | 2 | ✅ |
| S-T | 0x3b1c3ae9... | 2 | ✅ |
| V-W | 0x40fad7b4... | 2 | ✅ |

All 5 multisig contracts respond with `num_signatures_required = 2` (2-of-N threshold).

### MNX Markets (testnet.mnx.fi)

`/api/markets` → HTTP 404. Root URL renders a minimal JavaScript SPA with no
extractable market data. Status: **unavailable** (JS-only SPA, no public API
endpoints accessible without browser execution).

---

## DuckDB State

```
world_increments : 73 rows  (cumulative, GF3 color chain)
repo_snapshots   : 994 rows (cumulative, multi-sweep history)
aptos_snapshots  : 28 rows  (this sweep)
multisig_probes  : 5 rows   (this sweep)
mnx_snapshots    : 0 rows   (API unavailable)
```

Database: `packages/world-increment/ducklake/world-increments.duckdb`
