# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3) increment id:** 24 — trit=+1, color=#b8bb26 **PLUS**

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 985 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — This Sweep

```
id mod 3 == 0 → trit=0,  #d3869b  ERGODIC
id mod 3 == 1 → trit=+1, #b8bb26  PLUS     ← id=24 (this sweep)
id mod 3 == 2 → trit=-1, #cc241d  MINUS
```

**id=24 → PLUS #b8bb26** — Next: id=25 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources crawled this sweep

| Source | Type | Repos captured |
|--------|------|---------------|
| plurigrid | org | 10 |
| kubeflow | org | 8 |
| TeglonLabs | org | 4 |
| bmorphism | user | 5 |
| zubyul | user | 4 |
| migalkin | social graph | 3 |
| wasita | social graph | 2 |
| kristinezheng | social graph | 1 |
| AustinCStone | social graph | 2 |
| M1shaaa | social graph | 1 |
| DJedamski | social graph | 1 |
| **Total** | | **41** |

### Notable recent activity

**plurigrid/gorj** — Clojure, pushed 2026-07-19 (today), 1251 open issues  
**plurigrid/asi** — HTML, 31★, pushed 2026-07-10, "everything is topological chemputer!"  
**plurigrid/eirobri** — Clojure, EiRoBri replay world, 30 issues, pushed 2026-07-14  
**kubeflow/pipelines** — Python, 4167★/2043⑂, pushed 2026-07-19 — dominant active repo  
**kubeflow/trainer** — Go, 2151★/989⑂, distributed AI training on K8s  
**kubeflow/spark-operator** — Python, 3138★, K8s Spark lifecycle manager  
**bmorphism/Gay.jl** — Julia, 187 open issues, wide-gamut color sampling, pushed 2026-07-14  
**bmorphism/gay-chat** — Scheme, gay://chat over Spritely Brassica Chat, pushed 2026-07-14  
**bmorphism/ocaml-mcp-sdk** — OCaml, 61★, Jane Street oxcaml_effect MCP SDK  
**migalkin/NodePiece** — Python, 144★, ICLR'22 compositional KG representations  
**migalkin/kgcourse2021** — HTML, 24★, Knowledge Graphs course materials, pushed 2026-07-10  
**wasita/wasita.github.io** — Svelte, 8 open issues, pushed 2026-07-16  
**AustinCStone/byteruckus** — HTML, newest repo, pushed 2026-07-15

### Top Repos by Source (this sweep)

#### plurigrid
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-10 |
| gorj | Clojure | 1 | 2026-07-19 |
| place | TeX | 1 | 2026-07-14 |
| nash-portal | Rust | 2 | 2026-05-19 |
| asi-skills | Julia | 3 | 2026-04-26 |

#### kubeflow
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| pipelines | Python | 4167 | 2026-07-19 |
| spark-operator | Python | 3138 | 2026-07-17 |
| trainer | Go | 2151 | 2026-07-18 |
| katib | Python | 1691 | 2026-07-16 |
| hub | Go | 177 | 2026-07-17 |

#### bmorphism
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| anti-bullshit-mcp-server | JavaScript | 22 | 2026-07-12 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| whale | MATLAB | 2 | 2026-04-20 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-19)

Query: `POST /v1/view` → `0x1::coin::balance<0x1::aptos_coin::AptosCoin>`

| World | Balance (APT) | Address (prefix) |
|-------|--------------|-----------------|
| **bob** | **12.657007** | 0x0a3c00c5... |
| **F** | **1.960516** | 0x18a14b5b... |
| **L** | **1.927269** | 0x7c2eaeaf... |
| **J** | **1.895093** | 0x4d964db8... |
| alice | 0.436434 | 0xc793acde... |
| O | 0.210136 | 0x73252b60... |
| K | 0.161961 | 0xa732040a... |
| P | 0.140136 | 0x62187929... |
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

**Total swarm APT:** ~21.07 APT  
**Heaviest world:** bob (12.657 APT, ~60% of total)  
**Top-3 (excl. alice/bob):** F (1.96), L (1.93), J (1.90)  
**Dust (<0.01 APT):** E, H, G, I

### Multisig Contract Probes

All 5 multisig contracts returned **healthy** status (2-of-N signing threshold):

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ HEALTHY |
| A-G | 0xf56c4a1c... | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ffe181... | 2 | ✓ HEALTHY |
| S-T | 0x3b1c3ae9... | 2 | ✓ HEALTHY |
| V-W | 0x40fad7b4... | 2 | ✓ HEALTHY |

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE**: Vercel deployment protection is active.  
Requires OIDC token, Vercel CLI, or bypass token to access.

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

## Notable Highlights
- **kubeflow/pipelines**: 4,167★ — most active, pushed today
- **bmorphism/Gay.jl**: 187 open issues — high activity
- **bob world**: 12.657 APT — dominant balance in swarm
- **All 5 multisigs healthy** — 2-of-N threshold operational
- **MNX testnet**: Vercel-protected, not accessible without auth
- **plurigrid/gorj**: pushed 2026-07-19 — this very sweep recorded
