# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (cumulative DB)

| Metric | Value |
|--------|-------|
| Total World Increments | 34 (11 new this run) |
| Total Repo Snapshots | 1014 (70 new this run) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapshotted | 28 |
| Multisig Probes | 5 |

---

## GF(3) Color Chain — This Run (increments 24–34)

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 24 | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 25 | kubeflow | org | 1 | `#b8bb26` | **PLUS** |
| 26 | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 27 | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 28 | zubyul | user | 1 | `#b8bb26` | **PLUS** |
| 29 | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 30 | wasita | user | 0 | `#d3869b` | **ERGODIC** |
| 31 | AustinCStone | user | 1 | `#b8bb26` | **PLUS** |
| 32 | DJedamski | user | -1 | `#cc241d` | **MINUS** |
| 33 | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 34 | M1shaaa | user | 1 | `#b8bb26` | **PLUS** |

---

## Top Repos by Source (this run sample)

### plurigrid (103 repos discovered)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 31 | 2026-07-17 |
| gorj | Clojure | 1 | 2026-07-07 |
| ontology | JavaScript | 8 | 2026-05-09 |
| nash-portal | Rust | 2 | 2026-05-19 |
| vcg-auction | Rust | 7 | 2025-12-16 |

### kubeflow (49 repos discovered)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15779 | 2026-07-16 |
| pipelines | Python | 4168 | 2026-07-17 |
| spark-operator | Python | 3138 | 2026-07-17 |
| trainer | Go | 2151 | 2026-07-17 |
| katib | Python | 1690 | 2026-07-16 |

### bmorphism (106 repos discovered)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| anti-bullshit-mcp-server | JS | 22 | 2026-07-12 |
| penrose-mcp | JS | 9 | 2026-06-24 |
| Gay.jl | Julia | 2 | 2026-07-14 |
| risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |

### migalkin (19 repos discovered)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 24 | 2026-07-10 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

---

## Repo Counts by Source (this run)

| Source | Type | Repos discovered |
|--------|------|-----------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| DJedamski | user | 6 |
| **TOTAL** | | **~403** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses, Mainnet)

Query: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**All 28 addresses (alice, bob, A–Z) returned 0 APT via legacy CoinStore.**  
Note: `alice` (0xc793…cc7b) has `sequence_number=72` confirming it's an active account, but no `CoinStore<AptosCoin>` resource — likely uses the Fungible Asset (FA) standard (post-Aptos v1.6 migration). All others similarly returned 0 via the legacy coin store query path.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|--------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…12d5 | 0.0 |
| A–Z (26) | various | 0.0 each |

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|--------------|--------|
| A-B | 0x0da4…7003 | 2 | ✅ healthy |
| A-G | 0xf56c…0096 | 2 | ✅ healthy |
| Y-Z | 0xd3ff…b883 | 2 | ✅ healthy |
| S-T | 0x3b1c…7883 | 2 | ✅ healthy |
| V-W | 0x40fa…eb6d | 2 | ✅ healthy |

**All 5 multisig contracts healthy — 2-of-2 threshold on all pairs.**

### MNX Markets (testnet.mnx.fi)

❌ **Unavailable** — Vercel deployment protection active (HTTP 401). Requires visitor password or SSO. No market data extractable.

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

## Notable Highlights (2026-07-17)
- **kubeflow/pipelines**: 4,168 stars, pushed today — active ML pipeline infra
- **kubeflow/trainer**: 2,151 stars — LLM fine-tuning on Kubernetes, pushed today
- **bmorphism/ocaml-mcp-sdk**: 61 stars — OCaml MCP SDK using Jane Street oxcaml_effect
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22)
- **plurigrid/asi**: 31 stars, pushed today — topological chemputer
- **All 5 hamming-swarm multisigs**: healthy at 2-of-2
- **alice wallet**: active (seq=72) but on FA standard — 0 via legacy CoinStore
