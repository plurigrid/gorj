# World-Increment Sweep + Hamming Swarm Snapshot — 2026-06-27

## Sweep Metadata
- **Date:** 2026-06-27
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 314 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Addresses Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Vercel auth) |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name | Hash |
|----|--------|------|-----------|-------|------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** | 51a45b3150ad |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** | 799563f1a8f6 |
| 3  | bmorphism | user | 0 | `#d3869b` | **ERGODIC** | 272bd3bac505 |
| 4  | zubyul | user | +1 | `#b8bb26` | **PLUS** | 0ab0d49173d0 |
| 5  | TeglonLabs | org | -1 | `#cc241d` | **MINUS** | 280679739c02 |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** | b0701e71ef37 |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** | 33bb9a4ac823 |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** | 09f8f167e966 |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** | e4c60469204a |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** | bd0e163dc7d4 |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** | ad9f00aa7ba5 |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 of 101 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| place | TeX | 0 | 2026-06-27 |
| asi | HTML | 26 | 2026-06-26 |
| eirobri | Clojure | 0 | 2026-06-23 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15748 | 2026-06-18 |
| pipelines | Python | 4157 | 2026-06-27 |
| spark-operator | Python | 3129 | 2026-06-26 |
| trainer | Go | 2124 | 2026-06-26 |
| katib | Python | 1687 | 2026-06-23 |

### TeglonLabs (5 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| jank-crane | C++ | 0 | 2026-06-08 |
| mathpix-gem | Ruby | 2 | 2026-01-01 |
| coin-flip-mcp | JavaScript | 0 | 2025-09-21 |
| monad-mcp-server | — | 0 | 2025-05-14 |
| topoi | Python | 0 | 2025-01-24 |

### bmorphism (100 of 105 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| Gay.jl | Julia | 2 | 2026-06-27 |
| satreadout | HTML | 0 | 2026-06-20 |
| bci-preview | HTML | 0 | 2026-06-20 |

### zubyul (49 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| voice-observatory | Python | 0 | 2026-04-24 |
| ghostel-emacs-worlds | GLSL | 0 | 2026-04-24 |
| nash-tui | Rust | 0 | 2026-04-13 |

### migalkin (19 repos — knowledge graphs / ML)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| NodePiece | Python | 144 | 2026-05-07 |
| StarE | Python | 89 | 2026-04-16 |
| kgcourse2021 | HTML | 25 | 2026-02-16 |
| NBFNet_mlx | Python | 10 | 2026-03-11 |

### AustinCStone (40 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| TextGAN | Python | 92 | 2025-03-03 |
| StereoVisionMRF | Python | 11 | 2026-04-01 |
| SpectralClustering | Python | 3 | 2021-04-16 |

---

## Repo Counts by Source

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| zubyul | user | 49 |
| AustinCStone | user | 40 |
| migalkin | user | 19 |
| wasita | user | 11 |
| TeglonLabs | org | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| kristinezheng | user | 5 |
| **TOTAL** | | **314** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses queried against `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result: All 28 addresses show 0.00000000 APT.**

Addresses exist on-chain but hold no liquid APT in the CoinStore resource. Full address list stored in `aptos_snapshots` table.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A–Z   | (26 addresses) | 0.0 each |

### Multisig Contract Probes

All 5 multisig contracts healthy — all require 2-of-N signatures (`num_signatures_required`):

| Pair | Address | Sigs Required | Healthy |
|------|---------|--------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Unavailable.** `testnet.mnx.fi` requires Vercel deployment authentication. No market data could be retrieved. `mnx_snapshots` table has 0 rows.

---

## Schema
```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)           -- 11 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)           -- 314 rows

aptos_snapshots(timestamp, world, address, balance_apt)  -- 28 rows
multisig_probes(timestamp, pair, address, sigs_required, healthy)  -- 5 rows
mnx_snapshots(timestamp, ticker, name, category, price, change_pct) -- 0 rows
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights (2026-06-27)
- **kubeflow/kubeflow**: 15,748 stars — flagship ML platform, active as of 2026-06-18
- **kubeflow/pipelines**: 4,157 stars — pushed today (2026-06-27)
- **migalkin/NodePiece**: 144 stars — scalable KG embeddings (ICLR'22), pushed 2026-05-07
- **AustinCStone/TextGAN**: 92 stars — TF text generation GAN
- **plurigrid/asi**: 26 stars — pushed 2026-06-26, most active plurigrid repo
- **TeglonLabs/jank-crane**: C++ repo for GF3 convergence maps — pushed 2026-06-08
- **Hamming swarm**: All 28 addresses at 0 APT; all 5 multisig pairs require 2 sigs (healthy)
