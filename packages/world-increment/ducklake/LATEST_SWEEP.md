# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-06

## Sweep Metadata
- **Date:** 2026-06-06T07:12:51Z
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 56 |
| Total Repo Snapshots (cumulative) | 1334 |
| New Increments This Sweep | 33 |
| New Repos This Sweep | 390 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain — This Sweep (33 new increments, IDs 24–56)

Assignment rule:
- `id mod 3 == 0` → trit=0, color=#d3869b, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=**MINUS**

Sources this sweep: plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone + 22 event increments

---

## GitHub Social Graph — Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15706 | Jupyter Notebook |
| kubeflow/pipelines | 4152 | Python |
| kubeflow/training-operator | 1748 | Go |
| kubeflow/katib | 1517 | Go |
| migalkin/NodePiece | 143 | Python |
| migalkin/StarE | 88 | Python |
| AustinCStone/TextGAN | 92 | Python |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| plurigrid/asi | 25 | HTML |
| plurigrid/gorj | — | Clojure |

### Repo Counts by Source (this sweep)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **390** |

### Recent Events

- **bmorphism:** 15 repos with PushEvents — top: `bmorphism/Gay.jl`, `plurigrid/gorj`, `akshttdev/pcg-cc-mcp`, `bmorphism/world`, `bmorphism/oxgame`
- **zubyul:** 7 repos with PushEvents — top: `zubyul/jonikas_for_weronika.-annotated-code`, `plurigrid/gorj`, `zubyul/wasita_website`

---

## Hamming Swarm — Aptos Mainnet Snapshot

### Wallet Balances (28 addresses)

All 28 wallets (alice, bob, A–Z) returned `null` APT balance.  
**Reason:** `resource_not_found` for `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` — accounts exist but CoinStore not yet registered (no APT received).

| World | Address | APT Balance |
|-------|---------|-------------|
| alice | 0xc793...cc7b | null |
| bob | 0x0a3c...512d | null |
| A–Z | (26 addresses) | null |

### Multisig Contract Probes — 5/5 Healthy

All 5 multisig contracts require **2 signatures**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | healthy |
| A-G | 0xf56c...0096 | 2 | healthy |
| Y-Z | 0xd3ff...b883 | 2 | healthy |
| S-T | 0x3b1c...7883 | 2 | healthy |
| V-W | 0x40fa...eb6d | 2 | healthy |

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** (Vercel deployment protection, requires visitor bypass token).

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes (pushed 2026-06-06)
- **kubeflow/pipelines**: 4,152 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 143 stars — scalable KG embeddings, zubyul social graph
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **bmorphism/Gay.jl**: 189 open issues, most active bmorphism repo as of 2026-06-06
- **plurigrid/gorj**: 389 open issues, Clojure, pushed 2026-06-06 — this repo
- **Hamming swarm**: 5/5 multisigs healthy at 2-of-N; wallet CoinStores unregistered (new accounts)
