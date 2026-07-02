# World-Increment Sweep + Hamming Swarm Snapshot

**Timestamp:** 2026-07-02 16:14 UTC  
**DB:** `packages/world-increment/ducklake/world-increments.duckdb`

---

## JOB 1: GitHub Social Graph Sweep

### Coverage

| Source | Type | Repos Snapped |
|--------|------|--------------|
| `plurigrid` | org/user | 250 |
| `bmorphism` | org/user | 219 |
| `kubeflow` | org/user | 142 |
| `TeglonLabs` | org/user | 111 |
| `AustinCStone` | org/user | 88 |
| `migalkin` | org/user | 65 |
| `wasita` | org/user | 62 |
| `zubyul` | org/user | 58 |
| `kristinezheng` | org/user | 37 |
| `M1shaaa` | org/user | 33 |
| `DJedamski` | org/user | 23 |

**Total:** 1088 repo snapshots, 167 world increments

### GF(3) Color Chain

| Trit | Color | Name | Count |
|------|-------|------|-------|
| -1 | `#cc241d` | MINUS | 56 |
| 0 | `#d3869b` | ERGODIC | 55 |
| 1 | `#b8bb26` | PLUS | 56 |

### Top Repos by Stars

| Repo | Stars | Language | Description |
|------|-------|----------|-------------|
| `kubeflow/kubeflow` | 15757 | — | Machine Learning Toolkit for Kubernetes |
| `kubeflow/kubeflow` | 15572 | — | Machine Learning Toolkit for Kubernetes |
| `kubeflow/kubeflow` | 15565 | — | Machine Learning Toolkit for Kubernetes |
| `kubeflow/pipelines` | 4167 | Python | Machine Learning Pipelines for Kubeflow |
| `kubeflow/pipelines` | 4119 | Python | Machine Learning Pipelines for Kubeflow |
| `kubeflow/pipelines` | 4119 | Python | Machine Learning Pipelines for Kubeflow |
| `kubeflow/spark-operator` | 3130 | Python | Kubernetes operator for managing the lifecycle of Apache Spa |
| `kubeflow/spark-operator` | 3114 | Python | Kubernetes operator for managing the lifecycle of Apache Spa |
| `kubeflow/spark-operator` | 3111 | Python | Kubernetes operator for managing the lifecycle of Apache Spa |
| `kubeflow/trainer` | 2128 | Go | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| `kubeflow/trainer` | 2082 | Go | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| `kubeflow/trainer` | 2080 | Go | Distributed AI Model Training and LLM Fine-Tuning on Kuberne |
| `kubeflow/katib` | 1688 | Python | Automated Machine Learning on Kubernetes |
| `kubeflow/katib` | 1678 | Python | Automated Machine Learning on Kubernetes |
| `kubeflow/katib` | 1676 | Python | Automated Machine Learning on Kubernetes |

---

## JOB 2: Hamming Swarm Snapshot

### Aptos Wallet Balances (mainnet)

All 28 wallets queried. All returned `Resource not found` for CoinStore — consistent with unfunded or uninitialized accounts (0 APT).

| World | Address (prefix) | Balance APT |
|-------|-----------------|-------------|
| A | `0x8699edc0960dd5b916...` | 0.0000 |
| B | `0x3f892ebe6e45164e63...` | 0.0000 |
| C | `0x38b99e63ada9b6fef1...` | 0.0000 |
| D | `0xf77656248f64d5dd00...` | 0.0000 |
| E | `0xdc1d9d533bac3507f9...` | 0.0000 |
| F | `0x18a14b5b4bec118c1c...` | 0.0000 |
| G | `0x69a394c0b0ac842127...` | 0.0000 |
| H | `0xce67c327a7844e5488...` | 0.0000 |
| I | `0x070fe5d74e4eda30e2...` | 0.0000 |
| J | `0x4d964db8f538374034...` | 0.0000 |
| K | `0xa732040a6b0d559041...` | 0.0000 |
| L | `0x7c2eaeafad9725492e...` | 0.0000 |
| M | `0x6fed37a7553ef16b2a...` | 0.0000 |
| N | `0xe7dde6da0a65f51062...` | 0.0000 |
| O | `0x73252b6011a75115a2...` | 0.0000 |
| P | `0x6218792de4a9bc3891...` | 0.0000 |
| Q | `0xac40fa50b81b4ca6b1...` | 0.0000 |
| R | `0x7ce605cc8fda4f8e4a...` | 0.0000 |
| S | `0xb8753014e4888ea48a...` | 0.0000 |
| T | `0x35781dc0e42fef3f25...` | 0.0000 |
| U | `0x75860da47565f6509b...` | 0.0000 |
| V | `0xb59dd8170321dfab5a...` | 0.0000 |
| W | `0x5f32aef70f5ba530d3...` | 0.0000 |
| X | `0xa95cbbd116548ac990...` | 0.0000 |
| Y | `0xd8e32848f1dffa811b...` | 0.0000 |
| Z | `0x7af0ef6e1bd706f4b3...` | 0.0000 |
| alice | `0xc793acdec12b4a6371...` | 0.0000 |
| bob | `0x0a3c00c58fdf9020b2...` | 0.0000 |

> **Note:** `Resource not found` on `/v1/accounts/{addr}/resource/0x1::coin::CoinStore<0x1::aptos_coin::AptosCoin>` 
> indicates account has no CoinStore resource — typical for accounts with 0 APT balance or accounts not yet receiving APT.

### Multisig Contract Probes

| Pair | Address (prefix) | Sigs Required | Healthy |
|------|-----------------|--------------|---------|
| A-B | `0x0da4f428a0c007da0f...` | 2 | ✓ |
| A-G | `0xf56c4a1c0906214f3f...` | 2 | ✓ |
| S-T | `0x3b1c3ae905d44c3a49...` | 2 | ✓ |
| V-W | `0x40fad7b423a843650f...` | 2 | ✓ |
| Y-Z | `0xd3ffe1812b2df40622...` | 2 | ✓ |

**Result:** All 5 multisig contracts probed healthy — each requires 2-of-N signatures.

### MNX Markets (testnet.mnx.fi)

**Status:** Unavailable — endpoint returns HTTP 401 (authentication required). SPA with Vercel deployment; no public API data accessible without credentials.

---

## Summary

| Component | Status | Count |
|-----------|--------|-------|
| World increments (GF3 chain) | ✓ | 167 |
| Repo snapshots | ✓ | 1088 |
| Aptos wallets snapped | ✓ | 28 |
| Aptos wallets with APT balance | — | 0 (all unfunded) |
| Multisig contracts probed | ✓ healthy | 5/5 |
| MNX market data | ✗ | 401 auth required |
