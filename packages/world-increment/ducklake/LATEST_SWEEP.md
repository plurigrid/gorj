# World Increment Sweep + Hamming Swarm Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Increment ID:** 13 · GF3=PLUS · trit=+1 · color=#b8bb26
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### API Scope Note
GitHub API in this session is proxied and restricted to repository-scoped endpoints
for `plurigrid/gorj` only. Requests to external orgs/users (plurigrid org-wide, kubeflow,
TeglonLabs, bmorphism, zubyul, and their social graph) returned proxy 403. Only
the configured repo could be snapshotted this run.

### Accessible Repo: plurigrid/gorj
| Field | Value |
|---|---|
| full_name | plurigrid/gorj |
| language | Clojure |
| description | MCP server + hooks that give AI coding agents a Clojure REPL |
| last_pushed | 2026-05-08T14:04:34Z |
| last_commit | 5b28fe0 — chore: ignore duckdb binary in repo root |
| open sweep branches | 29 (world-increment/sweep-* from 2026-04-27 through 2026-04-30) |

### DuckDB State After Insert

| Table | Rows | Notes |
|---|---|---|
| world_increments | 24 | max id=13 |
| repo_snapshots | 945 | gorj snapshot added (id=474) |
| aptos_snapshots | 28 | all Hamming swarm wallets |
| multisig_probes | 5 | all pairs healthy |
| mnx_snapshots | 0 | SPA, no JSON data |

---

## GF(3) Color Chain — All 13 Increments

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
| 12 | bmorphism | sweep_complete | 0 | `#d3869b` | **ERGODIC** |
| 13 | plurigrid/gorj | sweep_complete | +1 | `#b8bb26` | **PLUS** ← current |

GF(3) chain: `PLUS → MINUS → ERGODIC` × 4 + **PLUS**

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-07-31)
All 28 addresses queried via `fullnode.mainnet.aptoslabs.com/v1`. All accounts have
`CoinStore<AptosCoin>` resource absent (`resource_not_found`) — on-chain accounts with
no funded APT balance.

| World | Balance (APT) |
|---|---|
| alice, bob, A–Z (all 28) | 0.00000000 |

**Total swarm APT:** 0.00000000

### Multisig Contract Probes (Mainnet — 2026-07-31)
All 5 contracts responded via `POST /v1/view → 0x1::multisig_account::num_signatures_required`.

| Pair | Address (short) | Sigs Required | Healthy |
|---|---|---|---|
| A-B | 0x0da4f428… | 2 | ✓ |
| A-G | 0xf56c4a1c… | 2 | ✓ |
| Y-Z | 0xd3ffe181… | 2 | ✓ |
| S-T | 0x3b1c3ae9… | 2 | ✓ |
| V-W | 0x40fad7b4… | 2 | ✓ |

**5/5 multisig contracts healthy** — all 2-of-2 threshold, all on-chain.

### MNX Markets (testnet.mnx.fi — 2026-07-31)
`GET /api/markets` returns Next.js SPA shell (no JSON). Market data: **unavailable this run**.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Prior Sweep Highlights (from id=1–12, 2026-04-12)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars
- **plurigrid/asi**: 16 stars — topological chemputer
