# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-25 (automated sweep)
**GF(3) Color Chain:** ERGODIC #d3869b · PLUS #b8bb26 · MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured | Total Stars |
|--------|------|----------------|-------------|
| kubeflow | org | 30 (of 49) | 100,862 |
| migalkin | user (social) | 5 top | 829 |
| bmorphism | user | 50 top | 377 |
| AustinCStone | user (social) | 3 top | 319 |
| plurigrid | org | 50 top | 138 |
| zubyul | user | 30 top | 28 |
| DJedamski | user (social) | 2 | 15 |
| TeglonLabs | org | 5 | 14 |
| wasita | user (social) | 4 | 9 |
| M1shaaa | user (social) | 2 | 0 |
| kristinezheng | user (social) | 2 | 0 |

**Total this sweep:** 183 repo snapshots → DuckDB (cumulative: 1,127 records)

### Notable Repos (Recent Activity)

- **plurigrid/asi** — `HTML` · ★31 · pushed 2026-07-10 — "everything is topological chemputer!"
- **wasita/wasita.github.io** — `Svelte` · pushed 2026-07-21 (most recent in social graph)
- **TeglonLabs/jank-crane** — `C++` · pushed 2026-06-08 — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps"
- **migalkin/NodePiece** — `Python` · ★144 · ICLR'22 knowledge graph embeddings
- **AustinCStone/TextGAN** — `Python` · ★92 · TF text generation GAN

### GF(3) Distribution (this sweep)
- **ERGODIC** (trit=0, #d3869b): 68 increments
- **PLUS** (trit=1, #b8bb26): 69 increments
- **MINUS** (trit=-1, #cc241d): 69 increments — balanced chain ✓

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) queried against Aptos mainnet CoinStore resource.

**Result:** All 28 wallets returned 0 APT balance. Addresses are either unfunded on mainnet or holdings are in staked/delegated form outside the base CoinStore.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f4... | 2 | ✓ |
| A-G | 0xf56c4a... | 2 | ✓ |
| Y-Z | 0xd3ffe1... | 2 | ✓ |
| S-T | 0x3b1c3a... | 2 | ✓ |
| V-W | 0x40fad7... | 2 | ✓ |

**Status: 5/5 multisig contracts healthy** — all requiring 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

- `https://testnet.mnx.fi/api/markets` → **404 Not Found**
- `https://testnet.mnx.fi` → SPA shell only (requires JavaScript; only "MNX" text visible)
- **Status: Unavailable** — `mnx_snapshots` table empty this sweep.

---

## DuckDB Ducklake State

**Path:** `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Records (cumulative) |
|-------|---------------------|
| world_increments | 206 |
| repo_snapshots | 1,127 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 |

---

## Action Items / Anomalies

1. **Aptos wallets all zero** — Hamming swarm addresses appear unfunded on mainnet. Verify if these are testnet-intended addresses or if APT is held in staked/delegated form.
2. **MNX testnet unavailable** — SPA requires JS rendering. Consider Playwright-based fetch for future sweeps.
3. **Multisig all 2-of-N** — Consistent threshold across all 5 pairs. No anomalies detected.
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
