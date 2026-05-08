-- World Increment DuckLake: Schema + Data Population
-- GF(3) chain: id%3=0 → trit=0 ERGODIC #d3869b, id%3=1 → trit=1 PLUS #b8bb26, id%3=2 → trit=-1 MINUS #cc241d

CREATE TABLE IF NOT EXISTS world_increments (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  gf3_trit INTEGER,
  gf3_color VARCHAR,
  gf3_name VARCHAR,
  source_type VARCHAR,
  source_name VARCHAR,
  event_type VARCHAR,
  repo_name VARCHAR,
  actor VARCHAR,
  snapshot_hash VARCHAR
);

CREATE TABLE IF NOT EXISTS repo_snapshots (
  id INTEGER,
  timestamp TIMESTAMP DEFAULT now(),
  increment_id INTEGER,
  org_or_user VARCHAR,
  repo_name VARCHAR,
  full_name VARCHAR,
  language VARCHAR,
  stars INTEGER,
  forks INTEGER,
  open_issues INTEGER,
  pushed_at VARCHAR,
  description VARCHAR
);

CREATE TABLE IF NOT EXISTS aptos_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  world VARCHAR,
  address VARCHAR,
  balance_apt DOUBLE
);

CREATE TABLE IF NOT EXISTS multisig_probes (
  timestamp TIMESTAMP DEFAULT now(),
  pair VARCHAR,
  address VARCHAR,
  sigs_required INTEGER,
  healthy BOOLEAN
);

CREATE TABLE IF NOT EXISTS mnx_snapshots (
  timestamp TIMESTAMP DEFAULT now(),
  ticker VARCHAR,
  name VARCHAR,
  category VARCHAR,
  price DOUBLE,
  change_pct DOUBLE
);

CREATE SEQUENCE IF NOT EXISTS increment_seq START 1;
CREATE SEQUENCE IF NOT EXISTS repo_seq START 1;

-- World Increments (one per source sweep)
INSERT INTO world_increments VALUES
(1, now(), 1, '#b8bb26', 'PLUS', 'org', 'plurigrid', 'repo_sweep', NULL, 'sweep-agent', md5('plurigrid-2026-05-08')),
(2, now(), -1, '#cc241d', 'MINUS', 'org', 'kubeflow', 'repo_sweep', NULL, 'sweep-agent', md5('kubeflow-2026-05-08')),
(3, now(), 0, '#d3869b', 'ERGODIC', 'org', 'TeglonLabs', 'repo_sweep', NULL, 'sweep-agent', md5('TeglonLabs-2026-05-08')),
(4, now(), 1, '#b8bb26', 'PLUS', 'user', 'bmorphism', 'repo_sweep', NULL, 'sweep-agent', md5('bmorphism-2026-05-08')),
(5, now(), -1, '#cc241d', 'MINUS', 'user', 'zubyul', 'repo_sweep', NULL, 'sweep-agent', md5('zubyul-2026-05-08')),
(6, now(), 0, '#d3869b', 'ERGODIC', 'user', 'migalkin', 'repo_sweep', NULL, 'sweep-agent', md5('migalkin-2026-05-08')),
(7, now(), 1, '#b8bb26', 'PLUS', 'user', 'DJedamski', 'repo_sweep', NULL, 'sweep-agent', md5('DJedamski-2026-05-08')),
(8, now(), -1, '#cc241d', 'MINUS', 'user', 'wasita', 'repo_sweep', NULL, 'sweep-agent', md5('wasita-2026-05-08')),
(9, now(), 0, '#d3869b', 'ERGODIC', 'user', 'kristinezheng', 'repo_sweep', NULL, 'sweep-agent', md5('kristinezheng-2026-05-08')),
(10, now(), 1, '#b8bb26', 'PLUS', 'user', 'M1shaaa', 'repo_sweep', NULL, 'sweep-agent', md5('M1shaaa-2026-05-08')),
(11, now(), -1, '#cc241d', 'MINUS', 'user', 'AustinCStone', 'repo_sweep', NULL, 'sweep-agent', md5('AustinCStone-2026-05-08')),
(12, now(), 0, '#d3869b', 'ERGODIC', 'chain', 'aptos-mainnet', 'wallet_sweep', NULL, 'sweep-agent', md5('aptos-hamming-2026-05-08')),
(13, now(), 1, '#b8bb26', 'PLUS', 'chain', 'aptos-mainnet', 'multisig_probe', NULL, 'sweep-agent', md5('aptos-multisig-2026-05-08'));

-- REPO SNAPSHOTS: plurigrid
INSERT INTO repo_snapshots VALUES
(1, now(), 1, 'plurigrid', 'gorj', 'plurigrid/gorj', 'Clojure', 0, 0, 115, '2026-05-08T18:12:14Z', 'forj + Rama topology nREPL routing + GF(3) gay trit coloring for compositional open game REPL orchestration'),
(2, now(), 1, 'plurigrid', 'zig-syrup', 'plurigrid/zig-syrup', 'Zig', 2, 2, 0, '2026-04-30T03:52:16Z', 'High-performance Zig implementation of OCapN Syrup with CapTP optimizations'),
(3, now(), 1, 'plurigrid', 'asi', 'plurigrid/asi', 'HTML', 21, 5, 4, '2026-04-26T08:51:41Z', 'everything is topological chemputer!'),
(4, now(), 1, 'plurigrid', 'nash-portal', 'plurigrid/nash-portal', 'Rust', 2, 2, 0, '2026-04-26T08:50:56Z', 'NASH token TUI in the browser'),
(5, now(), 1, 'plurigrid', 'horse', 'plurigrid/horse', 'TeX', 1, 1, 9, '2026-05-07T04:35:12Z', ''),
(6, now(), 1, 'plurigrid', 'asi-skills', 'plurigrid/asi-skills', 'Julia', 3, 1, 0, '2026-04-26T08:09:26Z', '69 skills with Galois Hole Type accessibility'),
(7, now(), 1, 'plurigrid', 'bci-blue-share', 'plurigrid/bci-blue-share', 'JavaScript', 0, 0, 0, '2026-04-26T07:08:03Z', 'BCI signal infrastructure'),
(8, now(), 1, 'plurigrid', 'nanoclj-zig', 'plurigrid/nanoclj-zig', 'Zig', 1, 2, 20, '2026-04-25T07:29:09Z', 'NaN-boxed Clojure interpreter in Zig 0.15'),
(9, now(), 1, 'plurigrid', 'spi-race', 'plurigrid/spi-race', 'Swift', 0, 0, 0, '2026-04-21T19:31:56Z', 'Splitmix Parallel Integrity'),
(10, now(), 1, 'plurigrid', 'reafference', 'plurigrid/reafference', 'HTML', 0, 0, 0, '2026-04-16T05:21:49Z', 'Reafference adaptation workspace'),
(11, now(), 1, 'plurigrid', 'web-browser', 'plurigrid/web-browser', 'Rust', 0, 0, 0, '2026-04-10T02:54:47Z', 'web-browser from prepostweb lineage'),
(12, now(), 1, 'plurigrid', 'vivarium', 'plurigrid/vivarium', 'Clojure', 1, 0, 0, '2026-04-08T08:38:37Z', ''),
(13, now(), 1, 'plurigrid', 'flowglad-rs', 'plurigrid/flowglad-rs', 'Rust', 0, 0, 0, '2026-04-08T07:56:15Z', ''),
(14, now(), 1, 'plurigrid', 'forester', 'plurigrid/forester', 'XSLT', 0, 0, 0, '2026-03-30T01:32:26Z', 'CatColab mathematical documentation forest'),
(15, now(), 1, 'plurigrid', 'gatomic', 'plurigrid/gatomic', 'Clojure', 0, 0, 0, '2026-03-30T00:54:48Z', 'Deterministic color identity store'),
(16, now(), 1, 'plurigrid', 'nblm-flashcards', 'plurigrid/nblm-flashcards', 'Hy', 0, 0, 0, '2026-03-26T08:23:01Z', 'NotebookLM Enterprise flashcard pipeline'),
(17, now(), 1, 'plurigrid', 'graded-optic', 'plurigrid/graded-optic', 'Haskell', 0, 0, 0, '2026-02-08T16:10:16Z', 'Semiring-graded bidirectional processes'),
(18, now(), 1, 'plurigrid', 'lazygay', 'plurigrid/lazygay', 'Go', 0, 0, 0, '2026-01-08T14:19:25Z', 'lazygit fork with Gay.jl deterministic commit coloring'),
(19, now(), 1, 'plurigrid', 'gay-rs', 'plurigrid/gay-rs', 'Rust', 0, 0, 0, '2026-01-08T14:19:22Z', 'Rust crate for Gay.jl deterministic coloring'),
(20, now(), 1, 'plurigrid', 'ontology', 'plurigrid/ontology', 'JavaScript', 7, 9, 16, '2025-05-27T18:18:34Z', 'autopoietic ergodicity and embodied gradualism'),
(21, now(), 1, 'plurigrid', 'Plurigraph', 'plurigrid/Plurigraph', 'JavaScript', 2, 5, 4, '2025-01-05T08:39:09Z', 'Plurigrid knowledge base for Obsidian.md'),
(22, now(), 1, 'plurigrid', 'act', 'plurigrid/act', 'Python', 3, 1, 4, '2024-07-26T08:27:08Z', 'building blocks for cognitive category theory');

-- kubeflow repos
INSERT INTO repo_snapshots VALUES
(100, now(), 2, 'kubeflow', 'kubeflow', 'kubeflow/kubeflow', '', 15626, 2647, 2, '2026-05-07T13:46:41Z', 'Machine Learning Toolkit for Kubernetes'),
(101, now(), 2, 'kubeflow', 'pipelines', 'kubeflow/pipelines', 'Python', 4136, 1989, 492, '2026-05-08T16:29:12Z', 'Machine Learning Pipelines for Kubeflow'),
(102, now(), 2, 'kubeflow', 'spark-operator', 'kubeflow/spark-operator', 'Python', 3124, 1480, 88, '2026-05-08T16:09:29Z', 'Kubernetes operator for Apache Spark'),
(103, now(), 2, 'kubeflow', 'trainer', 'kubeflow/trainer', 'Go', 2096, 948, 116, '2026-05-08T12:38:29Z', 'Distributed AI Model Training on Kubernetes'),
(104, now(), 2, 'kubeflow', 'arena', 'kubeflow/arena', 'Go', 810, 190, 63, '2026-05-07T06:46:17Z', 'A CLI for Kubeflow'),
(105, now(), 2, 'kubeflow', 'kale', 'kubeflow/kale', 'Python', 684, 156, 55, '2026-05-08T11:18:29Z', 'Kubeflow superfood for Data Scientists'),
(106, now(), 2, 'kubeflow', 'mpi-operator', 'kubeflow/mpi-operator', 'Go', 524, 235, 100, '2026-05-05T05:00:55Z', 'Kubernetes Operator for MPI-based applications'),
(107, now(), 2, 'kubeflow', 'manifests', 'kubeflow/manifests', 'YAML', 1015, 1063, 27, '2026-05-08T18:34:32Z', 'Kubeflow AI Reference Platform Deployment Manifests'),
(108, now(), 2, 'kubeflow', 'hub', 'kubeflow/hub', 'Go', 175, 178, 39, '2026-05-08T13:06:29Z', 'Model Registry for ML model developers'),
(109, now(), 2, 'kubeflow', 'mcp-apache-spark-history-server', 'kubeflow/mcp-apache-spark-history-server', 'Python', 166, 57, 26, '2026-05-08T12:03:24Z', 'MCP Server for Apache Spark History Server'),
(110, now(), 2, 'kubeflow', 'community', 'kubeflow/community', 'Jsonnet', 196, 257, 13, '2026-05-08T18:59:29Z', 'Kubeflow community info'),
(111, now(), 2, 'kubeflow', 'notebooks', 'kubeflow/notebooks', '', 71, 106, 191, '2026-05-08T18:35:29Z', 'Kubeflow Notebooks interactive environments'),
(112, now(), 2, 'kubeflow', 'sdk', 'kubeflow/sdk', 'Python', 113, 174, 129, '2026-05-07T16:14:48Z', 'Universal Python SDK for AI workloads on Kubernetes'),
(113, now(), 2, 'kubeflow', 'website', 'kubeflow/website', 'HTML', 184, 919, 50, '2026-05-08T17:31:51Z', 'Kubeflow Website'),
(114, now(), 2, 'kubeflow', 'dashboard', 'kubeflow/dashboard', 'TypeScript', 17, 55, 74, '2026-05-06T23:37:51Z', 'Kubeflow Central Dashboard');

-- TeglonLabs repos
INSERT INTO repo_snapshots VALUES
(200, now(), 3, 'TeglonLabs', 'mathpix-gem', 'TeglonLabs/mathpix-gem', 'Ruby', 2, 0, 11, '2026-01-01T12:13:13Z', 'Transform mathematical images to LaTeX'),
(201, now(), 3, 'TeglonLabs', 'monad-mcp-server', 'TeglonLabs/monad-mcp-server', '', 0, 0, 0, '2025-05-14T11:36:14Z', 'Monad MCP Server'),
(202, now(), 3, 'TeglonLabs', 'topoi', 'TeglonLabs/topoi', 'Python', 0, 0, 1, '2025-01-24T04:49:26Z', ''),
(203, now(), 3, 'TeglonLabs', 'coin-flip-mcp', 'TeglonLabs/coin-flip-mcp', 'JavaScript', 0, 2, 1, '2025-09-21T08:57:27Z', 'MCP server for flipping coins with varying randomness');

-- bmorphism repos
INSERT INTO repo_snapshots VALUES
(300, now(), 4, 'bmorphism', 'Gay.jl', 'bmorphism/Gay.jl', 'Julia', 1, 0, 187, '2026-05-08T00:32:04Z', 'Wide-gamut color sampling with splittable determinism'),
(301, now(), 4, 'bmorphism', 'nanoclj-zig', 'bmorphism/nanoclj-zig', 'Zig', 0, 0, 0, '2026-05-07T20:12:15Z', ''),
(302, now(), 4, 'bmorphism', 'zig-syrup', 'bmorphism/zig-syrup', 'Zig', 0, 0, 0, '2026-05-07T19:49:05Z', 'Embeddable OCapN Syrup encoder/decoder in Zig'),
(303, now(), 4, 'bmorphism', 'boxxy', 'bmorphism/boxxy', 'Move', 0, 1, 0, '2026-04-30T03:35:47Z', ''),
(304, now(), 4, 'bmorphism', 'postweb', 'bmorphism/postweb', 'Go', 0, 0, 0, '2026-04-09T10:51:57Z', 'postweb evolved from prepostweb'),
(305, now(), 4, 'bmorphism', 'shitcoin', 'bmorphism/shitcoin', 'Python', 5, 0, 0, '2026-04-08T08:07:08Z', 'cw20 denom lookup for permissionless degeneracy in IBC'),
(306, now(), 4, 'bmorphism', 'magic-world-org', 'bmorphism/magic-world-org', 'Python', 1, 0, 0, '2026-04-05T07:03:50Z', 'Magic World Org Local MLX'),
(307, now(), 4, 'bmorphism', 'ocaml-mcp-sdk', 'bmorphism/ocaml-mcp-sdk', 'OCaml', 61, 2, 0, '2026-03-16T05:24:25Z', 'OCaml SDK for Model Context Protocol'),
(308, now(), 4, 'bmorphism', 'anti-bullshit-mcp-server', 'bmorphism/anti-bullshit-mcp-server', 'JavaScript', 23, 7, 1, '2026-01-16T08:54:58Z', 'MCP server for analyzing claims and detecting manipulation'),
(309, now(), 4, 'bmorphism', 'open-location-code-zig', 'bmorphism/open-location-code-zig', 'Zig', 3, 0, 0, '2025-12-30T19:33:45Z', 'Open Location Code for Zig'),
(310, now(), 4, 'bmorphism', 'monero-rental-hash-war', 'bmorphism/monero-rental-hash-war', 'Haskell', 1, 0, 0, '2025-10-05T23:08:54Z', 'Compositional OpenGame analysis of Monero rental hash war');

-- zubyul repos
INSERT INTO repo_snapshots VALUES
(400, now(), 5, 'zubyul', 'voice-observatory', 'zubyul/voice-observatory', 'Python', 0, 0, 0, '2026-04-24T05:56:17Z', 'Passive macOS TUI observing voice-download pathways'),
(401, now(), 5, 'zubyul', 'ghostel-emacs-worlds', 'zubyul/ghostel-emacs-worlds', 'GLSL', 0, 0, 0, '2026-04-24T00:20:56Z', 'Ghostty config + ghostel family'),
(402, now(), 5, 'zubyul', 'nash-tui', 'zubyul/nash-tui', 'Rust', 0, 0, 0, '2026-04-13T07:45:16Z', 'NASH token TUI via GeckoTerminal OHLCV'),
(403, now(), 5, 'zubyul', 'nash-web', 'zubyul/nash-web', 'Rust', 0, 0, 0, '2026-04-13T07:08:58Z', 'NASH token browser TUI via ratzilla WASM'),
(404, now(), 5, 'zubyul', 'big-bad-plurigrid-quiz', 'zubyul/big-bad-plurigrid-quiz', 'Emacs Lisp', 0, 0, 0, '2026-04-09T18:51:31Z', '27 flashcards from bmorphism/plurigrid/zubyul activity'),
(405, now(), 5, 'zubyul', 'Gay.jl', 'zubyul/Gay.jl', 'Julia', 0, 0, 0, '2026-03-28T11:30:01Z', 'Wide-gamut color sampling with splittable determinism'),
(406, now(), 5, 'zubyul', 'kinesis-kb360pro', 'zubyul/kinesis-kb360pro', 'Python', 0, 0, 0, '2026-03-26T10:29:40Z', 'Claude Code skill for Kinesis Advantage360 Pro'),
(407, now(), 5, 'zubyul', 'gay-world', 'zubyul/gay-world', 'Python', 1, 1, 0, '2026-03-26T04:03:39Z', 'Goblin world builder'),
(408, now(), 5, 'zubyul', 'tilelang-kernels', 'zubyul/tilelang-kernels', 'Python', 0, 0, 0, '2026-03-16T02:31:13Z', 'TileLang GPU kernels for SplitMix64 color generation'),
(409, now(), 5, 'zubyul', 'plurigrid-site', 'zubyul/plurigrid-site', 'Svelte', 0, 1, 11, '2026-02-04T03:20:08Z', 'Plurigrid world site deployment');

-- migalkin repos
INSERT INTO repo_snapshots VALUES
(500, now(), 6, 'migalkin', 'NodePiece', 'migalkin/NodePiece', 'Python', 144, 21, 0, '2022-02-02T03:34:04Z', 'Compositional KG Representations ICLR22'),
(501, now(), 6, 'migalkin', 'StarE', 'migalkin/StarE', 'Python', 89, 16, 1, '2023-12-01T20:12:24Z', 'EMNLP 2020: Message Passing for Hyper-Relational KGs'),
(502, now(), 6, 'migalkin', 'kgcourse2021', 'migalkin/kgcourse2021', 'HTML', 25, 9, 0, '2025-08-04T03:01:46Z', 'Materials for Knowledge Graphs course'),
(503, now(), 6, 'migalkin', 'RWL', 'migalkin/RWL', 'Python', 7, 1, 0, '2022-12-01T15:58:59Z', 'Weisfeiler and Leman Go Relational LOG 2022'),
(504, now(), 6, 'migalkin', 'NBFNet_mlx', 'migalkin/NBFNet_mlx', 'Python', 10, 1, 1, '2024-03-02T00:15:23Z', 'Neural Bellman-Ford networks in MLX for Apple Silicon'),
(505, now(), 6, 'migalkin', 'rambo', 'migalkin/rambo', 'Rust', 3, 0, 1, '2023-02-08T14:27:03Z', '');

-- DJedamski repos
INSERT INTO repo_snapshots VALUES
(600, now(), 7, 'DJedamski', 'kaggle_ncaa18', 'DJedamski/kaggle_ncaa18', 'Jupyter Notebook', 0, 0, 0, '2018-03-07T12:36:09Z', 'Code for NCAA March Madness 2018'),
(601, now(), 7, 'DJedamski', 'Project_Euler', 'DJedamski/Project_Euler', '', 0, 0, 0, '2015-10-14T02:10:45Z', ''),
(602, now(), 7, 'DJedamski', 'EDA', 'DJedamski/EDA', 'R', 0, 0, 0, '2014-11-09T16:51:34Z', 'Coursera Project'),
(603, now(), 7, 'DJedamski', 'Kaggle', 'DJedamski/Kaggle', '', 1, 0, 0, '2014-11-03T02:22:01Z', ''),
(604, now(), 7, 'DJedamski', 'Getting-and-Cleaning-Data', 'DJedamski/Getting-and-Cleaning-Data', 'R', 1, 0, 0, '2014-10-26T20:53:14Z', 'Coursera Project'),
(605, now(), 7, 'DJedamski', 'School', 'DJedamski/School', 'R', 1, 1, 0, '2014-10-09T02:55:13Z', 'Grad school projects');

-- wasita repos
INSERT INTO repo_snapshots VALUES
(700, now(), 8, 'wasita', 'vocoder', 'wasita/vocoder', 'JavaScript', 0, 0, 0, '2026-05-06T05:14:00Z', '');

-- kristinezheng repos
INSERT INTO repo_snapshots VALUES
(800, now(), 9, 'kristinezheng', 'kristinezheng.github.io', 'kristinezheng/kristinezheng.github.io', 'HTML', 0, 0, 0, '2026-04-09T17:09:42Z', ''),
(801, now(), 9, 'kristinezheng', 'Portfolio', 'kristinezheng/Portfolio', 'JavaScript', 0, 0, 0, '2025-02-12T00:00:42Z', 'July 2021'),
(802, now(), 9, 'kristinezheng', 'lookit-jenga', 'kristinezheng/lookit-jenga', 'Jupyter Notebook', 0, 0, 0, '2024-05-16T18:29:01Z', 'Lookit study for 9.85'),
(803, now(), 9, 'kristinezheng', 'auditory-illusion', 'kristinezheng/auditory-illusion', 'CSS', 0, 0, 0, '2022-03-11T19:22:33Z', '9.35 spring 2022 auditory illusion'),
(804, now(), 9, 'kristinezheng', 'graph_example', 'kristinezheng/graph_example', 'Python', 0, 0, 0, '2021-10-08T07:29:51Z', ''),
(805, now(), 9, 'kristinezheng', 'Green-Machine', 'kristinezheng/Green-Machine', 'Python', 0, 0, 0, '2021-09-19T05:33:01Z', 'HackMIT 2021 Sustainability Track');

-- M1shaaa repos
INSERT INTO repo_snapshots VALUES
(900, now(), 10, 'M1shaaa', 'M1shaaa', 'M1shaaa/M1shaaa', '', 0, 0, 0, '2026-05-08T13:25:36Z', 'Config files for GitHub profile'),
(901, now(), 10, 'M1shaaa', 'lab-bookshelf-', 'M1shaaa/lab-bookshelf-', 'TypeScript', 0, 0, 0, '2024-12-31T05:11:14Z', ''),
(902, now(), 10, 'M1shaaa', 'rosie-s-study-3-lookit-project', 'M1shaaa/rosie-s-study-3-lookit-project', '', 0, 0, 0, '2024-11-04T22:15:35Z', ''),
(903, now(), 10, 'M1shaaa', 'Python-Lookit-Uploads', 'M1shaaa/Python-Lookit-Uploads', 'Python', 0, 0, 0, '2024-02-16T15:20:50Z', 'random projects'),
(904, now(), 10, 'M1shaaa', 'Classes', 'M1shaaa/Classes', '', 0, 0, 0, '2023-12-07T08:16:20Z', ''),
(905, now(), 10, 'M1shaaa', 'Yale-Work', 'M1shaaa/Yale-Work', 'HTML', 0, 0, 0, '2023-12-06T18:33:10Z', ''),
(906, now(), 10, 'M1shaaa', 'MNIST-Classifier', 'M1shaaa/MNIST-Classifier', '', 0, 0, 0, '2023-11-28T06:12:13Z', ''),
(907, now(), 10, 'M1shaaa', 'Lookit-Demo', 'M1shaaa/Lookit-Demo', '', 0, 0, 0, '2023-04-10T02:50:03Z', '');

-- AustinCStone repos
INSERT INTO repo_snapshots VALUES
(1000, now(), 11, 'AustinCStone', 'EpsteinSearch', 'AustinCStone/EpsteinSearch', 'Python', 0, 0, 0, '2026-02-11T01:10:54Z', ''),
(1001, now(), 11, 'AustinCStone', 'bmforkupdate', 'AustinCStone/bmforkupdate', 'Python', 0, 0, 0, '2025-05-09T04:49:24Z', ''),
(1002, now(), 11, 'AustinCStone', 'bmfork', 'AustinCStone/bmfork', 'Python', 0, 0, 1, '2025-05-09T04:17:17Z', ''),
(1003, now(), 11, 'AustinCStone', 'bitmind-fork', 'AustinCStone/bitmind-fork', '', 0, 0, 0, '2025-01-09T06:16:51Z', 'forked on jan 8 2025'),
(1004, now(), 11, 'AustinCStone', 'TextGAN', 'AustinCStone/TextGAN', 'Python', 92, 30, 5, '2016-10-04T03:19:12Z', 'GAN for text generation in TensorFlow'),
(1005, now(), 11, 'AustinCStone', 'StructureFromMotion', 'AustinCStone/StructureFromMotion', 'Python', 1, 0, 0, '2018-06-10T18:56:16Z', 'Recover 3D geometry from videos'),
(1006, now(), 11, 'AustinCStone', 'StereoVisionMRF', 'AustinCStone/StereoVisionMRF', 'Python', 11, 4, 0, '2016-01-10T08:34:29Z', 'MRF with loopy belief propagation for stereo depth');

-- APTOS SNAPSHOTS: all wallets (balance 0 APT from mainnet query 2026-05-08)
INSERT INTO aptos_snapshots VALUES
(now(), 'alice', '0xc793acdec12b4a63717b001e21bbb7a8564d5e9690f80d41f556c2d0d624cc7b', 0.0),
(now(), 'bob', '0x0a3c00c58fdf9020b27854a3229042efa70cf782d7d2a9de0c13d00e05512d5d', 0.0),
(now(), 'A', '0x8699edc0960dd5b916074f1e9bd25d86fb416a8decfa46f78ab0af6eaebe9d7a', 0.0),
(now(), 'B', '0x3f892ebe6e45164e63416ad10e7c87ce81e1acf2264c32dcfe21105a4577cb13', 0.0),
(now(), 'C', '0x38b99e63ada9b6fef1d300b608b95bf7fa146ae39d0ab641e123f7952691535e', 0.0),
(now(), 'D', '0xf77656248f64d5dd00f2e9b8e3a104eb8936d027eda37688cc5bb2b1d9fcfdd1', 0.0),
(now(), 'E', '0xdc1d9d533bac3507f9b51b249bab86769361d3b651ab4f565906b7a8d0958d36', 0.0),
(now(), 'F', '0x18a14b5b4bec118c1cc0297e5f23d6a77f1a140b1bb9b979bcf5f6da74c3cf71', 0.0),
(now(), 'G', '0x69a394c0b0ac84212707a63f5aacaac2fd8b9ac2a44aba7c641dd3c5dbcc7f32', 0.0),
(now(), 'H', '0xce67c327a7844e5488814b79f1d660c258bc8290ddac32e6f02e850d94e5300f', 0.0),
(now(), 'I', '0x070fe5d74e4eda30e2c349d6afd7f30847c58cd5c01939da508ea15fc00c1fc9', 0.0),
(now(), 'J', '0x4d964db8f538374034194647d0e67ac395b9034ebbee111b98cb6e2293e87f54', 0.0),
(now(), 'K', '0xa732040a6b0d5590417adbdf0a1fb5f8e7d9f7e23d4ffadb2085e2a47a425dc4', 0.0),
(now(), 'L', '0x7c2eaeafad9725492e4f4688171da4c9a7c5feb68488e422194673ee6337eba9', 0.0),
(now(), 'M', '0x6fed37a7553ef16b2aaf218096b8609a0c4543adf4d4a74590fe483d49b7f2e9', 0.0),
(now(), 'N', '0xe7dde6da0a65f51062d1dbb2a3ca9569d35ec596408263a13fd4559a11551b2c', 0.0),
(now(), 'O', '0x73252b6011a75115a2853fdd924375224376f5a13822d07467bf3024a525a89d', 0.0),
(now(), 'P', '0x6218792de4a9bc38917b21aa6dbceff8565f33d27d4acd2d29366013621ec948', 0.0),
(now(), 'Q', '0xac40fa50b81b4ca6b198791824e817aa734bf4b61a1b096af0a3b6525e5c89a9', 0.0),
(now(), 'R', '0x7ce605cc8fda4f8e4a16ae0b2a40aa46e1a37d349de4d3a65d41ebeb36d76e10', 0.0),
(now(), 'S', '0xb8753014e4888ea48a2a315d9bde985af500c700bc3c27457a00beb4f99d0386', 0.0),
(now(), 'T', '0x35781dc0e42fef3f25ccc55381110751ce9969268fe8131b3759505f2d3f4588', 0.0),
(now(), 'U', '0x75860da47565f6509bcc46d8b033837163884af7eaa9a39e3fa521f395ef9956', 0.0),
(now(), 'V', '0xb59dd8170321dfab5ae9fba7c5a7fee0e9ad8a66c9e559862cff6ea8a89af2c3', 0.0),
(now(), 'W', '0x5f32aef70f5ba530d3922d4ebcb41733e7e5844aa15be8b8d8963d45a6ccc7b0', 0.0),
(now(), 'X', '0xa95cbbd116548ac9901feb0871914d297ce4f6dd6d030457d4569b2cbe33047d', 0.0),
(now(), 'Y', '0xd8e32848f1dffa811b971a12f9bede35ee5e3ecf617ba53ef2b39100fa2444c4', 0.0),
(now(), 'Z', '0x7af0ef6e1bd706f4b310ecd5246128c6c3e4c723f5223f67915ebd5e6e4e197c', 0.0);

-- MULTISIG PROBES: all 5 healthy, 2-of-2
INSERT INTO multisig_probes VALUES
(now(), 'A-B', '0x0da4f428a0c007da0f7629c3ec6a08a661ee20847556e6bf6ce880def4987003', 2, true),
(now(), 'A-G', '0xf56c4a1c0906214f3f859ccd8b498ab673979df61d7e35b2d98c5bee3fbc0096', 2, true),
(now(), 'Y-Z', '0xd3ffe1812b2df4062281c7ddd502bec5867fdc6d47175e316df742638e75b883', 2, true),
(now(), 'S-T', '0x3b1c3ae905d44c3a49f0dedd918a4c2d8aae6ae5e8339fd3570060b23ded7883', 2, true),
(now(), 'V-W', '0x40fad7b423a843650fddcad36b7de6609eead0cf1d12cb4d81b0f9082c80eb6d', 2, true);

-- MNX: no data available (SPA, API endpoint returns HTML)
-- mnx_snapshots table remains empty, noted as unavailable

-- Verification queries
SELECT 'world_increments' as tbl, count(*) as n FROM world_increments
UNION ALL SELECT 'repo_snapshots', count(*) FROM repo_snapshots
UNION ALL SELECT 'aptos_snapshots', count(*) FROM aptos_snapshots
UNION ALL SELECT 'multisig_probes', count(*) FROM multisig_probes
UNION ALL SELECT 'mnx_snapshots', count(*) FROM mnx_snapshots;
