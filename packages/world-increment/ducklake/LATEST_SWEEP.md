# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-05

## Sweep Metadata
- **Date:** 2026-07-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 296 |
| Total Repo Snapshots | 296 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` (rose) | 98 |
| 1 | PLUS | `#b8bb26` (yellow-green) | 99 |
| −1 | MINUS | `#cc241d` (red) | 99 |
| | **TOTAL** | | **296** |

GF(3) assignment: `id%3==0 → ERGODIC`, `id%3==1 → PLUS`, `id%3==2 → MINUS`

---

## Top Repos by Stars (2026-07-05)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/kubeflow | 15,761 | — | 2026-07-04 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-04 |
| kubeflow/spark-operator | 3,132 | Python | 2026-07-03 |
| kubeflow/trainer | 2,129 | Go | 2026-07-05 |
| kubeflow/katib | 1,689 | Python | 2026-07-03 |
| kubeflow/examples | 1,460 | Jsonnet | 2026-06-16 |
| kubeflow/community-distribution | 1,028 | YAML | 2026-07-03 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml | 2026-03-16 |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | 2026-01-16 |
| plurigrid/asi | 28 | HTML | 2026-06-29 |

## Source Breakdown

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 20 |
| migalkin | user (social) | 5 |
| wasita | user (social) | 4 |
| AustinCStone | user (social) | 4 |
| TeglonLabs | org | 5 |
| DJedamski | user (social) | 3 |
| kristinezheng | user (social) | 3 |
| M1shaaa | user (social) | 3 |
| **TOTAL** | | **296** |

## Notable Activity (pushed 2026-07-05)
- `plurigrid/gorj` — forj + Rama topology nREPL routing + GF(3) gay trit coloring (979 open issues!)
- `kubeflow/trainer` — Distributed AI Model Training and LLM Fine-Tuning on Kubernetes
- `kubeflow/sdk` — Universal Python SDK for AI workloads on Kubernetes
- `kubeflow/docs-agent` — Kubeflow Documentation AI Agent
- `wasita/wasita.github.io` — personal website (Svelte + SvelteKit + Tailwind)
- `bmorphism/Gay.jl` — Wide-gamut color sampling with splittable determinism

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Queried 28 addresses (alice, bob, A–Z) via `https://fullnode.mainnet.aptoslabs.com/v1`.  
All 28 returned **0.0 APT** — accounts appear uninitialized or `CoinStore<AptosCoin>` resource not registered on mainnet.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C–Z | (22 more) | 0.0 each |

### Multisig Contract Probes

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`:

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✅ |
| A-G | 0xf56c…0096 | 2 | ✅ |
| Y-Z | 0xd3ff…b883 | 2 | ✅ |
| S-T | 0x3b1c…7883 | 2 | ✅ |
| V-W | 0x40fa…eb6d | 2 | ✅ |

All 5 multisigs are healthy 2-of-N.

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — Vercel deployment protection returns HTTP 401 (visitor password required). No market data accessible without credentials.

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
