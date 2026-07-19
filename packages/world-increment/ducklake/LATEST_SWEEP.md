# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-19T00:10:00Z
**Agent:** world-increment-sweep + hamming-swarm-snapshot
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (duckdb v1.5.4)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos | Total Stars | Latest Push | GF3 |
|--------|------|-------|-------------|-------------|-----|
| plurigrid | org | 100 | 489 | 2026-07-18 | PLUS `#b8bb26` (trit=+1) |
| kubeflow | org | 49 | 306,318 | 2026-07-18 | MINUS `#cc241d` (trit=-1) |
| TeglonLabs | org | 5 | 2 | 2026-06-08 | ERGODIC `#d3869b` (trit=0) |
| bmorphism | user | 100 | 810 | 2026-07-18 | PLUS `#b8bb26` (trit=+1) |
| zubyul | user | 49 | 886 | 2026-07-18 | MINUS `#cc241d` (trit=-1) |
| migalkin | user | 19 | 1,417 | 2026-06-08 | ERGODIC `#d3869b` (trit=0) |
| DJedamski | user | (prev) | 28 | 2018-03-07 | PLUS `#b8bb26` (trit=+1) |
| wasita | user | (prev) | 12 | 2026-04-13 | MINUS `#cc241d` (trit=-1) |
| kristinezheng | user | (prev) | 0 | 2026-04-09 | ERGODIC `#d3869b` (trit=0) |
| M1shaaa | user | (prev) | 0 | 2026-04-13 | PLUS `#b8bb26` (trit=+1) |
| AustinCStone | user | (prev) | 432 | 2026-02-11 | MINUS `#cc241d` (trit=-1) |

### Notable Active Repos

- `plurigrid/gorj` — Clojure, pushed **2026-07-18**, 1★, 1248 open issues — *forj + Rama topology nREPL routing + GF(3) gay trit coloring*
- `plurigrid/eirobri` — Clojure, pushed 2026-07-14, 30 open issues — *EiRoBri replay world*
- `plurigrid/place` — TeX, pushed 2026-07-14, 1★
- `plurigrid/asi` — HTML, pushed 2026-07-10, 31★ — *everything is topological chemputer!*
- `plurigrid/shrimp` — pushed 2026-07-03 — *Jank worked example: shrimp*
- `TeglonLabs/jank-crane` — C++, pushed 2026-06-08 — *crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps*
- `bmorphism` — 810 stars across 100 repos, latest push 2026-07-18
- `kubeflow/kubeflow` — 15,565★ — flagship ML platform for Kubernetes

### Top Languages (This Run)

| Language | Repos |
|----------|-------|
| Python | 207 |
| Rust | 57 |
| Go | 51 |
| HTML | 50 |
| JavaScript | 49 |
| TypeScript | 44 |
| Jupyter Notebook | 38 |
| Clojure | 30 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) returned **0 APT**.
The `CoinStore<AptosCoin>` resource was not registered at any of these addresses.
This may indicate uninitialised accounts or alternative storage paths.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Health (Aptos Mainnet)

All 5 contracts are **HEALTHY** — each requires 2-of-N signatures.

| Pair | Contract Address | sigs_required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | HEALTHY |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | HEALTHY |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection (HTTP 401). Visitor password required. No market data extracted.

---

## GF(3) Color Chain

```
id%3==1 → PLUS     #b8bb26  (plurigrid, bmorphism, DJedamski, M1shaaa)
id%3==2 → MINUS    #cc241d  (kubeflow, zubyul, wasita, AustinCStone)
id%3==0 → ERGODIC  #d3869b  (TeglonLabs, migalkin, kristinezheng)
```

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## DuckDB State

| Table | Rows |
|-------|------|
| world_increments | 29 |
| repo_snapshots | 3,562+ |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (unavailable) |
