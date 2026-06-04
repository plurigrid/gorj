# World-Increment Sweep — 2026-05-01

## Sweep Metadata
- **Date:** 2026-05-01
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Branch:** `world-increment/sweep-2026-05-01-0617`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 389 |
| Sources Covered | 3 orgs + 8 users |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | SPA — no API accessible |

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain — All 12 Increments

| ID | Source | Type | GF3 Trit | Color | Name |
|----|--------|------|-----------|-------|------|
| 1  | plurigrid | org | +1 | `#b8bb26` | **PLUS** |
| 2  | kubeflow | org | -1 | `#cc241d` | **MINUS** |
| 3  | TeglonLabs | org | 0 | `#d3869b` | **ERGODIC** |
| 4  | bmorphism | user | +1 | `#b8bb26` | **PLUS** |
| 5  | zubyul | user | -1 | `#cc241d` | **MINUS** |
| 6  | migalkin | user | 0 | `#d3869b` | **ERGODIC** |
| 7  | DJedamski | user | +1 | `#b8bb26` | **PLUS** |
| 8  | wasita | user | -1 | `#cc241d` | **MINUS** |
| 9  | kristinezheng | user | 0 | `#d3869b` | **ERGODIC** |
| 10 | M1shaaa | user | +1 | `#b8bb26` | **PLUS** |
| 11 | AustinCStone | user | -1 | `#cc241d` | **MINUS** |
| 12 | plurigrid/gorj | org | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repo Snapshot Counts

| Source | Repos | Total Stars | Top Language |
|--------|-------|-------------|--------------|
| bmorphism | 100 | 247 | Rust/Zig/Clojure |
| plurigrid | 100 | 65 | Zig/Rust/Julia |
| zubyul | 49 | 14 | Rust/Python |
| kubeflow | 47 | 33,974 | Python/Go |
| AustinCStone | 40 | 108 | Python |
| migalkin | 19 | 278 | Python |
| wasita | 10 | 4 | Svelte |
| M1shaaa | 8 | 0 | TypeScript |
| kristinezheng | 6 | 0 | Python |
| DJedamski | 6 | 3 | R |
| TeglonLabs | 4 | 2 | Ruby/Python |

**Total: 389 repos across 11 sources**

### Top Repos by Stars

| Repo | Stars | Language | Last Push |
|------|-------|----------|-----------|
| kubeflow/kubeflow | 15,609 | — | 2026-04-29 |
| kubeflow/pipelines | 4,130 | Python | 2026-04-30 |
| kubeflow/spark-operator | 3,121 | Python | 2026-04-28 |
| kubeflow/trainer | 2,095 | Go | 2026-04-30 |
| kubeflow/katib | 1,681 | Python | 2026-04-14 |
| migalkin/StarE | 89 | Python | 2023-12-01 |
| plurigrid/asi | 17 | HTML | 2026-04-26 |
| bmorphism/shitcoin | 5 | Python | 2026-04-08 |

### Notable Activity (Social Graph Edges)
- **bmorphism/boxxy** (Move) — pushed 2026-04-30, forked by zubyul social graph
- **plurigrid/gorj** (Clojure) — 30 open issues, pushed 2026-05-01 (this repo)
- **plurigrid/nanoclj-zig** (Zig) — NaN-boxed Clojure in Zig 0.15 with interaction nets
- **zubyul/voice-observatory** — passive macOS TUI for voice signal paths, 2026-04-24
- **wasita/wasita.github.io** (Svelte) — personal site, active April 2026
- **M1shaaa/M1shaaa** — profile config pushed 2026-05-01 (same day as this sweep)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 wallets (alice, bob, A–Z) queried against Aptos mainnet fullnode.
**Result: All wallets return `resource_not_found`** — the CoinStore resource for APT has not been initialized on any of these addresses. Addresses are freshly generated or have never received an APT deposit that would auto-register the CoinStore module.

| World | Address (truncated) | Balance (APT) | Status |
|-------|---------------------|---------------|--------|
| alice | 0xc793...4cc7b | 0.0 | resource_not_found |
| bob | 0x0a3c...512d5d | 0.0 | resource_not_found |
| A–Z | 0x8699...–0x7af0... | 0.0 | resource_not_found |

**Interpretation:** Hamming swarm addresses are pre-registered in the topology but await on-chain activation (first APT transfer initializes CoinStore automatically).

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Multisig Address | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | yes |
| A-G | 0xf56c...0096 | 2 | yes |
| Y-Z | 0xd3ff...b883 | 2 | yes |
| S-T | 0x3b1c...7883 | 2 | yes |
| V-W | 0x40fa...eb6d | 2 | yes |

**All 5 multisig contracts healthy — 2-of-N threshold on each.** The contracts exist and respond correctly on mainnet.

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. Endpoints `/api/markets` and `/api/v1/markets` returned no JSON API data — market data loads client-side only. **Status: unavailable via REST API.**

---

## DuckDB Schema State

| Table | Rows |
|-------|------|
| world_increments | 12 |
| repo_snapshots | 389 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA) |

## GF(3) Trit Legend
- **PLUS** `#b8bb26` (trit=+1): ids 1,4,7,10 → plurigrid, bmorphism, DJedamski, M1shaaa
- **MINUS** `#cc241d` (trit=-1): ids 2,5,8,11 → kubeflow, zubyul, wasita, AustinCStone
- **ERGODIC** `#d3869b` (trit=0): ids 3,6,9,12 → TeglonLabs, migalkin, kristinezheng, gorj
