# World-Increment Sweep + Hamming Snapshot — 2026-07-31

## Sweep Metadata
- **Date:** 2026-07-31
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Snapshotted | Total ★ |
|--------|------|-------------------|---------|
| plurigrid | org | 23 | 81 |
| bmorphism | user | 17 | 101 |
| zubyul | user | 11 | 7 |
| migalkin | social-graph | 6 | 278 |
| AustinCStone | social-graph | 9 | 107 |
| wasita | social-graph | 7 | 5 |
| DJedamski | social-graph | 5 | 3 |
| M1shaaa | social-graph | 3 | 0 |
| kristinezheng | social-graph | 4 | 0 |
| **TOTAL** | | **85** | **582** |

Note: kubeflow and TeglonLabs are present in the DB from prior sweeps. This run covers the personal social graph around plurigrid/bmorphism/zubyul.

### Top Repos by Stars (This Sweep)

| Repo | Stars | Language |
|------|-------|----------|
| migalkin/NodePiece | 144 | Python |
| AustinCStone/TextGAN | 92 | Python |
| migalkin/StarE | 89 | Python |
| bmorphism/ocaml-mcp-sdk | 61 | OCaml |
| plurigrid/asi | 56 | HTML |
| bmorphism/anti-bullshit-mcp-server | 22 | JavaScript |
| migalkin/kgcourse2021 | 24 | HTML |
| AustinCStone/StereoVisionMRF | 11 | Python |
| plurigrid/ontology | 8 | JavaScript |
| migalkin/NBFNet_mlx | 10 | Python |

### Notable Activity

- **plurigrid/gorj** (this repo): pushed 2026-07-31, 1541 open issues — most recently active
- **plurigrid/zig-syrup**: pushed 2026-07-28, OCapN Syrup Zig implementation
- **bmorphism/Gay.jl**: pushed 2026-07-21, wide-gamut color sampling with splittable determinism
- **wasita/wasita.github.io**: pushed 2026-07-21, active personal site
- **bmorphism/gay-chat**: new 2026-07-14, Spritely Brassica Chat operationalization
- **AustinCStone/byteruckus**: new 2026-07-15

### GF(3) World-Increment Chain (85 New Increments)

GF(3) trit distribution for this sweep:
- trit=0 ERGODIC (#d3869b): 28 increments
- trit=1 PLUS (#b8bb26): 29 increments
- trit=-1 MINUS (#cc241d): 28 increments

Chain: `ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ...` (85 steps)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-07-31)

All 28 wallets (alice, bob, A–Z) queried against `fullnode.mainnet.aptoslabs.com`.

**Result: All 28 wallets return 0.00000000 APT.**

The Hamming swarm wallets are structurally defined but unfunded on Aptos mainnet.

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | 0xc793...c7b | 0.0 APT |
| bob | 0x0a3c...d5d | 0.0 APT |
| A–Z (26 wallets) | 0x8699...–0x7af0... | 0.0 APT each |

### Multisig Contract Probes

All 5 pairs probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4... | 2 | ✓ |
| A-G | 0xf56c... | 2 | ✓ |
| Y-Z | 0xd3ff... | 2 | ✓ |
| S-T | 0x3b1c... | 2 | ✓ |
| V-W | 0x40fa... | 2 | ✓ |

**All 5 multisig contracts healthy: 2-of-2 threshold confirmed.**

### MNX Markets (testnet.mnx.fi)

`/api/markets` and `/api/v1/markets` both return the Next.js SPA HTML. No REST API is accessible without authentication or client-side JS execution. Market data: **unavailable**.

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
- `id mod 3 == 0` → trit=0, name=ERGODIC, color=#d3869b
- `id mod 3 == 1` → trit=1, name=PLUS, color=#b8bb26
- `id mod 3 == 2` → trit=-1, name=MINUS, color=#cc241d
