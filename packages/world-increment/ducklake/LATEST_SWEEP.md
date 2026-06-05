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
| Total Repo Snapshots | 318 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 (alice, bob, A–Z) |
| Multisig Contracts Healthy | 5/5 |

---

## GF(3) Color Chain — All 11 Increments

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|------:|-----------|-------|------|
| 1  | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | 30 | -1 | `#cc241d` | **MINUS** |
| 3  | bmorphism | user | 100 | 0 | `#d3869b` | **ERGODIC** |
| 4  | zubyul | user | 49 | +1 | `#b8bb26` | **PLUS** |
| 5  | TeglonLabs | org | 4 | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 7 | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | 5 | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | 7 | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | 4 | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | 7 | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

## Top Repos by Source

### plurigrid (100 repos, pushed June 2026)
| Repo | Language | Stars | Pushed At |
|------|----------|------:|-----------|
| gorj | Clojure | 0 | 2026-06-05 |
| asi | HTML | 25 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 2026-04-25 |
| zig-syrup | Zig | 2 | 2026-04-30 |
| nash-portal | Rust | 2 | 2026-05-19 |
| ontology | JavaScript | 8 | 2025-05-27 |
| gay-rs | Rust | 0 | 2026-01-08 |

### kubeflow (30 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|------:|-----------|
| kubeflow | — | 15,706 | 2026-05-24 |
| pipelines | Python | 4,152 | 2026-06-05 |
| spark-operator | Python | 3,125 | 2026-06-04 |
| trainer | Go | 2,111 | 2026-06-05 |
| katib | Python | 1,684 | 2026-06-04 |
| manifests | YAML | 1,020 | 2026-06-05 |

### bmorphism (100 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|------:|-----------|
| Gay.jl | Julia | 1 | 2026-06-05 |
| world | Python | 0 | 2026-06-02 |
| oxgame | OCaml | 0 | 2026-05-15 |

### TeglonLabs (4 repos)
| Repo | Language | Stars |
|------|----------|------:|
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### migalkin (7 repos)
| Repo | Language | Stars |
|------|----------|------:|
| NodePiece | Python | 144 |
| StarE | Python | 89 |
| kgcourse2021 | HTML | 25 |
| NBFNet_mlx | Python | 10 |

### AustinCStone (7 repos)
| Repo | Language | Stars |
|------|----------|------:|
| TextGAN | Python | 92 |
| StereoVisionMRF | Python | 11 |
| SpectralClustering | Python | 3 |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances — 28 addresses (alice, bob, A–Z)

All queried via `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: 0.0 APT across all 28 addresses.** No `CoinStore` resource found — accounts are not initialized for APT holding on mainnet.

| World | Address |
|-------|---------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9... |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf78... |
| A–Z | 0x8699edc0... → 0x7af0ef6e... |

### Multisig Probes — 5 contracts

`POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Status |
|------|---------|:-------------:|:------:|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee208... | 2 | ✅ healthy |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df... | 2 | ✅ healthy |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6... | 2 | ✅ healthy |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae... | 2 | ✅ healthy |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0c... | 2 | ✅ healthy |

All 5 multisig contracts live on mainnet, requiring **2-of-N signatures**, all healthy.

### MNX Markets

`https://testnet.mnx.fi/api/markets` — **unavailable** (HTTP 401, Vercel deployment protection). No data captured.

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
- `id mod 3 == 0` → trit=0, color=`#d3869b`, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=`#b8bb26`, name=PLUS
- `id mod 3 == 2` → trit=-1, color=`#cc241d`, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,706 stars — flagship ML platform for Kubernetes (active June 2026)
- **kubeflow/pipelines**: 4,152 stars — pushed 2026-06-05
- **migalkin/NodePiece**: 144 stars — scalable knowledge graph embeddings (ICLR'22)
- **AustinCStone/TextGAN**: 92 stars — GAN text generation in TensorFlow
- **plurigrid/gorj**: This very repo — forj + GF(3) trit coloring for compositional REPL orchestration
- **plurigrid/asi**: 25★ — "everything is topological chemputer!"
- **plurigrid/Gay.jl** (bmorphism): 189 open issues — wide-gamut color sampling with splittable determinism
- **Hamming swarm**: 28 wallets probed, all unfunded; 5 multisigs all live 2-of-N
