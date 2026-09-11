# International Commission on Stratigraphy
This repository contains the source code for the International Commission on Stratigraphy's website online at <https://stratigraphy.org>. 

## Technical notes
This is a [Jekyll](https://jekyllrb.com/) *static site generator* website which means the source files are pretty much simplified HTML pages - [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)-formatted text files which you can see stored in the [pages/](pages/) folder. These are combined with a very simple template to add headers & footers to all pages and produce the final HTML web pages which are then delivered online with a web server. We are using the built-in [GitHub Pages](https://pages.github.com/).

### Development

```sh
bundle install
bundle exec jekyll serve
```

Open http://localhost:4000. To keep dependencies inside this checkout, prefix both
commands with `BUNDLE_PATH=vendor/bundle`.

```sh
bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

### Theme and page conventions

The site uses [Bulma Clean Theme 1.3](https://github.com/chrisrhymes/bulma-clean-theme),
the theme listed at https://jekyllthemes.io/theme/bulma. Its `page` and `default`
layouts provide the document shell and content typography. `_config.yml` defaults
apply the page layout without a sidebar. Add YAML front matter to every new page;
keep existing permalinks when editing pages.

- Edit `_data/navigation.yml` for the navbar dropdowns. The header include follows
  the upstream navbar, with the ICS logo and keyboard/expanded-state fixes.
- `_includes/hero.html` retains the full ICS heading and picks one banner from
  `images/banner-*` per document load. No timer or slideshow is used. Without
  JavaScript the first banner remains visible.
- `assets/css/app.scss` imports the theme and contains the small shared overrides
  for fluid containers, branding, portraits, responsive images and wide tables.
  Prefer Markdown and Bulma utility classes over inline styles or page CSS.
- Model reference documents use the same page layout, preserving their anchors,
  content and JSON-LD metadata. IUGS Markdown pages also receive the theme.
- `_includes/footer.html` supplies the ICS copyright.

### GitHub Pages: original site and preview

`.github/workflows/pages.yml` publishes one combined Pages artifact:

- `master` is built with GitHub's standard `actions/jekyll-build-pages` action at
  `https://stratigraphy.org/`, using its own unchanged source and configuration.
- `new-ui` is built with its locked Ruby dependencies and `--baseurl /new` at
  `https://stratigraphy.org/new/`.
- The assembly script copies the original build without changing any bytes, adds
  the preview under `new/`, and verifies all production file hashes. If `master`
  already contains `new/`, the workflow fails instead of overwriting it.
- Byte-identical downloads in `ICSchart/` and `files/` are shared from the root
  to stay below the Pages size limit; changed downloads remain under `/new`.
- Preview HTML links to existing preview pages and assets are prefixed with
  `/new`. Links to applications outside this repository (including `/chart`,
  `/guide/`, and `/gssps/`) continue pointing to the existing root destinations.
- Pull requests build and validate without deploying. Pushes and manual runs on
  `new-ui` or `master` publish both sites. Deployments are serialized.

#### First publication

Commit and push the `new-ui` changes, including this workflow and `scripts/`.
In repository **Settings → Pages**, change the build source from **Deploy from a
branch** to **GitHub Actions**, retaining the `stratigraphy.org` custom domain and
HTTPS settings. In the `github-pages` environment, permit deployments from
`new-ui` as well as `master`. The existing branch-based builder cannot append a
second independently built site; GitHub Pages replaces the full deployment.

Run **Publish original site and new UI preview** on `new-ui` (or push another
commit after configuring Pages). The workflow file must be present on the
selected branch. GitHub may not offer manual dispatch in the UI until a workflow
is registered on the default branch; pushing `new-ui` triggers it directly.

No workflow or content changes have been made to `master`. Consequently, pushes
to `master` alone will not trigger this workflow until its workflow file is also
installed there. Until then, rerun the workflow on `new-ui` after master updates
to publish both branches' latest versions. Do not restore the legacy builder
while keeping this preview: its next deployment would remove `/new`.

#### Local assembly check

Build master into a separate directory and build new-ui with
`bundle exec jekyll build --baseurl /new --destination /tmp/ics-preview`.
Then run:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/assemble_pages.py /tmp/ics-master /tmp/ics-preview /tmp/ics-combined
```

The output directory must not already exist. Serve the combined directory to
check the root website and `/new/` together. This does not publish anything.

## License & Rights
The content of this repository is licensed using the Creative Commons Attribution 4.0 license:

* <https://creativecommons.org/licenses/by/4.0/>

See the [local copy of the license deed](LICENSE) for details.

&copy; International Commission on Stratigraphy, all rights reserved


## Support and contacts
*For website technical matters:*  
**Dr Nicholas J. Car**  
<nick@kurrawong.ai>  

*For all ICS matters:*  
**Prof Charles Henderson**  
ICS Secretary  
<cmhender@ucalgary.ca>  
