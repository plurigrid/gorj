# World Increment + Hamming Swarm Snapshot
**Sweep date:** 2026-08-05  
**GF(3) increment #24 — ERGODIC (#d3869b) — trit=0**

---

## JOB 1: GitHub Social Graph Sweep

### Scope
- **Accessible:** `plurigrid` org (50 repos via MCP GitHub server)
- **Blocked by proxy scope:** kubeflow, TeglonLabs, bmorphism, zubyul, and social graph users (migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone) — session is scoped to `plurigrid/gorj` REST endpoints only; those sources exist in prior increments (#1–#12)

### plurigrid org — Top repos by activity

| Repo | Stars | Forks | Open Issues | Last Push | Language |
|------|-------|-------|-------------|-----------|----------|
| gorj | 1 | 0 | 1651 | 2026-08-05 | Clojure |
| eirobri | 0 | 0 | 31 | 2026-08-04 | Clojure |
| place | 1 | 2 | 15 | 2026-08-02 | Clojure |
| zig-syrup | 2 | 2 | 0 | 2026-07-28 | Zig |
| asi | 59 | 13 | 4 | 2026-07-10 | HTML |
| shrimp | 0 | 0 | 0 | 2026-07-03 | TeX |
| nash-portal | 2 | 2 | 1 | 2026-05-19 | Rust |
| asi-skills | 3 | 0 | 0 | 2026-04-26 | Julia |
| bci-blue-share | 0 | 0 | 0 | 2026-04-26 | JavaScript |
| nanoclj-zig | 1 | 1 | 20 | 2026-04-25 | Zig |

**50 repos snapshotted this run** (994 cumulative in world-increments.duckdb)

### Notable Activity Since Last Sweep
- **gorj** (1651 open issues) — most active, pushed today 2026-08-05
- **eirobri** (31 issues) — EiRoBri replay world, pushed 2026-08-04
- **place** (15 issues) — pushed 2026-08-02
- **nanoclj-zig** (20 issues) — NaN-boxed Clojure interpreter in Zig 0.15
- **asi** (59 stars) — highest stars in org, topological chemputer

### GF(3) Color Chain State
| Increment ID | Source | GF3 Trit | Color | Name |
|---|---|---|---|---|
| 24 | plurigrid (org) | 0 | #d3869b | ERGODIC |
| 23 | prior sweep | 2→-1 | #cc241d | MINUS |
| 22 | prior sweep | 1 | #b8bb26 | PLUS |

GF(3) rule: `id%3==0 → ERGODIC, id%3==1 → PLUS, id%3==2 → MINUS`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (Mainnet — 2026-08-05)
**28 addresses surveyed — all 0.0 APT** (unfunded/dormant as of sweep)

Endpoint: `https://fullnode.mainnet.aptoslabs.com/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>`

| World | Address (prefix) | APT Balance |
|-------|-----------------|-------------|
| alice | 0xc793ac... | 0.0 |
| bob | 0x0a3c00... | 0.0 |
| A | 0x8699ed... | 0.0 |
| B–Z (25 wallets) | ... | 0.0 each |

All 28 hamming-swarm addresses return zero APT balance. No funded wallets detected.

### Multisig Contract Probes (Aptos Mainnet)
**All 5 pairs healthy — 2-of-N signatures required**

| Pair | Address | Sigs Required | Status |
|------|---------|--------------|--------|
| A-B | 0x0da4f4... | 2 | ✓ healthy |
| A-G | 0xf56c4a... | 2 | ✓ healthy |
| Y-Z | 0xd3ffe1... | 2 | ✓ healthy |
| S-T | 0x3b1c3a... | 2 | ✓ healthy |
| V-W | 0x40fad7... | 2 | ✓ healthy |

All multisig contracts are live and configured with 2-of-N threshold.

### MNX Markets (testnet.mnx.fi)
**Status: SPA only — no public JSON API endpoint**  
`https://testnet.mnx.fi/api/markets` → 200 HTML (Next.js SPA, server-rendered shell). No machine-readable market data accessible without client-side JS. Recorded 0 rows in `mnx_snapshots`.

---

## DuckDB State After Sweep

```
world_increments:  24 rows  (+1 this sweep, increment #24 ERGODIC)
repo_snapshots:   994 rows  (+50 this sweep, plurigrid org)
aptos_snapshots:   28 rows  (+28 this sweep, all 0.0 APT)
multisig_probes:    5 rows  (+5 this sweep, all healthy 2-of-N)
mnx_snapshots:      0 rows  (SPA unavailable)
```

---

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
