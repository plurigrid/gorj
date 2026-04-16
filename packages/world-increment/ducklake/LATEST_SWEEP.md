# World Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-04-16 03:09:37 UTC
**Branch:** world-increment/sweep-2026-04-16-0309

---

## JOB 1: GitHub Social Graph Sweep

### GF(3) Color Chain
| id%3 | Trit | Color   | Name    |
|------|------|---------|---------|
| 0    | 0    | #d3869b | ERGODIC |
| 1    | +1   | #b8bb26 | PLUS    |
| 2    | -1   | #cc241d | MINUS   |

### Sources Swept (11 increments)

| ID | GF3    | Color   | Type | Source         | Repos |
|----|--------|---------|------|----------------|-------|
| 1  | PLUS   | #b8bb26 | org  | plurigrid      | 100   |
| 2  | MINUS  | #cc241d | org  | kubeflow       | 47    |
| 3  | ERGODIC| #d3869b | org  | TeglonLabs     | 53    |
| 4  | PLUS   | #b8bb26 | user | bmorphism      | 100   |
| 5  | MINUS  | #cc241d | user | zubyul         | 24    |
| 6  | ERGODIC| #d3869b | user | migalkin       | 30    |
| 7  | PLUS   | #b8bb26 | user | DJedamski      | 11    |
| 8  | MINUS  | #cc241d | user | wasita         | 31    |
| 9  | ERGODIC| #d3869b | user | kristinezheng  | 18    |
| 10 | PLUS   | #b8bb26 | user | M1shaaa        | 16    |
| 11 | MINUS  | #cc241d | user | AustinCStone   | 43    |

**Total repos snapshotted this sweep: 473**

### Top Repos by Stars
| Repo                      | Stars | Language |
|---------------------------|-------|----------|
| kubeflow/kubeflow         | 15577 |          |
| kubeflow/pipelines        | 4120  | Python   |
| kubeflow/spark-operator   | 3116  | Python   |
| kubeflow/trainer          | 2085  | Go       |
| kubeflow/katib            | 1678  | Python   |
| kubeflow/examples         | 1460  | Jsonnet  |
| kubeflow/manifests        | 1010  | YAML     |

### Recent Events (bmorphism + zubyul)
| User      | Event              | Repo                      |
|-----------|--------------------|---------------------------|
| bmorphism | PushEvent          | plurigrid/reafference     |
| bmorphism | CreateEvent        | plurigrid/reafference     |
| bmorphism | CommitCommentEvent | plurigrid/nash-portal     |
| bmorphism | PushEvent          | plurigrid/nash-portal     |
| bmorphism | CreateEvent        | plurigrid/nash-portal     |
| zubyul    | PullRequestEvent   | plurigrid/horse           |
| zubyul    | CreateEvent        | plurigrid/horse           |
| zubyul    | PullRequestEvent   | plurigrid/gorj            |
| zubyul    | CreateEvent        | plurigrid/gorj            |
| zubyul    | PullRequestEvent   | plurigrid/gorj            |

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (28 addresses)

| World | Balance (APT) |
|-------|--------------|
| bob   | 12.65700700  |
| F     | 1.96051600   |
| L     | 1.92726900   |
| J     | 1.89509300   |
| alice | 0.43643352   |
| O     | 0.21013600   |
| K     | 0.16196100   |
| P     | 0.14013600   |
| M     | 0.11228500   |
| N     | 0.10612100   |
| Q     | 0.10324000   |
| S     | 0.09178800   |
| R     | 0.09021700   |
| T     | 0.07371300   |
| U     | 0.05577300   |
| A     | 0.05176700   |
| V     | 0.04883299   |
| Y     | 0.04444900   |
| X     | 0.04257700   |
| W     | 0.04070500   |
| B     | 0.03625600   |
| Z     | 0.02426800   |
| D     | 0.01162900   |
| C     | 0.01018500   |
| E     | 0.00937200   |
| H     | 0.00168100   |
| I     | 0.00068100   |
| G     | 0.00068100   |

**Total APT (all 28 wallets): 20.34477251 APT**

*Note: Balances queried via `0x1::coin::balance` view function (accounts use FA model, no legacy CoinStore).*

### Multisig Contract Probes (5 pairs)

| Pair | Address (truncated)   | Sigs Required | Healthy |
|------|-----------------------|---------------|---------|
| A-B  | 0x0da4f428...987003  | 2             | ✓       |
| A-G  | 0xf56c4a1c...c0096   | 2             | ✓       |
| Y-Z  | 0xd3ffe181...b883    | 2             | ✓       |
| S-T  | 0x3b1c3ae9...d7883   | 2             | ✓       |
| V-W  | 0x40fad7b4...eb6d    | 2             | ✓       |

All 5/5 multisigs healthy — 2-of-N threshold each.

### MNX Markets (testnet.mnx.fi)

Status: **Unavailable** — testnet.mnx.fi is a Next.js SPA; no REST API endpoints respond to JSON queries (all paths return HTML). Market data is rendered client-side and not accessible via curl.

---

## DuckDB Tables

| Table              | Rows (this run) |
|--------------------|----------------|
| world_increments   | 22 (11 sweeps + 10 events + prev) |
| repo_snapshots     | 473 new        |
| aptos_snapshots    | 28             |
| multisig_probes    | 5              |
| mnx_snapshots      | 1 (unavailable)|

DB: `packages/world-increment/ducklake/world-increments.duckdb`
