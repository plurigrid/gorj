# World-Increment Sweep + Hamming Swarm Snapshot — 2026-04-13

**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**DuckDB:** v1.5.2 (Variegata)  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary Counts

| Metric | Value |
|--------|-------|
| Total world_increments | 176 |
| Total repo_snapshots | 176 |
| Sources covered | 3 orgs + 8 users |
| Total GitHub stars | 34,460 |

### GF(3) Color Chain Distribution

| Trit | Name | Color | Count |
|------|------|-------|-------|
| 0 | ERGODIC | `#d3869b` | 58 |
| +1 | PLUS | `#b8bb26` | 59 |
| -1 | MINUS | `#cc241d` | 59 |

GF(3) rule: `id%3==0 → ERGODIC #d3869b`, `id%3==1 → PLUS #b8bb26`, `id%3==2 → MINUS #cc241d`

### Repos by Source

| Source | Type | Repos | Stars |
|--------|------|-------|-------|
| plurigrid | org | 99 | 62 |
| kubeflow | org | 47 | 33,868 |
| bmorphism | user | 10 | 181 |
| zubyul | user | 5 | 1 |
| TeglonLabs | org | 4 | 2 |
| migalkin | social | 3 | 241 |
| wasita | social | 3 | 1 |
| AustinCStone | social | 2 | 103 |
| kristinezheng | social | 1 | 0 |
| M1shaaa | social | 1 | 0 |
| DJedamski | social | 1 | 1 |
| **TOTAL** | | **176** | **34,460** |

### Notable Repos

| Repo | Lang | Stars | Pushed |
|------|------|-------|--------|
| kubeflow/spark-operator | Python | 3,114 | 2026-04-11 |
| kubeflow/trainer | Go | 2,081 | 2026-04-10 |
| migalkin/NodePiece | Python | 143 | 2026-03-02 |
| AustinCStone/TextGAN | Python | 92 | 2025-03-03 |
| migalkin/StarE | Python | 88 | 2026-02-22 |
| bmorphism/ocaml-mcp-sdk | OCaml | 60 | 2026-03-28 |
| bmorphism/anti-bullshit-mcp-server | JavaScript | 23 | 2026-02-05 |
| bmorphism/risc0-cosmwasm-example | Rust | 23 | 2025-05-21 |
| bmorphism/say-mcp-server | JavaScript | 20 | 2026-03-19 |
| bmorphism/manifold-mcp-server | JavaScript | 13 | 2025-12-30 |
| bmorphism/penrose-mcp | JavaScript | 10 | 2026-04-12 |
| AustinCStone/StereoVisionMRF | Python | 11 | 2026-04-01 |
| migalkin/NBFNet_mlx | Python | 10 | 2026-03-11 |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (28 wallets, 2026-04-13)

**Total APT: 20.3448 APT** (queried via `0x1::coin::balance` view function on mainnet)

| World | Balance (APT) | Address (truncated) |
|-------|--------------|---------------------|
| bob | 12.657007 | `0x0a3c00c5...` |
| F | 1.960516 | `0x18a14b5b...` |
| L | 1.927269 | `0x7c2eaeaf...` |
| J | 1.895093 | `0x4d964db8...` |
| alice | 0.436434 | `0xc793acde...` |
| O | 0.210136 | `0x73252b60...` |
| K | 0.161961 | `0xa732040a...` |
| P | 0.140136 | `0x62187920...` |
| M | 0.112285 | `0x6fed37a7...` |
| N | 0.106121 | `0xe7dde6da...` |
| Q | 0.103240 | `0xac40fa50...` |
| S | 0.091788 | `0xb8753014...` |
| R | 0.090217 | `0x7ce605cc...` |
| T | 0.073713 | `0x35781dc0...` |
| U | 0.055773 | `0x75860da4...` |
| A | 0.051767 | `0x8699edc0...` |
| V | 0.048833 | `0xb59dd817...` |
| Y | 0.044449 | `0xd8e32848...` |
| X | 0.042577 | `0xa95cbbd1...` |
| W | 0.040705 | `0x5f32aef7...` |
| B | 0.036256 | `0x3f892ebe...` |
| Z | 0.024268 | `0x7af0ef6e...` |
| D | 0.011629 | `0xf7765624...` |
| C | 0.010185 | `0x38b99e63...` |
| E | 0.009372 | `0xdc1d9d53...` |
| H | 0.001681 | `0xce67c327...` |
| G | 0.000681 | `0x69a394c0...` |
| I | 0.000681 | `0x070fe5d7...` |

### Multisig Contract Probes (5/5 healthy, 2-of-N each)

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | `0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003` | 2 | ✓ healthy |
| A-G | `0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096` | 2 | ✓ healthy |
| Y-Z | `0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883` | 2 | ✓ healthy |
| S-T | `0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883` | 2 | ✓ healthy |
| V-W | `0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d` | 2 | ✓ healthy |

### MNX Markets — testnet.mnx.fi (32 markets, 2026-04-13)

**Top movers (24h):**

| Ticker | Name | Category | Price | 24h Δ |
|--------|------|----------|-------|-------|
| USO | United States Oil Fund | Commodities | $133.63 | **+6.91%** |
| VIX | CBOE Volatility Index | Financial | 20.53 | **+6.76%** |
| CPI26 | U.S. CPI Annual Inflation Dec 2026 | Financial | 3% | **+6.51%** |
| CRWV | CoreWeave | Stocks | $106.07 | **+3.13%** |
| INTC | Intel | Stocks | $64.20 | **+2.84%** |
| SFHOME26 | SF Home Price Index 2026 | Financial | 387.0 | **+1.18%** |
| INVADE27 | China invades Taiwan before 2027 | Politics | 16% | **+0.61%** |
| ANT26 | Anthropic Final 2026 Valuation | Valuations | $421B | **+0.96%** |
| DPREZ | Democrat Elected President 2028 | Politics | 50% | **-3.31%** |
| SILVER | Silver Spot | Commodities | $73.77 | **-2.99%** |
| URA | Global X Uranium ETF | Commodities | $50.00 | **-1.81%** |
| ARC26 | Arc AGI 2 Highest 2026 Score | AI | 56% | **-1.75%** |
| NVDA | NVIDIA | Stocks | $186.28 | -1.17% |
| AAPL | Apple | Stocks | $258.41 | -0.92% |
| ASML | ASML Holding | Stocks | $1,500 | -0.80% |

**AI prediction markets snapshot:**

| Ticker | Description | Price |
|--------|-------------|-------|
| OAI26 | OpenAI Final 2026 Valuation | $523B |
| ANT26 | Anthropic Final 2026 Valuation | $421B |
| ARC26 | Arc AGI 2 Highest 2026 Score | 56% |
| ECI26 | Epoch Capabilities Index Max Score 2026 | 171 |
| FMATH26 | FrontierMath Highest 2026 Score 2026 | 50% |
| OAITOP26 | OpenAI Produces Top AI Model in 2026 | 23% |

---

## DuckDB Schema

```sql
world_increments(id, timestamp, gf3_trit, gf3_color, gf3_name,
                 source_type, source_name, event_type, repo_name,
                 actor, snapshot_hash)          -- 176 rows

repo_snapshots(id, timestamp, increment_id, org_or_user, repo_name,
               full_name, language, stars, forks, open_issues,
               pushed_at, description)          -- 176 rows

aptos_snapshots(timestamp, world, address,
                balance_apt)                     -- 28 rows

multisig_probes(timestamp, pair, address,
                sigs_required, healthy)          -- 5 rows

mnx_snapshots(timestamp, ticker, name,
              category, price, change_pct)       -- 32 rows
```
