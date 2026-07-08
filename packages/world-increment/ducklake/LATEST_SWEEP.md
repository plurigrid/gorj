# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-07-08  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | social graph | 5 |
| DJedamski | social graph | 2 |
| wasita | social graph | 3 |
| kristinezheng | social graph | 1 |
| M1shaaa | social graph | 2 |
| AustinCStone | social graph | 4 |

**Total repos snapshotted:** 320 (deduplicated)

### GF(3) Color Chain

```
id= 1  trit=+1  #b8bb26  PLUS     AustinCStone
id= 2  trit=-1  #cc241d  MINUS    DJedamski
id= 3  trit= 0  #d3869b  ERGODIC  M1shaaa
id= 4  trit=+1  #b8bb26  PLUS     TeglonLabs
id= 5  trit=-1  #cc241d  MINUS    bmorphism
id= 6  trit= 0  #d3869b  ERGODIC  kristinezheng
id= 7  trit=+1  #b8bb26  PLUS     kubeflow
id= 8  trit=-1  #cc241d  MINUS    migalkin
id= 9  trit= 0  #d3869b  ERGODIC  plurigrid
id=10  trit=+1  #b8bb26  PLUS     wasita
id=11  trit=-1  #cc241d  MINUS    zubyul
```

### Top Repos by Stars

| Rank | Repo | Stars | Language |
|------|------|-------|----------|
| 1 | kubeflow/kubeflow | 15,768 | — |
| 2 | kubeflow/pipelines | 4,169 | Python |
| 3 | kubeflow/spark-operator | 3,135 | Python |
| 4 | kubeflow/trainer | 2,132 | Go |
| 5 | kubeflow/katib | 1,689 | Python |
| 6 | kubeflow/examples | 1,460 | Jsonnet |
| 7 | kubeflow/community-distribution | 1,029 | YAML |
| 8 | kubeflow/arena | 815 | Go |
| 9 | kubeflow/kale | 695 | Python |
| 10 | migalkin/NodePiece | 144 | Python |
| 11 | AustinCStone/TextGAN | 92 | Python |
| 12 | migalkin/StarE | 89 | Python |

### Notable Activity
- **TeglonLabs/jank-crane** (C++): crane-jank converged-IR hub with GF3 convergence maps — last push 2026-06-08
- **wasita/wasita.github.io** (Svelte): last updated 2026-07-06
- **AustinCStone/EpsteinSearch** (Python): last updated 2026-02-11

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

**Queried:** 28 addresses (alice, bob, A–Z)  
**Method:** `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**Result:** All 28 addresses returned `Resource not found` — addresses are uninitialized on mainnet (CoinStore resource not registered). Balance recorded as 0.0 APT for all.

| World | Address (first 20 chars) | Balance (APT) |
|-------|--------------------------|--------------|
| alice | 0xc793acdec12b4a63... | 0.0 |
| bob | 0x0a3c00c58fdf9020... | 0.0 |
| A | 0x8699edc0960dd5b9... | 0.0 |
| B | 0x3f892ebe6e45164e... | 0.0 |
| C | 0x38b99e63ada9b6fe... | 0.0 |
| D | 0xf77656248f64d5dd... | 0.0 |
| E | 0xdc1d9d533bac3507... | 0.0 |
| F | 0x18a14b5b4bec118c... | 0.0 |
| G | 0x69a394c0b0ac8421... | 0.0 |
| H | 0xce67c327a7844e54... | 0.0 |
| I | 0x070fe5d74e4eda30... | 0.0 |
| J | 0x4d964db8f5383740... | 0.0 |
| K | 0xa732040a6b0d5590... | 0.0 |
| L | 0x7c2eaeafad972549... | 0.0 |
| M | 0x6fed37a7553ef16b... | 0.0 |
| N | 0xe7dde6da0a65f510... | 0.0 |
| O | 0x73252b6011a75115... | 0.0 |
| P | 0x6218792de4a9bc38... | 0.0 |
| Q | 0xac40fa50b81b4ca6... | 0.0 |
| R | 0x7ce605cc8fda4f8e... | 0.0 |
| S | 0xb8753014e4888ea4... | 0.0 |
| T | 0x35781dc0e42fef3f... | 0.0 |
| U | 0x75860da47565f650... | 0.0 |
| V | 0xb59dd8170321dfab... | 0.0 |
| W | 0x5f32aef70f5ba530... | 0.0 |
| X | 0xa95cbbd116548ac9... | 0.0 |
| Y | 0xd8e32848f1dffa81... | 0.0 |
| Z | 0x7af0ef6e1bd706f4... | 0.0 |

### Multisig Contract Probes

**Endpoint:** `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Contract Address | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4f428a0c007da... | 2 | healthy |
| A-G | 0xf56c4a1c0906214f... | 2 | healthy |
| Y-Z | 0xd3ffe1812b2df406... | 2 | healthy |
| S-T | 0x3b1c3ae905d44c3a... | 2 | healthy |
| V-W | 0x40fad7b423a84365... | 2 | healthy |

All 5 multisig contracts: **2-of-2 signatures required**, all responding.

### MNX Markets

`https://testnet.mnx.fi` — **Unavailable**: Vercel deployment protection authentication required. No market data accessible without credentials. `mnx_snapshots` table is empty.

---

## DuckDB Tables

| Table | Rows | Description |
|-------|------|-------------|
| `world_increments` | 11 | One GF(3)-tagged increment per source |
| `repo_snapshots` | 320 | Full repo metadata per increment |
| `aptos_snapshots` | 28 | Hamming swarm wallet balances |
| `multisig_probes` | 5 | Multisig contract health checks |
| `mnx_snapshots` | 0 | MNX market data (auth-gated, unavailable) |
