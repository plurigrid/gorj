# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-19

## Sweep Metadata
- **Date:** 2026-07-19
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4 (Python)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **Prior sweep:** 2026-04-12 (12 increments, 471 repos)

---

## Summary Counts

| Metric | This Sweep | Cumulative |
|--------|-----------|-----------|
| New World Increments | 12 | 24 |
| Repo Snapshots (new) | 394 | 1338 total |
| Sources Covered | 3 orgs + 8 users | — |
| Aptos Wallets Probed | 28 | — |
| Multisig Contracts Probed | 5 | — |
| MNX Markets | unavailable (Vercel auth) | — |

---

## JOB 1: GitHub Social Graph — GF(3) Color Chain

### New Increments (13–24)

| ID | Source | Type | Repos | GF3 Trit | Color | Name |
|----|--------|------|-------|-----------|-------|------|
| 13 | plurigrid | org | 100 | +1 | `#b8bb26` | **PLUS** |
| 14 | kubeflow | org | 49 | -1 | `#cc241d` | **MINUS** |
| 15 | TeglonLabs | org | 5 | 0 | `#d3869b` | **ERGODIC** |
| 16 | bmorphism | user | 100 | +1 | `#b8bb26` | **PLUS** |
| 17 | zubyul | user | 49 | -1 | `#cc241d` | **MINUS** |
| 18 | migalkin | user | 19 | 0 | `#d3869b` | **ERGODIC** |
| 19 | DJedamski | user | 6 | +1 | `#b8bb26` | **PLUS** |
| 20 | wasita | user | 12 | -1 | `#cc241d` | **MINUS** |
| 21 | kristinezheng | user | 5 | 0 | `#d3869b` | **ERGODIC** |
| 22 | M1shaaa | user | 8 | +1 | `#b8bb26` | **PLUS** |
| 23 | AustinCStone | user | 41 | -1 | `#cc241d` | **MINUS** |
| 24 | plurigrid/gorj | sweep_complete | — | 0 | `#d3869b` | **ERGODIC** |

GF(3) chain continues: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC`

### Repo Counts by Source

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| AustinCStone | user | 41 |
| migalkin | user | 19 |
| wasita | user | 12 |
| M1shaaa | user | 8 |
| DJedamski | user | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | user | 5 |
| **TOTAL** | | **394** |

### Notable Repos (by stars)

| Repo | Language | Stars | Note |
|------|----------|-------|------|
| kubeflow/kubeflow | — | 15,782 | flagship ML platform |
| kubeflow/pipelines | Python | 4,169 | active |
| kubeflow/spark-operator | Python | 3,139 | active |
| kubeflow/trainer | Go | 2,152 | active |
| kubeflow/katib | Python | 1,691 | active |
| migalkin/NodePiece | Python | 143 | KG embeddings |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | MCP in OCaml |
| plurigrid/asi | HTML | 31 | +15 stars since Apr |
| kubeflow/mcp-server | Python | 28 | new! MCP for Kubeflow |
| TeglonLabs/jank-crane | C++ | 0 | new! GF3 convergence maps |

### Delta Since 2026-04-12

- **plurigrid/asi**: ★16 → ★31 (+15 stars, pushed 2026-07-10)
- **plurigrid/gorj**: pushed 2026-07-19 (this repo, active)
- **kubeflow/trainer**: ★2080 → ★2152 (+72 stars)
- **kubeflow/pipelines**: ★4119 → ★4169 (+50 stars)
- **TeglonLabs/jank-crane**: new repo (C++, GF3 convergence maps, 2026-06-08)
- **kubeflow/mcp-server**: new repo (Python MCP integration, ★28)
- **wasita**: new repos created in 2026 (pnas-typst-template, vocoder, ch3-lib)
- **M1shaaa/M1shaaa**: pushed 2026-07-19 (active today)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 wallets (alice, bob, A–Z) returned `resource_not_found` from Aptos mainnet
(ledger version ~6.36B), indicating no initialized `CoinStore<AptosCoin>` resource.
**Balance: 0.0 APT** for all addresses.

| World | Address (truncated) | APT Balance |
|-------|---------------------|-------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...512d | 0.0 |
| A | 0x8699...9d7a | 0.0 |
| B | 0x3f89...b13 | 0.0 |
| C | 0x38b9...535e | 0.0 |
| D | 0xf776...fdd1 | 0.0 |
| E | 0xdc1d...8d36 | 0.0 |
| F | 0x18a1...cf71 | 0.0 |
| G | 0x69a3...7f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...7f54 | 0.0 |
| K | 0xa732...5dc4 | 0.0 |
| L | 0x7c2e...eba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...6e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...f956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...197c | 0.0 |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts healthy — each requires **2 signatures**.

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | ✓ healthy |
| A-G | 0xf56c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ff...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c...7883 | 2 | ✓ healthy |
| V-W | 0x40fa...eb6d | 2 | ✓ healthy |

Uniform 2-of-N threshold across all probed pairs. All contracts responsive to
`0x1::multisig_account::num_signatures_required` view function.

### MNX Markets

`https://testnet.mnx.fi` is protected by Vercel deployment authentication.
No market data could be extracted without an OIDC token or bypass token.

---

## Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)

aptos_snapshots(timestamp, world, address, balance_apt)
multisig_probes(timestamp, pair, address, sigs_required, healthy)
mnx_snapshots(timestamp, ticker, name, category, price, change_pct)
```

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
