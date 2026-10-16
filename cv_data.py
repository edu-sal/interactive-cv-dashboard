PROFILE = {'name': 'Eduardo Salgado-Liceaga',
 'headline': 'Statistics student at American University | Python and data analysis',
 'location': 'Washington, D.C.',
 'email': 'js0596a@american.edu',
 'phone': '(202) 595-5801',
 'summary': "Hi, I'm Eduardo. I'm a senior studying Statistics, with a specialization in Applied "
            'Statistics and a Mathematics minor. I use Python to extract and clean spreadsheet and '
            'PDF data, make charts, and explore questions through coursework and internship '
            'projects. I use Codex for coding and debugging assistance.',
 'links': {'GitHub': 'https://github.com/js0596a',
           'LinkedIn': 'https://linkedin.com/in/edu-sal',
           'Costos Dashboard Demo': 'https://github.com/js0596a/costos-dashboard',
           'FoodBridge': 'https://devpost.com/software/food-bridge-isqzu0'}}

EXPERIENCE = [{'role': 'Data Scientist Intern',
  'company': 'Curfimex S.A. de C.V.',
  'location': 'León, Guanajuato, Mexico',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-05',
  'end_month': '2026-08',
  'date_range': 'May 2026 - Aug 2026',
  'section': 'work',
  'highlights': ['Used Python to extract and clean company data from Excel files, combining '
                 'production and material-cost records into tables for analysis.',
                 'Built Dash and Plotly dashboards to review monthly costs and compare customers '
                 'and batches, with Codex assistance for coding and debugging.',
                 'Created Pareto (80/20) charts to highlight the materials accounting for most '
                 'spending, along with Excel summaries of monthly results.'],
  'tech': ['Python', 'pandas', 'openpyxl', 'Excel', 'Dash', 'Plotly', 'Codex']},
 {'role': 'Data Analyst Intern',
  'company': 'FinEx Concierge Solutions, LLC',
  'location': 'Washington, D.C.',
  'start_year': 2025,
  'end_year': 2025,
  'start_month': '2025-05',
  'end_month': '2025-08',
  'date_range': 'May 2025 - Aug 2025',
  'section': 'work',
  'highlights': ['Used Python to extract and clean data from ABCA PDF reports for a cannabis '
                 'market-sizing project.',
                 'Created Python dashboards and Excel summaries using the ABCA data to compare '
                 'reported figures and explore market trends.',
                 'Prepared charts and presentation slides explaining the findings for review with '
                 'the project team and client.'],
  'tech': ['Python', 'PDF data extraction', 'Excel', 'Data visualization']},
 {'role': 'Undergraduate Research Assistant (Part-Time)',
  'company': 'Department of Mathematics and Statistics, American University',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-05',
  'end_month': '2026-08',
  'date_range': 'May 2026 - Aug 2026',
  'section': 'project',
  'highlights': ['Implemented a baseline matrix-factorization model in Python using MovieLens '
                 'ratings, and documented its calculations and evaluation methods in a Jupyter '
                 'notebook.',
                 'Ran experiments with 3 random seeds and compared prediction error, top-10 '
                 'recommendation quality, and catalog coverage using tables and plots.'],
  'tech': ['Python', 'NumPy', 'Jupyter', 'Model evaluation']},
 {'role': 'Product & Data Contributor',
  'company': 'George Hacks x UN Reboot the Earth Hackathon - FoodBridge',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-04',
  'end_month': '2026-04',
  'date_range': 'Apr 2026',
  'section': 'project',
  'highlights': ['Collaborated on a meal-planning prototype, contributing to how dietary '
                 'preferences, budget, and location inputs were used to suggest meals.',
                 'Presented FoodBridge with the team at George Hacks x UN Reboot the Earth, '
                 'placing 1st in the UN/FAO track.'],
  'tech': ['Prototyping', 'Presentation']},
 {'role': 'Team Lead',
  'company': 'Goldman Sachs Case Competition - American University',
  'location': 'Washington, D.C.',
  'start_year': 2026,
  'end_year': 2026,
  'start_month': '2026-04',
  'end_month': '2026-04',
  'date_range': 'Apr 2026',
  'section': 'project',
  'highlights': ['Led a 5-member student team in developing an investment recommendation for a '
                 'university endowment case competition.',
                 "Compared investment options against the case's return objectives, liquidity "
                 'needs, and divestment requirements, and summarized the analysis in a team '
                 'presentation.'],
  'tech': ['Data analysis', 'Presentation']}]

PROJECTS = [{'name': 'Costos Dashboard Demo',
  'description': 'A Dash and Plotly demo for reviewing monthly material costs, comparing customers '
                 'and batches, and exploring Pareto (80/20) charts.',
  'impact': 'Adapted from my internship app. The public demo and screenshots use synthetic data.',
  'tech': ['Python', 'pandas', 'Excel', 'Dash', 'Plotly', 'Codex'],
  'link': 'https://github.com/js0596a/costos-dashboard',
  'badge': 'Synthetic data demo'},
 {'name': 'MovieLens Recommendation Baseline',
  'description': 'A matrix-factorization model in Python, with notebook explanations and results '
                 'from three random seeds.',
  'impact': 'Compared prediction error, top-10 recommendation quality, and catalog coverage.',
  'tech': ['Python', 'NumPy', 'Jupyter', 'Model evaluation'],
  'link': 'https://github.com/js0596a',
  'link_label': 'GitHub profile'},
 {'name': 'FoodBridge',
  'description': 'A team hackathon prototype for meal planning using dietary preferences, budget, '
                 'and location.',
  'impact': 'Our team placed first in the UN/FAO track at George Hacks x UN Reboot the Earth.',
  'tech': ['Prototyping', 'Presentation'],
  'link': 'https://devpost.com/software/food-bridge-isqzu0',
  'badge': 'UN/FAO track: first place'},
 {'name': 'Leather Operations MLP Dashboard',
  'description': 'An earlier Dash project for uploading Excel data, viewing production charts, and '
                 'trying an MLP regression model.',
  'impact': 'Includes local model training and predictions from an uploaded dataset.',
  'tech': ['Python', 'Excel', 'Dash', 'Plotly', 'scikit-learn'],
  'link': 'https://github.com/js0596a/recurtido-mlp-dashboard'},
 {'name': 'Production Flow Simulator',
  'description': 'An earlier Python and SimPy project for exploring production-flow and cost '
                 'scenarios.',
  'impact': 'A separate project with charts and simulation inputs to explore.',
  'tech': ['Python', 'Dash', 'Plotly', 'SimPy'],
  'link': 'https://github.com/js0596a/empirical-lot-cost-simulator'}]

SKILLS = {'Python and data files': {'Python': 'Internship projects, research, and coursework',
                           'pandas': 'Data cleaning and analysis',
                           'NumPy': 'Research and coursework',
                           'openpyxl': 'Working with Excel files in Python',
                           'Excel': 'Data tables and summaries',
                           'Excel/PDF data extraction': 'Internship projects'},
 'Charts and dashboards': {'Dash': 'Internship and personal projects',
                           'Plotly': 'Charts and dashboards',
                           'Power BI': 'Familiarity'},
 'Statistics and coursework': {'R': 'Coursework',
                               'SQL': 'Current Database and AI coursework',
                               'Descriptive statistics': 'Coursework and data analysis',
                               'Regression': 'Coursework',
                               'Exploratory analysis': 'Coursework and internship projects',
                               'Model evaluation': 'Coursework and recommender research'},
 'Project tools': {'Git/GitHub': 'Project repositories',
                   'Codex': 'Coding and debugging assistance'}}

EDUCATION = [{'degree': 'B.S. in Statistics; Applied Statistics specialization; Mathematics minor',
  'school': 'American University, College of Arts and Sciences',
  'year': 2027,
  'graduation': 'Expected May 2027',
  'coursework': 'Probability, Mathematical Statistics, Regression, Linear Algebra, Algorithms and '
                'Data Structures, Scientific Computing, Data Mining, Machine Learning, Neural '
                'Networks/Deep Learning',
  'in_progress': 'Database and AI (SQL), Numerical Analysis, Advanced Machine Learning'}]

AWARDS = [{'title': 'Hanna Miriam Sandler Professional Society Membership Award',
  'issuer': 'Department of Mathematics and Statistics, American University',
  'year': 2026,
  'type': 'Academic Award',
  'amount': None,
  'details': ['Recognized for outstanding performance in a Department of Mathematics and '
              'Statistics course.',
              'Award includes a one-year membership in either the Mathematical Association of '
              'America (MAA) or the American Statistical Association (ASA).',
              'Membership benefits include undergraduate publications and access to research and '
              'networking conferences.']},
 {'title': 'Capital CoLAB Emerging Tech Talent Scholarship',
  'issuer': 'Capital CoLAB (administered through American University)',
  'year': 2026,
  'type': 'Scholarship',
  'amount': 2500,
  'details': ['Awarded for integrating technical training and skills into the AU curriculum.',
              'Academic Year 2026 scholarship award amount: $2,500.']}]
