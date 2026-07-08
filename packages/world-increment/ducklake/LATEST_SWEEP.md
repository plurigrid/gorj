# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-08

**Run date:** 2026-07-08  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d  
**Total world increments:** 333  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos | Stars | Forks |
|--------|------|-------|-------|-------|
| kubeflow | org | 49 | 15,769 (flagship) | 2,685 (flagship) |
| plurigrid | org | 100 | 162 | 84 |
| bmorphism | user | 100 | 509 | 99 |
| zubyul | user | 49 | 40 | 4 |
| TeglonLabs | org | 5 | 14 | 8 |
| migalkin | user | 19 | 833 | 146 |
| AustinCStone | user | 40 | 380 | 112 |
| wasita | user | 11 | 11 | 3 |
| DJedamski | user | 6 | 17 | 5 |
| kristinezheng | user | 5 | 0 | 0 |
| M1shaaa | user | 8 | 0 | 0 |

### Top Repos by Stars

| Repo | Stars | Forks | Lang | Last Push |
|------|-------|-------|------|-----------|
| kubeflow/kubeflow | 15,769 | 2,685 | — | 2026-07-06 |
| kubeflow/pipelines | 4,169 | 2,029 | Python | 2026-07-08 |
| kubeflow/spark-operator | 3,134 | 1,498 | Python | 2026-07-02 |
| kubeflow/trainer | 2,132 | 981 | Go | 2026-07-08 |
| kubeflow/katib | 1,690 | 532 | Python | 2026-07-08 |
| migalkin/NodePiece | 144 | 21 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | 30 | Python | 2025-03-03 |
| migalkin/StarE | 89 | 16 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | 2 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | 7 | JS | 2026-01-16 |

### Notable Recent Activity (pushed within 7 days of 2026-07-08)

- **plurigrid/gorj** — Clojure — GF(3) gay trit coloring for compositional open game REPL orchestration
- **kubeflow/community-distribution** — YAML — Kubeflow Community Distribution
- **kubeflow/pipelines** — Python — ML Pipelines for Kubeflow
- **kubeflow/trainer** — Go — Distributed AI Model Training and LLM Fine-Tuning
- **kubeflow/katib** — Python — Automated Machine Learning on Kubernetes
- **wasita/wasita.github.io** — Svelte — personal website (updated 2026-07-06)
- **bmorphism/Gay.jl** — Julia — Wide-gamut color sampling with splittable determinism (187 open issues, active!)

### Social Graph Notes

- **bmorphism** links to **AustinCStone** via `bmfork`/`bmforkupdate` repos (AustinCStone forked bmorphism's work)
- **migalkin** (Michael Galkin) — Knowledge Graph researcher; NodePiece (144★) widely cited in KGE literature
- **zubyul** repos cluster around Gay.jl, BCI, and GF(3) color work; nash-tui/web pushed 2026-04-13
- **wasita** — network science / Svelte personal site, active through 2026-07
- **TeglonLabs/jank-crane** — C++, GF3 convergence maps, loopify pass spec (most recent push: 2026-06-08)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` on the APT CoinStore at ledger version 6,174,656,471. These accounts were created but the `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource was never initialized — wallets may hold other Move resources or modules.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793...cc7b | 0.00000000 |
| bob | 0x0a3c...2d5d | 0.00000000 |
| A | 0x8699...9d7a | 0.00000000 |
| B | 0x3f89...b13 | 0.00000000 |
| C | 0x38b9...35e | 0.00000000 |
| D | 0xf776...dd1 | 0.00000000 |
| E | 0xdc1d...d36 | 0.00000000 |
| F | 0x18a1...f71 | 0.00000000 |
| G | 0x69a3...f32 | 0.00000000 |
| H | 0xce67...00f | 0.00000000 |
| I | 0x070f...c9 | 0.00000000 |
| J | 0x4d96...f54 | 0.00000000 |
| K | 0xa732...dc4 | 0.00000000 |
| L | 0x7c2e...ba9 | 0.00000000 |
| M | 0x6fed...2e9 | 0.00000000 |
| N | 0xe7dd...b2c | 0.00000000 |
| O | 0x7325...89d | 0.00000000 |
| P | 0x6218...948 | 0.00000000 |
| Q | 0xac40...89a9 | 0.00000000 |
| R | 0x7ce6...e10 | 0.00000000 |
| S | 0xb875...386 | 0.00000000 |
| T | 0x3578...588 | 0.00000000 |
| U | 0x7586...956 | 0.00000000 |
| V | 0xb59d...2c3 | 0.00000000 |
| W | 0x5f32...7b0 | 0.00000000 |
| X | 0xa95c...47d | 0.00000000 |
| Y | 0xd8e3...44c4 | 0.00000000 |
| Z | 0x7af0...97c | 0.00000000 |

### Multisig Contract Probes

All 5 multisig accounts responded with `num_signatures_required = 2`. All **HEALTHY**.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY |
| A-G | 0xf56c...0096 | 2 | HEALTHY |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY |
| S-T | 0x3b1c...7883 | 2 | HEALTHY |
| V-W | 0x40fa...eb6d | 2 | HEALTHY |

All multisigs require 2-of-N signatures. No anomalies detected.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — `testnet.mnx.fi` returns a Vercel deployment protection auth wall on all probed endpoints (`/`, `/api/markets`, `/api/v1/markets`). No market data accessible without a Vercel bypass token or Trusted Source OIDC token. mnx_snapshots table has 0 rows this run.

---

## DuckDB Schema Summary

```
world_increments   — 333 rows  (GF3-colored repo push events)
repo_snapshots     — 333 rows  (per-repo metadata)
aptos_snapshots    —  28 rows  (wallet balance snapshot; all 0 APT / resource not found)
multisig_probes    —   5 rows  (all healthy, sigs_required=2)
mnx_snapshots      —   0 rows  (unavailable this run — Vercel auth wall)
```

## GF(3) Color Distribution (333 increments)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 111 |
| 1 | #b8bb26 | PLUS | 111 |
| -1 | #cc241d | MINUS | 111 |

---

*Previous sweep metadata below (2026-04-12):*

## Sweep Metadata
- **Date:** 2026-04-12
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
