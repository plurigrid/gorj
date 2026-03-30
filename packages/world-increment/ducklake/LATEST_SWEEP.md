# World-Increment Sweep — 2026-03-30T04:45:00Z

## Sweep Metadata
- **Date:** 2026-03-30T04:45:00Z
- **Agent:** claude-agent (world-increment-sweep)
- **DuckDB version:** v1.5.1 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Snapshot hash:** `b7a3c9d8e2f14a56`

---

## Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments | 12 |
| Total Repo Snapshots | 36 |
| Aptos Snapshots | 28 |
| Multisig Probes | 5 |
| Sources Covered | 3 orgs + 8 users |

---

## GitHub Sources Covered

| Source | Type | Repos Collected | Repos Stored |
|--------|------|-----------------|--------------|
| plurigrid | org | 100 | 10 |
| kubeflow | org | 0 (rate limited) | 0 |
| TeglonLabs | org | 0 (rate limited) | 0 |
| bmorphism | user | 100 | 6 |
| zubyul | user | 23 | 4 |
| migalkin | user | 19 | 4 |
| DJedamski | user | 6 | 2 |
| wasita | user | 9 | 3 |
| kristinezheng | user | 6 | 2 |
| M1shaaa | user | 8 | 2 |
| AustinCStone | user | 40 | 3 |
| **TOTAL** | | **311** | **36** |

---

## Top 5 Repos by Stars (All Sources)

| Rank | Repo | Stars | Language | Description |
|------|------|-------|----------|-------------|
| 1 | migalkin/NodePiece | 143 | Python | Compositional KG representations |
| 2 | AustinCStone/TextGAN | 92 | Python | GAN for text generation in TensorFlow |
| 3 | migalkin/StarE | 88 | Python | Message passing for hyper-relational KGs |
| 4 | bmorphism/ocaml-mcp-sdk | 60 | OCaml | OCaml SDK for Model Context Protocol |
| 5 | bmorphism/anti-bullshit-mcp-server | 23 | JavaScript | MCP claim validation server |

---

## Aptos Wallet Balances

All 28 addresses returned 0.0 APT. The Aptos mainnet CoinStore resource was not found or balance is zero for all probed addresses.

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A-Z | 0x8699...197c | 0.0 (all) |

---

## Multisig Probe Results

All 5 multisig accounts confirmed healthy with 2-of-N signatures required.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | true |
| A-G | 0xf56c...0096 | 2 | true |
| Y-Z | 0xd3ff...b883 | 2 | true |
| S-T | 0x3b1c...7883 | 2 | true |
| V-W | 0x40fa...eb6d | 2 | true |

---

## MNX Market Data

**Status: Unavailable**
All three API endpoints (`/api/markets`, `/api/v1/markets`, `/api/tickers`) at `https://testnet.mnx.fi` returned HTML (Next.js frontend). No JSON market data available. No rows inserted into `mnx_snapshots`.

---

## GF(3) Color Chain for This Run

| ID | Trit | Color | Name | Assigned To |
|----|------|-------|------|-------------|
| 1 | +1 | #b8bb26 | PLUS | sweep/world-increment |
| 2 | -1 | #cc241d | MINUS | org/plurigrid |
| 3 | 0 | #d3869b | ERGODIC | org/kubeflow |
| 4 | +1 | #b8bb26 | PLUS | org/TeglonLabs |
| 5 | -1 | #cc241d | MINUS | user/bmorphism |
| 6 | 0 | #d3869b | ERGODIC | user/zubyul |
| 7 | +1 | #b8bb26 | PLUS | user/migalkin |
| 8 | -1 | #cc241d | MINUS | user/DJedamski |
| 9 | 0 | #d3869b | ERGODIC | user/wasita |
| 10 | +1 | #b8bb26 | PLUS | user/kristinezheng |
| 11 | -1 | #cc241d | MINUS | user/M1shaaa |
| 12 | 0 | #d3869b | ERGODIC | user/AustinCStone |

GF(3) chain: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

**Distribution:** PLUS(+1): 4, MINUS(-1): 4, ERGODIC(0): 4

---

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
