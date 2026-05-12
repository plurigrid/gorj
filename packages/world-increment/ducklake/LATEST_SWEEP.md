# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-12

## Sweep Metadata
- **Date:** 2026-05-12
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Role |
|--------|------|------|
| plurigrid | org | primary |
| kubeflow | org | primary |
| TeglonLabs | org | primary |
| bmorphism | user | primary |
| zubyul | user | primary |
| migalkin | user | zubyul social graph |
| wasita | user | zubyul social graph |
| kristinezheng | user | zubyul social graph |
| M1shaaa | user | zubyul social graph |
| AustinCStone | user | zubyul social graph |
| DJedamski | user | zubyul social graph |

### DuckDB Ducklake State (cumulative)

```
world_increments : 99  rows  (GF3 color chain, this sweep)
repo_snapshots   : 1020 rows total, 489 unique repos (inc. prior sweeps)
aptos_snapshots  : 28  rows  (all NULL balance — unfunded CoinStore)
multisig_probes  : 5   rows  (all healthy, 2-of-N)
mnx_snapshots    : 0   rows  (testnet.mnx.fi SPA, API unavailable)
```

### GF(3) Trit Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 32 |
| 1 | `#b8bb26` | PLUS | 34 |
| -1 | `#cc241d` | MINUS | 33 |

GF(3) rule: `id%3==0 → ERGODIC #d3869b` · `id%3==1 → PLUS #b8bb26` · `id%3==2 → MINUS #cc241d`

### Top Repos by Stars (2026-05-12 snapshot)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,629 | — | 2026-05-07 |
| kubeflow/pipelines | 4,139 | Python | 2026-05-12 |
| kubeflow/spark-operator | 3,125 | Python | 2026-05-12 |
| kubeflow/trainer | 2,097 | Go | 2026-05-12 |
| kubeflow/katib | 1,683 | Python | 2026-05-09 |
| kubeflow/mcp-apache-spark-history-server | 168 | Python | 2026-05-12 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 21 | HTML | 2026-04-26 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2025-01-07 |

### Notable Activity (last 30 days)

**plurigrid:** `gorj` (164 open issues, active), `nanoclj-zig` (Zig 0.15 NaN-boxed Clojure + GF(3)), `zig-syrup` (OCapN Syrup), `asi-skills` (69 skills, Julia), `nash-portal`, `horse`

**kubeflow:** `mcp-apache-spark-history-server` (🆕 168★, MCP for Spark debugging), `pipelines`, `trainer`, `manifests`, `sdk`, `mpi-operator`, `hub`

**bmorphism:** `Gay.jl` (188 issues, Julia wide-gamut colors), `nanoclj-zig` (fork), `zig-syrup`, `postweb`

**zubyul:** `ghostel-emacs-worlds`, `voice-observatory`, `nash-tui`, `nash-web`, `gay-world`

**TeglonLabs:** `mathpix-gem` (Ruby math OCR via Mathpix API)

**wasita:** `wasita.github.io` (Svelte, active), `vocoder` (pushed 2026-05-06), `wm-cv`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds)

**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793acdec1... | NULL (404) |
| bob | 0x0a3c00c58f... | NULL (404) |
| A–Z | (26 addresses) | NULL (404) |

**Finding:** All 28 CoinStore resources return 404. However, accounts ARE active on-chain:
- `alice` (0xc793...): `sequence_number=72` — highly active
- `A` (0x8699...): `sequence_number=58` — active
- `Z` (0x7af0...): `sequence_number=2` — recently created

Accounts exist but APT CoinStore is uninitialized. Wallets may use custom tokens or have transferred APT outbound. All 28 recorded as `NULL` in `aptos_snapshots`.

### Multisig Contract Probes

**Method:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|:---:|:---:|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

**All 5 multisig accounts healthy.** All require 2-of-N signatures (2-of-2 presumed given A/B, Y/Z, etc. naming).

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi` is a React/Vue SPA. All REST API paths probed:
- `/api/markets` → 404
- `/api/v1/markets` → 404
- `/api/tickers` → 404
- `/api/v1/tickers` → 404

Market data **unavailable** this sweep. `mnx_snapshots` table remains empty.

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

## Highlights

- **kubeflow/mcp-apache-spark-history-server** (168★): Brand new MCP tool for Spark debugging from AI agents — significant signal for MCP ecosystem growth
- **plurigrid/gorj** (164 issues): This very repo — highly active GF(3) trit-colored REPL orchestration
- **bmorphism/Gay.jl** (188 issues): Julia wide-gamut deterministic color sampling via SplitMix64 SPI
- **All 5 Hamming swarm multisigs healthy** — 2-of-N consensus intact across A-B, A-G, Y-Z, S-T, V-W pairs
- **28 wallet accounts active** — alice has 72 sequence_number, indicating substantial on-chain history despite no visible APT coinstore
