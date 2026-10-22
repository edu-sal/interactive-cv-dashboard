from cv_data import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS
from scripts.validate_cv_data import validate


def test_cv_data_satisfies_the_renderer_contract():
    assert validate() == []


def test_optional_project_links_do_not_imply_unpublished_repositories():
    projects = {project["name"]: project for project in PROJECTS}
    assert "link" not in projects["MovieLens Recommendation Baseline"]
    assert "link" not in projects["Goldman Sachs Case Competition"]
    assert projects["Costos Dashboard Demo"]["link"] == "https://github.com/edu-sal/costos-dashboard"


def test_skill_categories_preserve_the_resume_lists_and_coursework_label():
    assert SKILLS == {
        "Tools": ["Python", "R", "pandas", "NumPy", "openpyxl", "Excel", "Power BI", "Plotly", "Dash", "Git/GitHub", "Codex", "SQL (coursework)"],
        "Methods": ["Excel/PDF data extraction", "Data cleaning", "Exploratory analysis", "Descriptive statistics", "Regression", "Data visualization", "Model evaluation"],
    }


def test_experience_matches_confirmed_roles_dates_and_bullet_counts():
    assert [(role["role"], role["date_range"], len(role["highlights"])) for role in EXPERIENCE] == [
        ("Data Scientist Intern (Full-Time, Unpaid)", "May 2026 - Aug 2026", 3),
        ("Data Analyst Intern (Part-Time, Unpaid)", "May 2025 - Aug 2025", 3),
        ("Undergraduate Research Assistant (Part-Time)", "May 2026 - Aug 2026", 2),
        ("Business & Presentation Contributor", "Apr 2026", 2),
        ("Team Lead (Student Case Competition)", "Apr 2026", 2),
    ]


def test_project_scope_and_research_description_are_grounded_in_resume():
    assert [project["name"] for project in PROJECTS] == [
        "Costos Dashboard Demo", "MovieLens Recommendation Baseline", "FoodBridge", "Goldman Sachs Case Competition"
    ]
    research = PROJECTS[1]
    assert [research["description"], research["details"]] == EXPERIENCE[2]["highlights"]
    assert "synthetic data" in PROJECTS[0]["details"]
    assert all(not {"score", "impact", "rating"}.intersection(project) for project in PROJECTS)


def test_degree_and_current_coursework_remain_distinct():
    education = EDUCATION[0]
    assert education["gpa"] == "3.91"
    assert "B.S. in Statistics" in education["degree"]
    assert "Mathematics minor" in education["degree"]
    assert education["in_progress"] == "Database and AI (SQL), Numerical Analysis, Advanced Machine Learning"
    assert "Advanced Machine Learning" not in education["coursework"]
