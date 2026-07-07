# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-07

## Sweep Metadata
- **Date:** 2026-07-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 103 |
| Total Repo Snapshots | 103 |
| Aptos Wallet Snapshots | 28 |
| Multisig Probes | 5 |
| MNX Markets | 0 (auth required) |
| GF(3) ERGODIC (trit=0, #d3869b) | 34 |
| GF(3) PLUS (trit=1, #b8bb26) | 35 |
| GF(3) MINUS (trit=-1, #cc241d) | 34 |

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
- **Orgs:** plurigrid, kubeflow, TeglonLabs
- **Users:** bmorphism, zubyul
- **Zubyul Social Graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 32 |
| bmorphism | user | 21 |
| kubeflow | org | 15 |
| zubyul | user | 11 |
| TeglonLabs | org | 5 |
| migalkin | user | 5 |
| AustinCStone | user | 5 |
| wasita | user | 3 |
| kristinezheng | user | 2 |
| DJedamski | user | 2 |
| M1shaaa | user | 2 |
| **TOTAL** | | **103** |

### Most Recently Pushed

| Repo | Pushed At | Stars |
|------|-----------|-------|
| kubeflow/hub | 2026-07-07T11:06:36Z | 175 |
| kubeflow/sdk | 2026-07-07T10:49:12Z | 123 |
| plurigrid/gorj | 2026-07-07T10:15:32Z | 0 (1033 issues) |
| kubeflow/community-distribution | 2026-07-07T08:37:48Z | 1028 |
| kubeflow/katib | 2026-07-07T06:24:11Z | 1690 |
| kubeflow/pipelines | 2026-07-07T04:09:59Z | 4169 |
| wasita/wasita.github.io | 2026-07-06T23:51:09Z | 1 |
| bmorphism/Gay.jl | 2026-07-07T00:35:36Z | 2 (187 issues) |
| plurigrid/place | 2026-07-07T03:10:28Z | 1 |

### Top Repos by Stars

| Repo | Language | Stars |
|------|----------|-------|
| kubeflow/kubeflow | — | 15,769 |
| kubeflow/pipelines | Python | 4,169 |
| kubeflow/spark-operator | Python | 3,132 |
| kubeflow/trainer | Go | 2,129 |
| kubeflow/katib | Python | 1,690 |
| kubeflow/examples | Jsonnet | 1,460 |
| migalkin/NodePiece | Python | 144 |
| AustinCStone/TextGAN | Python | 92 |
| migalkin/StarE | Python | 89 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 |
| plurigrid/gorj | Clojure | 0 (1033 open issues!) |

### Notable Highlights

- **bmorphism/Gay.jl** — 187 open issues, pushed 2026-07-07 (very active)
- **plurigrid/gorj** — 1033 open issues; this very repo
- **bmorphism/ocaml-mcp-sdk** — 61★, OCaml MCP SDK using Jane Street's oxcaml_effect library
- **bmorphism/anti-bullshit-mcp-server** — 23★, claim analysis + manipulation detection
- **migalkin/NodePiece** — 144★, ICLR'22 knowledge graph embeddings
- **AustinCStone/bmfork** — fork of bmorphism repo (social graph connection)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 addresses (alice, bob, A–Z) returned **0.0 APT** on Aptos mainnet.
Accounts either hold no APT or have not been funded.

| Label | Address | Balance |
|-------|---------|---------|
| alice | 0xc793acdec12b4a63... | 0.0 APT |
| bob | 0x0a3c00c58fdf9020... | 0.0 APT |
| A–Z | (26 addresses) | 0.0 APT each |

### Multisig Contract Probes

All 5 Aptos multisig contracts respond to `0x1::multisig_account::num_signatures_required` and are **healthy**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ healthy |
| V-W | 0x40fad7b423a84365... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

The `/api/markets` endpoint returned **Vercel authentication required** (HTTP 200 with auth gate HTML, no JSON data). Market data unavailable without `x-vercel-protection-bypass` token or Trusted Source OIDC. `mnx_snapshots` table is empty.

---

## GF(3) Color Chain Distribution

| Name | Color | Trit | Count | Rule |
|------|-------|------|-------|------|
| ERGODIC | #d3869b | 0 | 34 | id % 3 == 0 |
| PLUS | #b8bb26 | 1 | 35 | id % 3 == 1 |
| MINUS | #cc241d | -1 | 34 | id % 3 == 2 |

---

## DuckDB Schema

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
