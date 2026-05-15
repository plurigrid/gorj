# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-15

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `v1.5.2 (Variegata)` → `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Table | Rows |
|-------|------|
| `world_increments` | 538 |
| `repo_snapshots` | 478 |

Sources: 3 orgs (plurigrid, kubeflow, TeglonLabs) + 2 users (bmorphism, zubyul) + 6 zubyul social-graph users + 60 public events.

### GF(3) Color Chain Distribution

| Color | Name | Trit | Count |
|-------|------|------|-------|
| `#d3869b` | ERGODIC | 0 | 179 |
| `#b8bb26` | PLUS | +1 | 180 |
| `#cc241d` | MINUS | -1 | 179 |

Assignment rule: `id % 3 == 0` → ERGODIC, `id % 3 == 1` → PLUS, `id % 3 == 2` → MINUS.

### Repos by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 48 |
| AustinCStone | user (zubyul graph) | 43 |
| wasita | user (zubyul graph) | 32 |
| migalkin | user (zubyul graph) | 30 |
| zubyul | user | 27 |
| kristinezheng | user (zubyul graph) | 18 |
| M1shaaa | user (zubyul graph) | 16 |
| DJedamski | user (zubyul graph) | 11 |
| **TOTAL** | | **478** |

Plus 60 public events (30 bmorphism + 30 zubyul) → 538 world_increments total.

### Top Repos by Source

#### plurigrid (100 repos, sorted by stars)
| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| asi | HTML | 21 | 5 |
| ontology | JavaScript | 8 | 9 |
| asi-skills | Julia | 3 | 1 |
| zig-syrup | Zig | 2 | 2 |
| nash-portal | Rust | 2 | 3 |

#### kubeflow (48 repos)
| Repo | Language | Stars |
|------|----------|-------|
| kubeflow | — | 15,565 |
| pipelines | Python | 4,119 |
| spark-operator | Python | 3,111 |
| trainer | Go | 2,080 |
| katib | Python | 1,676 |

#### bmorphism highlights
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |

#### migalkin highlights
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `0x1::primary_fungible_store::balance` FA view function (with CoinStore fallback). All 28 addresses returned balances.

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | 0x0a3c00c5... |
| F | 1.960516 | 0x18a14b5b... |
| L | 1.927269 | 0x7c2eaeaf... |
| J | 1.895093 | 0x4d964db8... |
| alice | 0.436434 | 0xc793acde... |
| O | 0.210136 | 0x73252b60... |
| K | 0.161961 | 0xa732040a... |
| P | 0.140136 | 0x62187922... |
| M | 0.112285 | 0x6fed37a7... |
| N | 0.106121 | 0xe7dde6da... |
| Q | 0.103240 | 0xac40fa50... |
| S | 0.091788 | 0xb8753014... |
| R | 0.090217 | 0x7ce605cc... |
| T | 0.073713 | 0x35781dc0... |
| U | 0.055773 | 0x75860da4... |
| A | 0.051767 | 0x8699edc0... |
| V | 0.048833 | 0xb59dd817... |
| Y | 0.044449 | 0xd8e32848... |
| X | 0.042577 | 0xa95cbbd1... |
| W | 0.040705 | 0x5f32aef7... |
| B | 0.036256 | 0x3f892ebe... |
| Z | 0.024268 | 0x7af0ef6e... |
| D | 0.011629 | 0xf7765624... |
| C | 0.010185 | 0x38b99e63... |
| E | 0.009372 | 0xdc1d9d53... |
| H | 0.001681 | 0xce67c327... |
| G | 0.000681 | 0x69a394c0... |
| I | 0.000681 | 0x070fe5d7... |

**Total swarm balance: ~20.13 APT**

Note: `alice` (0xc793...) is a contract account with `multiverse::MultiverseState`, `address_book::Mapping`, and `lending_pool::UserPosition` resources — not a simple wallet.

### Multisig Contract Probes

All 5 probed via `0x1::multisig_account::num_signatures_required` view function.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

All 5 contracts require **2-of-N signatures** and respond healthily.

### MNX Markets (testnet.mnx.fi)

Status: **SPA — no public REST API accessible**. Site is a Next.js app; no JSON endpoints found at `/api/markets`, `/api/tickers`, `/api/v1/markets`, `/v1/markets`, etc. `mnx_snapshots` table has 0 rows.

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)              -- 538 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)              -- 478 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)  -- 0 rows
```
