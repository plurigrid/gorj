# LATEST_SWEEP — World Increment + Hamming Swarm Snapshot

**Timestamp:** 2026-04-30T15:27:58Z  
**DuckDB Version:** v1.5.2 (Variegata)  
**GF(3) Color Chain:** ERGODIC #d3869b (trit=0) · PLUS #b8bb26 (trit=1) · MINUS #cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### Summary

| Metric | Value |
|--------|-------|
| World Increments | 385 |
| Repo Snapshots | 385 |
| Sources Queried | plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul, migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone |

### GF(3) Distribution

```
gf3_name,gf3_color,cnt
ERGODIC,#d3869b,128
MINUS,#cc241d,128
PLUS,#b8bb26,129
```

### Repos by Source

```
org_or_user,repos
plurigrid,100
bmorphism,100
zubyul,49
kubeflow,47
AustinCStone,36
migalkin,19
wasita,10
M1shaaa,8
kristinezheng,6
DJedamski,6
TeglonLabs,4
```

### Top Starred Repos

```
full_name,language,stars,forks
kubeflow/kubeflow,,15610,2646
kubeflow/pipelines,Python,4130,1986
kubeflow/spark-operator,Python,3121,1483
kubeflow/trainer,Go,2095,947
kubeflow/katib,Python,1681,521
kubeflow/examples,Jsonnet,1460,757
kubeflow/manifests,YAML,1013,1065
kubeflow/arena,Go,810,191
kubeflow/kale,Python,684,157
kubeflow/mpi-operator,Go,524,235
kubeflow/fairing,Jsonnet,337,143
kubeflow/pytorch-operator,Jsonnet,310,143
kubeflow/community,Jsonnet,195,256
kubeflow/website,HTML,184,918
kubeflow/kfctl,Go,182,134
```

### Recent Pushes — plurigrid

```
full_name,language,pushed_at
plurigrid/gorj,Clojure,2026-04-30T12:34:59Z
plurigrid/zig-syrup,Zig,2026-04-30T03:52:16Z
plurigrid/horse,TeX,2026-04-29T20:35:13Z
plurigrid/asi,HTML,2026-04-26T08:51:41Z
plurigrid/nash-portal,Rust,2026-04-26T08:50:56Z
plurigrid/asi-skills,Julia,2026-04-26T08:09:26Z
plurigrid/bci-blue-share,JavaScript,2026-04-26T07:08:03Z
plurigrid/nanoclj-zig,Zig,2026-04-25T07:29:09Z
```

### Recent Pushes — bmorphism

```
full_name,language,pushed_at
bmorphism/boxxy,Move,2026-04-30T03:35:47Z
bmorphism/Gay.jl,Julia,2026-04-30T00:32:01Z
bmorphism/nanoclj-zig,Zig,2026-04-25T07:29:15Z
bmorphism/postweb,Go,2026-04-09T10:51:57Z
bmorphism/shitcoin,Python,2026-04-08T08:07:08Z
bmorphism/magic-world-org,Python,2026-04-05T07:03:50Z
bmorphism/zig-syrup,Zig,2026-03-28T21:42:32Z
bmorphism/ocaml-mcp-sdk,OCaml,2026-03-16T05:24:25Z
```

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances

**Total APT across swarm:** 20.34477251 APT

```
world,balance_apt
world,balance_apt
bob,12.657007
F,1.960516
L,1.927269
J,1.895093
alice,0.43643352
O,0.210136
K,0.161961
P,0.140136
M,0.112285
N,0.106121
Q,0.10324
S,0.091788
R,0.090217
T,0.073713
U,0.055773
A,0.051767
V,0.04883299
Y,0.044449
X,0.042577
W,0.040705
B,0.036256
Z,0.024268
D,0.011629
C,0.010185
E,0.009372
H,0.001681
I,0.000681
G,0.000681
```

### Multisig Contract Probes

All 5 multisig contracts are **healthy** (2-of-2 threshold):

```
pair,address,sigs_required,healthy
A-B,0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003,2,true
A-G,0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096,2,true
Y-Z,0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883,2,true
S-T,0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883,2,true
V-W,0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d,2,true
```

| Pair | Address | Sigs Required | Status |
|------|---------|---------------|--------|
| A-B | 0x0da4f428...87003 | 2 | ✓ healthy |
| A-G | 0xf56c4a1c...0096 | 2 | ✓ healthy |
| Y-Z | 0xd3ffe181...b883 | 2 | ✓ healthy |
| S-T | 0x3b1c3ae9...7883 | 2 | ✓ healthy |
| V-W | 0x40fad7b4...b6d | 2 | ✓ healthy |

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable via direct API — `testnet.mnx.fi` is a Next.js SPA; no REST/JSON endpoints found at `/api/markets`, `/api/v1/markets`, `/markets`, `/api/tickers`. Market data requires browser JS execution.

---

## DuckDB Schema

```
world_increments  — 385 rows  (GF3 color-chained event log)
repo_snapshots    — 385 rows  (GitHub repo metadata)
aptos_snapshots   — 28 rows          (Hamming swarm wallet balances)
multisig_probes   — 5 rows           (Aptos multisig health checks)
mnx_snapshots     — 1 row            (MNX unavailable marker)
```
