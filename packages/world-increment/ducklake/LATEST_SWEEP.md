# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-26

## Sweep Metadata
- **Date:** 2026-06-26
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 322 |
| Total Repo Snapshots | 322 |
| Sources Covered | 3 orgs + 8 users (social graph) |

### Repo Counts by Source

| Source | Type | Repos | Total Stars | Latest Push |
|--------|------|-------|-------------|-------------|
| bmorphism | user | 100 | 247 | 2026-06-26T00:41:24Z |
| plurigrid | org | 100 | 77 | 2026-06-26T12:19:57Z |
| zubyul | user | 49 | 14 | 2026-04-24T05:56:17Z |
| kubeflow | org | 48 | 34257 | 2026-06-26T08:53:17Z |
| migalkin | social | 6 | 279 | 2025-08-04T03:01:46Z |
| TeglonLabs | org | 5 | 2 | 2026-06-08T19:03:03Z |
| wasita | social | 4 | 3 | 2026-06-25T16:23:37Z |
| M1shaaa | social | 3 | 0 | 2026-06-26T03:21:54Z |
| AustinCStone | social | 3 | 93 | 2026-02-11T01:10:54Z |
| kristinezheng | social | 2 | 0 | 2026-06-03T13:11:37Z |
| DJedamski | social | 2 | 2 | 2018-03-07T12:36:09Z |
| **TOTAL** | | **322** | **34974** | |

### GF(3) Color Chain Distribution

- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=**ERGODIC**
- `id mod 3 == 1` → trit=+1, color=`#b8bb26`, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=**MINUS**

| Name | Trit | Color | Count |
|------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 107 |
| PLUS | +1 | `#b8bb26` | 108 |
| MINUS | -1 | `#cc241d` | 107 |

### Notable Repos (2026-06-26 snapshot)

- **kubeflow/kubeflow** (34,257★) — flagship ML platform for Kubernetes; active push 2026-06-26
- **migalkin/NodePiece** (144★) — Compositional KG representations (ICLR'22)
- **migalkin/StarE** (89★) — Hyper-relational KG message passing (EMNLP'20)
- **AustinCStone/TextGAN** (92★) — GAN for text generation in TensorFlow
- **bmorphism/satreadout** — Machine-checked saturating non-Riemannian perceptual readout (Lean 4.28 + mathlib)
- **bmorphism/Gay.jl** (2★) — Wide-gamut color sampling w/ splittable determinism (Pigeons.jl SPI)
- **plurigrid/asi** (26★) — topological chemputer; pushed 2026-06-26
- **TeglonLabs/jank-crane** (C++) — crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps
- **wasita/wasita.github.io** (Svelte) — personal site, pushed 2026-06-25
- **M1shaaa/M1shaaa** — profile config, pushed 2026-06-26

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. CoinStore resource returned null for all addresses — accounts exist on-chain but APT CoinStore uninitialized (balance = 0.0 APT).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z (26) | 0x8699…7c | 0.0 each |

### Multisig Contract Probes

Queried via `POST /v1/view → 0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

All 5 multisigs require **2-of-N** signatures. All healthy.

### MNX Markets

`testnet.mnx.fi` — behind Vercel authentication wall. No market data accessible. Status: **UNAVAILABLE** (auth required).

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| `world_increments` | 322 |
| `repo_snapshots` | 322 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 0 (auth-gated) |

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
