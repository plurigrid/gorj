# World-Increment Sweep + Hamming Snapshot

**Run timestamp:** 2026-06-28T12:19 UTC
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## GF(3) Color Chain

| trit | name    | color     | count |
|------|---------|-----------|-------|
| -1   | MINUS   | `#cc241d` | 43    |
|  0   | ERGODIC | `#d3869b` | 43    |
| +1   | PLUS    | `#b8bb26` | 43    |

**Total world-increment events:** 129 (perfectly balanced — 43×3)

Assignment rule: `id mod 3 == 0` → ERGODIC, `id mod 3 == 1` → PLUS, `id mod 3 == 2` → MINUS

---

## Job 1 — GitHub Social Graph Sweep

**Sources:** orgs `plurigrid`, `kubeflow`, `TeglonLabs` + users `bmorphism`, `zubyul`, `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`

### Repos by Owner

| owner         | repos |
|---------------|-------|
| plurigrid     | 46    |
| bmorphism     | 23    |
| kubeflow      | 20    |
| zubyul        | 11    |
| migalkin      | 6     |
| wasita        | 6     |
| TeglonLabs    | 5     |
| AustinCStone  | 4     |
| kristinezheng | 3     |
| DJedamski     | 3     |
| M1shaaa       | 2     |
| **Total**     | **129** |

### Top Repos by Stars

| repo                            | stars  | forks | lang    |
|---------------------------------|--------|-------|---------|
| kubeflow/kubeflow               | 15,750 | 2,680 | —       |
| kubeflow/pipelines              | 4,158  | 2,013 | Python  |
| kubeflow/spark-operator         | 3,129  | 1,491 | Python  |
| kubeflow/trainer                | 2,125  | 972   | Go      |
| kubeflow/katib                  | 1,687  | 527   | Python  |
| kubeflow/examples               | 1,460  | 756   | Jsonnet |
| kubeflow/community-distribution | 1,028  | 1,065 | YAML    |
| kubeflow/arena                  | 814    | 192   | Go      |
| kubeflow/kale                   | 694    | 156   | Python  |
| kubeflow/mpi-operator           | 528    | 236   | Go      |

Notable: `plurigrid/gorj` (881 open issues), `bmorphism/Gay.jl` (187 open issues), `bmorphism/anti-bullshit-mcp-server` (23 stars)

---

## Job 2 — Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Wallets probed:** 28 (alice, bob, A–Z)
**Balances found:** 0 of 28 — all `resource_not_found` for `CoinStore<AptosCoin>`

Derivation-path placeholder addresses hold no mainnet APT; `balance_apt = NULL` for all 28 rows.

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| pair | address                                                               | sigs_required | healthy |
|------|-----------------------------------------------------------------------|---------------|---------|
| A-B  | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2             | ✓       |
| A-G  | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2             | ✓       |
| Y-Z  | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2             | ✓       |
| S-T  | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2             | ✓       |
| V-W  | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2             | ✓       |

All 5 multisig contracts healthy — require 2-of-N signatures.

### MNX Testnet Markets

**Status:** 401 Unauthorized — `https://testnet.mnx.fi/api/markets` unavailable during this sweep.
`mnx_snapshots` table: 0 rows.

---

## DuckDB Table Summary

| table            | rows | notes                              |
|------------------|------|------------------------------------|
| world_increments | 129  | GF3-colored, balanced 43/43/43     |
| repo_snapshots   | 129  | full metadata per repo             |
| aptos_snapshots  |  28  | all balance_apt = NULL             |
| multisig_probes  |   5  | all sigs_required=2, healthy=True  |
| mnx_snapshots    |   0  | API returned 401                   |

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(id, timestamp, world, address, balance_apt)
multisig_probes(id, timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(id, timestamp, ticker, name, category, price, change_pct)
```
