# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-11

## Sweep Metadata
- **Date:** 2026-07-11
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 35 (this run) |
| Total Repo Snapshots | 35 (this run) |
| Sources Covered | 3 orgs + 8 users |
| Aptos wallets probed | 28 (alice, bob, A–Z) |
| Multisig contracts probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Total Repos | Notable |
|--------|------|------------|---------|
| plurigrid | org | 103 | asi (30★), ontology (8★), asi-skills (3★) |
| kubeflow | org | 49 | kubeflow (15,771★), spark-operator (3,137★), pipelines (4,169★) |
| TeglonLabs | org | 5 | jank-crane (GF3 maps, 2026-06), mathpix-gem (2★) |
| bmorphism | user | 105 | ocaml-mcp-sdk (61★), Gay.jl (187 open issues), satreadout |
| zubyul | user | 49 | gay-world (1★), voice-observatory, big-bad-plurigrid-quiz |
| migalkin | user | 19 | NodePiece (144★ ICLR'22), kgcourse2021 (24★, active 2026-07-10) |
| DJedamski | user | 6 | kaggle_ncaa18 |
| wasita | user | 11 | wasita.github.io (active 2026-07-06), send2kobo |
| kristinezheng | user | 5 | kristinezheng.github.io (active 2026-07-01) |
| M1shaaa | user | 8 | lab-bookshelf- (Dec 2024) |
| AustinCStone | user | 40 | TextGAN (92★), EpsteinSearch (2026-02) |

### GF(3) Color Chain (first 12 world-increment IDs shown)

| ID | Source | GF3 Trit | Color | Name |
|----|--------|----------|-------|------|
| 1  | plurigrid/asi | +1 | `#b8bb26` | PLUS |
| 2  | plurigrid/gorj | -1 | `#cc241d` | MINUS |
| 3  | plurigrid/shrimp | 0 | `#d3869b` | ERGODIC |
| 4  | plurigrid/place | +1 | `#b8bb26` | PLUS |
| 5  | plurigrid/eirobri | -1 | `#cc241d` | MINUS |
| 6  | plurigrid/nash-portal | 0 | `#d3869b` | ERGODIC |
| 7  | kubeflow/pipelines | +1 | `#b8bb26` | PLUS |
| 8  | kubeflow/kubeflow | -1 | `#cc241d` | MINUS |
| 9  | kubeflow/trainer | 0 | `#d3869b` | ERGODIC |
| 10 | kubeflow/spark-operator | +1 | `#b8bb26` | PLUS |
| 11 | kubeflow/katib | -1 | `#cc241d` | MINUS |
| 12 | TeglonLabs/jank-crane | 0 | `#d3869b` | ERGODIC |

### Key Recent Activity (pushed < 72h of sweep date 2026-07-11)
- `kubeflow/spark-operator` — pushed 2026-07-11
- `kubeflow/kubeflow` — pushed 2026-07-11
- `kubeflow/trainer` — pushed 2026-07-11
- `kubeflow/pipelines` — pushed 2026-07-10
- `plurigrid/asi` — pushed 2026-07-10 (HTML/topological chemputer, 30★)
- `migalkin/kgcourse2021` — pushed 2026-07-10
- `plurigrid/gorj` — pushed 2026-07-07 (**1,110 open issues** — high)
- `wasita/wasita.github.io` — pushed 2026-07-06

### Top Repos by Stars (2026-07-11 snapshot)

| Repo | Stars | Language | Last Pushed |
|------|-------|----------|------------|
| kubeflow/kubeflow | 15,771 | — | 2026-07-11 |
| kubeflow/spark-operator | 3,137 | Python | 2026-07-11 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-10 |
| kubeflow/trainer | 2,135 | Go | 2026-07-11 |
| kubeflow/katib | 1,689 | Python | 2026-07-09 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| plurigrid/asi | 30 | HTML | 2026-07-10 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice, bob, A–Z)

All 28 addresses returned **HTTP 404 (account not found)** on Aptos mainnet.

> Accounts return 404 until initialized with a first transaction. The swarm addresses have not been activated on mainnet as of 2026-07-11.

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — 2-of-2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4f428…4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c…fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181…e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9…3ded7883 | 2 | ✓ |
| V-W | 0x40fad7b4…c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

API returned **401 Unauthorized** on all probed endpoints. Requires authentication.

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

## Signal Summary
1. **kubeflow is highly active** — spark-operator, kubeflow core, trainer, pipelines all pushed 2026-07-10/11
2. **plurigrid/gorj has 1,110 open issues** — unusually high, may warrant triage
3. **All 5 Hamming swarm multisigs operational** — 2-of-2 threshold intact
4. **Swarm wallet addresses (alice, bob, A-Z) uninitialized** — no APT on mainnet
5. **MNX testnet behind auth wall** — no public market data available
