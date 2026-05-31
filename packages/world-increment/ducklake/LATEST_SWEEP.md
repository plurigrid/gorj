# World-Increment Sweep + Hamming Snapshot
**Timestamp:** 2026-05-31  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.3 (Variegata) — `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Swept
| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| kubeflow | org | 48 |
| TeglonLabs | org | 4 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| migalkin | user (social) | 7 |
| AustinCStone | user (social) | 7 |
| wasita | user (social) | 6 |
| DJedamski | user (social) | 4 |
| kristinezheng | user (social) | 4 |
| M1shaaa | user (social) | 4 |
| **TOTAL** | | **333** |

### Top Repos by Stars
| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow (flagship) | 15,565 | — | — |
| kubeflow/pipelines | 4,119 | Python | 2026-04-10 |
| kubeflow/spark-operator | 3,111 | Python | 2026-04-10 |
| kubeflow/trainer | 2,080 | Go | 2026-04-10 |
| migalkin/NodePiece | 144 | Python | 2026-05-07 |
| migalkin/StarE | 89 | Python | 2026-04-16 |
| AustinCStone/TextGAN | 92 | Python | 2025-03-03 |
| migalkin/RWL | 8 | Python | 2026-05-28 |

### GF(3) Color Chain Distribution
- **ERGODIC** (#d3869b, trit=0): 111 repos (id%3==0)
- **PLUS** (#b8bb26, trit=1): 111 repos (id%3==1)
- **MINUS** (#cc241d, trit=-1): 111 repos (id%3==2)

Chain pattern: `PLUS → MINUS → ERGODIC → PLUS → MINUS → ERGODIC → ...` (×111 cycles)

### Notable Recent Activity
- `wasita/vocoder` — pushed 2026-05-06 (audio synthesis tool)
- `migalkin/RWL` — pushed 2026-05-28 (Weisfeiler & Leman Go Relational, LOG 2022)
- `wasita/wasita.github.io` — pushed 2026-05-20 (personal site, Svelte+Tailwind)
- `wasita/send2kobo` — pushed 2026-05-19 (Kobo e-reader book sender)
- `plurigrid/gorj` — this very repository

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances
All 28 addresses probed via `fullnode.mainnet.aptoslabs.com/v1`.  
**Result:** All accounts return `resource_not_found` for `0x1::coin::CoinStore<AptosCoin>` — balances are 0.0 APT (accounts unfunded on mainnet).

| World | Address | Balance (APT) |
|-------|---------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob   | 0x0a3c...512d | 0.0 |
| A     | 0x8699...9d7a | 0.0 |
| B     | 0x3f89...b13  | 0.0 |
| C     | 0x38b9...35e  | 0.0 |
| D     | 0xf776...dd1  | 0.0 |
| E     | 0xdc1d...d36  | 0.0 |
| F     | 0x18a1...f71  | 0.0 |
| G     | 0x69a3...f32  | 0.0 |
| H     | 0xce67...00f  | 0.0 |
| I–Z   | (18 addresses) | 0.0 each |

### Multisig Contract Probes
All 5 contracts probed via `POST /v1/view → 0x1::multisig_account::num_signatures_required`.

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

All 5 multisig contracts are **healthy** with 2-of-2 threshold.

### MNX Markets (testnet.mnx.fi)
SPA with client-side rendering; market data captured via browser-rendered DOM.

| Ticker | Name | Price | Change |
|--------|------|-------|--------|
| OAI26 | OpenAI Final 2026 Valuation | $532B | +0.57% |
| ANT26 | Anthropic Final 2026 Valuation | $419B | — |
| ECI26 | Epoch Capabilities Index 2026 | 167 | -1.76% |
| DPREZ | Democrat Elected President 2028 | 50% | -1.18% |
| INVADE27 | China Invades Taiwan (by end 2027) | 16% | -2.44% |
| NVDA | NVIDIA | $212.77 | +0.01% |
| AAPL | Apple | $311.12 | +0.06% |
| MSFT | Microsoft | $449.43 | +0.01% |
| TSLA | Tesla | $434.93 | +0.06% |
| SPX | S&P 500 Index | 7,575 | — |
| ASML | ASML Holding | $1,600 | -0.06% |
| INTC | Intel | $115.41 | -0.06% |
| TLT | iShares 20+ Year Treasury | $85.71 | +0.06% |
| H100 | SemiAnalysis H100 Rental Index | $2.88 | +1.05% |
| CPER | US Copper Index Fund | $38.92 | +0.10% |

---

## DuckDB Table Counts

| Table | Rows | Description |
|-------|------|-------------|
| world_increments | 333 | GF(3)-tagged repo events |
| repo_snapshots | 333 | Full repo metadata |
| aptos_snapshots | 28 | Hamming swarm wallet balances |
| multisig_probes | 5 | 2-of-2 multisig health checks |
| mnx_snapshots | 15 | MNX testnet market snapshot |

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
