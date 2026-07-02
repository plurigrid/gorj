# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-02

## Sweep Metadata
- **Date:** 2026-07-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB:** 1.5.4 (pip)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1 — GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Top Stars |
|--------|------|-------------------|-----------|
| plurigrid | org | 30 | ontology(8), vcg-auction(7), agent(5) |
| kubeflow | org | 15 | kubeflow(15756), pipelines(4167), spark-operator(3130) |
| TeglonLabs | org | 5 | mathpix-gem(2) |
| bmorphism | user | 18 | ocaml-mcp-sdk(61), say-mcp-server(20), babashka-mcp-server(19) |
| zubyul | user | 12 | gay-world(1), WGCNA(2), Nikolova_lab(2) |
| migalkin | social | 5 | NodePiece(144), StarE(89), NBFNet_mlx(10) |
| DJedamski | social | 2 | Kaggle(1) |
| wasita | social | 4 | magic-garden(2), send2kobo(1) |
| kristinezheng | social | 2 | (0 stars) |
| M1shaaa | social | 2 | (0 stars) |
| AustinCStone | social | 3 | TextGAN(92), StereoVisionMRF(11) |

**Total repos snapshotted: 98**

### GF(3) Trit Distribution (id%3)

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | #d3869b | ERGODIC | 33 |
| 1 | #b8bb26 | PLUS | 33 |
| -1 | #cc241d | MINUS | 32 |

### Notable Activity (as of 2026-07-02)

- **plurigrid/gorj** — pushed today (913 open issues, active GF3 work)
- **plurigrid/eirobri** — pushed 2026-06-30 (EiRoBri replay world)
- **plurigrid/place** — pushed 2026-06-29 (TeX, 12 open issues)
- **plurigrid/asi** — pushed 2026-06-29 (HTML, 29★, topological chemputer)
- **kubeflow/pipelines** — pushed 2026-07-02 (4167★, MLOps core)
- **kubeflow/trainer** — pushed 2026-07-02 (2128★, distributed AI training)
- **bmorphism/Gay.jl** — pushed 2026-06-20 (2★, 187 issues, wide-gamut SPI)
- **wasita/wasita.github.io** — pushed 2026-07-02 (Svelte, active)
- **kristinezheng.github.io** — pushed 2026-07-01 (HTML, active)

---

## JOB 2 — Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-02)

Queried via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/...`  
All 28 addresses (alice, bob, A–Z) returned **0.0 APT** — empty or uninitialized `CoinStore<AptosCoin>` resources.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A–Z | 26 addresses | 0.0 each |

### Multisig Contract Probes — 5/5 HEALTHY

`0x1::multisig_account::num_signatures_required` probed on 5 contracts:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | ✓ HEALTHY |
| A-G | 0xf56c…0096 | 2 | ✓ HEALTHY |
| Y-Z | 0xd3ff…b883 | 2 | ✓ HEALTHY |
| S-T | 0x3b1c…7883 | 2 | ✓ HEALTHY |
| V-W | 0x40fa…eb6d | 2 | ✓ HEALTHY |

All require 2-of-N signatures — consistent, healthy m-of-n Aptos multisig configuration.

### MNX Markets (testnet.mnx.fi)

**UNAVAILABLE** — Vercel deployment auth required. No market data extractable without bypass token.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 98 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 98 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
