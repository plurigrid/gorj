# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-06-02 21:18 UTC
**GF(3) color chain:** ERGODIC=#d3869b (trit=0) | PLUS=#b8bb26 (trit=1) | MINUS=#cc241d (trit=-1)

---

## JOB 1: GitHub Social Graph Sweep

### World Increments (GF3 chain)

```
id,gf3_name,gf3_color,source_name,event_type
1,PLUS,#b8bb26,plurigrid,repo_snapshot
1,PLUS,#b8bb26,plurigrid,repo_sweep
2,MINUS,#cc241d,kubeflow,repo_snapshot
2,MINUS,#cc241d,kubeflow,repo_sweep
3,ERGODIC,#d3869b,TeglonLabs,repo_sweep
3,ERGODIC,#d3869b,TeglonLabs,repo_snapshot
4,PLUS,#b8bb26,bmorphism,repo_snapshot
4,PLUS,#b8bb26,bmorphism,repo_sweep
5,MINUS,#cc241d,zubyul,repo_snapshot
5,MINUS,#cc241d,zubyul,repo_sweep
6,ERGODIC,#d3869b,migalkin,repo_snapshot
6,ERGODIC,#d3869b,migalkin,repo_sweep
7,PLUS,#b8bb26,DJedamski,repo_snapshot
7,PLUS,#b8bb26,DJedamski,repo_sweep
8,MINUS,#cc241d,wasita,repo_snapshot
8,MINUS,#cc241d,wasita,repo_sweep
9,ERGODIC,#d3869b,kristinezheng,repo_snapshot
9,ERGODIC,#d3869b,kristinezheng,repo_sweep
10,PLUS,#b8bb26,M1shaaa,repo_snapshot
10,PLUS,#b8bb26,M1shaaa,repo_sweep
11,MINUS,#cc241d,AustinCStone,repo_snapshot
11,MINUS,#cc241d,AustinCStone,repo_sweep
12,ERGODIC,#d3869b,bmorphism,sweep_complete
13,PLUS,#b8bb26,plurigrid+kubeflow+TeglonLabs+bmorphism+zubyul+social-graph,repo-snapshot
14,MINUS,#cc241d,bmorphism+zubyul+TeglonLabs+social-graph,repo-snapshot
```

### Repo Snapshots by Source

```
org_or_user,count,total_stars
org_or_user,n,total_stars
bmorphism,300,508
plurigrid,300,155
kubeflow,142,101895
AustinCStone,126,324
TeglonLabs,110,14
zubyul,97,40
migalkin,79,834
wasita,71,11
kristinezheng,42,0
M1shaaa,40,0
DJedamski,28,17
```

**Total sources:** plurigrid, kubeflow, TeglonLabs, bmorphism, zubyul
**Social graph:** migalkin, DJedamski, wasita, kristinezheng, M1shaaa, AustinCStone

### Top Starred Repos

```
owner,repo,language,stars,pushed_at
org_or_user,repo_name,language,stars,pushed_at
kubeflow,kubeflow,,15703,2026-05-24T11:31:41Z
kubeflow,kubeflow,NULL,15572,2026-01-05T13:47:10Z
kubeflow,kubeflow,,15565,2026-01-05T13:47:10Z
kubeflow,pipelines,Python,4151,2026-06-02T19:02:03Z
kubeflow,pipelines,Python,4119,2026-04-10T23:07:19Z
kubeflow,pipelines,Python,4119,2026-04-14T01:20:50Z
kubeflow,spark-operator,Python,3125,2026-06-01T18:54:42Z
kubeflow,spark-operator,Python,3114,2026-04-13T18:28:43Z
kubeflow,spark-operator,Python,3111,2026-04-10T18:21:12Z
kubeflow,trainer,Go,2110,2026-06-02T15:38:58Z
kubeflow,trainer,Go,2082,2026-04-13T23:41:09Z
kubeflow,trainer,Go,2080,2026-04-10T13:35:59Z
kubeflow,katib,Python,1685,2026-05-29T21:30:47Z
kubeflow,katib,Python,1678,2026-04-14T01:21:37Z
kubeflow,katib,Python,1676,2026-04-02T07:08:12Z
kubeflow,examples,Jsonnet,1462,2025-04-14T01:54:52Z
kubeflow,examples,Jsonnet,1459,2025-04-14T01:54:52Z
kubeflow,examples,Jsonnet,1458,2025-04-14T01:54:52Z
kubeflow,manifests,YAML,1020,2026-06-02T18:56:27Z
kubeflow,manifests,YAML,1010,2026-04-11T13:16:34Z
```

---

## JOB 2: Hamming Swarm Snapshot (Aptos Mainnet)

### Wallet Balances (APT)

All 28 Hamming swarm wallets queried against Aptos mainnet CoinStore resource.
All wallets returned 0 APT (accounts exist but CoinStore resource not initialized
or balance is zero — standard for fresh or pre-funded accounts awaiting deployment).

```
world,address,balance_apt
world,address,balance_apt
A,0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a,0.0
B,0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13,0.0
C,0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e,0.0
D,0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1,0.0
E,0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36,0.0
F,0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71,0.0
G,0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32,0.0
H,0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f,0.0
I,0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9,0.0
J,0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54,0.0
K,0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4,0.0
L,0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9,0.0
M,0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9,0.0
N,0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c,0.0
O,0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d,0.0
P,0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948,0.0
Q,0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9,0.0
R,0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10,0.0
S,0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386,0.0
T,0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588,0.0
U,0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956,0.0
V,0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3,0.0
W,0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0,0.0
X,0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d,0.0
Y,0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4,0.0
Z,0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c,0.0
alice,0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b,0.0
bob,0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d,0.0
```

### Multisig Contract Probes

All 5 multisig contracts probed via `0x1::multisig_account::num_signatures_required`.

```
pair,address,sigs_required,healthy
pair,address,sigs_required,healthy
A-B,0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003,2,true
A-G,0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096,2,true
Y-Z,0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883,2,true
S-T,0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883,2,true
V-W,0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d,2,true
```

**Result:** All 5 multisig pairs responded with **2 signatures required** — all HEALTHY ✓

### MNX Markets (testnet.mnx.fi)

Status: **SPA-only** — `testnet.mnx.fi` serves a Next.js SPA with no accessible
REST API at `/api/markets` or `/api/v1/markets`. Market data is loaded client-side
via JavaScript bundles. No structured market data extractable via HTTP. Recorded as unavailable.

---

## DuckDB Ducklake Summary

- **world_increments:** 2 sweep records (GF3 PLUS + MINUS)
- **repo_snapshots:** 1335 rows across all sources
- **aptos_snapshots:** 28 wallets snapshotted
- **multisig_probes:** 5 pairs probed
- **mnx_snapshots:** 0 (SPA unavailable)

Database: `packages/world-increment/ducklake/world-increments.duckdb`
