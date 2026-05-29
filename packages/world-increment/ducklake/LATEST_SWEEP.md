# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-29  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`  
**GF(3) color chain:** id%3==0 → trit=0 ERGODIC #d3869b · id%3==1 → trit=1 PLUS #b8bb26 · id%3==2 → trit=-1 MINUS #cc241d

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| id | GF(3) | Color | Source | Type | Repos | Stars |
|----|-------|-------|--------|------|-------|-------|
| 1 | PLUS | #b8bb26 | plurigrid | org | 100 | 74 |
| 2 | MINUS | #cc241d | kubeflow | org | 48 | 34,147 |
| 3 | ERGODIC | #d3869b | TeglonLabs | org | 4 | 2 |
| 4 | PLUS | #b8bb26 | bmorphism | user | 100 | 247 |
| 5 | MINUS | #cc241d | zubyul | user | 49 | 14 |
| 6 | ERGODIC | #d3869b | migalkin | user (social) | 19 | 280 |
| 7 | PLUS | #b8bb26 | AustinCStone | user (social) | 30 | 108 |
| 8 | MINUS | #cc241d | wasita | user (social) | 11 | 5 |
| 9 | ERGODIC | #d3869b | DJedamski | user (social) | 6 | 3 |
| 10 | PLUS | #b8bb26 | kristinezheng | user (social) | 6 | 0 |
| 11 | MINUS | #cc241d | M1shaaa | user (social) | 8 | 0 |

**Total repos snapshotted: 381**

### Notable Repos (most-recently-pushed)

**plurigrid** (top by pushed_at):
- `plurigrid/place` (TeX, ⭐1) — pushed 2026-05-21
- `plurigrid/eirobri` (Clojure) — EiRoBri replay world, pushed 2026-05-26
- `plurigrid/gorj` (Clojure, 251 open issues) — forj + Rama topology nREPL + GF(3) gay trit coloring

**kubeflow** (top by stars):
- `kubeflow/kubeflow` — ⭐15,686 Machine Learning Toolkit for Kubernetes
- `kubeflow/pipelines` — ⭐4,150 ML Pipelines
- `kubeflow/trainer` — ⭐2,107 Distributed AI Model Training
- `kubeflow/spark-operator` — ⭐3,124 Kubernetes operator for Apache Spark
- `kubeflow/katib` — ⭐1,685 AutoML on Kubernetes
- `kubeflow/manifests` (YAML, ⭐1,019) — most recently pushed 2026-05-29

**bmorphism** (top by pushed_at):
- `bmorphism/Gay.jl` (Julia, 189 open issues) — Wide-gamut color sampling, pushed 2026-05-29
- `bmorphism/oxgame` (OCaml) — Stellar resolution + open-game composition
- `bmorphism/ocaml-mcp-sdk` (OCaml, ⭐61) — OxCaml SDK for MCP
- `bmorphism/anti-bullshit-mcp-server` (JS, ⭐23) — claim validation MCP server

**TeglonLabs:**
- `TeglonLabs/mathpix-gem` (Ruby, ⭐2) — Mathematical OCR to LaTeX/SMILES/Markdown
- `TeglonLabs/coin-flip-mcp` (JS) — MCP server for random.org coin flips

**migalkin** (ML/KG researcher):
- `migalkin/NodePiece` (Python, ⭐144) — Compositional KG representations
- `migalkin/StarE` (Python, ⭐89) — Hyper-relational KG message passing (EMNLP 2020)
- `migalkin/kgcourse2021` (HTML, ⭐25) — Knowledge Graphs course materials

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Result:** All 28 wallets returned 0 APT. The `CoinStore<AptosCoin>` resource is either unregistered or unfunded on mainnet for all addresses. This is consistent with these being freshly generated or testnet-intended addresses.

### Multisig Contract Probes

All 5 multisig accounts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**Result:** All 5 multisig contracts respond and require exactly 2 signatures. Fully healthy — no quorum drift detected.

### MNX Markets (testnet.mnx.fi)

The endpoint `https://testnet.mnx.fi` resolves to a Next.js SPA. All API probe paths (`/api/markets`, `/api/v1/markets`, `/api/tickers`) return the SPA HTML shell rather than JSON. **Market data unavailable via REST scraping** — requires client-side JS execution to hydrate.

---

## DuckDB Tables Summary

| Table | Rows |
|-------|------|
| `world_increments` | 11 |
| `repo_snapshots` | 381 |
| `aptos_snapshots` | 28 |
| `multisig_probes` | 5 |
| `mnx_snapshots` | 1 |

### GF(3) World-Increment Chain

```
id=1  PLUS    #b8bb26  plurigrid    (org,   100 repos)
id=2  MINUS   #cc241d  kubeflow     (org,    48 repos)
id=3  ERGODIC #d3869b  TeglonLabs   (org,     4 repos)
id=4  PLUS    #b8bb26  bmorphism    (user,  100 repos)
id=5  MINUS   #cc241d  zubyul       (user,   49 repos)
id=6  ERGODIC #d3869b  migalkin     (user,   19 repos)
id=7  PLUS    #b8bb26  AustinCStone (user,   30 repos)
id=8  MINUS   #cc241d  wasita       (user,   11 repos)
id=9  ERGODIC #d3869b  DJedamski    (user,    6 repos)
id=10 PLUS    #b8bb26  kristinezheng(user,    6 repos)
id=11 MINUS   #cc241d  M1shaaa      (user,    8 repos)
```
