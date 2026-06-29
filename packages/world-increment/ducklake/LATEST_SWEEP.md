# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-29

## Sweep Metadata
- **Date:** 2026-06-29
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts (cumulative ducklake)

| Metric | Value |
|--------|-------|
| Total World Increments | 168 |
| Total Repo Snapshots | 1089 |
| New this sweep | 145 increments |
| Sources Covered | 3 orgs + 2 users + 6 social-graph |

---

## JOB 1: GitHub Social Graph Sweep

### Repos captured this sweep (145 total)

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 30 |
| kubeflow | org | 30 |
| bmorphism | user | 30 |
| zubyul | user | 30 |
| TeglonLabs | org | 5 |
| migalkin | social-graph | 5 |
| DJedamski | social-graph | 3 |
| wasita | social-graph | 3 |
| kristinezheng | social-graph | 3 |
| M1shaaa | social-graph | 3 |
| AustinCStone | social-graph | 3 |

### Notable repos (by stars)

| Repo | Language | Stars | Forks | Last pushed |
|------|----------|-------|-------|-------------|
| migalkin/NodePiece | Python | 144 | 21 | 2021-06-14 |
| AustinCStone/TextGAN | Python | 92 | 30 | 2016-09-19 |
| migalkin/StarE | Python | 89 | 16 | 2020-09-17 |
| migalkin/kgcourse2021 | HTML | 25 | 9 | 2020-09-01 |
| AustinCStone/StereoVisionMRF | Python | 11 | 4 | 2016-01-10 |
| migalkin/NBFNet_mlx | Python | 10 | 1 | 2024-03-01 |
| migalkin/RWL | Python | 8 | 1 | 2022-11-30 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 | 2026-01-01 |
| wasita/magic-garden | Python | 2 | 1 | 2025-12-10 |

### Recently active (TeglonLabs)

- **TeglonLabs/jank-crane** (C++): crane-jank converged-IR hub: loopify pass spec, GF3 maps — pushed **2026-06-08**
- **TeglonLabs/mathpix-gem** (Ruby): LaTeX/SMILES/Markdown OCR — pushed 2026-01-01
- **TeglonLabs/coin-flip-mcp** (JS): random.org MCP coins — pushed 2025-09-21

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

**Result: All 28 addresses returned Resource Not Found** — `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` not registered. Accounts are uninitialized on-chain.

| World | Balance APT |
|-------|-------------|
| alice | null (uninitialized) |
| bob | null (uninitialized) |
| A–Z (26 addresses) | null (all uninitialized) |

### Multisig Contract Probes (Aptos Mainnet)

All 5 contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428...87003 | 2 | ✓ |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ |
| V-W | 0x40fad7b4...eb6d | 2 | ✓ |

**5/5 multisigs healthy — all require 2-of-N signatures.**

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — HTTP 401 (Vercel authentication wall). No public API access. No market data captured.

---

## GF(3) Color Chain — This Sweep

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC** (49 increments)
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=**PLUS** (48 increments)
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS** (48 increments)

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

## Notable Highlights (all-time)
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,119 stars — most popular ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml SDK for Model Context Protocol
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs in TensorFlow
- **TeglonLabs/jank-crane**: newest push (2026-06-08) — GF3 convergence maps + loopify pass
- **All 5 multisigs**: healthy, 2-of-N, active on Aptos mainnet
- **Hamming swarm wallets**: 28 addresses probed, all awaiting on-chain initialization
