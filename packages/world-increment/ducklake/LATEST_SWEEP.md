# World-Increment Sweep — 2026-08-06

## Sweep Metadata
- **Date:** 2026-08-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 (max id=13) |
| Repo Snapshots This Run | 50 (plurigrid org, 55 found via search) |
| Aptos Wallets Probed | 28 |
| Multisig Contracts Probed | 5 |
| MNX Markets | Unavailable (Next.js SPA, no API) |

---

## GF(3) Color Chain — Increment #13 (This Run)

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | plurigrid (org) | sweep_complete | +1 | `#b8bb26` | **PLUS** |

GF(3) chain (full history through id=13): `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS`

---

## GitHub Social Graph Sweep

### Scope
- GitHub MCP access scoped to `plurigrid/gorj`; search covered `org:plurigrid` (55 public repos found)
- Other orgs (kubeflow, TeglonLabs) and users (bmorphism, zubyul, migalkin, etc.) outside MCP scope → not snapshotted this run

### plurigrid Org — 50 Repos Snapshotted (top by activity)

| Repo | Language | Stars | Issues | Last Pushed |
|------|----------|-------|--------|-------------|
| place | TeX | 2 | 17 | 2026-08-06 |
| asi | HTML | 59 | 4 | 2026-08-05 |
| gorj | Clojure | 1 | 1679 | 2026-07-29 |
| zig-syrup | Zig | 2 | 0 | 2026-07-28 |
| shrimp | — | 0 | 0 | 2026-07-03 |
| eirobri | Clojure | 0 | 31 | 2026-05-19 |
| nash-portal | Rust | 2 | 1 | 2026-05-19 |
| Plurigraph | JavaScript | 3 | 4 | 2026-05-12 |
| ontology | JavaScript | 8 | 16 | 2026-05-09 |
| asi-skills | Julia | 3 | 0 | 2026-04-26 |
| nanoclj-zig | Zig | 1 | 20 | 2026-04-25 |

### Recent gorj Commits (last 5)
| SHA | Date | Message |
|-----|------|---------|
| 5b28fe0 | 2026-05-08 | chore: ignore duckdb binary in repo root |
| ebf263f | 2026-04-14 | world-increment ducklake: sync world.duckdb sweep state |
| b434a43 | 2026-04-14 | Merge sweep state into master |
| e76792f | 2026-04-14 | world-increments.duckdb: sync latest sweep state |
| 631518b | 2026-04-12 | world-increment sweep 2026-04-12: insert id=12 ERGODIC |

---

## Hamming Swarm Snapshot

### Aptos Wallet Balances (2026-08-06T20:16Z, Mainnet Ledger v6644552444+)

All 28 Hamming swarm addresses queried via `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`. All returned `resource_not_found` — wallets exist on-chain but hold 0 APT (no CoinStore resource initialized).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...4cc7b | 0.0 |
| bob | 0x0a3c...512d5d | 0.0 |
| A–Z (26 addresses) | 0x8699...–0x7af0... | 0.0 each |

**Total APT across swarm:** 0.0 APT

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts healthy — 2-of-2 signatures required.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — `testnet.mnx.fi` is a Next.js SPA (59KB HTML). No REST API endpoints found at `/api/markets` or `/api/v1/markets` — those routes serve the same SPA shell. Market data requires browser-side JS execution. No mnx_snapshots inserted.

---

## DuckDB Table Summary

| Table | Rows (total) |
|-------|-------------|
| world_increments | 24 |
| repo_snapshots | 994 (cumulative) |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 0 |
