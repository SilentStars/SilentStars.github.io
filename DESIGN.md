# Design

## Source of truth
- Status: Active. Last refreshed: 2026-10-25.
- Surfaces: homepage, publications, activities, teaching, blog, CV, and existing paper URLs.
- Evidence: owner chose the official al-folio demo; _pages/about.md, _data/activities.yml, original CV, and the supplied portrait.

## Brand
- Natural, thoughtful, approachable academic voice. Research and accurate professional history provide trust.
- Avoid marketing slogans, inflated roles, invented posts, placeholder content, and dashboard-style cards on the homepage.

## Product goals
- Help collaborators understand the researcher, read papers, and find contact details and CV.
- Keep future content updates simple. No account system or paid hosting.
- Success: clear mobile navigation, readable paper entries, working CV download, and an easy-to-maintain repository.

## Personas and jobs
- Researchers, potential collaborators, students, and academic reviewers.
- Learn about current research; follow sources; find teaching, service, contact, and career history.

## Information architecture
- Navigation: about, publications, activities, teaching, blog, CV.
- Homepage: identity, biography, research questions, recent activities, selected papers, contact.
- Preserve /publication/hysteretic-graph-odes/, /publication/heterophily-graph-level-tasks/, and /talks/.

## Design principles
- Reuse al-folio components. Prefer white space and typography over decoration.
- Make scientific and professional claims traceable to the owner’s CV or paper records.
- Keep a full publication list on its own page; three selected papers are enough for the homepage.

## Visual language
- Use al-folio light/dark themes, Roboto text, and a restrained teal accent (#176a72 light, #79c9cc dark).
- Keep a 960px content width, generous paragraph spacing, and the supplied portrait with CSS cropping.
- Keep motion limited to existing theme interactions; avoid decorative effects.

## Components
- Reuse theme about/page/CV/post layouts, BibTeX paper entries, search, and navigation.
- Site-owned additions: activity-entry.liquid and _personal.scss.
- The Sass entry point override appends personal rules; other runtime remains gem-owned.

## Accessibility
- Aim for WCAG 2.2 AA: readable contrast, semantic headings, descriptive links, and visible keyboard focus.
- Use text alongside icons where appropriate; preserve the theme’s keyboard and menu semantics.
- Respect system reduced-motion preferences in theme components.

## Responsive behavior
- Portrait sits to the right on wider screens and above the text on phones. Navigation collapses below 768px so all six links fit comfortably.
- Publication and CV entries must fit narrow screens without horizontal scrolling.
- CV dates stack above the details below 768px, and the CV sidebar is hidden at that width to preserve reading space.
- Navigation collapses into a keyboard-accessible menu on small screens.

## Interaction states
- Static pages need no loading UI. Search and paper disclosure controls use theme states.
- An empty blog displays a short, natural note; it must not contain fictional posts.
- Missing pages show a clear home link. CV download links point to the actual PDF.

## Content voice
- First-person English, concrete questions and plain language; warm without exaggerated claims.
- Use NeurIPS consistently; keep Main Track, workshop, and extended abstract distinctions visible.
- Treat the PDF CV as a professional record; keep the homepage more conversational.

## Implementation constraints
- Jekyll/al-folio v1 runtime in pinned gems; GitHub Actions builds and deploys to GitHub Pages.
- Extend existing tokens; no additional design system or frontend build pipeline.
- Keep identity assets local and publication links explicit. Avoid analytics and external post ingestion.
- Include local Sass and dependency changes in the stylesheet version so returning visitors receive layout updates automatically.
- Verify generated internal links and inspect the live homepage, publications, CV, mobile menu, and theme switch.

## Open questions
- None blocking. Future blog content and project images can be added when supplied by the owner.
