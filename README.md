# ESRA AI-SIG website

The website for the **Artificial Intelligence Special Interest Group (AI-SIG)**
of the European Survey Research Association (ESRA). It is a static
[Jekyll](https://jekyllrb.com/) site hosted on **GitHub Pages** — no server, no
database, no build step to run yourself. GitHub builds and publishes it
automatically every time you edit a file.

Most maintenance is done by **editing plain-text data files in GitHub's web
interface** — no coding required.

---

## Contents

- [What I still need from the chairs](#what-i-still-need-from-the-chairs)
- [Quick start: before you publish](#quick-start-before-you-publish)
- [Adding content (events, resources, papers)](#adding-content)
- [Editing other things (chairs, topics, navigation)](#editing-other-things)
- [Where the placeholders live](#placeholders-to-replace)
- [How the site is structured](#site-structure)
- [Running it locally (optional)](#running-locally-optional)
- [Licence](#licence)

---

## What I still need from the chairs

The site is publishable with safe fallbacks, but these inputs make it fully live:

| Item | Why it matters | Where it goes |
| --- | --- | --- |
| Mailing-list provider and public signup URL | Enables one-click joining and provider-managed unsubscribing | `mailing_list_url` in `_config.yml` |
| Suggestion form endpoint | Lets visitors submit resources, papers, events, and webinar ideas without a custom backend | `suggestion_form_action` in `_config.yml` |
| First real events | Replaces the three template webinar/symposium/course entries | `_data/events.yml` |
| Initial curated papers/preprints | Makes the Papers page useful at launch | `_data/papers.yml` |
| Extra organisations/resources | Grows the Resources page beyond the seeded AAPOR report | `_data/resources.yml` |
| GitHub owner/repo decision | Determines the free GitHub Pages URL and `baseurl` | `url` and `baseurl` in `_config.yml` |
| Optional custom domain | Only needed if you want a URL outside `github.io` | `CNAME` file plus DNS records |

Recommended service choices:

- Mailing list: use a managed list with public subscribe/unsubscribe links, such as JISCMail, Google Groups, Mailchimp, Brevo, or Buttondown.
- Suggestions: use a static form provider such as Formspree, Tally, or Netlify Forms. GitHub Pages cannot process forms by itself.
- Domain: start with the free GitHub Pages project URL, then add a custom domain later only if ESRA or the chairs want one.

---

## Quick start: before you publish

You must do these **two things once** before launch:

### 1. Set `url` and `baseurl`

This site is configured for a GitHub Pages **project page** at
`https://<username>.github.io/<REPO-NAME>/`.

The current default assumes this repository will be published as
`pamato/esrasig`, which would serve the site at:

```text
https://pamato.github.io/esrasig/
```

If the owner or repository name changes, update `_config.yml`:

```yaml
url: "https://USERNAME.github.io"   # your GitHub username/org, no trailing slash
baseurl: "/REPO-NAME"               # the repository name, leading slash
```

Example — a repo named `ai-sig` owned by `esra`, served at
`esra.github.io/ai-sig`:

```yaml
url: "https://esra.github.io"
baseurl: "/ai-sig"
```

If you later add a **custom domain** (for example `ai-surveys.esra.org`), set
`url` to the domain, set `baseurl: ""`, and add a `CNAME` file. GitHub's
Settings → Pages screen can create the `CNAME` file for you.

> Every link and asset in the site already uses Jekyll's `relative_url` filter,
> so once `baseurl` is correct, **everything else just works**.

### 2. Turn on GitHub Pages

In the repository: **Settings → Pages → Build and deployment → Source:
GitHub Actions**. The included workflow at `.github/workflows/pages.yml` builds
and deploys the site on every push to `main`.

GitHub Pages is free for public repositories. The GitHub documentation explains
that project sites are served by default at
`https://<owner>.github.io/<repositoryname>` and can later be attached to a
custom domain.

### 3. Make changes through pull requests

Give co-chairs write access or ask them to fork the repository. The normal flow:

1. Create a branch.
2. Edit one of the `_data/*.yml` files or page files.
3. Open a pull request.
4. Review the rendered diff and merge.
5. GitHub Pages rebuilds automatically.

For fuller contributor notes, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

Visitors can also suggest events, papers, and resources through GitHub issue
forms. Those templates live in `.github/ISSUE_TEMPLATE/` and give maintainers a
structured queue even before the public suggestion form endpoint is connected.

### Domain recommendation

Use the free project URL for launch unless ESRA can provide a subdomain:

1. Best zero-cost launch: `https://pamato.github.io/esrasig/`
2. Best institutional custom domain: `https://ai-surveys.europeansurveyresearch.org/` or another ESRA-owned subdomain
3. Avoid buying a separate domain unless the SIG needs a standalone brand; it adds renewal and ownership admin

---

## Adding content

All content lives in **`_data/*.yml`** files. To edit one on GitHub: open the
file, click the ✏️ pencil, make your change, and **Commit changes**. The site
rebuilds in ~1 minute.

> 💡 YAML is indentation-sensitive. Copy an existing block, keep the same
> indentation, and edit the values. Wrap any value containing a colon, `#`, or
> quote in double quotes.

### Events — `_data/events.yml`

Webinars, symposia/panels, and short courses. Copy a block and edit it:

```yaml
- type: event           # always "event"
  kind: webinar         # webinar | symposium | course
  title: "Using LLMs to code open-ended responses"
  date: "2027-03-12"    # YYYY-MM-DD  (leave "" if not yet scheduled)
  status: upcoming      # upcoming | past
  speaker: "A. Researcher (University of …)"
  location: "Online"
  link: "https://…"     # registration or recording (optional)
  note: "A one-line description."
  # template: true      # delete this line — it is only for placeholders
```

Seed entries have `template: true`, which shows a dashed **Template** badge and
hides the date. **Delete that line** when the entry becomes real. Please don't
invent realistic dates for placeholders.

### Resources — `_data/resources.yml`

Guidance, organisations, datasets/tools, and methods resources. The `section`
field decides which group it appears under:

```yaml
- type: resource                 # always "resource"
  section: guidance              # guidance | organisations | datasets | methods
  title: "Responsible AI Integration in Survey Research"
  org: "AAPOR"
  date: "2026-05-01"             # used for ordering (YYYY-MM-DD)
  year: 2026                     # display year (optional)
  link: "https://…"
  note: "A one-line description."
```

### Papers & preprints — `_data/papers.yml`

A curated reading list (we do **not** scrape):

```yaml
- type: paper                    # always "paper"
  title: "Paper title"
  authors: "Surname, A., Surname, B."
  year: 2026
  date: "2026-02-01"             # used for ordering; YYYY-01-01 if only year known
  venue: "Journal / arXiv / preprint server"
  link: "https://doi.org/…"
  note: "Why it is relevant."
```

### The "Latest" box on the home page updates itself

The home page **Latest** list is generated automatically from the three files
above (newest first). You don't edit the home page — just add to the data files
and it updates on the next build. See `_includes/latest.html`.

---

## Editing other things

- **Chairs** — `_data/chairs.yml` (name, institution, email). Shown on About and
  Join.
- **Topics in focus** — `_data/topics.yml` (a plain list; numbering is
  automatic). Shown on Home and About.
- **Navigation menu** — `_data/navigation.yml` (labels, order, the Join button).
- **Page intros / copy** — the `.html` files in the project root
  (`index.html`, `about.html`, `activities.html`, `resources.html`,
  `papers.html`, `join.html`). The text at the top of each file between the
  `---` lines (the "front matter") sets that page's heading, intro, and SEO
  description.

---

## Placeholders to replace

Two endpoints are stubbed in `_config.yml`:

| Key | What to set it to |
| --- | --- |
| `mailing_list_url` | The subscribe link from your mailing-list provider (JISCMail, Google Group, Mailchimp, …). Leave blank until chosen; the site will show an email fallback. |
| `suggestion_form_action` | A form endpoint that receives the suggestion form. GitHub Pages can't process forms itself — use a free service like [Formspree](https://formspree.io) and paste the endpoint, e.g. `https://formspree.io/f/abcdwxyz`. Leave blank until chosen; the site will show an email fallback. |
| `suggestion_email` | The fallback email address used when the mailing-list or suggestion form service is not yet live. |

The suggestion form fields (name, email, type, title, link, description) are in
`join.html`.

To customise link previews, drop a 1200×630 PNG at
`assets/img/og-card.png` and point `og_image` in `_config.yml` at it.

---

## Site structure

```
_config.yml            Site settings — url/baseurl, placeholders (edit me first)
index.html             Home
about.html             About + chairs
activities.html        Activities programme (from _data/events.yml)
resources.html         Resources (from _data/resources.yml)
papers.html            Papers & preprints (from _data/papers.yml)
join.html              Join + suggestion form + contacts
_data/                 ← the files chairs edit
  navigation.yml  chairs.yml  topics.yml  events.yml  resources.yml  papers.yml
_layouts/              Page shells (default, page)
_includes/             head, header, footer, latest (the auto "Latest" loop)
assets/css/main.css    All styling and colours (CSS custom properties at the top)
assets/img/            Logo and images
```

Only GitHub Pages-supported plugins are used (`jekyll-sitemap`) — no custom
plugins, so the Pages build will not fail.

---

## Running locally (optional)

You do **not** need this to publish — GitHub builds the site for you. But to
preview changes before committing:

```bash
bundle install
bundle exec jekyll serve
# open http://localhost:4000/esrasig/
```

Requires Ruby and Bundler. See the
[GitHub Pages docs](https://docs.github.com/pages/setting-up-a-github-pages-site-with-jekyll).

---

## Licence

See [`LICENSE`](LICENSE). The repository ships with the permissive **MIT**
licence as a default for the site code. **Please confirm this is what you want** —
for the *written content* (resource notes, descriptions) you may prefer a
Creative Commons licence such as **CC BY 4.0**. We can split the two (MIT for
code, CC BY for content) if you'd like; just say the word.
