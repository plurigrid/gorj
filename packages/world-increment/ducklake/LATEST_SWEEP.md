# World-Increment Sweep + Hamming Snapshot — 2026-04-22

## Sweep Metadata
- **Date:** 2026-04-22
- **Agent:** world-increment-sweep + hamming-swarm-snapshot
- **DuckDB version:** v1.5.2 (Variegata)
- **Database:** `packages/world-increment/ducklake/world-increments.duckdb`
- **GF(3):** Increment 24, id%3=0 → trit=0 **ERGODIC #d3869b**

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried
| Source | Type | Repos | Total Stars |
|--------|------|-------|-------------|
| plurigrid | org | 100 | 65 |
| kubeflow | org | 47 | 33,923 |
| TeglonLabs | org | 4 | 2 |
| bmorphism | user | 100 | 246 |
| zubyul | user | 47 | 14 |
| migalkin | social graph | 5 | 274 |
| wasita | social graph | 3 | 2 |
| AustinCStone | social graph | 4 | 104 |
| kristinezheng | social graph | 2 | 0 |
| DJedamski | social graph | 2 | 1 |
| M1shaaa | social graph | 2 | 0 |
| **TOTAL** | | **316** | **34,631** |

### Top Repos by Stars (this sweep)
| Org/User | Repo | Language | Stars | Last Push |
|----------|------|----------|-------|-----------|
| kubeflow | kubeflow | — | 15,594 | 2026-01-05 |
| kubeflow | pipelines | Python | 4,125 | 2026-04-21 |
| kubeflow | spark-operator | Python | 3,117 | 2026-04-21 |
| kubeflow | trainer | Go | 2,085 | 2026-04-21 |
| kubeflow | katib | Python | 1,680 | 2026-04-14 |
| kubeflow | examples | Jsonnet | 1,460 | 2025-04-14 |
| kubeflow | manifests | YAML | 1,012 | 2026-04-11 |
| migalkin | NodePiece | Python | 143 | 2026-03-02 |
| migalkin | StarE | Python | 89 | 2026-04-16 |
| AustinCStone | TextGAN | Python | 92 | 2025-03-03 |

### DuckDB State
- `world_increments`: 24 rows total
- `repo_snapshots`: 1,260 rows total (316 new this sweep)
- Cumulative sources: 11 orgs/users + social graph nodes

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances — Mainnet
> Method: `0x1::coin::balance<0x1::aptos_coin::AptosCoin>` view function  
> Ledger version: ~4,963,779,027

| World | Address (prefix) | Balance (APT) |
|-------|-----------------|---------------|
| bob | 0x0a3c00c5... | **12.65700700** |
| F | 0x18a14b5b... | 1.96051600 |
| L | 0x7c2eaeaf... | 1.92726900 |
| J | 0x4d964db8... | 1.89509300 |
| alice | 0xc793acde... | 0.43643352 |
| O | 0x73252b60... | 0.21013600 |
| K | 0xa732040a... | 0.16196100 |
| P | 0x62187... | 0.14013600 |
| M | 0x6fed37a7... | 0.11228500 |
| N | 0xe7dde6da... | 0.10612100 |
| Q | 0xac40fa50... | 0.10324000 |
| R | 0x7ce605cc... | 0.09021700 |
| S | 0xb8753014... | 0.09178800 |
| T | 0x35781dc0... | 0.07371300 |
| U | 0x75860da4... | 0.05577300 |
| A | 0x8699edc0... | 0.05176700 |
| V | 0xb59dd817... | 0.04883299 |
| Y | 0xd8e32848... | 0.04444900 |
| X | 0xa95cbbd1... | 0.04257700 |
| W | 0x5f32aef7... | 0.04070500 |
| B | 0x3f892ebe... | 0.03625600 |
| Z | 0x7af0ef6e... | 0.02426800 |
| D | 0xf7765624... | 0.01162900 |
| C | 0x38b99e63... | 0.01018500 |
| H | 0xce67c327... | 0.00168100 |
| E | 0xdc1d9d53... | 0.00937200 |
| G | 0x69a394c0... | 0.00068100 |
| I | 0x070fe5d7... | 0.00068100 |

**Total swarm balance: ~20.07 APT**

Note: `CoinStore<AptosCoin>` resource not found (accounts use legacy coin module).  
`0x1::coin::balance` view function returns correct balances.

### Multisig Contract Probes
> Function: `0x1::multisig_account::num_signatures_required`

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4f428... | 2 | ✓ |
| A-G | 0xf56c4a1c... | 2 | ✓ |
| Y-Z | 0xd3ffe181... | 2 | ✓ |
| S-T | 0x3b1c3ae9... | 2 | ✓ |
| V-W | 0x40fad7b4... | 2 | ✓ |

All 5 multisig contracts respond healthy. All require 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)
- **Status:** `503 Service Unavailable` — testnet unreachable at sweep time.
- Recorded as `UNAVAILABLE` in `mnx_snapshots` table.

---

## GF(3) Color Chain
```
id%3==0 → trit=0   ERGODIC  #d3869b  (pink/rose)
id%3==1 → trit=+1  PLUS     #b8bb26  (yellow-green)
id%3==2 → trit=-1  MINUS    #cc241d  (red)
```
Current sweep: id=24, 24%3=0 → **ERGODIC #d3869b**

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

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent*  
*Aptos Mainnet ledger version: ~4,963,779,027*
