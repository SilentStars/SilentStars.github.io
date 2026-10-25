# Theme provenance

This personal site uses [al-folio](https://github.com/alshedivat/al-folio), starter commit f2a2765c8a9413f6ec703fc02070fbe6becf1572, with the upstream Gemfile.lock and pinned al_folio_core 1.0.15 / al_folio_cv 1.0.2.

The MIT license in LICENSE covers the upstream starter. Runtime components retain their gem licenses. The footer credits Jekyll and al-folio.

The one runtime override is assets/css/main.scss. It retains the upstream imports and appends _sass/_personal.scss for portrait framing, accent colors, and the owner’s activity list. Run `bundle exec al-folio upgrade overrides audit` after runtime updates.

The site-specific _plugins/local_style_cache.rb extends the pinned cache digester to include local Sass, the entry point, and Gemfile.lock. Core 1.0.15 only hashes its own Sass fallback, which leaves returning visitors with stale CSS after local edits. The regression check in test/style_cache_test.rb covers those update paths.

Personal source data: the owner’s CV and confirmed publication/activity records. Paper metadata was cross-checked against arXiv, OpenReview, the EMBC programme, the University of Bremen publication record, and Uppsala’s DiVA repository.
