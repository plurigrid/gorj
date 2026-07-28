# World-Increment Sweep + Hamming Snapshot — 2026-07-28

## Sweep Metadata
- **Date:** 2026-07-28
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Aptos mainnet ledger version:** 6,495,058,771 (chain_id: 1)

---

## JOB 1: GitHub Social Graph Sweep

### Scope Note

GitHub MCP session is scoped to `plurigrid/gorj`. External orgs (`kubeflow`, `TeglonLabs`) and user accounts (`bmorphism`, `zubyul`, social graph: `migalkin`, `DJedamski`, `wasita`, `kristinezheng`, `M1shaaa`, `AustinCStone`) were outside session scope and not queried. Only `plurigrid` org repos were accessible.

### plurigrid Org — 100 Repos Snapshotted

**Most recently pushed:**

| Repo | Language | Stars | Forks | Open Issues | Pushed At |
|------|----------|-------|-------|-------------|-----------|
| plurigrid/gorj | Clojure | 1 | 0 | 1464 | 2026-07-28T13:15Z |
| plurigrid/zig-syrup | Zig | 2 | 2 | 0 | 2026-07-28T13:02Z |
| plurigrid/eirobri | Clojure | 0 | 0 | 31 | 2026-07-21T02:24Z |
| plurigrid/place | TeX | 1 | 2 | 14 | 2026-07-14T09:11Z |
| plurigrid/asi | HTML | 52 | 11 | 4 | 2026-07-10T09:47Z |
| plurigrid/shrimp | — | 0 | 0 | 0 | 2026-07-03T01:24Z |
| plurigrid/nash-portal | Rust | 2 | 2 | 1 | 2026-05-19T01:49Z |
| plurigrid/asi-skills | Julia | 3 | 0 | 0 | 2026-04-26T08:09Z |
| plurigrid/nanoclj-zig | Zig | 1 | 1 | 20 | 2026-04-25T07:29Z |

**Language distribution (today's 100 repos):**

| Language | Repos |
|----------|-------|
| Rust | 12 |
| TypeScript | 10 |
| Clojure | 9 |
| Python | 8 |
| HTML | 5 |
| Scheme | 4 |
| JavaScript | 3 |
| Julia | 3 |
| Zig | 2 |
| Hy | 2 |
| Go | 2 |

### GF(3) Color Chain (world_increments — today)

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 33 |
| 1 | PLUS | #b8bb26 | 34 |
| 2 | MINUS | #cc241d | 33 |

**Total world_increments (all time):** 123 (100 today)
**Total repo_snapshots (all time):** 1044 (100 today + 944 from April 2026 sweeps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**28 addresses probed** (alice, bob, A–Z). All returned `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

- `alice` (0xc793...) — active contract account (seq: 72), hosts `multiverse::MultiverseState`, `address_book::Mapping`, `store_v2::ACSetMeta2` — no APT CoinStore
- A–Z addresses — exist on-chain with `0x1::account::Account` resource only, no CoinStore (zero APT)

**Total APT across 28 wallets: 0.0 APT**

### Multisig Probes (5 contracts)

All 5 contracts responded via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-N signatures required.**

### MNX Markets (testnet.mnx.fi)

Site reachable (HTTP 200) but is a Next.js SPA. No REST API found at `/api/markets` or `/api/v1/markets` — data loads client-side via JS. **No rows inserted into `mnx_snapshots`.**

---

## DuckDB State

```
packages/world-increment/ducklake/world-increments.duckdb
  world_increments:  123 rows (100 today, GF3 color chain applied)
  repo_snapshots:   1044 rows (100 today + 944 historical Apr 2026)
  aptos_snapshots:    28 rows (all NULL balance, resource_not_found)
  multisig_probes:     5 rows (all healthy, sigs_required=2)
  mnx_snapshots:       0 rows (SPA, no accessible API)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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

## Notable Highlights
- **plurigrid/gorj**: 1464 open issues — most active repo, pushed today
- **plurigrid/zig-syrup**: High-performance OCapN Syrup with CapTP, pushed today
- **plurigrid/asi**: 52 stars — topological chemputer, most-starred plurigrid repo
- **Hamming swarm**: All 5 multisig contracts healthy at 2-of-N threshold
- **alice contract**: `multiverse::MultiverseState` resource active on mainnet (seq: 72)
