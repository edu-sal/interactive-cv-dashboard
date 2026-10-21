# CV Dashboard Architecture

## Overview

The project is configuration-driven: `cv_data.py` acts as a structured data source, while `app.py` renders a multi-view interactive dashboard with Plotly visualizations and card components.

## Runtime flow

1. `app.py` imports structured content from `cv_data.py`.
2. Helper functions filter/shape data for each panel (overview, experience, projects, skills).
3. A single callback updates KPIs, charts, cards, and panel visibility.
4. CSS in `assets/styles.css` controls visual identity, animation, and responsiveness.

## Data model

- `PROFILE`: headline, contact, external links
- `EXPERIENCE`: month-level role dates and activity descriptions
- `PROJECTS`: résumé project descriptions, a synthetic Costos demo, and optional verified links
- `SKILLS`: Tools and Methods lists from the résumé; SQL is marked as coursework
- `EDUCATION`: academic entries

## Quality gates

- `scripts/validate_cv_data.py`: validates data contract and URL format
- `pytest` tests in `tests/`: sanity checks for data consistency
- GitHub Actions in `.github/workflows/ci.yml`: compile + validate + test on push/PR

## Automation assets

- `scripts/capture_demo.py`: captures repeatable walkthrough visuals from live app interactions
- `scripts/check_links.sh`: HTTP checks for links defined in `cv_data.py`
- `Makefile`: repeatable local commands for setup, check, test, and demo generation


