# World-Increment Sweep + Hamming Swarm Snapshot

**Date:** 2026-05-05  
**Session:** https://claude.ai/code/session_01U9b5xLDBgXSX7VnSKDjV1x  
**Aptos ledger version:** 5137289209  
**Base commit (master):** ebf263f — 2026-04-14

---

## JOB 1: GitHub Social Graph Sweep

### Sources Targeted

| Source | Type | Status |
|--------|------|--------|
| plurigrid | org | gorj snapshotted via MCP tools |
| kubeflow | org | rate-limited (no auth token) |
| TeglonLabs | org | rate-limited |
| bmorphism | user | rate-limited |
| zubyul | user | rate-limited |
| migalkin | user (zubyul social graph) | rate-limited |
| DJedamski | user (zubyul social graph) | rate-limited |
| wasita | user (zubyul social graph) | rate-limited |
| kristinezheng | user (zubyul social graph) | rate-limited |
| M1shaaa | user (zubyul social graph) | rate-limited |
| AustinCStone | user (zubyul social graph) | rate-limited |

> **Note:** Unauthenticated GitHub REST API rate-limited (0/60 remaining). No `gh` CLI or `GITHUB_TOKEN` in environment. `plurigrid/gorj` data accessed via MCP tools; all 11 sources recorded as GF(3) world-increment events.

### plurigrid/gorj via MCP

| Field | Value |
|-------|-------|
| full_name | plurigrid/gorj |
| language | Clojure |
| open_issues | 58 |
| pushed_at | 2026-05-05 |
| open PRs | 352+ (all world-increment sweep branches) |
| active sweep branches | 50+ (2026-04-27 through 2026-05-02) |
| latest master commit | ebf263f "world-increment ducklake: sync world.duckdb sweep state" |

### GF(3) Color Chain — This Sweep (IDs 13–24)

| ID | Trit | Color | Name | Source | Event |
|----|------|-------|------|--------|-------|
| 13 | +1 | #b8bb26 | **PLUS** | plurigrid | repo_sweep |
| 14 | -1 | #cc241d | **MINUS** | kubeflow | repo_sweep |
| 15 | 0 | #d3869b | **ERGODIC** | TeglonLabs | repo_sweep |
| 16 | +1 | #b8bb26 | **PLUS** | bmorphism | repo_sweep |
| 17 | -1 | #cc241d | **MINUS** | zubyul | repo_sweep |
| 18 | 0 | #d3869b | **ERGODIC** | migalkin | repo_sweep |
| 19 | +1 | #b8bb26 | **PLUS** | DJedamski | repo_sweep |
| 20 | -1 | #cc241d | **MINUS** | wasita | repo_sweep |
| 21 | 0 | #d3869b | **ERGODIC** | kristinezheng | repo_sweep |
| 22 | +1 | #b8bb26 | **PLUS** | M1shaaa | repo_sweep |
| 23 | -1 | #cc241d | **MINUS** | AustinCStone | repo_sweep |
| 24 | 0 | #d3869b | **ERGODIC** | sweep | sweep_complete |

Chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`  
(4th complete GF(3) cycle, IDs 13–24)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

Probed via: `GET /v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

**All 28 wallets (alice, bob, A–Z) return `resource_not_found`** — CoinStore not initialized on mainnet (ledger v5137289209).

| World | Balance APT | Address (prefix) |
|-------|-------------|-----------------|
| alice | 0.0 | 0xc793ac... |
| bob | 0.0 | 0x0a3c00... |
| A | 0.0 | 0x8699ed... |
| B | 0.0 | 0x3f892e... |
| C | 0.0 | 0x38b99e... |
| D | 0.0 | 0xf77656... |
| E | 0.0 | 0xdc1d9d... |
| F | 0.0 | 0x18a14b... |
| G | 0.0 | 0x69a394... |
| H | 0.0 | 0xce67c3... |
| I | 0.0 | 0x070fe5... |
| J | 0.0 | 0x4d964d... |
| K | 0.0 | 0xa73204... |
| L | 0.0 | 0x7c2eae... |
| M | 0.0 | 0x6fed37... |
| N | 0.0 | 0xe7dde6... |
| O | 0.0 | 0x732526... |
| P | 0.0 | 0x621879... |
| Q | 0.0 | 0xac40fa... |
| R | 0.0 | 0x7ce605... |
| S | 0.0 | 0xb87530... |
| T | 0.0 | 0x357815... |
| U | 0.0 | 0x758604... |
| V | 0.0 | 0xb59dd8... |
| W | 0.0 | 0x5f32ae... |
| X | 0.0 | 0xa95cbb... |
| Y | 0.0 | 0xd8e328... |
| Z | 0.0 | 0x7af0ef... |

**Total swarm APT: 0.0**

### Multisig Contract Probes

Probed via: `POST /v1/view` → `0x1::multisig_account::num_signatures_required`

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4f428a0c007... | 2 | ✓ |
| A-G | 0xf56c4a1c090621... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df4... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c... | 2 | ✓ |
| V-W | 0x40fad7b423a843... | 2 | ✓ |

**5/5 multisig contracts healthy — all at 2-of-2 threshold.**

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. HTTP 200 returned but data is client-side rendered — no public REST JSON API endpoint accessible. `mnx_snapshots` table empty this sweep.

---

## DuckDB Ducklake State

File: `packages/world-increment/ducklake/world-increments.duckdb`

| Table | Rows | Delta |
|-------|------|-------|
| world_increments | 35 | +12 (IDs 13–24) |
| repo_snapshots | 945 | +1 (gorj via MCP) |
| aptos_snapshots | 28 | +28 (all 0.0 APT) |
| multisig_probes | 5 | +5 (all healthy) |
| mnx_snapshots | 0 | — (SPA unavailable) |

### GF(3) Assignment Rule

```
id % 3 == 0  →  trit=0,   ERGODIC  #d3869b
id % 3 == 1  →  trit=+1,  PLUS     #b8bb26
id % 3 == 2  →  trit=-1,  MINUS    #cc241d
```

---

## Repo Counts (cumulative from prior sweeps, ducklake)

| org_or_user | repos |
|-------------|-------|
| plurigrid | 944 (prior sweeps) |
| gorj (this sweep) | +1 |

---

## Quick Reference Queries

```sql
-- GF(3) chain — this sweep
SELECT id, gf3_trit, gf3_color, gf3_name, source_name, event_type
FROM world_increments WHERE id BETWEEN 13 AND 24 ORDER BY id;

-- Multisig health (latest)
SELECT pair, sigs_required, healthy FROM multisig_probes ORDER BY timestamp DESC LIMIT 5;

-- Aptos swarm (latest 28)
SELECT world, balance_apt FROM aptos_snapshots ORDER BY timestamp DESC LIMIT 28;

-- Total world increments by GF(3) name
SELECT gf3_name, count(*) as cnt FROM world_increments GROUP BY 1 ORDER BY 1;
```

---

## Notable Prior Sweep Highlights (from ducklake)

- **kubeflow/kubeflow**: 15,565–15,619 stars (tracked across sweeps)
- **kubeflow/pipelines**: 4,119–4,132 stars
- **migalkin/NodePiece**: 143 stars — ICLR'22 scalable KG embeddings
- **bmorphism/ocaml-mcp-sdk**: 60 stars — OCaml MCP SDK (oxcaml_effect)
- **AustinCStone/TextGAN**: 92 stars — text generation with GANs
- **plurigrid/gorj**: This repo — 58 open issues, pushed 2026-05-05
