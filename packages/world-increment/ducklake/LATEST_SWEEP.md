# World Increment Sweep + Hamming Swarm Snapshot

**Run date:** 2026-07-30  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Captured |
|--------|------|---------------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 49 |
| migalkin | social-graph | 19 |
| AustinCStone | social-graph | 15 |
| wasita | social-graph | 12 |
| M1shaaa | social-graph | 8 |
| DJedamski | social-graph | 6 |
| TeglonLabs | org | 5 |
| kristinezheng | social-graph | 5 |
| **TOTAL** | | **368** |

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color | Count |
|----------|------|-------|-------|
| ERGODIC | 0 | `#d3869b` | 122 |
| PLUS | +1 | `#b8bb26` | 123 |
| MINUS | -1 | `#cc241d` | 123 |

### Notable Repos (by stars)

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/spark-operator | 3142 | Python |
| kubeflow/trainer | 2163 | Go |
| kubeflow/kale | 698 | Python |
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| plurigrid/asi | 56 | HTML |

### TeglonLabs (new since last sweep)
- `jank-crane` (C++) — crane-jank converged-IR hub, GF3 convergence maps — pushed 2026-06-08
- `mathpix-gem` (Ruby, 2★) — math image→LaTeX OCR gem — pushed 2026-01-01
- `coin-flip-mcp` (JavaScript) — MCP server with random.org integration
- `monad-mcp-server` — Monad MCP Server
- `topoi` (Python) — topoi research

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 accounts)

All 28 Hamming swarm wallets (alice, bob, A–Z) returned **0.00 APT**.  
Accounts are either unfunded on mainnet or the coin store resource is not initialized.

| World | Address (prefix) | Balance |
|-------|-----------------|---------|
| alice | 0xc793…4cc7b | 0.0 APT |
| bob | 0x0a3c…512d | 0.0 APT |
| A–Z (26) | various | 0.0 APT each |

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts are **healthy** — all requiring 2-of-2 signatures.

| Pair | Address (prefix) | Sigs Required | Status |
|------|-----------------|---------------|--------|
| A-B | 0x0da4…7003 | 2 | healthy |
| A-G | 0xf56c…0096 | 2 | healthy |
| Y-Z | 0xd3ff…b883 | 2 | healthy |
| S-T | 0x3b1c…7883 | 2 | healthy |
| V-W | 0x40fa…eb6d | 2 | healthy |

### MNX Markets (testnet.mnx.fi)

The MNX testnet frontend is a **Next.js SPA** — no public REST API endpoint is exposed. Paths probed:
- `https://testnet.mnx.fi` → renders SPA HTML (no embedded market data)
- `https://testnet.mnx.fi/api/markets` → not found
- `https://testnet.mnx.fi/api/v1/markets` → not found

Status: **unavailable** — recorded as placeholder in `mnx_snapshots`.

---

## DuckDB Tables

| Table | Rows |
|-------|------|
| world_increments | 368 |
| repo_snapshots | 368 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 1 (placeholder) |

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
