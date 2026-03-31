# World-Increment Sweep — 2026-03-31

Sweep timestamp: 2026-03-31T09:13:38Z
DuckDB: v1.5.1 (Variegata) — world-increments.duckdb

---

## JOB 1: GitHub Social Graph Sweep

### Orgs and Users Queried
- **Orgs**: plurigrid, kubeflow, TeglonLabs
- **Users**: bmorphism, zubyul
- **Zubyul social graph**: migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Repo Snapshot Counts (repo_snapshots table)

| org_or_user   | repo count |
|---------------|-----------|
| plurigrid     | 120 |
| bmorphism     | 108 |
| kubeflow      | 56 |
| AustinCStone  | 46 |
| migalkin      | 33 |
| wasita        | 31 |
| zubyul        | 30 |
| kristinezheng | 20 |
| TeglonLabs    | 3 |
| M1shaaa       | 2 |
| DJedamski     | 2 |

**Total repo_snapshots rows**: 451 (cumulative including previous sweeps)
**New world_increments entries from this sweep**: 63 repos (76 total increments)

### GF(3) Color Chain Distribution

| GF3 Name | Trit | Color   | Count |
|----------|------|---------|-------|
| ERGODIC  | 0    | #d3869b | 25    |
| PLUS     | 1    | #b8bb26 | 26    |
| MINUS    | -1   | #cc241d | 25    |

GF(3) rule: id%3==0 → trit=0 ERGODIC #d3869b | id%3==1 → trit=1 PLUS #b8bb26 | id%3==2 → trit=-1 MINUS #cc241d

### Notable Repos by Source

**plurigrid**: `asi` (14 stars, HTML, pushed 2026-03-30), `asi-skills` (Julia, 69 Galois skills, 2026-03-28), `zig-syrup` (Zig OCapN Syrup), `blue` (TeX, 2026-03-29), `graded-optic` (Haskell semiring-graded optics), `nblm-flashcards` (Hy+Babashka, 2026-03-26)
**kubeflow**: `kubeflow` (15,547 stars), `pipelines` (4,114 stars, pushed 2026-03-31), `spark-operator` (3,110 stars), `trainer` (2,071 stars Go, pushed 2026-03-31)
**bmorphism**: `ocaml-mcp-sdk` (60 stars, OCaml, Jane Street oxcaml_effect), `anti-bullshit-mcp-server` (23 stars), `say-mcp-server` (20 stars TTS), `babashka-mcp-server` (18 stars)
**zubyul**: `gay-world` (Python MLX goblin worlds, 2026-03-26), `Gay.jl` (Julia wide-gamut SplitMix64, 2026-03-28), `tilelang-kernels` (GPU kernels for GF3 trit classification, 2026-03-16)
**migalkin**: `NodePiece` (143 stars, Knowledge Graph ICLR'22), `StarE` (88 stars, EMNLP 2020 hyper-relational KGs)
**AustinCStone**: `TextGAN` (92 stars, TensorFlow text generation GAN)
**TeglonLabs**: `mathpix-gem` (Ruby math OCR), `coin-flip-mcp` (JS random.org MCP)

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 addresses)

All 28 Hamming swarm wallets queried via Aptos mainnet fullnode:
`https://fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...2d5d | 0.0 |
| A     | 0x8699...b7a  | 0.0 |
| B     | 0x3f89...b13  | 0.0 |
| C     | 0x38b9...35e  | 0.0 |
| D     | 0xf776...dd1  | 0.0 |
| E     | 0xdc1d...d36  | 0.0 |
| F     | 0x18a1...f71  | 0.0 |
| G     | 0x69a3...f32  | 0.0 |
| H     | 0xce67...00f  | 0.0 |
| I     | 0x070f...fc9  | 0.0 |
| J     | 0x4d96...f54  | 0.0 |
| K     | 0xa732...dc4  | 0.0 |
| L     | 0x7c2e...ba9  | 0.0 |
| M     | 0x6fed...e9   | 0.0 |
| N     | 0xe7dd...b2c  | 0.0 |
| O     | 0x7325...89d  | 0.0 |
| P     | 0x6218...948  | 0.0 |
| Q     | 0xac40...89a9 | 0.0 |
| R     | 0x7ce6...e10  | 0.0 |
| S     | 0xb875...386  | 0.0 |
| T     | 0x3578...588  | 0.0 |
| U     | 0x7586...956  | 0.0 |
| V     | 0xb59d...2c3  | 0.0 |
| W     | 0x5f32...b0   | 0.0 |
| X     | 0xa95c...47d  | 0.0 |
| Y     | 0xd8e3...4c4  | 0.0 |
| Z     | 0x7af0...97c  | 0.0 |

Note: All wallets returned 0.0 APT (CoinStore resource not initialized or unfunded on mainnet).

### Multisig Contract Probes (5 pairs)

All 5 multisig contracts probed via `POST /v1/view` with `0x1::multisig_account::num_signatures_required`.

| Pair | Multisig Address (truncated)  | Sigs Required | Healthy |
|------|-------------------------------|---------------|---------|
| A-B  | 0x0da4...003                  | 2             | YES     |
| A-G  | 0xf56c...096                  | 2             | YES     |
| Y-Z  | 0xd3ff...883                  | 2             | YES     |
| S-T  | 0x3b1c...883                  | 2             | YES     |
| V-W  | 0x40fa...b6d                  | 2             | YES     |

All 5 multisig contracts are 2-of-N and responding on Aptos mainnet.

### MNX Markets (testnet.mnx.fi)

`https://testnet.mnx.fi/api/markets` returned a Next.js HTML page — no machine-readable JSON API endpoint is publicly accessible. Recorded as unavailable in `mnx_snapshots` table.

---

## DuckDB Tables Summary

| Table             | Rows |
|-------------------|------|
| world_increments  | 76   |
| repo_snapshots    | 451  |
| aptos_snapshots   | 28   |
| multisig_probes   | 5    |
| mnx_snapshots     | 1 (unavailable note) |

Database: `packages/world-increment/ducklake/world-increments.duckdb`

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS

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
