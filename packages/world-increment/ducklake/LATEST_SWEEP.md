# World-Increment Sweep + Hamming Swarm Snapshot — 2026-08-04

## Sweep Metadata
- **Date:** 2026-08-04
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.5 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total World Increments (cumulative) | 24 |
| Total Repo Snapshots (cumulative) | 978 |
| Sources Covered | 3 orgs + 8 users |
| Repos Added This Sweep | ~507 new records |

### GF(3) Color Chain — This Sweep

GF(3) chain: `ERGODIC → PLUS → MINUS → ERGODIC → ...`
- `id mod 3 == 0` → trit=0, color=**#d3869b**, name=**ERGODIC**
- `id mod 3 == 1` → trit=1, color=**#b8bb26**, name=**PLUS**
- `id mod 3 == 2` → trit=-1, color=**#cc241d**, name=**MINUS**

Current sweep increment: trit=0, **ERGODIC** #d3869b

### Repo Counts by Source

| Source | Type | Repos Found |
|--------|------|-------------|
| plurigrid | org | 103 |
| kubeflow | org | 49 |
| TeglonLabs | org | 5 |
| bmorphism | user | 106 |
| zubyul | user | 49 |
| migalkin | social | 19 |
| DJedamski | social | 6 |
| wasita | social | 14 |
| kristinezheng | social | 5 |
| M1shaaa | social | 8 |
| AustinCStone | social | 41 |

### Top Repos by Stars (2026-08-04)

| Repo | Language | Stars | Last Push |
|------|----------|-------|-----------|
| kubeflow/kubeflow | — | 15,805 | 2026-08-04 |
| kubeflow/pipelines | Python | 4,175 | 2026-08-04 |
| kubeflow/spark-operator | Python | 3,143 | 2026-08-04 |
| kubeflow/trainer | Go | 2,169 | 2026-08-04 |
| kubeflow/katib | Python | 1,694 | 2026-08-01 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| bmorphism/ocaml-mcp-sdk | OCaml | 61 | 2026-05-08 |
| plurigrid/asi | HTML | 58 | 2026-08-01 |
| migalkin/NodePiece | Python | 144 | 2026-05-07 |
| migalkin/StarE | Python | 89 | 2026-04-16 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-08-02 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2026-03-19 |
| bmorphism/babashka-mcp-server | JavaScript | 19 | 2026-06-05 |
| plurigrid/vcg-auction | Rust | 7 | 2025-12-16 |

### Notable Activity (2026-08-04 live updates)

- **wasita/xoxowasita-analysis** — created AND pushed today (2026-08-04)
- **wasita/joint-planning-lit** — pushed today
- **kubeflow** — 6+ repos with activity today (kubeflow, pipelines, trainer, spark-operator, testing, common)
- **plurigrid/microworlds** — Rust, last push 2026-08-02

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet, 2026-08-04)

Queried 28 addresses via `fullnode.mainnet.aptoslabs.com/v1/accounts/{ADDR}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`.

**All 28 wallets: 0 APT**

No `CoinStore<AptosCoin>` resource found on any address. Wallets may be uninitiated on mainnet or hold no liquid APT in the standard coin module.

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
| G | 0x69a3...f32 | 0.0 |
| H | 0xce67...300f | 0.0 |
| I | 0x070f...1fc9 | 0.0 |
| J | 0x4d96...f54 | 0.0 |
| K | 0xa732...dc4 | 0.0 |
| L | 0x7c2e...ba9 | 0.0 |
| M | 0x6fed...f2e9 | 0.0 |
| N | 0xe7dd...1b2c | 0.0 |
| O | 0x7325...a89d | 0.0 |
| P | 0x6218...c948 | 0.0 |
| Q | 0xac40...c89a9 | 0.0 |
| R | 0x7ce6...e10 | 0.0 |
| S | 0xb875...0386 | 0.0 |
| T | 0x3578...4588 | 0.0 |
| U | 0x7586...9956 | 0.0 |
| V | 0xb59d...f2c3 | 0.0 |
| W | 0x5f32...c7b0 | 0.0 |
| X | 0xa95c...047d | 0.0 |
| Y | 0xd8e3...44c4 | 0.0 |
| Z | 0x7af0...97c | 0.0 |

### Multisig Contract Probes

Probed via `POST /v1/view` → `0x1::multisig_account::num_signatures_required`:

| Pair | Address (truncated) | Sigs Required | Status |
|------|---------------------|---------------|--------|
| A-B | 0x0da4...7003 | 2 | HEALTHY ✓ |
| A-G | 0xf56c...0096 | 2 | HEALTHY ✓ |
| Y-Z | 0xd3ff...b883 | 2 | HEALTHY ✓ |
| S-T | 0x3b1c...7883 | 2 | HEALTHY ✓ |
| V-W | 0x40fa...eb6d | 2 | HEALTHY ✓ |

All 5 multisig contracts respond on mainnet with 2-of-N threshold. **All HEALTHY.**

### MNX Markets (testnet.mnx.fi)

- `https://testnet.mnx.fi/api/markets` → **404 Not Found**
- `https://testnet.mnx.fi` → JavaScript SPA, renders only ticker symbol "MNX", no structured market data accessible via HTTP

**Status: UNAVAILABLE** — testnet.mnx.fi requires browser-side JS to render market data.

---

## Schema Reference

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
