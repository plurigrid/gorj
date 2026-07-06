# World-Increment Sweep + Hamming Swarm Snapshot — 2026-07-06

## Sweep Metadata
- **Date:** 2026-07-06
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.4
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 (100 captured) |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 105 |
| zubyul | user | 49 |
| migalkin | user (social) | 19 |
| DJedamski | user (social) | 6 |
| wasita | user (social) | 11 |
| kristinezheng | user (social) | 5 |
| M1shaaa | user (social) | 8 |
| AustinCStone | user (social) | 40 |

### Notable Activity (2026)

- **plurigrid/shrimp, /asi, /place, /gorj** — most recently pushed plurigrid repos
- **bmorphism/satreadout** (2026-06-10) — Lean 4.28 machine-checked saturating perceptual readout
- **bmorphism/Gay.jl** — 187 open issues, wide-gamut GF(3) color SPI pattern (Julia)
- **bmorphism/penrose-mcp** — 9 stars, pushed 2026-06-24 (most recent push)
- **bmorphism/ocaml-mcp-sdk** — 61 stars, OCaml SDK for MCP using Jane Street's oxcaml_effect
- **bmorphism/anti-bullshit-mcp-server** — 23 stars, 7 forks
- **TeglonLabs/jank-crane** — GF3 convergence maps + loopify pass spec (C++, 2026-06-08)
- **zubyul/voice-observatory** — passive macOS TUI for voice-download pathways (2026-04-24)
- **zubyul/tilelang-kernels** — GF(3) trit classification GPU kernels for NVIDIA Blackwell
- **wasita/wasita.github.io** — updated 2026-07-05 (most recent social graph push)
- **migalkin/NodePiece** — 144 stars, ICLR'22 knowledge graph embeddings
- **AustinCStone/TextGAN** — 92 stars, TensorFlow text GAN

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 72 |
| 1 | PLUS | #b8bb26 | 74 |
| -1 | MINUS | #cc241d | 73 |

GF(3) assignment: `id%3==0` → trit=0 ERGODIC #d3869b | `id%3==1` → trit=1 PLUS #b8bb26 | `id%3==2` → trit=-1 MINUS #cc241d

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (alice–Z, 28 addresses)

**Status:** All 28 addresses return HTTP 404 on `CoinStore<AptosCoin>` resource.

Accounts **exist on-chain** with activity (alice: seq=72, A: seq=58) but have **no registered APT CoinStore**. These Aptos Move accounts are active but hold no native APT (possibly using alternative Move resources or not yet funded with APT directly).

| World | Address (truncated) | Balance |
|-------|---------------------|---------|
| alice | 0xc793acdec12b4a63... | no APT CoinStore (seq=72) |
| bob   | 0x0a3c00c58fdf9020... | no APT CoinStore |
| A     | 0x8699edc0960dd5b9... | no APT CoinStore (seq=58) |
| B–Z   | (24 addresses) | no APT CoinStore (all 404) |

### Multisig Contract Probes — All Healthy ✓

All 5 multisig contracts respond with `num_signatures_required = 2`.

| Pair | Address (truncated) | Sigs Required | Healthy |
|------|---------------------|---------------|---------|
| A-B | 0x0da4f428a0c007da... | 2 | ✓ |
| A-G | 0xf56c4a1c0906214f... | 2 | ✓ |
| Y-Z | 0xd3ffe1812b2df406... | 2 | ✓ |
| S-T | 0x3b1c3ae905d44c3a... | 2 | ✓ |
| V-W | 0x40fad7b423a84365... | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status:** HTTP 401 Unauthorized on all probed endpoints:
`/`, `/api/markets`, `/api/v1/markets`, `/api/tokens`, `/markets`

Testnet requires authentication — market data unavailable externally. Recorded as `unavailable` in `mnx_snapshots`.

---

## DuckDB Schema

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

## Summary Counts (this run)

| Table | Records |
|-------|---------|
| world_increments | 219 total |
| repo_snapshots | 1140 total |
| aptos_snapshots | 28 (this run) |
| multisig_probes | 5 (this run) |
| mnx_snapshots | 1 (unavailable) |
