# Contributing to the ESRA AI-SIG website

This site is designed for small pull requests. Most updates should only edit
one file under `_data/`.

## Common edits

- Add an event in `_data/events.yml`.
- Add a paper or preprint in `_data/papers.yml`.
- Add a resource, organisation, dataset, tool, or method note in `_data/resources.yml`.
- Update chair details in `_data/chairs.yml`.
- Update top-level page copy in the root `.html` files.

Copy an existing YAML block, paste it in the same file, and edit the values.
Keep indentation exactly as it is.

If you are suggesting content but do not want to edit YAML, open one of the
GitHub issue forms for events, papers, or resources. A maintainer can convert
the suggestion into a data-file edit.

## Pull request checklist

- The entry has a working URL where relevant.
- The date uses `YYYY-MM-DD`; use `YYYY-01-01` when only the year is known.
- Placeholder entries keep `template: true`; real entries remove it.
- Notes are short and neutral.
- No private email addresses or unpublished personal information are added.

## Local preview

Local preview is optional because GitHub Pages builds the site automatically.

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/esrasig/`.

## Governance

The chairs review contributions for relevance to AI, machine learning, and
survey research. Inclusion on the site is not an endorsement of a method,
paper, provider, or organisation.
