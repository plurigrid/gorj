# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-02

**Sweep date:** 2026-07-02  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social graph) | 5 |
| DJedamski | user (social graph) | 3 |
| wasita | user (social graph) | 4 |
| kristinezheng | user (social graph) | 2 |
| M1shaaa | user (social graph) | 3 |
| AustinCStone | user (social graph) | 4 |
| **TOTAL** | | **323** |

### Top Active Repos (by push recency)

**plurigrid/**
- `asi` — HTML, ⭐29, pushed 2026-06-29 — "everything is topological chemputer!"
- `place` — TeX, 12 open issues, pushed 2026-06-29
- `eirobri` — Clojure, 30 open issues, pushed 2026-06-30

**TeglonLabs/**
- `jank-crane` — C++, pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- `mathpix-gem` — Ruby, ⭐2, 11 open issues — LaTeX/OCR gem

**Social Graph Highlights**
- `migalkin/NodePiece` — Python, ⭐144, 21 forks — ICLR'22 KG representation
- `migalkin/StarE` — Python, ⭐89, 16 forks — EMNLP 2020 hyper-relational KGs
- `AustinCStone/TextGAN` — Python, ⭐92, 30 forks — TensorFlow GAN for text
- `wasita/wasita.github.io` — Svelte, pushed 2026-07-02 (fresh today)
- `kristinezheng/kristinezheng.github.io` — pushed 2026-07-01

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color   | Count |
|----------|------|---------|-------|
| ERGODIC  | 0    | #d3869b | 107   |
| PLUS     | +1   | #b8bb26 | 108   |
| MINUS    | -1   | #cc241d | 108   |

Rule: `id%3==0` → ERGODIC, `id%3==1` → PLUS, `id%3==2` → MINUS

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming-swarm accounts (alice, bob, A–Z) exist on Aptos mainnet
but hold **0.00000000 APT** — accounts are registered with no CoinStore balance.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...12d5 | 0.0 |
| A–Z   | various       | 0.0 (all)     |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy**, each requiring 2-of-N signatures:

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B  | 0x0da4...7003 | 2 | ✓ |
| A-G  | 0xf56c...0096 | 2 | ✓ |
| Y-Z  | 0xd3ff...b883 | 2 | ✓ |
| S-T  | 0x3b1c...7883 | 2 | ✓ |
| V-W  | 0x40fa...eb6d | 2 | ✓ |

**Assessment:** Swarm multisig topology fully operational. All pairs healthy at 2-of-N.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `https://testnet.mnx.fi/api/markets` returned HTTP 401 Unauthorized.
The testnet requires authentication; no market data could be extracted.

---

## DuckDB Schema Summary

```
world_increments   323 rows  — GF3-tagged repo snapshot events
repo_snapshots     323 rows  — full repo metadata
aptos_snapshots     28 rows  — Hamming swarm wallet balances
multisig_probes      5 rows  — multisig contract health probes
mnx_snapshots        1 row   — MNX market status (unavailable)
```

---

## Notable Signals

1. **plurigrid/asi** most-starred plurigrid repo (⭐29), pushed 2026-06-29 — active "topological chemputer" work
2. **wasita** pushed today (2026-07-02) — live social graph activity
3. **TeglonLabs/jank-crane** references GF3 in its description — cross-system convergence marker
4. **All 28 Hamming swarm accounts** exist on mainnet but are unfunded (0 APT) — swarm registered, not capitalized
5. **All 5 multisig pairs** online at 2-of-N — governance structure intact

---

## Previous Sweep Metadata
- **Agent:** world-increment-sweep
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 471 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — All 12 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 12 | bmorphism (org) | sweep_complete (gorj) | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 16 | 2026-04-10 |
| ontology | JavaScript | 7 | 2025-05-27 |
| asi-skills | Julia | 3 | 2026-04-09 |
| zig-syrup | Zig | 2 | 2026-04-09 |
| vivarium | Clojure | 1 | 2026-04-08 |

### kubeflow (47 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565 | 2026-01-05 |
| pipelines | Python | 4119 | 2026-04-10 |
| spark-operator | Python | 3111 | 2026-04-10 |
| trainer | Go | 2080 | 2026-04-10 |
| katib | Python | 1676 | 2026-04-02 |

### TeglonLabs (53 repos)
| Repo | Language | Stars |
|------|----------|-------|
| mathpix-gem | Ruby | 2 |
| vibespace | HTML | 2 |
| acp.el | — | 1 |
| mcp-terminal | — | 1 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| ocaml-mcp-sdk | OCaml | 60 |
| anti-bullshit-mcp-server | JavaScript | 23 |
| shitcoin | Python | 5 |
| open-location-code-zig | Zig | 3 |

### migalkin (30 repos)
| Repo | Language | Stars |
|------|----------|-------|
| NodePiece | Python | 143 |
| StarE | Python | 88 |
| kgcourse2021 | HTML | 25 |

### AustinCStone (43 repos)
| Repo | Language | Stars |
|------|----------|-------|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| TeglonLabs | org | 53 |
| kubeflow | org | 47 |
| AustinCStone | user | 43 |
| migalkin | user | 30 |
| wasita | user | 29 |
| zubyul | user | 24 |
| kristinezheng | user | 18 |
| M1shaaa | user | 16 |
| DJedamski | user | 11 |
| **TOTAL** | | **471** |

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes (pushed 2026-04-10)
- **kubeflow/spark-operator**: 3,111 stars — Kubernetes operator for Apache Spark (pushed 2026-04-10)
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 16 stars — topological chemputer (pushed 2026-04-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL routing + GF(3) gay trit coloring
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
