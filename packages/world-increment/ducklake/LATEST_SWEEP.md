# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-09

## Sweep Metadata
- **Date:** 2026-05-09
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Previous sweep:** 2026-04-12 (471 repos, 12 increments)

---

## Summary Counts

| Metric | Value | Delta vs 2026-04-12 |
|--------|-------|---------------------|
| Total World Increments | 17 | +5 |
| Total Repo Snapshots (distinct) | 508 | +37 |
| Sources Covered | 3 orgs + 14 users | +6 social-graph users |
| Aptos Wallets Probed | 28 | NEW (Hamming swarm) |
| Multisig Contracts Probed | 5 | NEW (Hamming swarm) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 17 Increments

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
| 13 | migalkin (social-graph) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 14 | DJedamski (social-graph) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 15 | wasita (social-graph) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 16 | kristinezheng (social-graph) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 17 | M1shaaa (social-graph) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain (continued): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### New This Sweep (2026-05-09 deltas)
| Repo | Language | Stars | Delta | Notes |
|------|----------|-------|-------|-------|
| kubeflow/kubeflow | — | 15,628 | +63★ | Active ML platform, pushed 2026-05-07 |
| kubeflow/pipelines | Python | 4,137 | +18★ | Pushed 2026-05-08 |
| kubeflow/spark-operator | Python | 3,125 | +14★ | Pushed 2026-05-08 |
| kubeflow/trainer | Go | 2,096 | +16★ | LLM fine-tuning on K8s |
| bmorphism/Gay.jl | Julia | 1 | — | 187 open issues, pushed 2026-05-09 |
| plurigrid/gorj | Clojure | 0 | — | 122 open issues, pushed today |
| migalkin/NodePiece | Python | 144 | +1★ | KG embedding ICLR'22 |

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
| migalkin (social) | user | 6 |
| DJedamski (social) | user | 4 |
| wasita (social) | user | 6 |
| kristinezheng (social) | user | 4 |
| M1shaaa (social) | user | 3 |
| AustinCStone (social) | user | 5 |
| **TOTAL (2026-05-09)** | | **508 distinct** |

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

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 worlds, mainnet)

Queried `fullnode.mainnet.aptoslabs.com` for `CoinStore<AptosCoin>` on each address.
All 28 Hamming-swarm wallets returned zero balance — the addresses exist on-chain
but no `CoinStore` resource has been initialized (never funded).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | `0xc793...4cc7b` | 0.00 |
| bob | `0x0a3c...512d5d` | 0.00 |
| A | `0x8699...e9d7a` | 0.00 |
| B | `0x3f89...cb13` | 0.00 |
| C | `0x38b9...535e` | 0.00 |
| D | `0xf776...fcfdd1` | 0.00 |
| E | `0xdc1d...8d36` | 0.00 |
| F | `0x18a1...c3cf71` | 0.00 |
| G | `0x69a3...c7f32` | 0.00 |
| H | `0xce67...5300f` | 0.00 |
| I | `0x070f...c1fc9` | 0.00 |
| J | `0x4d96...7f54` | 0.00 |
| K | `0xa732...425dc4` | 0.00 |
| L | `0x7c2e...7eba9` | 0.00 |
| M | `0x6fed...7f2e9` | 0.00 |
| N | `0xe7dd...551b2c` | 0.00 |
| O | `0x7325...5a89d` | 0.00 |
| P | `0x6218...ec948` | 0.00 |
| Q | `0xac40...c89a9` | 0.00 |
| R | `0x7ce6...76e10` | 0.00 |
| S | `0xb875...d0386` | 0.00 |
| T | `0x3578...3f4588` | 0.00 |
| U | `0x7586...f9956` | 0.00 |
| V | `0xb59d...af2c3` | 0.00 |
| W | `0x5f32...c7b0` | 0.00 |
| X | `0xa95c...3047d` | 0.00 |
| Y | `0xd8e3...2444c4` | 0.00 |
| Z | `0x7af0...e197c` | 0.00 |

**Total swarm APT: 0.00** — all wallets unfunded / no CoinStore initialized.

### Multisig Contract Probes

All five probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4...7003` | **2** | ✅ |
| A-G | `0xf56c...0096` | **2** | ✅ |
| Y-Z | `0xd3ff...b883` | **2** | ✅ |
| S-T | `0x3b1c...7883` | **2** | ✅ |
| V-W | `0x40fa...eb6d` | **2** | ✅ |

All 5 multisig accounts are healthy with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi/api/markets` returns the Next.js SPA HTML shell — no JSON API
endpoint is accessible without a browser runtime. Market data is **unavailable**
via direct HTTP probe. Recorded as placeholder in `mnx_snapshots`.

---

## Notable Highlights
- **kubeflow/kubeflow**: 15,628 stars (+63 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,137 stars (+18) — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,125 stars (+14) — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 144 stars (+1) — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/Gay.jl**: 187 open issues — widest active discussion in swarm social graph
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml SDK for MCP using Jane Street's oxcaml_effect
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs (TensorFlow)
- **plurigrid/asi**: 21 stars — topological chemputer, pushed 2026-04-26
- **plurigrid/gorj**: This very repo — 122 open issues, pushed today (2026-05-09)
- **Hamming swarm**: 28 Aptos wallets + 5 multisig pairs all probed — swarm unfunded, multisigs healthy
- **Increment 17**: MINUS — closes the 5th partial GF(3) cycle (ERGODIC closes at 18)
