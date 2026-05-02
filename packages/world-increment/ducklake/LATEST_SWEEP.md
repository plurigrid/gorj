# World-Increment Sweep + Hamming Snapshot — 2026-05-02

## Sweep Metadata
- **Date:** 2026-05-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 11 |
| Total Repo Snapshots | 389 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — 11 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | AustinCStone | user | +1 | `#b8bb26` | **PLUS** |
| 2  | DJedamski | user | -1 | `#cc241d` | **MINUS** |
| 3  | M1shaaa | user | 0 | `#d3869b` | **ERGODIC** |
| 4  | TeglonLabs | org | +1 | `#b8bb26` | **PLUS** |
| 5  | bmorphism | user | -1 | `#cc241d` | **MINUS** |
| 6  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | kubeflow | org | +1 | `#b8bb26` | **PLUS** |
| 8  | migalkin | user | -1 | `#cc241d` | **MINUS** |
| 9  | plurigrid | org | 0 | `#d3869b` | **ERGODIC** |
| 10 | wasita | user | +1 | `#b8bb26` | **PLUS** |
| 11 | zubyul | user | -1 | `#cc241d` | **MINUS** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`

### Repo Counts by Source

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| kubeflow | org | 47 | 33,986 |
| plurigrid | org | 100 | 65 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 247 |
| zubyul | user | 49 | 14 |
| migalkin | user | 19 | 278 |
| AustinCStone | user | 40 | 108 |
| wasita | user | 10 | 4 |
| M1shaaa | user | 8 | 0 |
| DJedamski | user | 6 | 3 |
| kristinezheng | user | 6 | 0 |
| **TOTAL** | | **389** | **34,707** |

### Top Repos by Stars

| Repo | Language | Stars | Forks |
|------|----------|-------|-------|
| kubeflow/kubeflow | — | 15,615 | 2,646 |
| kubeflow/pipelines | Python | 4,130 | 1,986 |
| kubeflow/spark-operator | Python | 3,121 | 1,483 |
| kubeflow/trainer | Go | 2,095 | 948 |
| kubeflow/katib | Python | 1,681 | 521 |
| kubeflow/examples | Jsonnet | 1,460 | 757 |
| kubeflow/manifests | YAML | 1,013 | 1,065 |
| kubeflow/arena | Go | 810 | 191 |
| kubeflow/kale | Python | 684 | 156 |
| AustinCStone/TextGAN | Python | 92 | 30 |

### Top Languages

Python (80) · Rust (26) · JavaScript (24) · TypeScript (23) · Go (15) · HTML (15) · Jupyter Notebook (14) · Clojure (13) · Julia (9) · Jsonnet (8)

### Most Recent Activity

| Repo | Pushed |
|------|--------|
| plurigrid/gorj | 2026-05-02T02:16:57Z |
| bmorphism/Gay.jl | 2026-05-02T00:31:20Z |
| kubeflow/hub | 2026-05-01T22:27:57Z |
| kubeflow/pipelines | 2026-05-01T19:55:52Z |
| kubeflow/notebooks | 2026-05-01T18:47:18Z |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 Hamming-space addresses probed via `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C–Z | (see DB) | 0.0 |

**All 28 wallets: 0.0 APT** (accounts have zero APT balance on mainnet)

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...003 | 2 | ✓ |
| A-G | 0xf56c...096 | 2 | ✓ |
| Y-Z | 0xd3ff...883 | 2 | ✓ |
| S-T | 0x3b1c...883 | 2 | ✓ |
| V-W | 0x40fa...b6d | 2 | ✓ |

**All 5 multisig contracts: 2-of-N threshold, HEALTHY**

### MNX Markets

`https://testnet.mnx.fi` — **UNAVAILABLE** (SPA returned no parseable JSON from probed API paths: `/`, `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`, `/api/v1/tickers`)

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
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

## Notable Highlights
- **kubeflow/kubeflow**: 15,615 stars — flagship ML platform for Kubernetes
- **kubeflow/pipelines**: 4,130 stars — most active push 2026-05-01
- **plurigrid/gorj**: most recent push 2026-05-02 — this very repo
- **bmorphism/Gay.jl**: pushed 2026-05-02 — active development
- **AustinCStone/TextGAN**: 92 stars — TF text generation with GANs
- **migalkin/NodePiece**: 278 stars total across 19 repos — KG embeddings researcher
- **All multisig 2-of-N**: A-B, A-G, Y-Z, S-T, V-W all healthy at threshold=2
