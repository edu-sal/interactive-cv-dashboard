from cv_data import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS
from scripts.validate_cv_data import validate


def test_cv_data_satisfies_the_renderer_contract():
    assert validate() == []


def test_optional_project_links_do_not_imply_unpublished_repositories():
    projects = {project["name"]: project for project in PROJECTS}
    assert "link" not in projects["MovieLens Recommendation Baseline"]
    assert "link" not in projects["Goldman Sachs Case Competition"]
    assert projects["Costos Dashboard Demo"]["link"] == "https://github.com/edu-sal/costos-dashboard"


def test_skills_preserve_supported_tools_and_academic_context():
    all_skills = {skill for items in SKILLS.values() for skill in items}
    assert "Power BI" not in all_skills
    assert "SQL (coursework)" in SKILLS["Tools"]
    assert {"Literature review", "Research communication"} <= set(SKILLS["Methods"])
    assert "Reviewing outputs in context" in SKILLS["AI-assisted problem solving"]

    # Academic topics must retain their qualifications rather than imply industry use.
    academic_methods = {"Data preprocessing", "Feature-engineering fundamentals", "Cross-validation"}
    academic_optimization = {"Gradients", "Regularization", "Lagrange multipliers (theory)", "Non-convex matrix factorization"}
    assert academic_methods <= set(SKILLS["Academic ML methods"])
    assert academic_optimization <= set(SKILLS["Academic optimization"])
    practical_skills = set(SKILLS["Tools"]) | set(SKILLS["Methods"])
    assert not (academic_methods | academic_optimization) & practical_skills


def test_experience_matches_confirmed_roles_and_dates():
    assert [(role["role"], role["date_range"]) for role in EXPERIENCE] == [
        ("Data Scientist Intern (Full-Time, Unpaid)", "May 2026 - Aug 2026"),
        ("Data Analyst Intern (Part-Time, Unpaid)", "May 2025 - Aug 2025"),
        ("Undergraduate Research Assistant (Part-Time)", "May 2026 - Aug 2026"),
        ("Business & Presentation Contributor", "Apr 2026"),
        ("Team Lead (Student Case Competition)", "Apr 2026"),
    ]


def test_project_scope_and_research_description_are_grounded_in_resume():
    assert [project["name"] for project in PROJECTS] == [
        "Costos Dashboard Demo", "MovieLens Recommendation Baseline", "FoodBridge", "Goldman Sachs Case Competition"
    ]
    research = PROJECTS[1]
    highlights = EXPERIENCE[2]["highlights"]
    # The project summarizes the model work; the role also explains mentoring and literature review.
    assert research["description"] in highlights
    assert research["details"] in highlights
    assert "AI as the primary coding assistant" in research["description"]
    assert "three random seeds" in research["details"]
    assert len(highlights) == len(set(highlights))
    assert highlights[0].startswith("Faculty mentor: Dr. Zois Boukouvalas,")
    assert "MS in Data Science and MS in Artificial Intelligence" in highlights[0]
    assert any("Reviewed research literature" in item and "findings, and limitations" in item for item in highlights)
    assert "synthetic data" in PROJECTS[0]["details"]
    assert all(not {"score", "impact", "rating"}.intersection(project) for project in PROJECTS)


def test_degree_and_coursework_match_the_resume():
    education = EDUCATION[0]
    assert education["gpa"] == "3.91"
    assert "B.S. in Statistics" in education["degree"]
    assert "Mathematics minor" in education["degree"]
    assert "in_progress" not in education
    for topic in ("Advanced Machine Learning", "Database Design", "SQL", "Numerical Linear Algebra", "Probability Theory"):
        assert topic in education["coursework"]
    assert "coursework and academic projects" in education["coursework"]
    assert "Lagrange multipliers (theory)" in education["coursework"]

