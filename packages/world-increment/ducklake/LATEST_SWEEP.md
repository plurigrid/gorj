# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-02

## Sweep Metadata
- **Date:** 2026-08-02
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 320 |
| Total Repo Snapshots | 320 |
| Sources Covered | 3 orgs + 8 users |

### Sources Queried
| Source | Type | Repos | Max Stars |
|--------|------|-------|-----------|
| plurigrid | org | 100 | 58 |
| kubeflow | org | 49 | 15,803 |
| TeglonLabs | org | 5 | 2 |
| bmorphism | user | 100 | 61 |
| zubyul | user | 49 | 2 |
| migalkin | social | 5 | 144 (NodePiece, ICLR'22) |
| DJedamski | social | 2 | 1 |
| wasita | social | 3 | 2 |
| kristinezheng | social | 2 | 0 |
| M1shaaa | social | 2 | 0 |
| AustinCStone | social | 3 | 92 (TextGAN) |
| **TOTAL** | | **320** | |

### GF(3) Color Chain Distribution
| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 106 |
| +1 | PLUS | #b8bb26 | 107 |
| -1 | MINUS | #cc241d | 107 |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

### Notable Repos (by stars)
| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,803 | — | recent |
| kubeflow/pipelines | 4,173 | Python | recent |
| kubeflow/spark-operator | 3,142 | Python | recent |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| bmorphism top | 61 | various | recent |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| TeglonLabs/jank-crane | 0 | C++ | 2026-06-08 |

### Recent Activity Highlights
- **TeglonLabs/jank-crane** (pushed 2026-06-08): "crane-jank converged-IR hub: loopify pass spec, GF3 convergence maps, simonw workflow" — C++
- **wasita/wasita.github.io** (pushed 2026-07-21): personal website (Svelte/Tailwind) — most recently pushed in social graph
- **migalkin/kgcourse2021** (pushed 2026-07-10): Knowledge Graphs course materials (HTML, 24★)
- **migalkin/RWL** (pushed 2026-05-28): Weisfeiler and Leman Go Relational (LOG 2022, Python)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)
All 28 wallets (alice, bob, A–Z) queried via Aptos fullnode API.

**Result:** All 28 wallets returned 0 APT. Accounts exist on-chain but hold zero balance at time of snapshot.

| Stat | Value |
|------|-------|
| Wallets queried | 28 |
| Non-zero balances | 0 |
| Total APT | 0.00 |

### Multisig Contract Probes
All 5 multisig contracts healthy — all require 2-of-N signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|--------------|--------|
| A-B | 0x0da4f428... | 2 | ✓ healthy |
| A-G | 0xf56c4a1c... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181... | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9... | 2 | ✓ healthy |
| V-W | 0x40fad7b4... | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)
**Status: SPA only — no JSON API found.**
All paths (`/`, `/api/markets`, `/api/v1/markets`, `/markets`, `/api`, `/api/v1`) return the Next.js SPA HTML shell. No market data extractable via HTTP without browser execution. `mnx_snapshots` table remains empty for this run.

---

## DuckDB Schema Summary

```sql
world_increments  -- 320 rows: GF3-tagged GitHub repo events
repo_snapshots    -- 320 rows: repo metadata (stars, forks, language, pushed_at)
aptos_snapshots   -- 28 rows:  wallet balances (all 0 APT)
multisig_probes   -- 5 rows:   all healthy, 2-of-N sigs
mnx_snapshots     -- 0 rows:   SPA, no API
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
