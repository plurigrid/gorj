# World-Increment Sweep — 2026-07-30

## Sweep Metadata
- **Date:** 2026-07-30
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Increment ID:** 13 — GF(3) PLUS (#b8bb26, trit=1)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Latest Increment ID | 13 |
| Total Repo Snapshots | 945 |
| Sources Covered (cumulative) | 3 orgs + 8 users + 1 (this run) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — Latest Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid/gorj | sweep_complete | +1 | `#b8bb26` | **PLUS** |
| 12 | bmorphism (org) | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 11 | AustinCStone (user) | repo_sweep | -1 | `#cc241d` | **MINUS** |
| 10 | M1shaaa (user) | repo_sweep | +1 | `#b8bb26` | **PLUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain (full): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## Hamming Swarm Snapshot (2026-07-30)

### Aptos Wallet Balances (Mainnet, Ledger ~6525918040)

All 28 addresses probed. All returned 0 APT (accounts empty or CoinStore not initialized).

| World | APT Balance |
|-------|-------------|
| alice | 0.0 |
| bob | 0.0 |
| A–Z | 0.0 each |

**Total APT across swarm: 0.0 APT**

### Multisig Contract Probes

| Pair | Sigs Required | Healthy |
|------|---------------|---------|
| A-B | 2 | ✓ |
| A-G | 2 | ✓ |
| Y-Z | 2 | ✓ |
| S-T | 2 | ✓ |
| V-W | 2 | ✓ |

**5/5 multisig contracts healthy (all 2-of-2 threshold).**

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no JSON API exposed.** All API paths return the Next.js HTML shell. Market data unavailable without headless browser execution.

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

## Repo Counts by Source (cumulative)

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
| gorj (this run) | org | 1 |
| **TOTAL** | | **472** |

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
- **plurigrid/gorj**: This very repo — last pushed 2026-05-08 (MCP server + hooks for Clojure REPL)
- **Increment 12**: ERGODIC — sweep_complete closing the 4th full GF(3) cycle
- **Increment 13**: PLUS — 2026-07-30 sweep, all 5 multisig contracts healthy (2-of-2), 28 Aptos wallets at 0 APT, MNX SPA unavailable
