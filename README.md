# Interactive CV Dashboard

Hi, I'm Eduardo. This is a Dash app for browsing my experience, projects, coursework, and skills while I finish my B.S. in Statistics at American University. My specialization is Applied Statistics, and I'm pursuing a Mathematics minor.

## What you'll find

- **Internships:** full-time, unpaid Data Scientist Intern at Curfimex (May-August 2026) and part-time, unpaid Data Analyst Intern at FinEx (May-August 2025).
- **Research:** a MovieLens matrix-factorization baseline from my part-time undergraduate research work (May-August 2026).
- **Student projects:** business and presentation contributions at the FoodBridge student hackathon, and team leadership in the Goldman Sachs student case competition (April 2026).
- **Tools and coursework:** the tools and methods listed on my résumé, with SQL marked as coursework.

At Curfimex I used Python to extract and clean Excel data, built Dash and Plotly views of monthly costs, and made Pareto (80/20) charts and Excel summaries. I used Codex for coding and debugging assistance. At FinEx I worked with ABCA PDF reports for a brief cannabis market research project and prepared dashboards, summaries, charts, and slides from those records.

For FoodBridge, I worked alongside software engineering students on the business concept and team pitch. For the Goldman Sachs case competition, I led a five-person student team examining a fictional university's endowment and funding needs, helping compare options and present our recommendations.

The app's education section separates completed coursework from my current courses: Database and AI (SQL), Numerical Analysis, and Advanced Machine Learning.

## Featured project: Costos

[Costos Dashboard Demo](https://github.com/js0596a/costos-dashboard) is a public demo adapted from my private internship app. Its data and screenshots are **synthetic**; they do not show company records.

![Costos demo: monthly overview using synthetic data](https://raw.githubusercontent.com/js0596a/costos-dashboard/main/assets/screenshots/overview.png)

![Costos demo: Pareto chart using synthetic data](https://raw.githubusercontent.com/js0596a/costos-dashboard/main/assets/screenshots/pareto.png)

## Using the CV app

Choose Overview, Experience, Projects, or Skills. You can filter experience and projects by tool or topic, search project descriptions, and browse the résumé's Tools and Methods lists. The charts show dates and listed tools.

The app uses Python, Dash, and Plotly. Its profile content lives in `cv_data.py`.

## Run it locally

```bash
git clone https://github.com/js0596a/interactive-cv-dashboard.git
cd interactive-cv-dashboard
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:8050`. If that port is busy:

```bash
python -c "from app import app; app.run(debug=True, port=8051)"
```

## Links

- [GitHub profile](https://github.com/js0596a)
- [Costos Dashboard Demo](https://github.com/js0596a/costos-dashboard)
- [FoodBridge](https://devpost.com/software/food-bridge-isqzu0)
- [LinkedIn](https://linkedin.com/in/edu-sal)

This repository contains portfolio content and app code. Private company datasets are not included.


