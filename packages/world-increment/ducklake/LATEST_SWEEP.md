# LATEST_SWEEP — 2026-05-17

> world-increment sweep + hamming snapshot | GF(3) trit color chain

## JOB 1: GitHub Social Graph Sweep

**Timestamp:** 2026-05-17 (UTC)
**DuckDB:** `packages/world-increment/ducklake/world-increments.duckdb`

### Sources Swept

| Source | Type |
|--------|------|
| plurigrid | org |
| kubeflow | org |
| TeglonLabs | org |
| bmorphism | user |
| zubyul | user |
| migalkin | user (social graph) |
| DJedamski | user (social graph) |
| wasita | user (social graph) |
| kristinezheng | user (social graph) |
| M1shaaa | user (social graph) |
| AustinCStone | user (social graph) |

### Repository Counts by Source

```
org_or_user,repos,total_stars
kubeflow,32,33377
migalkin,4,268
AustinCStone,4,103
plurigrid,61,74
bmorphism,6,6
wasita,4,3
TeglonLabs,4,2
DJedamski,2,1
kristinezheng,2,0
zubyul,5,0
M1shaaa,3,0
```

### Top 15 Repos by Stars

```
org_or_user,repo_name,language,stars,forks
kubeflow,kubeflow,NULL,15642,2647
kubeflow,pipelines,Python,4140,1993
kubeflow,spark-operator,Python,3125,1482
kubeflow,trainer,Go,2099,949
kubeflow,katib,Python,1682,521
kubeflow,examples,Jsonnet,1463,757
kubeflow,manifests,YAML,1017,1064
kubeflow,arena,Go,810,190
kubeflow,kale,Python,687,156
kubeflow,mpi-operator,Go,527,235
kubeflow,fairing,Jsonnet,337,143
kubeflow,pytorch-operator,Jsonnet,310,143
kubeflow,community,Jsonnet,196,257
kubeflow,website,HTML,184,920
kubeflow,hub,Go,175,178
```

### Most Recently Pushed (Top 10)

```
org_or_user,repo_name,pushed_at
plurigrid,gorj,2026-05-17T20:12:55Z
kubeflow,pipelines,2026-05-17T16:25:03Z
M1shaaa,M1shaaa,2026-05-17T13:13:06Z
wasita,wasita.github.io,2026-05-17T00:37:28Z
bmorphism,Gay.jl,2026-05-17T00:34:34Z
kubeflow,manifests,2026-05-16T16:37:54Z
kubeflow,dashboard,2026-05-16T00:25:13Z
kubeflow,mlflow-integration,2026-05-15T19:20:29Z
kubeflow,kale,2026-05-15T19:04:47Z
kubeflow,spark-operator,2026-05-15T16:31:02Z
```

### GF(3) Trit Color Chain Distribution

```
gf3_name,gf3_color,cnt
ERGODIC,#d3869b,42
MINUS,#cc241d,42
PLUS,#b8bb26,43
```

- `id%3==0` → trit=0  ERGODIC `#d3869b`
- `id%3==1` → trit=1  PLUS    `#b8bb26`
- `id%3==2` → trit=-1 MINUS   `#cc241d`

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

```
wallets,total_apt,funded
28,0.0,0
```

**All 28 wallets (alice, bob, A-Z) queried against Aptos mainnet fullnode.**
**Result: All balances 0.0 APT** — accounts hold no AptosCoin CoinStore resource (unfunded/uninitialized).

| World | Address (truncated)       | Balance APT |
|-------|---------------------------|-------------|
| alice | 0xc793...cc7b             | 0.0         |
| bob   | 0x0a3c...2d5d             | 0.0         |
| A     | 0x8699...9d7a             | 0.0         |
| B     | 0x3f89...b13              | 0.0         |
| C     | 0x38b9...535e             | 0.0         |
| D     | 0xf776...fdd1             | 0.0         |
| E     | 0xdc1d...8d36             | 0.0         |
| F     | 0x18a1...3cf71            | 0.0         |
| G     | 0x69a3...c7f32            | 0.0         |
| H     | 0xce67...300f             | 0.0         |
| I     | 0x070f...1fc9             | 0.0         |
| J     | 0x4d96...f54              | 0.0         |
| K     | 0xa732...25dc4            | 0.0         |
| L     | 0x7c2e...eba9             | 0.0         |
| M     | 0x6fed...7f2e9            | 0.0         |
| N     | 0xe7dd...51b2c            | 0.0         |
| O     | 0x7325...5a89d            | 0.0         |
| P     | 0x6218...ec948            | 0.0         |
| Q     | 0xac40...c89a9            | 0.0         |
| R     | 0x7ce6...76e10            | 0.0         |
| S     | 0xb875...d0386            | 0.0         |
| T     | 0x3578...3f4588           | 0.0         |
| U     | 0x7586...ef9956           | 0.0         |
| V     | 0xb59d...af2c3            | 0.0         |
| W     | 0x5f32...cc7b0            | 0.0         |
| X     | 0xa95c...3047d            | 0.0         |
| Y     | 0xd8e3...2444c4           | 0.0         |
| Z     | 0x7af0...e197c            | 0.0         |

### Multisig Contract Probes (Aptos mainnet)

```
pair,address,sigs_required,healthy
A-B,0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003,2,true
A-G,0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096,2,true
Y-Z,0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883,2,true
S-T,0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883,2,true
V-W,0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d,2,true
```

**All 5 multisig accounts are healthy, each requiring 2-of-N signatures.**

| Pair | Address (truncated)     | Sigs Required | Healthy |
|------|-------------------------|---------------|---------|
| A-B  | 0x0da4...7003           | 2             | true    |
| A-G  | 0xf56c...0096           | 2             | true    |
| Y-Z  | 0xd3ff...b883           | 2             | true    |
| S-T  | 0x3b1c...7883           | 2             | true    |
| V-W  | 0x40fa...eb6d           | 2             | true    |

### MNX Markets (testnet.mnx.fi)

**Status: SPA — no embedded market data available**

`testnet.mnx.fi` serves a Next.js single-page app. The `/markets` route
returns HTTP 200 (~18KB HTML) but renders client-side only. API paths
`/api/markets`, `/api/v1/markets`, `/api/tickers` all return 404. Market
data requires browser JavaScript execution.

---

## DuckDB Table Summary

```
tbl,rows
world_increments,127
repo_snapshots,127
aptos_snapshots,28
multisig_probes,5
mnx_snapshots,0
```

---

*Generated autonomously by world-increment-sweep + hamming-swarm-snapshot agent.*
