# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-26

## Sweep Metadata
- **Date:** 2026-07-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 1009 |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| Sources Covered | 3 orgs + 8 users + social graph |

---

## GF(3) Color Chain — Current Increment

Increment #24: trit=0, color=#d3869b, name=**ERGODIC**

GF(3) assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

### GF(3) Repo Snapshot Distribution (1009 total)

| Trit | Color | Name | Repo Count |
|------|-------|------|------------|
| 0 | #d3869b | ERGODIC | 336 |
| 1 | #b8bb26 | PLUS | 337 |
| -1 | #cc241d | MINUS | 336 |

---

## JOB 1: GitHub Social Graph Sweep

### Repo Counts by Source

| Source | Type | Repos Found | Retrieved |
|--------|------|-------------|-----------|
| plurigrid | org | 103 | 100 |
| kubeflow | org | 49 | 49 |
| TeglonLabs | org | 5 | 5 |
| bmorphism | user | 106 | 100 |
| zubyul | user | 49 | 49 |
| migalkin | social-graph | 19 | 19 |
| DJedamski | social-graph | 6 | 6 |
| wasita | social-graph | 12 | 12 |
| kristinezheng | social-graph | 5 | 5 |
| M1shaaa | social-graph | 8 | 8 |
| AustinCStone | social-graph | 41 | 30 |

### Most Active Repos (pushed July 2026)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| plurigrid/gorj | Clojure | 1 | 2026-07-26 |
| plurigrid/eirobri | Clojure | 0 | 2026-07-21 |
| plurigrid/place | TeX | 1 | 2026-07-14 |
| plurigrid/asi | HTML | 31 | 2026-07-10 |
| kubeflow/pipelines | Python | 4170 | 2026-07-25 |
| kubeflow/spark-operator | Python | 3143 | 2026-07-25 |
| kubeflow/trainer | Go | 2153 | 2026-07-25 |
| kubeflow/kale | Python | 697 | 2026-07-25 |
| kubeflow/kubeflow | — | 15794 | 2026-07-10 |
| bmorphism/Gay.jl | Julia | 2 | 2026-07-25 |
| wasita/wasita.github.io | Svelte | 1 | 2026-07-21 |
| migalkin/kgcourse2021 | HTML | 24 | 2026-07-10 |
| AustinCStone/byteruckus | HTML | 0 | 2026-07-15 |
| zubyul/from-possible-worlds | TeX | 0 | 2026-07-18 |
| TeglonLabs/jank-crane | C++ | 0 | 2026-06-08 |

### Notable Stars

| Repo | Stars | Notes |
|------|-------|-------|
| kubeflow/kubeflow | 15794 | Flagship ML platform for Kubernetes |
| kubeflow/pipelines | 4170 | Most popular ML pipeline |
| kubeflow/spark-operator | 3143 | K8s Spark operator |
| kubeflow/trainer | 2153 | Distributed training |
| kubeflow/katib | 1692 | AutoML on Kubernetes |
| migalkin/NodePiece | 144 | Parameter-efficient KG representations |
| AustinCStone/TextGAN | 92 | GAN for text generation (TensorFlow) |
| migalkin/StarE | 89 | Hyper-relational knowledge graphs |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml SDK for MCP (Jane Street oxcaml) |
| bmorphism/risc0-cosmwasm-example | 23 | CosmWasm + zkVM RISC-V |
| bmorphism/say-mcp-server | 20 | macOS TTS via MCP |
| bmorphism/anti-bullshit-mcp-server | 22 | Claim validation MCP server |
| plurigrid/asi | 31 | Topological chemputer |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-26)

All 28 wallets queried via `fullnode.mainnet.aptoslabs.com`. All returned **0.0 APT** — accounts are uninitialized or have zero `0x1::aptos_coin::AptosCoin` CoinStore balance.

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| alice | 0xc793… | 0.0 |
| bob | 0x0a3c… | 0.0 |
| A–Z (26 wallets) | 0x8699…7af0 | 0.0 each |

**Total APT across swarm: 0.0**

### Multisig Contract Probes (Aptos mainnet)

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4… | 2 | ✓ healthy |
| A-G | 0xf56c… | 2 | ✓ healthy |
| Y-Z | 0xd3ff… | 2 | ✓ healthy |
| S-T | 0x3b1c… | 2 | ✓ healthy |
| V-W | 0x40fa… | 2 | ✓ healthy |

**All 5 multisig contracts healthy — 2-of-2 signature threshold**

### MNX Markets (testnet.mnx.fi)

- `/api/markets` → HTTP 404
- Root `https://testnet.mnx.fi` → SPA renders ticker label "MNX" only, no embedded market data
- **Status: unavailable** — recorded in `mnx_snapshots` with NULL price/change_pct

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

## Notes
- kubeflow/kubeflow star count: +229 since 2026-04-12 sweep (15565→15794)
- kubeflow/pipelines: +51 stars since last sweep
- plurigrid/gorj open issues jumped to 1404 (active dev)
- bmorphism/Gay.jl still leading bmorphism open issue count (188 issues)
- All Aptos hamming-swarm wallets show 0.0 APT — consistent with prior sweeps
