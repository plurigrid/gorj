# World-Increment Sweep + Hamming Snapshot — 2026-07-03

## Sweep Metadata
- **Date:** 2026-07-03
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 319 |
| Sources Covered | 3 orgs + 8 users |

---

## GF(3) Color Chain — 11 Increments

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 1  | plurigrid (org) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 2  | bmorphism (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 3  | kubeflow (org) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs (org) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 7  | wasita (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 8  | DJedamski (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng (user) | repo_snapshot | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa (user) | repo_snapshot | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone (user) | repo_snapshot | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| (top 100 by update time — see repo_snapshots table) | | | |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15565+ | 2026-01-05 |
| pipelines | Python | 4119+ | 2026-04-10 |
| spark-operator | Python | 3111+ | 2026-04-10 |
| trainer | Go | 2080+ | 2026-04-10 |
| katib | Python | 1676+ | 2026-04-02 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 — GF3 convergence maps, loopify pass spec |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (100 repos)
| Repo | Language | Stars |
|------|----------|-------|
| (top 100 by update time — see repo_snapshots table) | | |

### Social Graph Highlights
| User | Repo | Stars | Language |
|------|------|-------|----------|
| migalkin | NodePiece | 144 | Python — ICLR'22 KG embeddings |
| migalkin | StarE | 89 | Python — EMNLP'20 hyper-relational KGs |
| AustinCStone | TextGAN | 92 | Python — GAN text generation |
| AustinCStone | StereoVisionMRF | 11 | Python — depth from stereo |
| wasita | wasita.github.io | 1 | Svelte — pushed 2026-07-02 |

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| migalkin | user (social) | 5 |
| wasita | user (social) | 3 |
| AustinCStone | user (social) | 3 |
| DJedamski | user (social) | 2 |
| kristinezheng | user (social) | 2 |
| M1shaaa | user (social) | 2 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **319** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet — 28 addresses)

All 28 addresses (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

**Result: All balances = 0.00000000 APT**

These wallets appear to be unfunded or not yet initialized on Aptos mainnet. The `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource returned 0 for all accounts.

| World | Address (truncated) | Balance APT |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — 5/5 Healthy ✓

All 5 multisig contracts on mainnet responded successfully; each requires **2 of N signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status: Unavailable — HTTP 401 Unauthorized**

Both `https://testnet.mnx.fi` and `https://testnet.mnx.fi/api/markets` returned 401. Testnet appears gated behind authentication. No market data extracted; `mnx_snapshots` table is empty this sweep.

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

## Notable Highlights
- **kubeflow/kubeflow**: 15,565 stars — flagship ML platform for Kubernetes
- **migalkin/NodePiece**: 144 stars — parameter-efficient KG representations (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — GAN-based text generation in TensorFlow
- **migalkin/StarE**: 89 stars — hyper-relational KG embeddings (EMNLP'20)
- **TeglonLabs/jank-crane**: newest org repo (2026-06-08) — GF3 convergence maps + loopify pass spec
- **wasita/wasita.github.io**: most recently pushed social-graph repo (2026-07-02)
- **Hamming Swarm**: All 5 multisig contracts healthy (2-of-N threshold). All wallets unfunded.
- **MNX**: testnet gated (401) — no market data this sweep.
