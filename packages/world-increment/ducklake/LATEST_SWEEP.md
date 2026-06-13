# World-Increment Sweep + Hamming Snapshot — 2026-06-13

## Sweep Metadata
- **Date:** 2026-06-13
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.3 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 414 |
| Total Repo Snapshots | 1,335 rows (646 distinct repos) |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Snapped | 28 |
| Multisig Contracts Probed | 5 |

---

## GF(3) Color Chain Distribution

| Trit | Color | Name | Count |
|------|-------|------|-------|
| 0 | `#d3869b` | ERGODIC | 137 |
| 1 | `#b8bb26` | PLUS | 139 |
| −1 | `#cc241d` | MINUS | 138 |

GF(3) chain rule: `id%3==0` → ERGODIC · `id%3==1` → PLUS · `id%3==2` → MINUS

---

## Top Repos by Source

### plurigrid (100 repos, 2026-06-13 snapshot)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| asi | HTML | 26 | 2026-06-10 |
| place | TeX | 1 | 2026-06-10 |
| gorj | Clojure | 0 | 2026-06-13 |
| eirobri | Clojure | 0 | 2026-06-03 |
| nash-portal | Rust | 2 | 2026-05-19 |

### kubeflow (48 repos)
| Repo | Language | Stars | Pushed At |
|------|----------|-------|-----------|
| kubeflow | — | 15,721 | 2026-06-11 |
| pipelines | Python | 4,153 | 2026-06-13 |
| spark-operator | Python | 3,128 | 2026-06-12 |
| trainer | Go | 2,114 | 2026-06-13 |

### TeglonLabs (5 repos)
| Repo | Language | Stars |
|------|----------|-------|
| jank-crane | C++ | 0 |
| mathpix-gem | Ruby | 2 |
| coin-flip-mcp | JavaScript | 0 |
| monad-mcp-server | — | 0 |
| topoi | Python | 0 |

### bmorphism (100 repos)
- ocaml-mcp-sdk, anti-bullshit-mcp-server, shitcoin, open-location-code-zig

### AustinCStone (40 repos)
- TextGAN (Python, ★92), StereoVisionMRF (Python, ★11)

### migalkin (19 repos)
- NodePiece (Python, ★143), StarE (Python, ★88), kgcourse2021 (HTML, ★25)

---

## Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| kubeflow | org | 48 |
| AustinCStone | user | 40 |
| zubyul | user | 49 |
| migalkin | user | 19 |
| wasita | user | 11 |
| kristinezheng | user | 5 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| **TOTAL** | | **391** |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-06-13)
Queried 28 addresses (alice, bob, A–Z) via `fullnode.mainnet.aptoslabs.com`.  
**Result:** All 28 accounts returned `0.0 APT` — accounts exist on-chain but  
hold no APT balance at time of snapshot.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b | 0.0 |
| bob | 0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d | 0.0 |
| A–Z | (see DuckDB aptos_snapshots) | 0.0 each |

### Multisig Probes (5 contracts)
All 5 multisig accounts are **healthy**, each requiring **2-of-N signatures**.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003 | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096 | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883 | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883 | 2 | ✓ |
| V-W | 0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)
**Status: UNAVAILABLE** — `testnet.mnx.fi` is behind Vercel deployment protection  
(authentication required). No market data accessible without a bypass token  
or trusted-source OIDC token. Recorded as `auth_required` in `mnx_snapshots`.

---

## DuckDB Schema

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
- **kubeflow/kubeflow**: 15,721 stars — flagship ML platform for Kubernetes (pushed 2026-06-11)
- **kubeflow/pipelines**: 4,153 stars — most popular ML pipeline for Kubernetes
- **kubeflow/spark-operator**: 3,128 stars — Kubernetes operator for Apache Spark
- **migalkin/NodePiece**: 143 stars — scalable knowledge graph embeddings
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/asi**: 26 stars — "everything is topological chemputer!" (pushed 2026-06-10)
- **plurigrid/gorj**: This very repo — forj + Rama topology nREPL (pushed 2026-06-13)
- **TeglonLabs/jank-crane**: new C++ repo — "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps" (pushed 2026-06-08)
- **M1shaaa/M1shaaa**: active today (pushed 2026-06-13)
- All 5 Hamming multisig contracts healthy — 2-of-N unanimous
