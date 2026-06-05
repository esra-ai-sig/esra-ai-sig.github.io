# Domain options

## Recommended launch path

Start with the free GitHub Pages organization URL:

```text
https://esra-ai-sig.github.io/
```

This costs nothing to host, works from a public GitHub repository, and lets
co-chairs contribute through pull requests.

## Custom domain later

If ESRA can provide a subdomain, prefer an institutional URL such as:

```text
https://ai-surveys.europeansurveyresearch.org/
```

or:

```text
https://ai-sig.europeansurveyresearch.org/
```

For a custom domain, change `_config.yml`:

```yaml
url: "https://ai-surveys.europeansurveyresearch.org"
baseurl: ""
```

Then add a `CNAME` file containing only the domain name:

```text
ai-surveys.europeansurveyresearch.org
```

GitHub recommends verifying the custom domain before use. For `www` and other
subdomains, configure a DNS `CNAME` record through the domain owner.

## Separate domain

A separate domain such as `esra-ai-sig.org` is technically fine but not
recommended for v1. It introduces purchase, renewal, DNS ownership, and handover
work that the SIG does not need for launch.
