# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-05

## Sweep Metadata
- **Date:** 2026-06-05
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 332 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul | user | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | org | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | social | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita | social | +1 | `#b8bb26` | **PLUS** |
| 8  | AustinCStone | social | -1 | `#cc241d` | **MINUS** |
| 9  | DJedamski | social | 0 | `#d3869b` | **ERGODIC** |
| 10 | kristinezheng | social | +1 | `#b8bb26` | **PLUS** |
| 11 | M1shaaa | social | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,706 | 2,670 |
| kubeflow/pipelines | Python | 4,152 | 2,007 |
| kubeflow/spark-operator | Python | 3,125 | 1,488 |
| kubeflow/trainer | Go | 2,111 | 964 |
| kubeflow/katib | Go | 1,684 | 640 |
| kubeflow/manifests | Shell | 1,020 | 597 |
| migalkin/NodePiece | Python | 144 | 21 |
| AustinCStone/TextGAN | Python | 92 | 30 |
| migalkin/StarE | Python | 89 | 16 |
| migalkin/kgcourse2021 | HTML | 25 | 9 |
| AustinCStone/StereoVisionMRF | Python | 11 | 4 |
| TeglonLabs/mathpix-gem | Ruby | 2 | 0 |

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 (capped) |
| bmorphism | user | 100 (capped) |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | social | 6 |
| migalkin | social | 6 |
| wasita | social | 6 |
| TeglonLabs | org | 4 |
| DJedamski | social | 4 |
| kristinezheng | social | 4 |
| M1shaaa | social | 5 |
| **TOTAL** | | **332** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Probed via `fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793…cc7b | 0.0 |
| bob | 0x0a3c…2d5d | 0.0 |
| A | 0x8699…9d7a | 0.0 |
| B | 0x3f89…b13 | 0.0 |
| C | 0x38b9…35e | 0.0 |
| D | 0xf776…dd1 | 0.0 |
| E | 0xdc1d…d36 | 0.0 |
| F | 0x18a1…f71 | 0.0 |
| G | 0x69a3…f32 | 0.0 |
| H | 0xce67…00f | 0.0 |
| I | 0x070f…fc9 | 0.0 |
| J | 0x4d96…f54 | 0.0 |
| K | 0xa732…dc4 | 0.0 |
| L | 0x7c2e…ba9 | 0.0 |
| M | 0x6fed…e9 | 0.0 |
| N | 0xe7dd…b2c | 0.0 |
| O | 0x7325…89d | 0.0 |
| P | 0x6218…948 | 0.0 |
| Q | 0xac40…a9 | 0.0 |
| R | 0x7ce6…e10 | 0.0 |
| S | 0xb875…386 | 0.0 |
| T | 0x3578…588 | 0.0 |
| U | 0x7586…956 | 0.0 |
| V | 0xb59d…b3 | 0.0 |
| W | 0x5f32…b0 | 0.0 |
| X | 0xa95c…47d | 0.0 |
| Y | 0xd8e3…c4 | 0.0 |
| Z | 0x7af0…97c | 0.0 |

**Note:** All addresses return 0 APT for `CoinStore<AptosCoin>`. Accounts may hold other fungible assets or be unfunded/non-existent on mainnet.

### Multisig Contract Probes

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4…003 | **2** | ✅ healthy |
| A-G | 0xf56c…096 | **2** | ✅ healthy |
| Y-Z | 0xd3ff…883 | **2** | ✅ healthy |
| S-T | 0x3b1c…883 | **2** | ✅ healthy |
| V-W | 0x40fa…b6d | **2** | ✅ healthy |

All 5/5 multisig contracts are live on mainnet and require **2-of-N signatures**.

### MNX Markets

`https://testnet.mnx.fi` → **HTTP 401 Unauthorized** — requires authentication. No market data available.

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 ⭐ — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,152 ⭐ — ML pipeline for Kubernetes
- **migalkin/NodePiece**: 144 ⭐ — scalable knowledge graph embeddings (ICLR'22)
- **migalkin/StarE**: 89 ⭐ — hyper-relational KG message passing (EMNLP 2020)
- **AustinCStone/TextGAN**: 92 ⭐ — text generation with GANs in TensorFlow
- **wasita/wasita.github.io**: active Svelte personal site (updated 2026-06-01)
- **TeglonLabs/mathpix-gem**: Ruby gem for mathematical OCR
- **All 5 multisigs**: healthy, requiring 2 signatures each
