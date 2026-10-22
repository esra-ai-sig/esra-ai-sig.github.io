# ESRA AI-SIG website

This repository contains the website for the **Artificial Intelligence Special
Interest Group (AI-SIG)** of the European Survey Research Association (ESRA).

The site is a static [Jekyll](https://jekyllrb.com/) site published with GitHub
Pages. Most contributions are small content updates to YAML files under
`_data/` or text edits to the top-level page files.

## Ways to contribute

You can contribute by opening a pull request or by using the repository's issue
forms to suggest content. Suitable contributions include:

- events, webinars, symposia, panels, and short courses
- papers or preprints relevant to AI and survey research
- resources, organisations, datasets, tools, or methods notes
- corrections to chair details, page copy, or links

For more detailed editing notes, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Common files to edit

- `_data/events.yml` for events and webinars
- `_data/papers.yml` for papers and preprints
- `_data/resources.yml` for resources and organisations
- `_data/tools.yml` for repositories, skills and workflows
- `_data/chairs.yml` for chair details
- `_data/topics.yml` for topics in focus
- `index.html`, `about.html`, `activities.html`, `resources.html`,
  `papers.html`, and `join.html` for page copy

When editing YAML, copy an existing block and keep the indentation unchanged.
Dates should use `YYYY-MM-DD`; do not invent a day if only a month or year is known.

## Pull request checklist

- Keep the change focused and easy to review.
- Include working links where relevant.
- Keep notes short, factual, and neutral.
- Do not add private contact details or unpublished personal information.
- Remove `template: true` from real entries; leave it only on placeholder
  examples.

## Local preview

Local preview is optional because GitHub Pages builds the site after changes are
merged.

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000/`.

## License

See [LICENSE](LICENSE).

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

Verification: `bundle exec ruby scripts/check_event_states.rb` checks date boundaries;
`python3 scripts/check_site.py` checks the generated site after a build.
