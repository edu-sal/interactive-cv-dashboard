# My interactive CV

Hi, I'm Eduardo. I'm finishing my B.S. in Statistics at American University, with an Applied Statistics specialization and a Mathematics minor.

This is a small Dash app for browsing my experience, projects, coursework, and skills. For a quick overview or a job application, here's my **[résumé (PDF)](https://github.com/edu-sal/edu-sal/blob/main/Eduardo_Salgado_Liceaga_Resume.pdf)**. The app keeps the same experience bullets, with filters and project links to help you explore.

My experience so far includes cleaning Excel records and making cost dashboards at Curfimex, using ABCA PDF reports for a brief market research project at FinEx, and evaluating a MovieLens recommendation model in a part-time research role. I also contributed to the business concept and presentation for FoodBridge and led a student team in an endowment case competition.

The internship and project descriptions explain my individual contribution. I use AI as a primary coding assistant, bringing the data context and research questions, refining prompts, and reviewing the outputs. Coursework appears in one list, matching the résumé.

## A project you can explore: Costos

**[Costos](https://github.com/edu-sal/costos-dashboard)** is a public demo based on the kind of dashboard work I did during my Curfimex internship. I used Codex as the primary coding assistant, supplying context from tanning and leather-processing cost records. The smaller public demo lets you compare monthly costs, look at spending concentration, and export Excel summaries. All data and screenshots are **synthetic**.

![Costos demo: monthly overview using synthetic data](https://raw.githubusercontent.com/edu-sal/costos-dashboard/main/assets/screenshots/overview.png)

## FoodBridge: a student team project

**[FoodBridge](https://github.com/damianleng/food-bridge)** is an AI-powered meal-planning prototype we worked on at the George Hacks x UN Reboot the Earth student hackathon. I collaborated with software engineering students on the business concept and presentation, using AI tools to help refine our ideas and explain the project. Our team placed first in the UN/FAO track.

The repository shows the team's application; my contribution focused on the business and presentation side.

## Using the CV app

Choose Overview, Experience, Projects, or Skills. You can filter experience and projects by tool or topic, search project descriptions, and browse the résumé's Tools, Methods, and AI-assisted work lists. The charts show dates and listed tools.

The app uses Python, Dash, and Plotly. Its profile content lives in `cv_data.py`.

## Run it locally

```bash
git clone https://github.com/edu-sal/interactive-cv-dashboard.git
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

- [GitHub profile](https://github.com/edu-sal)
- [Costos Dashboard Demo](https://github.com/edu-sal/costos-dashboard)
- [FoodBridge team repository](https://github.com/damianleng/food-bridge)
- [FoodBridge hackathon submission](https://devpost.com/software/food-bridge-isqzu0)
- [LinkedIn](https://linkedin.com/in/edu-sal)

This repository contains portfolio content and app code. Private company datasets are not included.


