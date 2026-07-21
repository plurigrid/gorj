# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-21

**Timestamp:** 2026-07-21T09:10:00Z  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos Captured | Total Stars | Languages |
|--------|------|---------------|-------------|-----------|
| kubeflow | org | 49 | 34,399 | Go, Python, TypeScript, YAML, Jsonnet, … |
| migalkin | user (social) | 5 | 275 | Python, HTML |
| bmorphism | user | 100 | 246 | Clojure, Rust, Haskell, Python, Move, Zig, … |
| AustinCStone | user (social) | 3 | 103 | Python, HTML |
| plurigrid | org | 100 | 83 | Clojure, Rust, Haskell, Python, Racket, Zig, … |
| zubyul | user | 49 | 14 | Clojure, Rust, Haskell, TypeScript, Move, … |
| wasita | user (social) | 4 | 3 | Svelte, Python |
| TeglonLabs | org | 5 | 2 | C++, JavaScript, Python, Ruby |
| DJedamski | user (social) | 2 | 1 | Jupyter Notebook |
| M1shaaa | user (social) | 2 | 0 | TypeScript |
| kristinezheng | user (social) | 2 | 0 | HTML, Jupyter Notebook |

**Total:** 321 repos snapshotted → 321 world_increments created

### Top 15 Repos by Stars
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,787 | – | 2026-07-10 |
| kubeflow/pipelines | 4,169 | Python | 2026-07-21 |
| kubeflow/spark-operator | 3,142 | Python | 2026-07-17 |
| kubeflow/trainer | 2,152 | Go | 2026-07-20 |
| kubeflow/katib | 1,692 | Python | 2026-07-20 |
| kubeflow/examples | 1,460 | Jsonnet | 2025-04-14 |
| kubeflow/community-distribution | 1,029 | YAML | 2026-07-21 |
| kubeflow/arena | 815 | Go | 2026-07-21 |
| kubeflow/kale | 695 | Python | 2026-07-16 |
| kubeflow/mpi-operator | 530 | Go | 2026-07-20 |
| kubeflow/fairing | 337 | Jsonnet | 2022-04-11 |
| kubeflow/pytorch-operator | 310 | Jsonnet | 2021-12-01 |
| kubeflow/community | 195 | Jupyter Notebook | 2026-07-16 |
| kubeflow/website | 184 | HTML | 2026-07-20 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |

### Notable Highlights
- **TeglonLabs/jank-crane** (C++): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" — pushed 2026-06-08
- **migalkin/NodePiece** (Python, 144★): ICLR'22 compositional KG representations — recently active
- **AustinCStone/TextGAN** (Python, 92★): TF text GAN, ongoing citations
- **wasita/wasita.github.io** (Svelte): personal site pushed 2026-07-20 — most recent activity in social graph
- **kubeflow/arena + community-distribution + pipelines**: all pushed 2026-07-21 — active release day

### GF(3) Color Chain Distribution (this sweep, 321 new increments)
| GF3 Name | Color | Count |
|----------|-------|-------|
| ERGODIC | #d3869b | 107 |
| PLUS | #b8bb26 | 107 |
| MINUS | #cc241d | 107 |

GF(3) chain perfectly balanced: 107 each across trit∈{0,+1,−1}

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
Queried 28 wallets (alice, bob, A–Z) via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**Result:** All 28 returned `resource_not_found`.  
**Interpretation:** These accounts likely use the Fungible Asset (FA) framework (post-AIP-21, `0x1::fungible_asset::FungibleStore`) rather than the legacy `CoinStore` module. Alternatively, accounts may not hold APT on mainnet. All addresses are syntactically valid Aptos accounts.

| World | Status |
|-------|--------|
| alice, bob | resource_not_found (FA or uninitialized) |
| A–Z (26 wallets) | resource_not_found |

### Multisig Contract Probes (5 pairs)
All 5 multisig contracts are **healthy and operational**:

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | 0x0da4f428a0c007da… | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406… | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a… | 2 | ✓ |
| V-W | 0x40fad7b423a84365… | 2 | ✓ |

All pairs require **2-of-2 signatures**. All contracts respond correctly to `0x1::multisig_account::num_signatures_required` view function.

### MNX Markets (testnet.mnx.fi)
**Status:** Unavailable — HTTP 401 from Vercel authentication layer. The testnet frontend requires Vercel deployment protection credentials. No market data captured this sweep.

---

## DuckDB Table Totals (cumulative)

| Table | New This Sweep | Cumulative |
|-------|---------------|------------|
| world_increments | 321 | see DB |
| repo_snapshots | 321 | see DB |
| aptos_snapshots | 28 | 28+ |
| multisig_probes | 5 | 5+ |
| mnx_snapshots | 0 | 0 |

---

## Schema Reference
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

---

*Generated by world-increment-sweep + hamming-swarm-snapshot agent, 2026-07-21*
