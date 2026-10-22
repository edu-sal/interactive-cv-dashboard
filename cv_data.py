PROFILE = {'name': 'Eduardo Salgado-Liceaga',
 'headline': 'Statistics student at American University | Python and data analysis',
 'location': 'Washington, D.C.',
 'email': 'eddy9202003@gmail.com',
 'phone': '(202) 595-5801',
 'summary': "I'm Eduardo, a Statistics senior at American University, graduating in May 2027. I "
            'like taking data from Excel files and PDF reports, organizing it, and finding a clear '
            'way to explain the results. My experience includes cost dashboards, a brief market '
            'research project, and undergraduate research with movie-rating data. I use Codex for '
            'coding and debugging assistance.',
 'links': {'GitHub': 'https://github.com/edu-sal',
           'LinkedIn': 'https://linkedin.com/in/edu-sal',
           'Costos Dashboard Demo': 'https://github.com/edu-sal/costos-dashboard',
           'Résumé (PDF)': 'https://github.com/edu-sal/edu-sal/blob/main/Eduardo_Salgado_Liceaga_Resume.pdf'}}

EXPERIENCE = [{'role': 'Data Scientist Intern (Full-Time, Unpaid)',
  'company': 'Curfimex S.A. de C.V.',
  'location': 'León, Guanajuato, Mexico',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-05',
  'end_month': '2026-08',
  'date_range': 'May 2026 - Aug 2026',
  'section': 'work',
  'highlights': ['Compiled and cleaned production and material-cost data from company Excel files '
                 'using Python.',
                 'Developed Dash and Plotly dashboards to compare costs by month, customer, and '
                 'batch, with Codex assistance for coding and debugging.',
                 'Identified materials contributing most to production costs using Pareto (80/20) '
                 'charts and prepared monthly Excel summaries.'],
  'tech': ['Python', 'Excel', 'Dash', 'Plotly', 'Codex']},
 {'role': 'Data Analyst Intern (Part-Time, Unpaid)',
  'company': 'FinEx Concierge Solutions, LLC',
  'location': 'Washington, D.C.',
  'start_year': 2025,
  'end_year': 2025,
  'start_month': '2025-05',
  'end_month': '2025-08',
  'date_range': 'May 2025 - Aug 2025',
  'section': 'work',
  'highlights': ['Extracted and organized data from ABCA PDF reports using Python for a brief '
                 'cannabis market research project.',
                 'Created Python dashboards and Excel summaries to compare figures reported in the '
                 'ABCA files.',
                 'Summarized market research findings in charts and presentation slides.'],
  'tech': ['Python', 'Excel', 'PDF data extraction', 'Data visualization']},
 {'role': 'Undergraduate Research Assistant (Part-Time)',
  'company': 'American University - Department of Mathematics and Statistics',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-05',
  'end_month': '2026-08',
  'date_range': 'May 2026 - Aug 2026',
  'section': 'project',
  'highlights': ['Implemented a matrix-factorization baseline in Python using MovieLens ratings, '
                 'documenting the model and its evaluation in a Jupyter notebook.',
                 'Evaluated rating-prediction error, top-10 recommendation quality, and the range '
                 'of movies recommended across experiments with three random seeds.'],
  'tech': ['Python', 'Jupyter notebook', 'Model evaluation']},
 {'role': 'Business & Presentation Contributor',
  'company': 'George Hacks x UN Reboot the Earth Hackathon - FoodBridge',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-04',
  'end_month': '2026-04',
  'date_range': 'Apr 2026',
  'section': 'project',
  'highlights': ['Collaborated with software engineering students on FoodBridge, a meal-planning '
                 'prototype, contributing to its business concept.',
                 'Presented FoodBridge with the team at a student hackathon, where the team placed '
                 '1st in the UN/FAO track.'],
  'tech': ['Business concept', 'Team presentation', 'Collaboration']},
 {'role': 'Team Lead (Student Case Competition)',
  'company': 'Goldman Sachs Case Competition - American University',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-04',
  'end_month': '2026-04',
  'date_range': 'Apr 2026',
  'section': 'project',
  'highlights': ['Led a five-person student team in a case competition about a fictional '
                 "university's endowment and funding needs.",
                 "Assessed investment options with teammates against the case's budget needs and "
                 "investment restrictions, and presented the team's recommendations."],
  'tech': ['Case analysis', 'Team presentation', 'Team leadership']}]

PROJECTS = [{'name': 'Costos Dashboard Demo',
  'description': 'A Dash and Plotly demo for reviewing monthly material costs, comparing customers '
                 'and batches, and exploring Pareto (80/20) charts.',
  'details': 'Adapted from my internship app. The public demo and screenshots use synthetic data.',
  'tech': ['Python', 'Excel', 'Dash', 'Plotly', 'Codex'],
  'link': 'https://github.com/edu-sal/costos-dashboard',
  'badge': 'Synthetic data demo'},
 {'name': 'MovieLens Recommendation Baseline',
  'description': 'Implemented a matrix-factorization baseline in Python using MovieLens ratings, '
                 'documenting the model and its evaluation in a Jupyter notebook.',
  'details': 'Evaluated rating-prediction error, top-10 recommendation quality, and the range of '
             'movies recommended across experiments with three random seeds.',
  'tech': ['Python', 'Jupyter notebook', 'Model evaluation']},
 {'name': 'FoodBridge',
  'description': 'Collaborated with software engineering students on FoodBridge, a meal-planning '
                 'prototype, contributing to its business concept.',
  'details': 'Presented FoodBridge with the team at a student hackathon, where the team placed 1st '
             'in the UN/FAO track.',
  'tech': ['Business concept', 'Team presentation', 'Collaboration'],
  'link': 'https://devpost.com/software/food-bridge-isqzu0'},
 {'name': 'Goldman Sachs Case Competition',
  'description': 'Led a five-person student team in a case competition about a fictional '
                 "university's endowment and funding needs.",
  'details': "Assessed investment options with teammates against the case's budget needs and "
             "investment restrictions, and presented the team's recommendations.",
  'tech': ['Case analysis', 'Team presentation', 'Team leadership']}]

SKILLS = {'Tools': ['Python',
           'R',
           'pandas',
           'NumPy',
           'openpyxl',
           'Excel',
           'Power BI',
           'Plotly',
           'Dash',
           'Git/GitHub',
           'Codex',
           'SQL (coursework)'],
 'Methods': ['Excel/PDF data extraction',
             'Data cleaning',
             'Exploratory analysis',
             'Descriptive statistics',
             'Regression',
             'Data visualization',
             'Model evaluation']}

EDUCATION = [{'degree': 'B.S. in Statistics; Applied Statistics specialization; Mathematics minor',
  'school': 'American University, College of Arts and Sciences',
  'year': 2027,
  'graduation': 'Expected May 2027',
  'coursework': 'Probability, Mathematical Statistics, Regression, Linear Algebra, Algorithms and '
                'Data Structures, Scientific Computing, Data Mining, Machine Learning, Neural '
                'Networks/Deep Learning',
  'in_progress': 'Database and AI (SQL), Numerical Analysis, Advanced Machine Learning',
  'gpa': '3.91'}]
