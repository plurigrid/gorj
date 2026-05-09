# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-09 16:08 UTC  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB version:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured | Status |
|--------|------|----------------|--------|
| plurigrid | org | 100 | ✓ via MCP |
| kubeflow | org | 48 | ✓ |
| TeglonLabs | org | 0 | rate-limited |
| bmorphism | user | 0 | rate-limited |
| zubyul | user | 0 repos, 30 events | rate-limited (events OK) |
| migalkin | user | 30 | ✓ |
| DJedamski | user | 11 | ✓ |
| wasita | user | 32 | ✓ |
| kristinezheng | user | 0 | rate-limited |
| M1shaaa | user | 0 | rate-limited |
| AustinCStone | user | 43 | ✓ |

**Total repos snapshotted:** 264  
**Total events (zubyul public):** 30  
**Total world_increments:** 294

### DuckDB Table Counts

| Table | Rows |
|-------|------|
| world_increments | 294 |
| repo_snapshots | 264 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

### GF(3) Color Chain Distribution

| Trit | Color Name | Hex | Count |
|------|-----------|-----|-------|
| 0 | ERGODIC | #d3869b | 98 |
| 1 | PLUS | #b8bb26 | 98 |
| -1 | MINUS | #cc241d | 98 |

GF(3) assignment: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

### Top Repos by Stars

| org/user | repo | language | stars | forks | last_pushed |
|----------|------|----------|-------|-------|-------------|
| kubeflow | kubeflow | — | 15628 | 2647 | 2026-05-07 |
| kubeflow | pipelines | Python | 4137 | 1989 | 2026-05-08 |
| kubeflow | spark-operator | Python | 3125 | 1480 | 2026-05-08 |
| kubeflow | trainer | Go | 2096 | 948 | 2026-05-08 |
| kubeflow | katib | Python | 1683 | 510 | 2026-05-08 |
| kubeflow | examples | Jsonnet | 1462 | 972 | 2026-05-05 |
| kubeflow | manifests | YAML | 1015 | 655 | 2026-05-08 |
| kubeflow | arena | Go | 810 | 204 | 2026-05-08 |
| kubeflow | kale | Python | 685 | 154 | 2023-07-03 |
| kubeflow | mpi-operator | Go | 524 | 253 | 2026-05-08 |
| migalkin | torchmetrics | Python | 236 | 55 | 2025-11-14 |
| AustinCStone | Sorting | C++ | 172 | 63 | 2022-06-11 |
| AustinCStone | Graphs | C++ | 118 | 53 | 2022-06-11 |
| migalkin | NodePiece | Python | 93 | 19 | 2023-05-28 |
| AustinCStone | DataStructures | C++ | 78 | 39 | 2021-02-01 |
| migalkin | StarE | Python | 66 | 19 | 2023-05-17 |
| plurigrid | ontology | Clojure | 42 | 3 | 2024-06-21 |
| migalkin | RNNs | Python | 41 | 18 | 2022-05-12 |
| plurigrid | gorj | Clojure | 30 | 1 | 2026-05-09 |
| wasita | wasita.github.io | HTML | 27 | 2 | 2025-04-04 |

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | 43 |
| wasita | user | 32 |
| migalkin | user | 30 |
| DJedamski | user | 11 |
| **TOTAL** | | **264** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets probed via `fullnode.mainnet.aptoslabs.com` at ledger version ~5.199B. All returned `resource_not_found` — accounts have no initialized `CoinStore<AptosCoin>` resource.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Total APT across swarm:** 0.0

### Multisig Contract Probes (Aptos Mainnet)

All 5 multisig contracts are **healthy**, all with `sigs_required = 2`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...987003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — TLS handshake succeeds (cert valid until 2026-06-08) but the site serves an SPA with no accessible JSON API at `/api/markets` or `/api/tickers`. Market data cannot be extracted without browser execution.

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## Notes

- GitHub unauthenticated API rate limit (60 req/hr) was hit after ~170 calls; TeglonLabs, bmorphism, zubyul repos, kristinezheng, M1shaaa could not be fetched. Zubyul's 30 most recent public events were captured before the limit.
- Aptos `resource_not_found` is expected for accounts with no coin store — not a probe error.
- GF(3) trit chain balances perfectly: 98 ERGODIC (#d3869b) + 98 PLUS (#b8bb26) + 98 MINUS (#cc241d) = 294 total.
