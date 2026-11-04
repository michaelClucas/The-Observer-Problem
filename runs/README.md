# Runs

One directory per agent run. Append-only: `OUTPUT.md` and `OUTPUT.json` are
never edited after they land. Corrections live in `REVIEW.md` or in a later
run.

Naming: `<NN>-<slug>-<YYYY-MM-DD>/`, with `-m2`, `-m3` suffixes for
replications of the same prompt on different models, and `-control` for a
seed-withheld control.

Example: `01-consolidate-approaches-2026-11-04-m2/`

## META.yaml template

```yaml
run: 01-consolidate-approaches
role: cartographer
model: ""              # exact model id, not a family name
prompt_path: prompts/01-consolidate-approaches.md
prompt_commit: ""      # git sha of the prompt as used
seed_docs_provided:
  - docs/problem-statement.md
  - docs/common-scaffold.md
  - docs/approach-clusters.md
  - protocol/EVIDENCE-RULES.md
  - protocol/output-schema.md
tools_available: []    # e.g. web_search, arxiv, none
retrieval_used: null   # true | false | unknown
started: ""
finished: ""
token_cost: null
operator: ""
notes: ""
```

`prompt_commit` matters. A run whose prompt cannot be reconstructed from
the repository is not a data point.
