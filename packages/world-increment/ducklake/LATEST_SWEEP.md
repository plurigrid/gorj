# World-Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-26  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb` (v1.5.2)

---

## JOB 1: GitHub Social Graph Sweep

### Sources Snapshotted

| Source | Type | Repos Captured | Latest Push |
|--------|------|---------------|-------------|
| plurigrid | org | 100 | 2026-04-26 |
| kubeflow | org | 47 | 2026-04-26 |
| TeglonLabs | org | 4 | 2026-01-01 |
| bmorphism | user | 100 | 2026-04-26 |
| zubyul | user | 49 | 2026-04-24 |
| migalkin | social | 6 | 2026-04-16 |
| AustinCStone | social | 6 | 2026-04-01 |
| wasita | social | 5 | 2026-04-22 |
| DJedamski | social | 4 | 2023-04-21 |
| M1shaaa | social | 3 | 2026-02-04 |
| kristinezheng | social | 3 | 2026-04-09 |

**Total repos this sweep:** 327  
**Total world_increments (all time):** 34  
**Total repo_snapshots (all time):** 1,271

### Top Languages (this sweep, by stars)

| Language | Repos | Total Stars |
|----------|-------|-------------|
| Python | 60 | 10,458 |
| Go | 15 | 3,986 |
| Jsonnet | 8 | 2,411 |
| YAML | 1 | 1,012 |
| TypeScript | 23 | 342 |
| Jupyter Notebook | 13 | 268 |
| HTML | 14 | 229 |
| JavaScript | 19 | 129 |
| OCaml | 2 | 61 |
| Rust | 26 | 40 |
| Zig | 7 | 6 |
| Julia | 9 | 4 |

### GF(3) Color Chain

| Trit | Color | Name | Meaning |
|------|-------|------|---------|
| 0 | `#d3869b` | ERGODIC | id % 3 == 0 |
| +1 | `#b8bb26` | PLUS | id % 3 == 1 |
| -1 | `#cc241d` | MINUS | id % 3 == 2 |

### Notable Repos (this sweep)

- **plurigrid/asi** — HTML, 17 stars — active 2026-04-25
- **plurigrid/nanoclj-zig** — Zig — active 2026-04-25
- **plurigrid/zig-syrup** — Zig, 2 stars — active 2026-04-24
- **kubeflow/pipelines** — Python, 4,125 stars, 1,983 forks — active 2026-04-26
- **kubeflow/mcp-apache-spark-history-server** — Python, 152 stars — active 2026-04-25
- **kubeflow/trainer** — Go, 2,092 stars, 947 forks — active 2026-04-25
- **bmorphism/Gay.jl** — Julia — active 2026-04-26
- **bmorphism/nanoclj-zig** — Zig — active 2026-04-25
- **zubyul/voice-observatory** — Python — active 2026-04-24
- **zubyul/ghostel-emacs-worlds** — GLSL — active 2026-04-24
- **migalkin/NodePiece** — Python, 143 stars (ICLR 2022 scalable KG embeddings)
- **migalkin/StarE** — Python, 89 stars (EMNLP 2020 hyper-relational KGs)
- **AustinCStone/TextGAN** — Python, 92 stars (GAN for text generation)
- **TeglonLabs/mathpix-gem** — Ruby, 2 stars — math/chem OCR gem
- **wasita/wasita.github.io** — Svelte, 1 star — active 2026-04-22

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances (28 addresses)

All 28 Hamming swarm addresses (alice, bob, A-Z) returned NULL balance.
Accounts have no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource on Aptos mainnet.

| World | Address | Balance APT |
|-------|---------|-------------|
| alice | 0xc793...cc7b | NULL |
| bob | 0x0a3c...2d5d | NULL |
| A | 0x8699...9d7a | NULL |
| B | 0x3f89...b13 | NULL |
| C | 0x38b9...535e | NULL |
| D | 0xf776...fdd1 | NULL |
| E | 0xdc1d...8d36 | NULL |
| F | 0x18a1...cf71 | NULL |
| G | 0x69a3...7f32 | NULL |
| H | 0xce67...300f | NULL |
| I | 0x070f...1fc9 | NULL |
| J | 0x4d96...7f54 | NULL |
| K | 0xa732...5dc4 | NULL |
| L | 0x7c2e...eba9 | NULL |
| M | 0x6fed...f2e9 | NULL |
| N | 0xe7dd...1b2c | NULL |
| O | 0x7325...a89d | NULL |
| P | 0x6218...c948 | NULL |
| Q | 0xac40...c89a9 | NULL |
| R | 0x7ce6...6e10 | NULL |
| S | 0xb875...0386 | NULL |
| T | 0x3578...4588 | NULL |
| U | 0x7586...f9956 | NULL |
| V | 0xb59d...af2c3 | NULL |
| W | 0x5f32...c7b0 | NULL |
| X | 0xa95c...047d | NULL |
| Y | 0xd8e3...444c4 | NULL |
| Z | 0x7af0...197c | NULL |

### Multisig Contract Probes (5 contracts)

All 5 multisig contracts are healthy: 2-of-n threshold confirmed live on Aptos mainnet.

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f428...987003 | 2 | HEALTHY |
| A-G | 0xf56c4a1c...c0096 | 2 | HEALTHY |
| Y-Z | 0xd3ffe181...eb883 | 2 | HEALTHY |
| S-T | 0x3b1c3ae9...d7883 | 2 | HEALTHY |
| V-W | 0x40fad7b4...0eb6d | 2 | HEALTHY |

All multisigs use a 2-of-n signature threshold, consistent with paired Hamming swarm topology.

### MNX Markets (testnet.mnx.fi)

MNX testnet is a SPA. All probed API paths (/api/markets, /api/v1/markets, /api/tickers)
return the same 16,963-byte HTML shell with no JSON data. Status: UNAVAILABLE via REST API.

---

## DuckDB Table Summary

| Table | Rows (all time) |
|-------|----------------|
| world_increments | 34 |
| repo_snapshots | 1,271 |
| aptos_snapshots | 28 |
| multisig_probes | 5 |
| mnx_snapshots | 0 (SPA, no data) |

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

- `id mod 3 == 0` -> trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` -> trit=+1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` -> trit=-1, color=#cc241d, name=MINUS
