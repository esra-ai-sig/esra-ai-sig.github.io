source "https://rubygems.org"

# Use the github-pages gem so your local build matches GitHub Pages exactly.
# It pins Jekyll and every allowed plugin to the versions Pages runs.
gem "github-pages", group: :jekyll_plugins

# Plugins declared in _config.yml (also bundled by github-pages, listed here
# so `bundle exec jekyll serve` picks them up locally).
group :jekyll_plugins do
  gem "jekyll-sitemap"
end

# Windows / JRuby compatibility shims (harmless elsewhere).
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]
