# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-05-10  
**DuckDB:** `world-increments.duckdb`  
**GF(3) chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (zubyul graph) | 19 |
| AustinCStone | user (zubyul graph) | 30 |
| wasita | user (zubyul graph) | 11 |
| DJedamski | user (zubyul graph) | 6 |
| kristinezheng | user (zubyul graph) | 6 |
| M1shaaa | user (zubyul graph) | 8 |
| **TOTAL** | | **381** |

### DuckDB Tables

```
repo_snapshots:   381 rows
world_increments: 381 rows  (GF3: 127 ERGODIC / 127 PLUS / 127 MINUS)
aptos_snapshots:   28 rows
multisig_probes:    5 rows
mnx_snapshots:      0 rows  (SPA, API unavailable)
```

### Top Repos by Stars

**kubeflow** (org):
- kubeflow/kubeflow — 15,628 ⭐
- kubeflow/pipelines — 4,137 ⭐ (Python)
- kubeflow/spark-operator — 3,125 ⭐ (Python)
- kubeflow/trainer — 2,097 ⭐ (Go)
- kubeflow/katib — 1,683 ⭐ (Python)

**plurigrid** (org):
- plurigrid/asi — 21 ⭐ (HTML)
- plurigrid/ontology — 8 ⭐ (JavaScript)
- plurigrid/vcg-auction — 7 ⭐ (Rust)
- plurigrid/agent — 5 ⭐ (Python)
- plurigrid/StochFlow — 4 ⭐ (Python)

**bmorphism** (user):
- bmorphism/ocaml-mcp-sdk — 61 ⭐ (OCaml)
- bmorphism/anti-bullshit-mcp-server — 23 ⭐ (JavaScript)
- bmorphism/risc0-cosmwasm-example — 23 ⭐ (Rust)
- bmorphism/say-mcp-server — 20 ⭐ (JavaScript)
- bmorphism/babashka-mcp-server — 18 ⭐ (JavaScript)

**TeglonLabs** (org):
- TeglonLabs/mathpix-gem — 2 ⭐ (Ruby)
- TeglonLabs/topoi — 0 ⭐ (Python)
- TeglonLabs/coin-flip-mcp — 0 ⭐ (JavaScript)
- TeglonLabs/monad-mcp-server — 0 ⭐

**migalkin** (user):
- migalkin/NodePiece — 144 ⭐ (Python, ICLR'22)
- migalkin/StarE — 89 ⭐ (Python, EMNLP 2020)
- migalkin/NBFNet_mlx — 10 ⭐ (Python)
- migalkin/rambo — 3 ⭐ (Rust)

**AustinCStone** (user):
- AustinCStone/TextGAN — 92 ⭐ (Python)
- AustinCStone/StereoVisionMRF — 11 ⭐ (Python)
- AustinCStone/SpectralClustering — 3 ⭐ (Python)

### GF(3) World-Increment Summary

Total increments: **381**
- trit=0 (ERGODIC #d3869b): 127 increments
- trit=1 (PLUS #b8bb26): 127 increments  
- trit=-1 (MINUS #cc241d): 127 increments

Conservation: Σ trits = 0 × 127 + 1 × 127 + (−1) × 127 = **0** (balanced)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

All 28 addresses (alice, bob, A–Z) returned `resource_not_found` from the Aptos fullnode — no `CoinStore<AptosCoin>` resource exists at any address. This indicates all wallets have **0 APT** (never funded or funds moved to FA migration).

| World | Balance (APT) | Status |
|-------|--------------|--------|
| alice | 0.0 | resource_not_found |
| bob | 0.0 | resource_not_found |
| A–Z (26 wallets) | 0.0 each | resource_not_found |

**Ledger version probed:** 5,214,471,493

### Multisig Contract Probes

All 5 multisig accounts returned `num_signatures_required = 2`. All healthy.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428... | 2 | healthy |
| A-G | 0xf56c4a1c... | 2 | healthy |
| Y-Z | 0xd3ffe181... | 2 | healthy |
| S-T | 0x3b1c3ae9... | 2 | healthy |
| V-W | 0x40fad7b4... | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

Status: **SPA only** — `testnet.mnx.fi` serves a Next.js single-page application. All probed API endpoints (`/api/markets`, `/api/v1/tickers`, `/api/v1/instruments`, etc.) returned either the HTML shell or DNS failures. No market data extractable without browser execution. `mnx_snapshots` table remains empty.

---

## Schema Reference

```sql
repo_snapshots   -- 381 GitHub repo states
world_increments -- 381 GF(3)-colored increment records  
aptos_snapshots  -- 28 Hamming swarm wallet readings
multisig_probes  -- 5 multisig account health checks
mnx_snapshots    -- 0 (SPA, no API data)
```

DuckDB file: `packages/world-increment/ducklake/world-increments.duckdb`
