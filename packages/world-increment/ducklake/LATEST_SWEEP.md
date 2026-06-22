# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-22

## Sweep Metadata
- **Date:** 2026-06-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (this run) | 88 |
| Total Repo Snapshots (DB cumulative) | 1,032 |
| Sources Covered | 4 orgs + 7 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### Top Repos by Stars (2026-06-22 snapshot)

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,740 | — | 2026-06-18 |
| kubeflow/pipelines | 4,157 | Python | 2026-06-22 |
| kubeflow/spark-operator | 3,128 | Python | 2026-06-18 |
| kubeflow/trainer | 2,118 | Go | 2026-06-22 |
| kubeflow/katib | 1,685 | Python | 2026-06-20 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,027 | YAML | 2026-06-18 |
| migalkin/NodePiece | 144 | Python | 2022-02-02 |
| AustinCStone/TextGAN | 92 | Python | 2016-10-04 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| plurigrid/asi | 26 | HTML | 2026-06-10 |
| migalkin/kgcourse2021 | 25 | HTML | 2025-08-04 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |

### Top Repos by Open Issues
| Repo | Open Issues | Language |
|------|-------------|----------|
| plurigrid/gorj | 742 | Clojure |
| bmorphism/Gay.jl | 187 | Julia |
| kubeflow/pipelines | 448 | Python |
| kubeflow/notebooks | 184 | — |
| kubeflow/docs-agent | 153 | Python |
| kubeflow/sdk | 133 | Python |

### Sources Queried
| Source | Type | Notable |
|--------|------|---------|
| plurigrid | org | 100+ repos, gorj (742 issues), asi (26★) |
| bmorphism | user | 105 repos, ocaml-mcp-sdk (61★), Gay.jl (187 issues) |
| zubyul | user | 49 repos, bioinformatics → Gay.jl/Plurigrid ecosystem |
| kubeflow | org | 48 repos, flagship ML-on-K8s platform |
| TeglonLabs | org | 5 repos, jank-crane (GF3 maps), mathpix-gem |
| DJedamski | user | 6 repos, Kaggle/Coursera ML work |
| wasita | user | 11 repos, Svelte/Python personal projects |
| kristinezheng | user | 5 repos, cognitive science/Lookit |
| M1shaaa | user | 8 repos, Lookit psychology research |
| migalkin | user | 19 repos, KG research (NodePiece, StarE) |
| AustinCStone | user | 40 repos, ML/CV (TextGAN, StereoVisionMRF) |

### GF(3) Color Chain (88 increments this run)
- **ERGODIC** #d3869b (trit=0): 30 increments
- **PLUS** #b8bb26 (trit=1): 29 increments
- **MINUS** #cc241d (trit=-1): 29 increments

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, mainnet)

**Result: All 28 wallets returned 0.00000000 APT**

Wallets probed: alice, bob, A–Z (full address list in `aptos_snapshots` table).
These appear to be unfunded or spent-out test wallets.

### Multisig Contract Probes

| Pair | Contract (prefix) | Sigs Required | Healthy |
|------|-------------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

**All 5 multisig contracts healthy — 2-of-2 threshold confirmed on Aptos mainnet.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Protected by Vercel deployment protection auth.
No market data accessible without bypass token.

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
- **kubeflow/kubeflow**: 15,740 stars (+175 since Apr 12) — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,157 stars (+38) — pushed today 2026-06-22
- **plurigrid/gorj**: 742 open issues — most active in plurigrid ecosystem by issues
- **bmorphism/Gay.jl**: 187 open issues — wide-gamut deterministic color sampling
- **bmorphism/ocaml-mcp-sdk**: 61 stars (+1) — OCaml SDK for Model Context Protocol
- **migalkin/NodePiece**: 144 stars (+1) — ICLR'22 knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars — GAN text generation
- **All multisigs**: 2-of-2 threshold, all responding on mainnet
- **Aptos swarm**: 28 wallets, all at 0 APT — likely unfunded test addresses
