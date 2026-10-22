# Contributing to the ESRA AI-SIG website

This site is designed for small pull requests. Most updates should only edit
one file under `_data/`.

## Common edits

- Add an event in `_data/events.yml`.
- Add a repository or workflow in `_data/tools.yml`.
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
- The date uses `YYYY-MM-DD`; omit the date when only the year is known.
- Placeholder entries keep `template: true`; real entries remove it.
- Notes are short and neutral.
- No private email addresses or unpublished personal information are added.

## Local preview

Local preview is optional because GitHub Pages builds the site automatically.

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/`.

## Governance

The chairs review contributions for relevance to AI, machine learning, and
survey research. Inclusion on the site is not an endorsement of a method,
paper, provider, or organisation.

## Event dates and status

Use quoted ISO dates (`"2026-11-05"`). Set `end_date` for a series or multi-day
event, and `dates` for individual teaching days. The site calculates upcoming,
in-progress and past labels at build time. A daily GitHub Actions build keeps
these labels current once the changes are merged.

For an announced webinar with no confirmed day, use `month: "2026-11"` and
`status: announced`. Use `status: pending` with no date for an unapproved
proposal. Accepted conference sessions use `status: accepted`; their date range
is explicitly labelled as the conference window until a session date is known.
Do not add a booking link for an unconfirmed event.

For a paper, use its publication year in `year`; add `date` only if known.
For software, include its purpose, requirements and evidence or limitations.
