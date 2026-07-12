# World-Increment Sweep + Hamming Snapshot — 2026-07-12

## Sweep Metadata
- **Date:** 2026-07-12T13:00:00Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 363 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth) |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user-social) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski (user-social) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita (user-social) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user-social) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user-social) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user-social) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Repo Counts by Source

| Source | Type | Repos | Notable |
|--------|------|-------|---------|
| plurigrid | org | 100 | gorj (push 2026-07-12), asi (30⭐, push 2026-07-10) |
| kubeflow | org | 49 | kubeflow (15771⭐), pipelines (4169⭐, push 2026-07-12) |
| TeglonLabs | org | 5 | jank-crane (C++, GF3), mathpix-gem (2⭐) |
| bmorphism | user | 100 | ocaml-mcp-sdk (61⭐), say-mcp-server (20⭐) |
| zubyul | user | 49 | gay-world, tilelang-kernels |
| migalkin | user-social | 19 | NodePiece (144⭐), StarE (89⭐) |
| DJedamski | user-social | 6 | legacy data science (2014–2018) |
| wasita | user-social | 11 | active (push 2026-07-06), magic-garden (2⭐) |
| kristinezheng | user-social | 5 | MIT cognitive science, active site (push 2026-07-01) |
| M1shaaa | user-social | 8 | lab-bookshelf TypeScript |
| AustinCStone | user-social | 40 | TextGAN (92⭐), StereoVisionMRF (11⭐) |
| **TOTAL** | | **363** | |

### Notable Recent Activity (pushed 2026-07)

- `plurigrid/gorj` — 2026-07-12 (this repo, 1136 open issues)
- `kubeflow/mcp-server` — 2026-07-12 (MCP for Kubeflow, 20⭐, 29 forks)
- `kubeflow/pipelines` — 2026-07-12 (4169⭐, 2030 forks)
- `kubeflow/spark-operator` — 2026-07-12 (3137⭐)
- `plurigrid/asi` — 2026-07-10 (topological chemputer, 30⭐)
- `migalkin/kgcourse2021` — 2026-07-10 (Knowledge Graphs course)
- `wasita/wasita.github.io` — 2026-07-06 (Svelte personal site)
- `kristinezheng/kristinezheng.github.io` — 2026-07-01

### Top Repos by Stars (this sweep)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,771 | — | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-12 |
| kubeflow/spark-operator | 3,137 | Python | 2026-07-12 |
| kubeflow/trainer | 2,136 | Go | 2026-07-10 |
| kubeflow/katib | 1,690 | Python | 2026-07-10 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-11 |
| kubeflow/arena | 815 | Go | 2026-07-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-05-08 |
| plurigrid/asi | 30 | HTML | 2026-07-10 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-02-05 |
| bmorphism/say-mcp-server | 20 | JavaScript | 2026-03-19 |
| bmorphism/babashka-mcp-server | 19 | JavaScript | 2026-06-05 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet, 2026-07-12)

Endpoint: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|--------------|
| alice | 0xc793ac… | 0.0 |
| bob | 0x0a3c00… | 0.0 |
| A | 0x8699ed… | 0.0 |
| B | 0x3f892e… | 0.0 |
| C | 0x38b99e… | 0.0 |
| D | 0xf77656… | 0.0 |
| E | 0xdc1d9d… | 0.0 |
| F | 0x18a14b… | 0.0 |
| G | 0x69a394… | 0.0 |
| H | 0xce67c3… | 0.0 |
| I–Z (18 wallets) | — | 0.0 each |

**Total APT across all 28 Hamming swarm wallets: 0.0 APT**  
All CoinStore resources return `value: "0"` — wallets initialized but empty.

### Multisig Contract Probes

Endpoint: `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f4… | 2 | ✅ HEALTHY |
| A-G | 0xf56c4a… | 2 | ✅ HEALTHY |
| Y-Z | 0xd3ffe1… | 2 | ✅ HEALTHY |
| S-T | 0x3b1c3a… | 2 | ✅ HEALTHY |
| V-W | 0x40fad7… | 2 | ✅ HEALTHY |

All 5 multisig contracts are **live on Aptos mainnet**, all require **2-of-n signatures**.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection active (HTTP 401).  
Password-protected; no market data accessible without credentials.

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
