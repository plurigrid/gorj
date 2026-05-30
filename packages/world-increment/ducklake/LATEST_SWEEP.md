# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-05-30T00:00:00Z  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.3 Variegata)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| org/user | role | snapshots in DB | GitHub stars (total) |
|---|---|---|---|
| kubeflow | org | 142 | 101,871 |
| plurigrid | org | 300 | 154 |
| bmorphism | user | 300 | 509 |
| AustinCStone | social-graph (zubyul) | 126 | 324 |
| TeglonLabs | org | 110 | 14 |
| zubyul | user | 97 | 40 |
| migalkin | social-graph (zubyul) | 79 | 834 |
| wasita | social-graph (zubyul) | 71 | 11 |
| kristinezheng | social-graph (zubyul) | 42 | 0 |
| M1shaaa | social-graph (zubyul) | 40 | 0 |
| DJedamski | social-graph (zubyul) | 28 | 17 |

**Total:** 1,335 repo_snapshot rows · 34 world_increment rows  
Unique source entities: ~391 repos across 11 orgs/users  
(Snapshot count is higher due to multi-batch ingestion from distinct API calls)

### Top Repos by Stars

| repo | language | stars | last push |
|---|---|---|---|
| kubeflow/kubeflow | — | 15,687 | 2026-05-24 |
| kubeflow/pipelines | Python | 4,150 | 2026-05-29 |
| kubeflow/spark-operator | Python | 3,124 | 2026-05-29 |
| kubeflow/trainer | Go | 2,107 | 2026-05-30 |
| migalkin/NodePiece | Python | ~143 | (historical) |
| migalkin/kgcourse2021 | HTML | 25 | (historical) |
| bmorphism/ocaml-mcp-sdk | OCaml | ~60 | (recent) |
| AustinCStone/TextGAN | Python | ~92 | (historical) |

### Notable Social Graph Observations

- **M1shaaa** pushed to `M1shaaa/M1shaaa` (profile config) on **2026-05-30** — same day as this sweep
- **kristinezheng** last pushed `kristinezheng.github.io` on 2026-05-14 (active web presence)
- **wasita** personal site `wasita.github.io` (Svelte) last pushed 2026-05-20
- **migalkin** focus: knowledge graph ML (NodePiece, StarE, kgcourse2021)
- **AustinCStone** repos include `bmfork`, `bmforkupdate` — direct bmorphism social link

### GF(3) Color Chain Distribution

| trit | color | name | world_increment sources |
|---|---|---|---|
| 0 | `#d3869b` | ERGODIC | 10 |
| +1 | `#b8bb26` | PLUS | 12 |
| -1 | `#cc241d` | MINUS | 12 |

GF(3) rule: `id%3==0 → ERGODIC #d3869b · id%3==1 → PLUS #b8bb26 · id%3==2 → MINUS #cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

**Endpoint:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`  
**Result for all 28 addresses:** HTTP 404 `resource_not_found`

The `resource_not_found` error indicates these accounts have no legacy CoinStore resource — either unfunded wallets or accounts holding APT via the newer Fungible Asset (FA) standard at `0x1::fungible_asset::FungibleStore`. Balance recorded as **0.0 APT** for all.

| world | address (first 10 chars) | balance_apt |
|---|---|---|
| alice | 0xc793acd... | 0.0 |
| bob | 0x0a3c00c... | 0.0 |
| A | 0x8699edc... | 0.0 |
| B | 0x3f892eb... | 0.0 |
| C | 0x38b99e6... | 0.0 |
| D | 0xf776562... | 0.0 |
| E | 0xdc1d9d5... | 0.0 |
| F | 0x18a14b5... | 0.0 |
| G | 0x69a394c... | 0.0 |
| H | 0xce67c32... | 0.0 |
| I | 0x070fe5d... | 0.0 |
| J | 0x4d964db... | 0.0 |
| K | 0xa732040... | 0.0 |
| L | 0x7c2eaea... | 0.0 |
| M | 0x6fed37a... | 0.0 |
| N | 0xe7dde6d... | 0.0 |
| O | 0x73252b6... | 0.0 |
| P | 0x621879... | 0.0 |
| Q | 0xac40fa5... | 0.0 |
| R | 0x7ce605c... | 0.0 |
| S | 0xb875301... | 0.0 |
| T | 0x35781dc... | 0.0 |
| U | 0x75860da... | 0.0 |
| V | 0xb59dd81... | 0.0 |
| W | 0x5f32aef... | 0.0 |
| X | 0xa95cbbd... | 0.0 |
| Y | 0xd8e3284... | 0.0 |
| Z | 0x7af0ef6... | 0.0 |

### Multisig Contract Probes (Aptos Mainnet)

**Function:** `0x1::multisig_account::num_signatures_required`  
**Ledger version probed:** ~5,484,211,332

| pair | address (prefix) | sigs_required | healthy |
|---|---|---|---|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig accounts configured as **2-of-N** threshold. All returned valid responses (healthy).

### MNX Markets (testnet.mnx.fi)

**Status:** `unavailable` — SPA only  
`testnet.mnx.fi` serves a Next.js SPA (dark theme). Probed `/api/markets`, `/api/v1/markets` — both return HTML, not JSON. No REST API endpoints found. Recorded as `category=unavailable` in `mnx_snapshots`.

---

## DuckDB Schema & Row Counts

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)                          -- 34 rows

repo_snapshots(id, timestamp, increment_id, org_or_user,
               repo_name, full_name, language, stars, forks,
               open_issues, pushed_at, description)             -- 1,335 rows

aptos_snapshots(timestamp, world, address, balance_apt)         -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy) -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 1 row
```

## Previous Sweep Reference

Prior sweep (2026-04-12): 12 world_increments, 471 repo_snapshots.  
This sweep (2026-05-30): 34 world_increments, 1,335 repo_snapshots (expanded social graph coverage).
