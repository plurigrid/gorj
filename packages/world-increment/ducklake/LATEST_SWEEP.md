# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-08-05 UTC  
**Run:** world-increment-sweep + hamming-swarm-snapshot

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept

| Source | Type | Repos | GF3 Trit | Color |
|--------|------|-------|----------|-------|
| plurigrid | org | 100 | +1 PLUS | #b8bb26 |
| kubeflow | org | 49 | -1 MINUS | #cc241d |
| TeglonLabs | org | 5 | 0 ERGODIC | #d3869b |
| bmorphism | user | 15 (sampled) | +1 PLUS | #b8bb26 |
| zubyul | user | 14 (sampled) | -1 MINUS | #cc241d |
| migalkin | social | 6 | 0 ERGODIC | #d3869b |
| DJedamski | social | 2 | +1 PLUS | #b8bb26 |
| wasita | social | 5 | -1 MINUS | #cc241d |
| kristinezheng | social | 2 | 0 ERGODIC | #d3869b |
| M1shaaa | social | 2 | +1 PLUS | #b8bb26 |
| AustinCStone | social | 5 | -1 MINUS | #cc241d |

**Total repos snapshotted this sweep:** 205  
**Cumulative repo_snapshots in ducklake:** 1,149

### Notable Activity

- **bmorphism/anti-bullshit-mcp-server** — 23 stars, 7 forks, pushed 2026-08-02 (most recent bmorphism push)
- **bmorphism/Gay.jl** — 188 open issues, 2 stars; active development on `gay` branch
- **bmorphism/ocaml-mcp-sdk** — 61 stars (highest in bmorphism repos)
- **migalkin/NodePiece** — 144 stars, 21 forks (ICLR'22 knowledge graph paper)
- **AustinCStone/TextGAN** — 92 stars, 30 forks (TF text generation)
- **wasita/xoxowasita-analysis** — pushed 2026-08-05 (TODAY — most recent in graph)
- **wasita/joint-planning-lit** — pushed 2026-08-04
- **TeglonLabs/jank-crane** — pushed 2026-06-08 (jank+crane converged-IR hub, GF3 maps)

### DuckDB Schema

```
world_increments: 34 rows (11 new this sweep)
repo_snapshots:   1,149 rows (205 new this sweep)
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet)

Queried via `fullnode.mainnet.aptoslabs.com` REST API.  
All 28 addresses (alice, bob, A–Z) returned **no CoinStore resource** — balances not resolvable via public APT CoinStore endpoint. Addresses may hold non-APT assets, be uninitialized, or the resource path may differ. Stored as NULL in `aptos_snapshots`.

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| alice | 0xc793acdec12b… | N/A |
| bob   | 0x0a3c00c58fdf… | N/A |
| A–Z   | (26 addresses)  | N/A |

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428a0c0… | 2 | ✓ |
| A-G | 0xf56c4a1c0906… | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2d… | 2 | ✓ |
| S-T | 0x3b1c3ae905d4… | 2 | ✓ |
| V-W | 0x40fad7b423a8… | 2 | ✓ |

**All 5 multisig contracts healthy (2-of-2 threshold).**

### MNX Markets

`https://testnet.mnx.fi` returns a Next.js SPA — no REST API endpoints accessible (`/api/markets`, `/api/v1/markets` return HTML). Market data unavailable via programmatic fetch. Stored 0 rows in `mnx_snapshots`.

---

## GF3 Color Chain Summary

The 11 new world increments follow the GF(3) color chain:

```
id%3==0 → trit=0   ERGODIC  #d3869b (pink)
id%3==1 → trit=+1  PLUS     #b8bb26 (yellow-green)
id%3==2 → trit=-1  MINUS    #cc241d (red)
```

GF(3) chain this sweep:  
`PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → PLUS → MINUS`  
(plurigrid→PLUS, kubeflow→MINUS, TeglonLabs→ERGODIC, bmorphism→PLUS, zubyul→MINUS, migalkin→ERGODIC, DJedamski→PLUS, wasita→MINUS, kristinezheng→ERGODIC, M1shaaa→PLUS, AustinCStone→MINUS)

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
