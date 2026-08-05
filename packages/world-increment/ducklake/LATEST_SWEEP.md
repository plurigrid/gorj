# World Increment Sweep + Hamming Swarm Snapshot
**Run date:** 2026-08-05  
**GF3 color chain:** ERGODIC #d3869b | PLUS #b8bb26 | MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Collected |
|--------|------|----------------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 50 |
| zubyul | user | 49 |
| migalkin | social graph | 19 |
| wasita | social graph | 14 |
| AustinCStone | social graph | 41 |
| DJedamski | social graph | 6 |
| kristinezheng | social graph | 5 |
| M1shaaa | social graph | 8 |
| **Total** | | **346 repos this run** |

### Top Repos by Stars (this sweep)
| Repo | Stars | Forks | Language | Last Push |
|------|-------|-------|----------|-----------|
| kubeflow/kubeflow | 15,805 | 2,692 | — | 2026-07-10 |
| kubeflow/pipelines | 4,176 | 2,078 | Python | 2026-08-04 |
| kubeflow/spark-operator | 3,143 | 1,511 | Python | 2026-08-04 |
| kubeflow/trainer | 2,170 | 1,012 | Go | 2026-08-04 |
| kubeflow/katib | 1,694 | 534 | Python | 2026-08-04 |
| kubeflow/arena | 816 | 196 | Go | 2026-07-29 |
| kubeflow/kale | 699 | 158 | Python | 2026-08-04 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-03-16 |
| plurigrid/asi | 58 | 13 | HTML | 2026-07-10 |

### Recently Active (pushed ≤7 days before 2026-08-05)
- **plurigrid/gorj** (Clojure) — 1638 open issues, pushed 2026-08-05
- **bmorphism/Gay.jl** (Julia) — pushed 2026-08-05
- **kubeflow/sdk** (Python) — pushed 2026-08-05
- **plurigrid/eirobri** (Clojure) — pushed 2026-08-04
- **kubeflow/pipelines** (Python) — pushed 2026-08-04
- **kubeflow/spark-operator** (Python) — pushed 2026-08-04
- **wasita/xoxowasita-analysis** (Python) — pushed 2026-08-04
- **wasita/joint-planning-lit** — pushed 2026-08-04
- **plurigrid/place** (TeX) — pushed 2026-08-02

### Notable Social Graph Activity
- **wasita**: 2 new repos created 2026-08-04 (xoxowasita-analysis, joint-planning-lit)
- **zubyul/from-possible-worlds** (TeX) — recently pushed 2026-07-18
- **migalkin/kgcourse2021** — activity spike on 2026-07-10

### GF3 Distribution (272 world_increment rows this run)
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 97 |
| 1 | PLUS | #b8bb26 | 99 |
| -1 | MINUS | #cc241d | 99 |

GF(3) rule: `id%3==0→ERGODIC`, `id%3==1→PLUS`, `id%3==2→MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
**Queried:** 2026-08-05 · 28 addresses (alice, bob, A–Z) · 1s delay between calls

**Result: All 28 addresses → `resource_not_found`**

None of the Hamming swarm addresses have an initialized `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` on Aptos mainnet. Accounts exist in the address space but have no APT coin resource registered. Balance recorded as NULL for all 28 worlds.

| Range | Addresses | Balance |
|-------|-----------|---------|
| alice, bob | 2 | NULL (no CoinStore) |
| A–Z | 26 | NULL (no CoinStore) |

### Multisig Contract Probes — **5/5 HEALTHY**
All 5 multisig pairs are live and require exactly **2-of-2 signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

Swarm multisig governance is intact. All pairs live, all 2-of-2.

### MNX Testnet Markets
`https://testnet.mnx.fi` — **SPA (Next.js) — no REST API accessible**

All probed paths (`/api/markets`, `/api/v1/markets`, `/api/v2/markets`) return the Next.js HTML shell. Market data requires in-browser JS execution and is not available via direct API probe. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB State (packages/world-increment/ducklake/world-increments.duckdb)

| Table | Row Count |
|-------|-----------|
| world_increments | 295 |
| repo_snapshots | 1,216 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 |

**Cumulative across all runs:** 11 distinct sources, 1,216 repo snapshots tracked.

---

## Schema Reference
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
- **kubeflow/kubeflow**: 15,805 stars — star count grew ~240 since last sweep (2026-04-12: 15,565)
- **kubeflow/pipelines**: 4,176 stars (+57 vs April), pushed 2026-08-04
- **bmorphism/Gay.jl**: active development, pushed 2026-08-05 (188 open issues)
- **plurigrid/gorj**: 1,638 open issues — highest issue count in the graph
- **Multisig swarm**: 5/5 healthy, all 2-of-2 — no governance changes detected
- **Aptos balances**: all NULL — Hamming swarm wallets uninitialized on mainnet
