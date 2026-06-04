# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-30  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Status |
|--------|------|-------------------|--------|
| plurigrid | org | 100 | OK |
| kubeflow | org | 2 | OK (public unauthenticated, rate-limited) |
| TeglonLabs | org | 53 | OK |
| bmorphism | user | 100 | OK |
| zubyul | user | 0 | Account inactive / no public repos |
| migalkin | user | 30 | OK |
| DJedamski | user | 11 | OK |
| wasita | user | 31 | OK |
| M1shaaa | user | 16 | OK |
| kristinezheng | user | 0 | Account not found |
| AustinCStone | user | 0 | Account not found |

**Total world_increments rows:** 341 (341 repo events + 2 bmorphism public events)
**Total repo_snapshots rows:** 341

### GF(3) Color Chain Distribution (341 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 113 |
| +1 | `#b8bb26` | PLUS | 114 |
| -1 | `#cc241d` | MINUS | 114 |

GF(3) assignment: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

### Top Repos by Stars

| Repo | Owner | Stars | Language | Last Pushed |
|------|-------|-------|----------|-------------|
| NodePiece | migalkin | 143 | Python | 2022-02-02 |
| StarE | migalkin | 89 | Python | 2023-12-01 |
| ocaml-mcp-sdk | bmorphism | 60 | OCaml | 2026-03-16 |
| kgcourse2021 | migalkin | 25 | HTML | 2025-08-04 |
| anti-bullshit-mcp-server | bmorphism | 23 | JavaScript | 2026-01-16 |
| asi | plurigrid | 17 | HTML | 2026-04-26 |
| ontology | plurigrid | 7 | JavaScript | 2025-05-27 |
| RWL | migalkin | 7 | Python | 2022-12-01 |
| shitcoin | bmorphism | 5 | Python | 2026-04-08 |

### Language Distribution by Source

| Source | Top Language | Repos | Stars |
|--------|-------------|-------|-------|
| migalkin | Python | 11 | 249 |
| bmorphism | OCaml | 1 | 60 |
| bmorphism | JavaScript | 1 | 23 |
| plurigrid | HTML | 3 | 17 |
| plurigrid | Rust | 9 | 3 |
| plurigrid | Zig | 2 | 3 |
| DJedamski | R | 4 | 2 |

### bmorphism Recent Events

2 recent public events captured (PushEvent / CreateEvent type). zubyul: 0 public events (inactive account).

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — 28 Addresses (alice, bob, A–Z)

**Result: All 28 addresses returned `resource_not_found` on Aptos mainnet**

The `CoinStore<AptosCoin>` resource is absent on all probed addresses. Possible causes:
1. Accounts are uninitialized (never received APT)
2. Accounts use Fungible Asset (FA) module rather than legacy CoinStore
3. Addresses are theoretical/test keys with no on-chain activity

All 28 records inserted with `balance_apt = NULL`.

### Multisig Contract Probes — 5 Pairs

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts healthy** — each requires 2-of-N signatures via `0x1::multisig_account::num_signatures_required`. Contracts exist and are responsive on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — pure client-side SPA**

- `https://testnet.mnx.fi` serves a React/Next.js bundle (292 KB)
- All API paths probed (`/api/markets`, `/api/v1/markets`, `/api/tickers`, `/api/v2/markets`, `/api/v3/*`, `/markets`, `/_next/data/...`) return SPA shell HTML
- No `__NEXT_DATA__` or embedded JSON in page source
- Data is loaded via client-side WebSocket/XHR requiring browser execution
- Recorded as `MNX_UNAVAILABLE` in `mnx_snapshots`

---

## DuckDB Table Summary

```
world-increments.duckdb
├── world_increments    341 rows  (GF3 color-chained event log)
├── repo_snapshots      341 rows  (GitHub repo metadata)
├── aptos_snapshots      28 rows  (Hamming swarm wallets, all NULL balance)
├── multisig_probes       5 rows  (all healthy, 2-of-N)
└── mnx_snapshots         1 row   (unavailable marker)
```

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

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

## Notable Highlights

- **migalkin/NodePiece**: 143 stars — scalable KG embeddings without node parameters
- **migalkin/StarE**: 89 stars — message passing for knowledge graph link prediction
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using Jane Street's oxcaml_effect (pushed 2026-03-16)
- **bmorphism/anti-bullshit-mcp-server**: 23 stars — LLM veracity filter (pushed 2026-01-16)
- **plurigrid/asi**: 17 stars — topological chemputer (pushed 2026-04-26, most recent plurigrid push)
- **All 5 Hamming multisigs**: healthy 2-of-N on Aptos mainnet
- **Aptos wallets**: all uninitialized (no CoinStore resource found)
