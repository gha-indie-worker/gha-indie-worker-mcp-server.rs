# gha-indie-worker/gha-indie-worker-mcp-server.rs#2 — docs: add AGENTS.md and fleet sops env layout

head: chore/agents-md-and-sops-env  base: main  author: ORESoftware  updated: 2026-08-27T19:14:33Z
dir: /Users/maca5/codes/.claude-fleet/scratch/merge/gha-indie-worker_gha-indie-worker-mcp-server.rs__2

## conflicted files
- justfile

## base (main) last 8 commits
c2c7994 Merge PR #4: DEN-965 gha-indie-worker MCP provider parity
90f455b docs(DEN-965): record worker MCP conformance evidence
18a5519 feat(DEN-965): harden GHA Indie Worker MCP provider parity
a215a93 Merge pull request #3 from gha-indie-worker/agent/ores-sops-ensure-dec-20260828b
4d856c7 Refuse unguarded env/dec mkdir before ores-sops.
54bc1e2 fix: recover from oversized MCP stdio frames
85d57e6 feat: specialize the hardened MCP server for gha-indie-worker
b54877c feat: establish hardened organization MCP template

## head (chore/agents-md-and-sops-env) last 8 commits
ee2a157 Replace yanked chacha20 0.10.1 with 0.10.2.
41f8ebb Run just env-check in primary CI and ignore env/dec/.
aad5c2d docs: point AGENTS.md at the parent my-ai contract and codes symlink
6f9b4ac docs: add functional programming coding patterns to AGENTS.md
1891cda docs: add AGENTS.md and fleet sops env layout
54bc1e2 fix: recover from oversized MCP stdio frames
85d57e6 feat: specialize the hardened MCP server for gha-indie-worker
b54877c feat: establish hardened organization MCP template

## merge-base: 54bc1e29406ca9c3fd784b95e5ce487ea1385dd9

## PR diff stat (merge-base..head)
 .envrc                              |   7 +
 .github/workflows/ci.yml            |  10 +
 .github/workflows/secrets-audit.yml |  32 +++
 .gitignore                          |  18 ++
 .just/dotenv.py                     |  87 +++++++
 .just/env.just                      | 461 ++++++++++++++++++++++++++++++++++++
 .sops.yaml                          |  27 ++-
 AGENTS.md                           | 105 ++++++++
 Cargo.lock                          |   4 +-
 env/README.md                       |  28 +++
 env/enc/prod.env.enc                |  10 +
 flake.nix                           |  13 +-
 justfile                            |  76 +++---
 13 files changed, 840 insertions(+), 38 deletions(-)

## base diff stat (merge-base..base)
 .github/workflows/ci.yml |   13 +-
 Cargo.lock               | 1575 +++++++++++++++++++++++++++++++++++++++++++---
 Cargo.toml               |   11 +-
 README.md                |   74 ++-
 justfile                 |    4 +-
 mcp-fleet-profile.json   |  214 +++++++
 src/http.rs              |   10 +
 src/main.rs              |   21 +-
 src/spec.rs              |   64 ++
 tests/stdio_parity.rs    |  258 ++++++++
 10 files changed, 2138 insertions(+), 106 deletions(-)

## merge output
Auto-merging .github/workflows/ci.yml
Auto-merging Cargo.lock
Auto-merging justfile
CONFLICT (content): Merge conflict in justfile
Automatic merge failed; fix conflicts and then commit the result.
