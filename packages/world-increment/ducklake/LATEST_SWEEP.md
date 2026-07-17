# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this sweep) | 394 |
| Total Repo Snapshots (this sweep) | 394 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain Distribution (394 repo increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| +1 | `#b8bb26` | PLUS | 132 |
| -1 | `#cc241d` | MINUS | 131 |
| 0 | `#d3869b` | ERGODIC | 131 |

GF(3) rule: `id mod 3 == 0 → ERGODIC`, `id mod 3 == 1 → PLUS`, `id mod 3 == 2 → MINUS`

---

## GitHub Social Graph — Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 (of 103) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 (of 106) |
| zubyul | user | 49 |
| migalkin | user | 19 |
| AustinCStone | user | 41 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

### Top Repos by Stars (this sweep)

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,779 |
| kubeflow/pipelines | Python | 4,167 |
| kubeflow/spark-operator | Python | 3,137 |
| kubeflow/trainer | Go | 2,151 |
| kubeflow/katib | Python | 2,042 |
| TeglonLabs/mathpix-gem | Ruby | 2 |
| TeglonLabs/jank-crane | C++ | 0 |

### Notable Activity (2026)

- **TeglonLabs/jank-crane** — crane-jank converged-IR hub with GF3 convergence maps, pushed 2026-06-08
- **wasita/wasita.github.io** — personal site, pushed 2026-07-16 (most recent in graph)
- **M1shaaa/M1shaaa** — profile pushed 2026-07-17 (today)
- **kristinezheng/kristinezheng.github.io** — pushed 2026-07-01

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 wallets: alice, bob, A–Z)

**Result:** All 28 addresses returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` at ledger version ~6,316,818,143. Accounts are uninitialized or have zero APT balance.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793ac... | null |
| bob | 0x0a3c00... | null |
| A | 0x8699ed... | null |
| B | 0x3f892e... | null |
| C | 0x38b99e... | null |
| D | 0xf77656... | null |
| E | 0xdc1d9d... | null |
| F | 0x18a14b... | null |
| G | 0x69a394... | null |
| H | 0xce67c3... | null |
| I | 0x070fe5... | null |
| J | 0x4d964d... | null |
| K | 0xa73204... | null |
| L | 0x7c2eae... | null |
| M | 0x6fed37... | null |
| N | 0xe7dde6... | null |
| O | 0x73252b... | null |
| P | 0x621879... | null |
| Q | 0xac40fa... | null |
| R | 0x7ce605... | null |
| S | 0xb87530... | null |
| T | 0x35781d... | null |
| U | 0x75860d... | null |
| V | 0xb59dd8... | null |
| W | 0x5f32ae... | null |
| X | 0xa95cbb... | null |
| Y | 0xd8e328... | null |
| Z | 0x7af0ef... | null |

### Multisig Contract Probes (5 pairs) — ALL HEALTHY ✅

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f4... | 2 | ✅ healthy |
| A-G | 0xf56c4a... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✅ healthy |
| S-T | 0x3b1c3a... | 2 | ✅ healthy |
| V-W | 0x40fad7... | 2 | ✅ healthy |

All 5 multisig accounts are responsive. All require exactly **2 signatures**.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable** — HTTP 401, Vercel authentication required. No market data accessible.

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
