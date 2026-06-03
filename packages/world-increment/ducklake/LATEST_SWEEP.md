# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-03T13:00:00Z  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Name | Hex |
|----|--------|------|----------|------|-----|
| 1 | plurigrid | org | +1 | PLUS | `#b8bb26` |
| 2 | kubeflow | org | -1 | MINUS | `#cc241d` |
| 3 | TeglonLabs | org | 0 | ERGODIC | `#d3869b` |
| 4 | bmorphism | user | +1 | PLUS | `#b8bb26` |
| 5 | zubyul | user | -1 | MINUS | `#cc241d` |
| 6 | migalkin | user | 0 | ERGODIC | `#d3869b` |
| 7 | DJedamski | user | +1 | PLUS | `#b8bb26` |
| 8 | wasita | user | -1 | MINUS | `#cc241d` |
| 9 | kristinezheng | user | 0 | ERGODIC | `#d3869b` |
| 10 | M1shaaa | user | +1 | PLUS | `#b8bb26` |
| 11 | AustinCStone | user | -1 | MINUS | `#cc241d` |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

---

### Repo Snapshot Summary

| Source | Type | Repos Captured | Total Stars | Latest Push |
|--------|------|----------------|-------------|-------------|
| kubeflow | org | 48 | 305,691 | 2026-06-03 |
| plurigrid | org | 100 | 465 | 2026-06-03 |
| bmorphism | user | 100 | 1,524 | 2026-06-03 |
| migalkin | user | 19 | 2,502 | 2026-05-28 |
| zubyul | user | 49 | 120 | 2026-04-24 |
| AustinCStone | user | 40 | 972 | 2026-04-01 |
| TeglonLabs | org | 4 | 42 | 2026-01-01 |
| wasita | user | 11 | 33 | 2026-06-01 |
| DJedamski | user | 6 | 51 | 2023-04-21 |
| kristinezheng | user | 6 | 0 | 2026-05-14 |
| M1shaaa | user | 8 | 0 | 2026-04-13 |
| **TOTAL** | | **391** | **311,400** | |

---

### Notable Repos

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| kubeflow/kubeflow | 15,705 ⭐ | — | Machine Learning Toolkit for Kubernetes |
| kubeflow/pipelines | 4,151 ⭐ | Python | ML Pipelines for Kubeflow |
| kubeflow/spark-operator | 3,125 ⭐ | Python | Kubernetes operator for Apache Spark |
| kubeflow/trainer | 2,110 ⭐ | Go | Distributed AI Training on Kubernetes |
| kubeflow/katib | 1,685 ⭐ | Python | Automated Machine Learning on Kubernetes |
| migalkin/NodePiece | 144 ⭐ | Python | Compositional KG Representations (ICLR'22) |
| migalkin/StarE | 89 ⭐ | Python | Message Passing for Hyper-Relational KGs |
| AustinCStone/TextGAN | 92 ⭐ | Python | GAN for text generation in TensorFlow |
| bmorphism/ocaml-mcp-sdk | 61 ⭐ | OCaml | OCaml SDK for Model Context Protocol |
| bmorphism/anti-bullshit-mcp-server | 23 ⭐ | JavaScript | Claim analysis and manipulation detection |
| bmorphism/risc0-cosmwasm-example | 23 ⭐ | Rust | CosmWasm + zkVM RISC-V EFI template |
| plurigrid/gorj | — | Clojure | forj + Rama topology nREPL + GF(3) trit coloring (324 open issues) |
| plurigrid/asi | 24 ⭐ | HTML | everything is topological chemputer! |

---

### Zubyul Social Graph

Connected accounts via zubyul's network:
- **migalkin** — Knowledge Graph researcher; NodePiece, StarE, RWL, NBFNet_mlx (MLX on Apple Silicon)
- **DJedamski** — ML practitioner; Kaggle, R/stats background
- **wasita** — Svelte/web dev; network science, neuroscience-adjacent; Typst, Kobo tools
- **kristinezheng** — MIT neurosci/ML; Lookit experiments, HackMIT sustainability
- **M1shaaa** — Yale dev-psych; Lookit, MNIST classifiers, lab experiments
- **AustinCStone** — ML/CV researcher; TextGAN (92★), StereoVisionMRF, Grover's algorithm sim

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming swarm wallets (alice, bob, A–Z) queried via  
`fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result: 0 APT across all 28 wallets.**  
No wallet has a registered CoinStore on Aptos mainnet — accounts have not been initialized on-chain (no APT ever deposited or account registered).

| World | Address | APT |
|-------|---------|-----|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z (×26) | 0x8699...c7b0 | 0.0 each |

---

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

All 5 multisig contracts return `sigs_required = 2` — **all healthy 2-of-2**.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

---

### MNX Markets (testnet.mnx.fi)

The MNX testnet is a **Next.js SPA** — no accessible REST/JSON API at `/api/markets`, `/api/v1/markets`, or `/api/tickers`. Market data requires browser runtime to hydrate client-side. `mnx_snapshots` table is empty for this sweep.

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type,
                 repo_name, actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user,
               repo_name, full_name, language, stars, forks,
               open_issues, pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, ERGODIC, `#d3869b`
- `id mod 3 == 1` → trit=+1, PLUS, `#b8bb26`
- `id mod 3 == 2` → trit=-1, MINUS, `#cc241d`
