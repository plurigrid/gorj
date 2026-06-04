#!/usr/bin/env python3
"""Insert GitHub repo snapshot data into DuckDB."""
import subprocess, sys, json, hashlib, datetime

DB = "/home/user/gorj/packages/world-increment/ducklake/world-increments.duckdb"

REPOS = [
  {"org_or_user": "plurigrid", "repo_name": "asi", "full_name": "plurigrid/asi", "language": "HTML", "stars": 17, "forks": 5, "open_issues": 4, "pushed_at": "2026-04-26T08:51:41Z", "description": "everything is topological chemputer!"},
  {"org_or_user": "plurigrid", "repo_name": "ontology", "full_name": "plurigrid/ontology", "language": "JavaScript", "stars": 7, "forks": 9, "open_issues": 16, "pushed_at": "2025-05-27T18:18:34Z", "description": "autopoietic ergodicity and embodied gradualism"},
  {"org_or_user": "plurigrid", "repo_name": "vcg-auction", "full_name": "plurigrid/vcg-auction", "language": "Rust", "stars": 7, "forks": 2, "open_issues": 1, "pushed_at": "2023-03-16T21:53:08Z", "description": "a simple contract that performs a VCG auction"},
  {"org_or_user": "plurigrid", "repo_name": "agent", "full_name": "plurigrid/agent", "language": "Python", "stars": 5, "forks": 1, "open_issues": 6, "pushed_at": "2023-03-31T18:45:23Z", "description": "Framework for agency amplification. A conversational agent for every DAO!"},
  {"org_or_user": "plurigrid", "repo_name": "StochFlow", "full_name": "plurigrid/StochFlow", "language": "Python", "stars": 4, "forks": 1, "open_issues": 0, "pushed_at": "2024-03-20T23:34:57Z", "description": "stochastic interpolant models"},
  {"org_or_user": "plurigrid", "repo_name": "asi-skills", "full_name": "plurigrid/asi-skills", "language": "Julia", "stars": 3, "forks": 1, "open_issues": 0, "pushed_at": "2026-04-26T08:09:26Z", "description": "69 skills with Galois Hole Type accessibility"},
  {"org_or_user": "plurigrid", "repo_name": "microworlds", "full_name": "plurigrid/microworlds", "language": "Rust", "stars": 3, "forks": 5, "open_issues": 3, "pushed_at": "2023-05-13T03:54:56Z", "description": None},
  {"org_or_user": "plurigrid", "repo_name": "act", "full_name": "plurigrid/act", "language": "Python", "stars": 3, "forks": 1, "open_issues": 4, "pushed_at": "2024-07-26T08:27:08Z", "description": "building blocks for cognitive category theory"},
  {"org_or_user": "plurigrid", "repo_name": "Plurigraph", "full_name": "plurigrid/Plurigraph", "language": "JavaScript", "stars": 2, "forks": 5, "open_issues": 4, "pushed_at": "2025-01-05T08:39:09Z", "description": "Plurigrid knowledge base"},
  {"org_or_user": "plurigrid", "repo_name": "org", "full_name": "plurigrid/org", "language": "Jupyter Notebook", "stars": 2, "forks": 0, "open_issues": 1, "pushed_at": "2023-11-07T01:08:05Z", "description": "Dynamically Replicating Duck"},
  {"org_or_user": "plurigrid", "repo_name": "zig-syrup", "full_name": "plurigrid/zig-syrup", "language": "Zig", "stars": 2, "forks": 2, "open_issues": 0, "pushed_at": "2026-04-30T03:52:16Z", "description": "High-performance Zig OCapN Syrup"},
  {"org_or_user": "plurigrid", "repo_name": "grid", "full_name": "plurigrid/grid", "language": "TypeScript", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2023-01-02T11:55:55Z", "description": "Plurigrid Testnet #0: Edith Clarke"},
  {"org_or_user": "plurigrid", "repo_name": "duck-kanban", "full_name": "plurigrid/duck-kanban", "language": "Rust", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-26T20:18:38Z", "description": "Duck intelligence kanban system"},
  {"org_or_user": "plurigrid", "repo_name": "nanoclj-zig", "full_name": "plurigrid/nanoclj-zig", "language": "Zig", "stars": 1, "forks": 1, "open_issues": 20, "pushed_at": "2026-04-25T07:29:09Z", "description": "NaN-boxed Clojure interpreter in Zig 0.15"},
  {"org_or_user": "plurigrid", "repo_name": "plurigrid.github.io", "full_name": "plurigrid/plurigrid.github.io", "language": "HTML", "stars": 1, "forks": 2, "open_issues": 2, "pushed_at": "2023-01-20T03:27:34Z", "description": None},
  {"org_or_user": "plurigrid", "repo_name": "nash-portal", "full_name": "plurigrid/nash-portal", "language": "Rust", "stars": 1, "forks": 2, "open_issues": 0, "pushed_at": "2026-04-26T08:50:56Z", "description": "NASH token TUI in the browser"},
  {"org_or_user": "plurigrid", "repo_name": "novella", "full_name": "plurigrid/novella", "language": "TypeScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2024-01-27T08:12:55Z", "description": None},
  {"org_or_user": "plurigrid", "repo_name": "vivarium", "full_name": "plurigrid/vivarium", "language": "Clojure", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:38:37Z", "description": None},
  {"org_or_user": "kubeflow", "repo_name": "kubeflow", "full_name": "kubeflow/kubeflow", "language": None, "stars": 15615, "forks": 2646, "open_issues": 0, "pushed_at": "2026-04-29T13:58:28Z", "description": "Machine Learning Toolkit for Kubernetes"},
  {"org_or_user": "kubeflow", "repo_name": "pipelines", "full_name": "kubeflow/pipelines", "language": "Python", "stars": 4130, "forks": 1986, "open_issues": 488, "pushed_at": "2026-05-01T19:55:52Z", "description": "Machine Learning Pipelines for Kubeflow"},
  {"org_or_user": "kubeflow", "repo_name": "spark-operator", "full_name": "kubeflow/spark-operator", "language": "Python", "stars": 3121, "forks": 1483, "open_issues": 90, "pushed_at": "2026-04-28T17:44:00Z", "description": "Kubernetes operator for Apache Spark"},
  {"org_or_user": "kubeflow", "repo_name": "trainer", "full_name": "kubeflow/trainer", "language": "Go", "stars": 2095, "forks": 948, "open_issues": 119, "pushed_at": "2026-05-01T16:41:03Z", "description": "Distributed AI Model Training on Kubernetes"},
  {"org_or_user": "kubeflow", "repo_name": "katib", "full_name": "kubeflow/katib", "language": "Python", "stars": 1681, "forks": 521, "open_issues": 121, "pushed_at": "2026-04-14T01:21:37Z", "description": "Automated Machine Learning on Kubernetes"},
  {"org_or_user": "kubeflow", "repo_name": "examples", "full_name": "kubeflow/examples", "language": "Jsonnet", "stars": 1460, "forks": 757, "open_issues": 111, "pushed_at": "2025-04-14T01:54:52Z", "description": "Extended examples and tutorials"},
  {"org_or_user": "kubeflow", "repo_name": "manifests", "full_name": "kubeflow/manifests", "language": "YAML", "stars": 1013, "forks": 1065, "open_issues": 29, "pushed_at": "2026-04-30T08:53:03Z", "description": "Kubeflow AI Reference Platform Manifests"},
  {"org_or_user": "kubeflow", "repo_name": "arena", "full_name": "kubeflow/arena", "language": "Go", "stars": 810, "forks": 191, "open_issues": 69, "pushed_at": "2026-04-28T11:45:01Z", "description": "A CLI for Kubeflow"},
  {"org_or_user": "kubeflow", "repo_name": "kale", "full_name": "kubeflow/kale", "language": "Python", "stars": 684, "forks": 156, "open_issues": 54, "pushed_at": "2026-04-30T18:03:46Z", "description": "Kubeflow superfood for Data Scientists"},
  {"org_or_user": "kubeflow", "repo_name": "mpi-operator", "full_name": "kubeflow/mpi-operator", "language": "Go", "stars": 524, "forks": 235, "open_issues": 100, "pushed_at": "2026-04-14T03:16:20Z", "description": "Kubernetes Operator for MPI-based applications"},
  {"org_or_user": "kubeflow", "repo_name": "fairing", "full_name": "kubeflow/fairing", "language": "Jsonnet", "stars": 337, "forks": 143, "open_issues": 134, "pushed_at": "2022-04-11T05:28:47Z", "description": "Python SDK for building, training, deploying ML models"},
  {"org_or_user": "kubeflow", "repo_name": "pytorch-operator", "full_name": "kubeflow/pytorch-operator", "language": "Jsonnet", "stars": 310, "forks": 143, "open_issues": 63, "pushed_at": "2021-12-01T17:44:48Z", "description": "PyTorch on Kubernetes"},
  {"org_or_user": "kubeflow", "repo_name": "community", "full_name": "kubeflow/community", "language": "Jsonnet", "stars": 196, "forks": 256, "open_issues": 13, "pushed_at": "2026-05-01T13:13:03Z", "description": "Kubeflow community information"},
  {"org_or_user": "kubeflow", "repo_name": "website", "full_name": "kubeflow/website", "language": "HTML", "stars": 184, "forks": 918, "open_issues": 50, "pushed_at": "2026-04-28T20:25:01Z", "description": "Kubeflow Website"},
  {"org_or_user": "kubeflow", "repo_name": "kfp-tekton", "full_name": "kubeflow/kfp-tekton", "language": "TypeScript", "stars": 182, "forks": 123, "open_issues": 79, "pushed_at": "2024-11-19T12:23:51Z", "description": "Kubeflow Pipelines on Tekton"},
  {"org_or_user": "kubeflow", "repo_name": "kfctl", "full_name": "kubeflow/kfctl", "language": "Go", "stars": 182, "forks": 134, "open_issues": 94, "pushed_at": "2023-08-15T20:19:22Z", "description": "CLI for deploying and managing Kubeflow"},
  {"org_or_user": "kubeflow", "repo_name": "hub", "full_name": "kubeflow/hub", "language": "Go", "stars": 174, "forks": 178, "open_issues": 45, "pushed_at": "2026-05-01T22:27:35Z", "description": "Model Registry for ML model developers"},
  {"org_or_user": "kubeflow", "repo_name": "example-seldon", "full_name": "kubeflow/example-seldon", "language": "Jupyter Notebook", "stars": 172, "forks": 56, "open_issues": 9, "pushed_at": "2021-12-01T01:49:58Z", "description": "End-to-end ML on Kubernetes using Kubeflow and Seldon Core"},
  {"org_or_user": "TeglonLabs", "repo_name": "mathpix-gem", "full_name": "TeglonLabs/mathpix-gem", "language": "Ruby", "stars": 2, "forks": 0, "open_issues": 11, "pushed_at": "2026-01-01T12:13:13Z", "description": "Transform math images to LaTeX via Mathpix"},
  {"org_or_user": "TeglonLabs", "repo_name": "topoi", "full_name": "TeglonLabs/topoi", "language": "Python", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2025-01-24T04:49:26Z", "description": None},
  {"org_or_user": "TeglonLabs", "repo_name": "monad-mcp-server", "full_name": "TeglonLabs/monad-mcp-server", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-14T11:36:14Z", "description": "Monad MCP Server"},
  {"org_or_user": "TeglonLabs", "repo_name": "coin-flip-mcp", "full_name": "TeglonLabs/coin-flip-mcp", "language": "JavaScript", "stars": 0, "forks": 2, "open_issues": 1, "pushed_at": "2025-09-21T08:57:27Z", "description": "MCP server for flipping coins"},
  {"org_or_user": "bmorphism", "repo_name": "ocaml-mcp-sdk", "full_name": "bmorphism/ocaml-mcp-sdk", "language": "OCaml", "stars": 60, "forks": 2, "open_issues": 0, "pushed_at": "2026-03-16T05:24:25Z", "description": "OCaml SDK for Model Context Protocol"},
  {"org_or_user": "bmorphism", "repo_name": "anti-bullshit-mcp-server", "full_name": "bmorphism/anti-bullshit-mcp-server", "language": "JavaScript", "stars": 23, "forks": 7, "open_issues": 1, "pushed_at": "2026-01-16T08:54:58Z", "description": "MCP server for analyzing claims and detecting manipulation"},
  {"org_or_user": "bmorphism", "repo_name": "risc0-cosmwasm-example", "full_name": "bmorphism/risc0-cosmwasm-example", "language": "Rust", "stars": 23, "forks": 2, "open_issues": 1, "pushed_at": "2022-10-20T23:50:40Z", "description": "CosmWasm + zkVM RISC-V EFI template"},
  {"org_or_user": "bmorphism", "repo_name": "say-mcp-server", "full_name": "bmorphism/say-mcp-server", "language": "JavaScript", "stars": 20, "forks": 9, "open_issues": 3, "pushed_at": "2025-01-07T03:15:18Z", "description": "MCP server for macOS text-to-speech"},
  {"org_or_user": "bmorphism", "repo_name": "babashka-mcp-server", "full_name": "bmorphism/babashka-mcp-server", "language": "JavaScript", "stars": 18, "forks": 6, "open_issues": 3, "pushed_at": "2025-01-05T11:09:42Z", "description": "MCP server for interacting with Babashka"},
  {"org_or_user": "bmorphism", "repo_name": "manifold-mcp-server", "full_name": "bmorphism/manifold-mcp-server", "language": "JavaScript", "stars": 14, "forks": 9, "open_issues": 5, "pushed_at": "2025-01-11T10:36:58Z", "description": "MCP server for Manifold Markets prediction markets"},
  {"org_or_user": "bmorphism", "repo_name": "penrose-mcp", "full_name": "bmorphism/penrose-mcp", "language": "JavaScript", "stars": 10, "forks": 4, "open_issues": 0, "pushed_at": "2025-01-20T21:44:55Z", "description": "Penrose server for Infinity-Topos environment"},
  {"org_or_user": "bmorphism", "repo_name": "marginalia-mcp-server", "full_name": "bmorphism/marginalia-mcp-server", "language": "JavaScript", "stars": 8, "forks": 6, "open_issues": 0, "pushed_at": "2025-01-06T05:47:24Z", "description": "MCP server for managing marginalia and annotations"},
  {"org_or_user": "bmorphism", "repo_name": "nats-mcp-server", "full_name": "bmorphism/nats-mcp-server", "language": None, "stars": 7, "forks": 3, "open_issues": 2, "pushed_at": "2025-01-06T23:33:41Z", "description": "MCP server for NATS messaging"},
  {"org_or_user": "bmorphism", "repo_name": "hypernym-mcp-server", "full_name": "bmorphism/hypernym-mcp-server", "language": "JavaScript", "stars": 6, "forks": 5, "open_issues": 0, "pushed_at": "2025-04-02T21:21:08Z", "description": None},
  {"org_or_user": "bmorphism", "repo_name": "penumbra-mcp", "full_name": "bmorphism/penumbra-mcp", "language": "JavaScript", "stars": 5, "forks": 6, "open_issues": 3, "pushed_at": "2025-01-07T01:15:23Z", "description": "MCP server for Penumbra blockchain"},
  {"org_or_user": "bmorphism", "repo_name": "shitcoin", "full_name": "bmorphism/shitcoin", "language": "Python", "stars": 5, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-08T08:07:08Z", "description": "gets denom for cw20 assets for IBC"},
  {"org_or_user": "bmorphism", "repo_name": "open-location-code-zig", "full_name": "bmorphism/open-location-code-zig", "language": "Zig", "stars": 3, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-30T19:33:45Z", "description": "Open Location Code for Zig"},
  {"org_or_user": "bmorphism", "repo_name": "slowtime-mcp-server", "full_name": "bmorphism/slowtime-mcp-server", "language": "TypeScript", "stars": 3, "forks": 5, "open_issues": 6, "pushed_at": "2025-01-02T01:23:33Z", "description": "MCP server for secure time-based operations"},
  {"org_or_user": "bmorphism", "repo_name": "graphistry-mcp", "full_name": "bmorphism/graphistry-mcp", "language": "Python", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2025-05-06T17:34:24Z", "description": "Graphistry MCP integration"},
  {"org_or_user": "bmorphism", "repo_name": "whale", "full_name": "bmorphism/whale", "language": "MATLAB", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-04T06:55:21Z", "description": "omniglot + sperm whale codas = metawhaling"},
  {"org_or_user": "zubyul", "repo_name": "WGCNA", "full_name": "zubyul/WGCNA", "language": "HTML", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-07-05T18:02:30Z", "description": "weighted gene correlation network analysis"},
  {"org_or_user": "zubyul", "repo_name": "jonikas_lab_data_analysis_misc", "full_name": "zubyul/jonikas_lab_data_analysis_misc", "language": "Jupyter Notebook", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-08-16T20:24:40Z", "description": "scripts for large genetic sequence data"},
  {"org_or_user": "zubyul", "repo_name": "Nikolova_lab_data_analysis", "full_name": "zubyul/Nikolova_lab_data_analysis", "language": "R", "stars": 2, "forks": 0, "open_issues": 0, "pushed_at": "2023-06-16T13:56:58Z", "description": "undergraduate thesis - cortical thickness and depression"},
  {"org_or_user": "zubyul", "repo_name": "gay-world", "full_name": "zubyul/gay-world", "language": "Python", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2026-03-26T04:03:39Z", "description": "Goblin world builder with MLX task decomposition"},
  {"org_or_user": "zubyul", "repo_name": "cascade-world", "full_name": "zubyul/cascade-world", "language": "Python", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-19T18:25:12Z", "description": "Cascade development environment"},
  {"org_or_user": "zubyul", "repo_name": "ghostty-modifications", "full_name": "zubyul/ghostty-modifications", "language": "JavaScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-15T02:45:21Z", "description": "Ghostty terminal modifications and MCP servers"},
  {"org_or_user": "zubyul", "repo_name": "zubyul.github.io", "full_name": "zubyul/zubyul.github.io", "language": "CSS", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2026-01-27T03:24:34Z", "description": None},
  {"org_or_user": "zubyul", "repo_name": "defcon", "full_name": "zubyul/defcon", "language": "JavaScript", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-09-17T02:07:00Z", "description": None},
  {"org_or_user": "zubyul", "repo_name": "GoofyLifeChoices", "full_name": "zubyul/GoofyLifeChoices", "language": "Python", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2025-07-30T18:48:13Z", "description": None},
  {"org_or_user": "zubyul", "repo_name": "repl", "full_name": "zubyul/repl", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-02-04T01:08:15Z", "description": None},
  {"org_or_user": "zubyul", "repo_name": "quantum-telephone", "full_name": "zubyul/quantum-telephone", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-08T22:54:16Z", "description": "Quantum telephone world: entangled message passing"},
  {"org_or_user": "migalkin", "repo_name": "NodePiece", "full_name": "migalkin/NodePiece", "language": "Python", "stars": 143, "forks": 21, "open_issues": 0, "pushed_at": "2022-02-02T03:34:04Z", "description": "Compositional representations for Large Knowledge Graphs (ICLR 2022)"},
  {"org_or_user": "migalkin", "repo_name": "StarE", "full_name": "migalkin/StarE", "language": "Python", "stars": 89, "forks": 16, "open_issues": 1, "pushed_at": "2023-12-01T20:12:24Z", "description": "Message Passing for Hyper-Relational Knowledge Graphs (EMNLP 2020)"},
  {"org_or_user": "migalkin", "repo_name": "kgcourse2021", "full_name": "migalkin/kgcourse2021", "language": "HTML", "stars": 25, "forks": 9, "open_issues": 0, "pushed_at": "2025-08-04T03:01:46Z", "description": "Knowledge Graphs course materials"},
  {"org_or_user": "migalkin", "repo_name": "NBFNet_mlx", "full_name": "migalkin/NBFNet_mlx", "language": "Python", "stars": 10, "forks": 1, "open_issues": 1, "pushed_at": "2024-03-02T00:15:23Z", "description": "Neural Bellman-Ford networks in MLX"},
  {"org_or_user": "migalkin", "repo_name": "RWL", "full_name": "migalkin/RWL", "language": "Python", "stars": 7, "forks": 1, "open_issues": 0, "pushed_at": "2022-12-01T15:58:59Z", "description": "Weisfeiler and Leman Go Relational (LOG 2022)"},
  {"org_or_user": "migalkin", "repo_name": "rambo", "full_name": "migalkin/rambo", "language": "Rust", "stars": 3, "forks": 0, "open_issues": 1, "pushed_at": "2023-02-08T14:27:03Z", "description": None},
  {"org_or_user": "DJedamski", "repo_name": "Getting-and-Cleaning-Data", "full_name": "DJedamski/Getting-and-Cleaning-Data", "language": "R", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2014-10-26T20:53:14Z", "description": "Coursera Project"},
  {"org_or_user": "DJedamski", "repo_name": "Kaggle", "full_name": "DJedamski/Kaggle", "language": None, "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2014-11-03T02:22:01Z", "description": None},
  {"org_or_user": "DJedamski", "repo_name": "School", "full_name": "DJedamski/School", "language": "R", "stars": 1, "forks": 1, "open_issues": 0, "pushed_at": "2014-10-09T02:55:13Z", "description": "Projects from grad school"},
  {"org_or_user": "DJedamski", "repo_name": "kaggle_ncaa18", "full_name": "DJedamski/kaggle_ncaa18", "language": "Jupyter Notebook", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2018-03-07T12:36:09Z", "description": "NCAA March Madness competition 2018"},
  {"org_or_user": "wasita", "repo_name": "magic-garden", "full_name": "wasita/magic-garden", "language": "Python", "stars": 2, "forks": 1, "open_issues": 1, "pushed_at": "2026-01-13T23:51:32Z", "description": "magic garden discord bot"},
  {"org_or_user": "wasita", "repo_name": "wasita.github.io", "full_name": "wasita/wasita.github.io", "language": "Svelte", "stars": 1, "forks": 0, "open_issues": 8, "pushed_at": "2026-04-28T05:28:20Z", "description": "personal website"},
  {"org_or_user": "wasita", "repo_name": "wins-search", "full_name": "wasita/wins-search", "language": "CSS", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2022-12-14T22:17:32Z", "description": "Women in Network Science member list website"},
  {"org_or_user": "wasita", "repo_name": "ch3-lib", "full_name": "wasita/ch3-lib", "language": "Typst", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-12T04:03:19Z", "description": None},
  {"org_or_user": "wasita", "repo_name": "wm-cv", "full_name": "wasita/wm-cv", "language": "Svelte", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-12T02:53:47Z", "description": "Academic CV as single page web app"},
  {"org_or_user": "wasita", "repo_name": "send2kobo", "full_name": "wasita/send2kobo", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-12-12T19:09:12Z", "description": "Website for sending books to Kobo e-reader"},
  {"org_or_user": "kristinezheng", "repo_name": "Portfolio", "full_name": "kristinezheng/Portfolio", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2025-02-12T00:00:42Z", "description": "Portfolio"},
  {"org_or_user": "kristinezheng", "repo_name": "Green-Machine", "full_name": "kristinezheng/Green-Machine", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2021-09-19T05:33:01Z", "description": "HackMIT 2021 Sustainability Track"},
  {"org_or_user": "kristinezheng", "repo_name": "kristinezheng.github.io", "full_name": "kristinezheng/kristinezheng.github.io", "language": "HTML", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-04-09T17:09:42Z", "description": None},
  {"org_or_user": "M1shaaa", "repo_name": "lab-bookshelf-", "full_name": "M1shaaa/lab-bookshelf-", "language": "TypeScript", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-12-31T05:11:14Z", "description": None},
  {"org_or_user": "M1shaaa", "repo_name": "Python-Lookit-Uploads", "full_name": "M1shaaa/Python-Lookit-Uploads", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2024-02-16T15:20:50Z", "description": "random projects"},
  {"org_or_user": "M1shaaa", "repo_name": "M1shaaa", "full_name": "M1shaaa/M1shaaa", "language": None, "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2026-05-02T02:27:57Z", "description": "GitHub profile config"},
  {"org_or_user": "AustinCStone", "repo_name": "TextGAN", "full_name": "AustinCStone/TextGAN", "language": "Python", "stars": 92, "forks": 30, "open_issues": 5, "pushed_at": "2016-10-04T03:19:12Z", "description": "Generative adversarial network for text generation in TensorFlow"},
  {"org_or_user": "AustinCStone", "repo_name": "StereoVisionMRF", "full_name": "AustinCStone/StereoVisionMRF", "language": "Python", "stars": 11, "forks": 4, "open_issues": 0, "pushed_at": "2016-01-10T08:34:29Z", "description": "MRF with loopy belief propagation for stereo depth"},
  {"org_or_user": "AustinCStone", "repo_name": "SpectralClustering", "full_name": "AustinCStone/SpectralClustering", "language": "Python", "stars": 3, "forks": 2, "open_issues": 0, "pushed_at": "2015-11-09T03:27:15Z", "description": "Spectral clustering implementation"},
  {"org_or_user": "AustinCStone", "repo_name": "StructureFromMotion", "full_name": "AustinCStone/StructureFromMotion", "language": "Python", "stars": 1, "forks": 0, "open_issues": 0, "pushed_at": "2018-06-10T18:56:16Z", "description": "Recover 3D geometry from videos"},
  {"org_or_user": "AustinCStone", "repo_name": "TFBirds", "full_name": "AustinCStone/TFBirds", "language": "Python", "stars": 0, "forks": 0, "open_issues": 0, "pushed_at": "2019-01-30T08:07:21Z", "description": "Bird flocking simulator in TensorFlow"},
  {"org_or_user": "AustinCStone", "repo_name": "bmfork", "full_name": "AustinCStone/bmfork", "language": "Python", "stars": 0, "forks": 0, "open_issues": 1, "pushed_at": "2025-05-09T04:17:17Z", "description": None},
]

def run_sql(sql):
    r = subprocess.run(["duckdb", "--csv", DB], input=sql, capture_output=True, text=True)
    if r.returncode != 0:
        print("SQL ERROR:", r.stderr[:500], file=sys.stderr)
    return r.stdout.strip()

def esc(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# Get current max repo id
cur_max = run_sql("SELECT COALESCE(MAX(id), 0) as m FROM repo_snapshots;")
next_id = int(cur_max.strip().split('\n')[-1]) + 1

# Get current increment id
inc_max = run_sql("SELECT COALESCE(MAX(id), 0) as m FROM world_increments;")
inc_id = int(inc_max.strip().split('\n')[-1])

print(f"Inserting {len(REPOS)} repos starting at id={next_id}, increment_id={inc_id}")

inserted = 0
for i, r in enumerate(REPOS):
    rid = next_id + i
    lang = esc(r.get("language"))
    desc = esc(r.get("description"))
    sql = (
        f"INSERT INTO repo_snapshots "
        f"(id, increment_id, org_or_user, repo_name, full_name, language, stars, forks, open_issues, pushed_at, description) "
        f"VALUES ({rid}, {inc_id}, {esc(r['org_or_user'])}, {esc(r['repo_name'])}, {esc(r['full_name'])}, "
        f"{lang}, {r['stars']}, {r['forks']}, {r['open_issues']}, {esc(r['pushed_at'])}, {desc});"
    )
    run_sql(sql)
    inserted += 1

print(f"Inserted {inserted} repo_snapshots")

# Verify
count = run_sql("SELECT COUNT(*) as c FROM repo_snapshots;")
print(f"Total repo_snapshots now: {count.split(chr(10))[-1]}")
inc_count = run_sql("SELECT COUNT(*) as c FROM world_increments;")
print(f"Total world_increments now: {inc_count.split(chr(10))[-1]}")
