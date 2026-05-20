# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-30T19:23Z  
**Agent:** world-increment-sweep + hamming-swarm-snapshot  
**Database:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Sources Queried

| Source | Type | Repos |
|--------|------|-------|
| plurigrid | org | 100 |
| bmorphism | user | 100 |
| zubyul | user | 49 |
| kubeflow | org | 47 |
| AustinCStone | social (zubyul graph) | 40 |
| migalkin | social (zubyul graph) | 19 |
| wasita | social (zubyul graph) | 10 |
| M1shaaa | social (zubyul graph) | 8 |
| kristinezheng | social (zubyul graph) | 6 |
| DJedamski | social (zubyul graph) | 6 |
| TeglonLabs | org | 4 |
| **TOTAL** | | **389** |

### GF(3) Color Chain Distribution

| GF3 Trit | Name | Color | Count |
|----------|------|-------|-------|
| 0 | ERGODIC | #d3869b | 129 |
| 1 | PLUS | #b8bb26 | 130 |
| -1 | MINUS | #cc241d | 130 |

GF(3) chain per-repo: `id%3==0→ERGODIC, id%3==1→PLUS, id%3==2→MINUS` (389 increments, 129⅓ full cycles)

### Notable Repos (by stars, from this sweep)

| Repo | Stars | Language | Pushed |
|------|-------|----------|--------|
| kubeflow/pipelines | 4130 | Python | 2026-04-30 |
| kubeflow/manifests | 1013 | YAML | 2026-04-30 |
| kubeflow/dashboard | 17 | TypeScript | 2026-04-30 |
| TeglonLabs/mathpix-gem | 2 | Ruby | 2026-01-01 |
| plurigrid/zig-syrup | 2 | Zig | 2026-04-30 |

### DuckDB Schema

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

## JOB 2: Hamming Swarm Snapshot

### Aptos Mainnet Wallet Balances

All 28 addresses queried via `fullnode.mainnet.aptoslabs.com` (1s sleep between calls). All returned 0.0 APT — addresses have no registered `0x1::coin::CoinStore<AptosCoin>` resource (uninitialized accounts on mainnet) or hold zero APT at sweep time.

| World | Address (prefix…suffix) | Balance APT |
|-------|------------------------|-------------|
| alice | 0xc793…cc7b | 0.00 |
| bob | 0x0a3c…12d5d | 0.00 |
| A | 0x8699…e9d7a | 0.00 |
| B | 0x3f89…cb13 | 0.00 |
| C | 0x38b9…535e | 0.00 |
| D | 0xf776…cfdd1 | 0.00 |
| E | 0xdc1d…8d36 | 0.00 |
| F | 0x18a1…3cf71 | 0.00 |
| G | 0x69a3…c7f32 | 0.00 |
| H | 0xce67…300f | 0.00 |
| I | 0x070f…1fc9 | 0.00 |
| J | 0x4d96…7f54 | 0.00 |
| K–Z | (16 addresses) | 0.00 each |

**Total swarm APT:** 0.00 across 28 worlds

### Multisig Contract Probes

All 5 multisig contracts **healthy** — respond to `0x1::multisig_account::num_signatures_required`, all require **2-of-2 signatures**.

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|---------------|---------|
| A-B | 0x0da4…7003 | 2 | ✓ |
| A-G | 0xf56c…0096 | 2 | ✓ |
| Y-Z | 0xd3ff…b883 | 2 | ✓ |
| S-T | 0x3b1c…7883 | 2 | ✓ |
| V-W | 0x40fa…eb6d | 2 | ✓ |

### MNX Markets (testnet.mnx.fi)

**Status: UNAVAILABLE** — `testnet.mnx.fi` is a Next.js SPA. Paths `/api/markets` and `/api/v1/markets` return the HTML shell rather than JSON. No REST endpoint is accessible without client-side JS execution. Recorded as placeholder row in `mnx_snapshots`.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| GitHub repos snapshotted | 389 |
| Orgs/users covered | 11 |
| world_increments rows | 389 |
| repo_snapshots rows | 389 |
| Aptos wallets probed | 28 |
| Total APT balance | 0.00 |
| Multisig contracts healthy | 5/5 (all 2-of-2) |
| MNX markets available | 0 (SPA, no REST API) |
| DuckDB size on disk | ~2.3 MB |

## GF(3) Assignment Rule
- `id mod 3 == 0` → trit=0, color=#d3869b, name=ERGODIC
- `id mod 3 == 1` → trit=1, color=#b8bb26, name=PLUS
- `id mod 3 == 2` → trit=-1, color=#cc241d, name=MINUS
