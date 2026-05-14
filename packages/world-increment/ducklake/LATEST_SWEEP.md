# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-14

## Sweep Metadata
- **Date:** 2026-05-14
- **Sweep IDs:** 13 (PLUS) · 14 (MINUS) · 15 (ERGODIC)
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Snapshot hash:** `888f8f6a2e39ff4e`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (all-time) | 15 |
| Total Repo Snapshots (all-time) | 1,265 |
| New Repos This Sweep | 321 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain — Increments 13–15

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid_social_graph | github_sweep | +1 | `#b8bb26` | **PLUS** |
| 14 | hamming_swarm | aptos_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | world_increment_sweep | sweep_complete | 0 | `#d3869b` | **ERGODIC** |

Continuing chain: `… ERGODIC(12) → PLUS(13) → MINUS(14) → ERGODIC(15)`

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 17 |
| migalkin | user (social graph) | 11 |
| wasita | user (social graph) | 11 |
| AustinCStone | user (social graph) | 10 |
| M1shaaa | user (social graph) | 8 |
| kristinezheng | user (social graph) | 6 |
| DJedamski | user (social graph) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **321** |

**Note:** Public GitHub REST API was rate-limited (0/60 unauthenticated). All data obtained via authenticated MCP `search_repositories`.

### Top Repos by Stars (this sweep)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,629 | — |
| kubeflow/pipelines | 4,140 | Python |
| kubeflow/spark-operator | 3,125 | Python |
| kubeflow/trainer | 2,098 | Go |
| kubeflow/katib | 1,682 | Python |
| kubeflow/examples | 1,462 | Jsonnet |
| kubeflow/arena | 810 | Go |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/NodePiece | 144 | Python |
| migalkin/StarE | 89 | Python |

### plurigrid/gorj (live snapshot)
- Language: Clojure · Stars: 0 · Forks: 0 · Open issues: 187
- Pushed: 2026-05-14T14:19:24Z
- Description: *forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration*

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses returned HTTP 404 from `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore`. These accounts have no APT CoinStore registered (never received a transaction on mainnet). Stored as `balance_apt = NULL`.

| Wallet | Address (prefix) | Balance |
|--------|-----------------|---------|
| alice | 0xc793acd... | NULL (404) |
| bob | 0x0a3c00c... | NULL (404) |
| A–Z (26) | 0x8699ed...–0x7af0ef... | NULL (404) |

### Multisig Contract Probes (`0x1::multisig_account::num_signatures_required`)

| Pair | Address (prefix) | sigs_required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig contracts healthy — 2-of-N threshold on each.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — wallet connection required**

`/api/markets` → 404. `/markets` → Next.js SPA with "Connect Wallet to View Account" gate. No public JSON market data accessible without an authenticated wallet session. `mnx_snapshots` table remains empty.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
