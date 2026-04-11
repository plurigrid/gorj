# World Increment Sweep + Hamming Swarm Snapshot

**Sweep timestamp:** 2026-04-11T00:30:53Z  
**GF(3) increment id:** 1 | trit=1 | color=PLUS | hex=#b8bb26  
**Snapshot hash:** `e5f8d213add9074c`  
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 98 |
| kubeflow | org | 47 |
| TeglonLabs | org | 4 |
| bmorphism | user | 99 |
| zubyul | user | 45 |
| migalkin | social (zubyul) | 19 |
| DJedamski | social (zubyul) | 6 |
| wasita | social (zubyul) | 6 |
| kristinezheng | social (zubyul) | 6 |
| M1shaaa | social (zubyul) | 8 |
| AustinCStone | social (zubyul) | 20 |
| **TOTAL** | | **358** |

### Top Repos by Stars

| Repo | Stars | Language |
|------|-------|----------|
| kubeflow/kubeflow | 15,565 | — |
| kubeflow/pipelines | 4,119 | Python |
| kubeflow/spark-operator | 3,111 | Python |
| kubeflow/trainer | 2,080 | Go |
| kubeflow/katib | 1,676 | Python |
| kubeflow/examples | 1,458 | Jsonnet |
| kubeflow/manifests | 1,010 | YAML |
| kubeflow/arena | 808 | Go |
| kubeflow/kale | 682 | Python |
| migalkin/NodePiece | 143 | Python |
| bmorphism/anti-bullshit-mcp-server | 23 | JavaScript |
| bmorphism/ocaml-mcp-sdk | 60 | OCaml |
| migalkin/StarE | 88 | Python |
| plurigrid/asi | 16 | HTML |
| plurigrid/asi-skills | 3 | Julia |

### Most Recently Pushed

| Repo | Last Push |
|------|-----------|
| plurigrid/gorj | 2026-04-10T23:20:48Z |
| kubeflow/pipelines | 2026-04-10T23:13:20Z |
| kubeflow/model-registry | 2026-04-10T22:07:31Z |
| plurigrid/horse | 2026-04-10T21:52:15Z |
| kubeflow/arena | 2026-04-10T18:21:33Z |
| kubeflow/spark-operator | 2026-04-10T18:21:12Z |
| kubeflow/sdk | 2026-04-10T16:34:20Z |
| kubeflow/notebooks | 2026-04-10T14:09:19Z |

### GF(3) Color Chain

Each world-increment row is colored by `id % 3`:
- `id%3==0` → trit=0, ERGODIC, `#d3869b`
- `id%3==1` → trit=1, PLUS, `#b8bb26` ← **this sweep**
- `id%3==2` → trit=-1, MINUS, `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

All 28 Hamming swarm addresses queried against Aptos mainnet. No CoinStore resources found — wallets are not initialized on mainnet (no APT deposited).

| World | Address (truncated) | Balance (APT) |
|-------|---------------------|---------------|
| alice | 0xc793...cc7b | 0.0 |
| bob | 0x0a3c...2d5d | 0.0 |
| A–Z | (26 addresses) | 0.0 each |

**Interpretation:** All 28 addresses have no `0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` resource, indicating uninitiated accounts on Aptos mainnet. Addresses may be active on testnet/devnet or used for smart contract deployment without holding APT.

### Multisig Contract Probes

All 5 multisig contracts are healthy (2-of-2 threshold).

| Pair | Address | Sigs Required | Healthy |
|------|---------|---------------|---------|
| A-B | 0x0da4...7003 | 2 | ✓ |
| A-G | 0xf56c...0096 | 2 | ✓ |
| Y-Z | 0xd3ff...b883 | 2 | ✓ |
| S-T | 0x3b1c...7883 | 2 | ✓ |
| V-W | 0x40fa...eb6d | 2 | ✓ |

**All 5 multisig contracts operational with 2-of-2 signature requirement.**

### MNX Markets (testnet.mnx.fi)

| Ticker | Name | Category | Price | 24h Change |
|--------|------|----------|-------|------------|
| CRWV | CoreWeave | tech | $103.11 | +12.52% |
| NVDA | NVIDIA | tech | $188.63 | +2.92% |
| ASML | ASML | tech | $1,482.98 | +2.27% |
| INVADE27 | China Taiwan Invasion 2027 | prediction | 18% | +1.73% |
| DPREZ | Democrat 2028 President | prediction | 50% | +1.63% |
| SLVR | Silver Spot | commodity | $76.09 | +1.16% |
| OAI26 | OpenAI 2026 Valuation | prediction | $527B | +0.19% |
| ARC26 | Arc AGI 2 Score | prediction | 59% | 0.00% |
| SPX | S&P 500 | index | 6,813 | -0.12% |
| GOLD | Gold Spot | commodity | $4,747.15 | -0.16% |
| ANT26 | Anthropic 2026 Valuation | prediction | $425B | -0.23% |
| USO | Oil Fund | commodity | $124.91 | -1.68% |

---

## DuckDB Schema

```sql
world_increments  -- GF(3)-colored sweep metadata (1 row this sweep)
repo_snapshots    -- 358 repos across 11 sources
aptos_snapshots   -- 28 wallet balances (all 0.0 APT, no CoinStore)
multisig_probes   -- 5 contracts, all 2-of-2, all healthy
mnx_snapshots     -- 12 MNX market entries
```

## Querying the ducklake

```bash
duckdb packages/world-increment/ducklake/world-increments.duckdb \
  "SELECT org_or_user, count(*) FROM repo_snapshots GROUP BY 1 ORDER BY 2 DESC;"
```
