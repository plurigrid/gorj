# World-Increment Sweep — 2026-07-17

## Sweep Metadata
- **Date:** 2026-07-17
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** 1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **New World Increment ID:** 13 (PLUS · #b8bb26)

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 24 |
| Total Repo Snapshots | 944 |
| Aptos Snapshots (cumulative) | 28 |
| Multisig Probes (cumulative) | 5 |
| Hamming Addresses Queried | 28 |
| Non-Zero APT Balances | 0 |
| Total APT (all wallets) | 0.00000000 |
| Healthy Multisigs | 5/5 |
| MNX Markets | unavailable (SPA) |

---

## GF(3) World Increment

| ID | Source | Event Type | GF3 Trit | Color | Name |
|----|--------|------------|-----------|-------|------|
| 13 | aptos_mainnet (hamming_swarm) | balance_snapshot | 1 | `#b8bb26` | **PLUS** |

GF(3) sequence position: `id=13` → trit=1 (PLUS)

---

## Hamming Swarm — Aptos Wallet Balances

### Non-Zero Balances
_All 28 addresses have zero APT balance (no CoinStore found on mainnet)._

### Zero-Balance Addresses
28 of 28 addresses returned 0 APT (resource_not_found = uninitialized account or empty).

---

## Multisig Contract Probes

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | `0x0da4f428a0c007da0f7629...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f859c...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df4062281c7...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49f0de...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650fddca...` | 2 | ✓ |

---

## MNX Testnet Markets

**Unavailable** — `testnet.mnx.fi` is a SPA; no JSON API endpoints responded at `/api/markets`, `/api/v1/markets`, or `/markets`.

---

## GitHub Context (plurigrid/gorj — MCP scope)

- MCP access scoped to `plurigrid/gorj` only.
- External orgs (kubeflow, TeglonLabs) and users (bmorphism, zubyul, social graph) not accessible without `gh` CLI.
- Previous repo_snapshots: 944 rows from prior sweeps covering 3 orgs + 8 users remain in DB.

---

## Notes
- `gh` CLI unavailable in this environment; GitHub queries limited to MCP-accessible scope (`plurigrid/gorj`).
- Aptos `resource_not_found` = account has no CoinStore (uninitialized or never received APT) → treated as 0.0 APT.
- All 28 Hamming addresses queried with 1s sleep between calls.
- Multisig probes via `0x1::multisig_account::num_signatures_required` view function.
