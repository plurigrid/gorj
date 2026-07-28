# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 · GF(3) trit=1 · #b8bb26 · **PLUS**

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 13 |
| New Repo Snapshots (this sweep) | 49 |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Total Repos |
|--------|------|-------------|
| plurigrid | org | 70+ |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 19 |
| DJedamski | user (social graph) | 6 |
| wasita | user (social graph) | 12 |
| kristinezheng | user (social graph) | 5 |
| M1shaaa | user (social graph) | 8 |
| AustinCStone | user (social graph) | 30 |

### Notable Active Repos (recently pushed)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/pipelines | Python | 4171 | 2026-07-28 |
| kubeflow/trainer | Go | 2156 | 2026-07-27 |
| kubeflow/spark-operator | Python | 3142 | 2026-07-25 |
| kubeflow/kubeflow | — | 15793 | 2026-07-10 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |
| bmorphism/world | Python | 0 | 2026-06-02 |
| plurigrid/asi-skills | Julia | 3 | 2026-04-26 |
| plurigrid/zig-syrup | Zig | 2 | 2026-04-30 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |
| M1shaaa/M1shaaa | — | 0 | 2026-07-28 |
| kristinezheng/kristinezheng.github.io | HTML | 0 | 2026-07-01 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A–Z) queried via Aptos mainnet fullnode API.

| Result | Count |
|--------|-------|
| 0.0 APT (no CoinStore resource / empty) | 28 |
| Non-zero balances | 0 |

All 28 addresses returned 0.0 APT. Accounts may not have an initialized CoinStore resource or hold zero APT at this snapshot.

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts on Aptos mainnet responded successfully.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

All contracts require 2 signatures — swarm coordination intact.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` returns a Next.js SPA — no JSON API endpoint publicly accessible. Market data unavailable; recorded as placeholder in `mnx_snapshots`.

---

## GF(3) Color Chain — All 13 Increments

| ID | Source | GF3 Trit | Color | Name |
|----|--------|-----------|-------|------|
| 1  | plurigrid (org) | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (sweep) | 0 | `#d3869b` | **ERGODIC** |
| **13** | **plurigrid+kubeflow+TeglonLabs+social (2026-07-28)** | **+1** | **`#b8bb26`** | **PLUS** |

GF(3) chain continues: `…ERGODIC → PLUS`

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

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
