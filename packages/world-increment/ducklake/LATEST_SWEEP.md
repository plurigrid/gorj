# World-Increment Sweep + Hamming Swarm Snapshot — 2026-05-07

## Sweep Metadata
- **Date:** 2026-05-07
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Source Summary

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 44 |
| bmorphism | user | 29 |
| kubeflow | org | 24 |
| zubyul | user | 22 |
| AustinCStone | social-graph (zubyul) | 7 |
| wasita | social-graph (zubyul) | 6 |
| migalkin | social-graph (zubyul) | 5 |
| TeglonLabs | org | 4 |
| kristinezheng | social-graph (zubyul) | 3 |
| M1shaaa | social-graph (zubyul) | 3 |
| DJedamski | social-graph (zubyul) | 3 |
| **TOTAL** | | **150** |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 50 |
| +1 | PLUS | `#b8bb26` | 50 |
| -1 | MINUS | `#cc241d` | 50 |

### Top Repos by Source

**plurigrid (44):** gorj (102 open issues), asi (HTML, 21★), ontology (JS, 7★), zig-syrup (Zig, 2★)

**kubeflow (24):** kubeflow (15,625★), pipelines (Python, 4,136★), spark-operator (3,124★), trainer (Go, 2,095★), katib (1,683★)

**bmorphism (29):** ocaml-mcp-sdk (OCaml, 60★), anti-bullshit-mcp-server (JS, 23★), Gay.jl (Julia, 187 open issues), shitcoin (Python, 5★)

**zubyul (22):** gay-world (Python, 1★), zubyul.github.io (CSS, 1★), plurigrid-site (Svelte)

**Social graph highlights:**
- migalkin/NodePiece (Python, 144★, ICLR'22)
- migalkin/StarE (Python, 89★, EMNLP'20)
- AustinCStone/TextGAN (Python, 92★)
- wasita/magic-garden (Python, 2★) — discord game bot

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm wallets (alice, bob, A–Z) queried against Aptos mainnet `fullnode.mainnet.aptoslabs.com`.

**Result:** All 28 addresses returned 0.0 APT — `CoinStore<AptosCoin>` resource not found on any address. Accounts exist on-chain but hold no APT in this sweep.

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...c7b | 0.0 |
| bob | 0x0a3c...d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

### Multisig Contract Probes — ALL HEALTHY ✓

All 5 Hamming swarm 2-of-2 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4...003 | 2 | ✓ healthy |
| A-G | 0xf56c...096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...883 | 2 | ✓ healthy |
| S-T | 0x3b1c...883 | 2 | ✓ healthy |
| V-W | 0x40fa...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

`testnet.mnx.fi` is a Next.js SPA. No public REST endpoints (`/api/markets`, `/api/tickers`, `/api`) returned structured JSON market data — all render client-side. `mnx_snapshots` table empty for this sweep.

---

## DuckDB Schema

```sql
world_increments  -- 150 rows  (GF3-colored repo push events, id%3 chain)
repo_snapshots    -- 150 rows  (org/user/repo metadata)
aptos_snapshots   -- 28 rows   (Hamming swarm APT balances)
multisig_probes   -- 5 rows    (2-of-2 multisigs, all healthy)
mnx_snapshots     -- 0 rows    (SPA, no JSON API accessible)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
