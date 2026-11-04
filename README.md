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

### GitHub Pages publication

The workflow publishes the current `master` theme at <https://stratigraphy.org/> and a frozen copy of
the previous website at <https://stratigraphy.org/old/>. The legacy checkout is pinned to commit
`ffa7a0f9baa4a77b5c4d9cf674eb887e1fecf38c`, the last published original site before the switch.

Both builds use the locked Ruby dependencies on master. The legacy build disables the unused Minima
theme to avoid compiling its obsolete Sass. The assembly script rebases legacy links, inline banner
paths and CSS assets to `/old`, while retaining links to separately hosted applications at the root.
Identical chart and file downloads are shared from the root to keep the artifact below 1 GB.
Former `/new` HTML routes redirect to their corresponding root routes.

Pushes to master publish automatically; pull requests validate without deploying. Keep Pages configured
for GitHub Actions with the existing custom domain and HTTPS settings. The `new-ui` branch is synchronized at the switch to retire its former publication workflow.
Future changes should go through master; pushes to `new-ui` no longer deploy.

To validate locally, build master to `/tmp/ics-current` and the pinned legacy checkout to
`/tmp/ics-legacy`, then run:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/assemble_pages.py /tmp/ics-current /tmp/ics-legacy /tmp/ics-combined
```

Use a fresh assembly output directory. Run `python3 scripts/check_site.py` after building master
to the default `_site` directory to verify page routes and theme coverage.

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
ICS Secretary-General
<cmhender@ucalgary.ca>
