from datetime import datetime

from app import app, filter_projects, flatten_skills, make_project_cards, make_timeline_figure, refresh_dashboard, split_experience_sections
from cv_data import EXPERIENCE


def test_research_is_grouped_with_student_projects():
    work, projects = split_experience_sections(EXPERIENCE)
    assert len(work) == 2
    assert len(projects) == 3
    assert all('Intern' in item['role'] for item in work)


def test_month_timeline_does_not_expand_internship_to_a_full_year():
    figure = make_timeline_figure([EXPERIENCE[0]])
    trace = figure.data[0]
    assert trace.base[0] == datetime(2026, 5, 1)
    assert trace.x[0] == (datetime(2026, 9, 1) - datetime(2026, 5, 1)).total_seconds() * 1000
    assert 'May 2026 - Aug 2026' == trace.customdata[0][0]


def test_search_and_skill_context_filters():
    assert [row['name'] for row in filter_projects(['Dash'], 'synthetic')] == ['Costos Dashboard Demo']
    assert {'category': 'Coursework tools', 'skill': 'SQL (coursework)'} in flatten_skills('Coursework tools')
    assert not flatten_skills('Missing category')


def test_callback_and_dash_endpoints_render_without_scores():
    for view in ['overview', 'experience', 'projects', 'skills']:
        output = refresh_dashboard('All', [], '', view)
        assert len(output) == 15
        assert sum(style['display'] == 'block' for style in output[-4:]) == 1
    client = app.server.test_client()
    assert client.get('/').status_code == 200
    layout = client.get('/_dash-layout')
    assert layout.status_code == 200
    assert 'skill-min' not in layout.get_data(as_text=True)
    assert 'awards-grid' not in layout.get_data(as_text=True)
    assert 'Scholarships' not in layout.get_data(as_text=True)



def test_projects_without_links_render_without_fabricated_anchors():
    from cv_data import PROJECTS
    for name in ["MovieLens Recommender and Popularity Analysis", "Goldman Sachs Case Competition"]:
        project = next(item for item in PROJECTS if item["name"] == name)
        card = make_project_cards([project])[0]
        assert all(getattr(child, "href", None) is None for child in card.children)


def test_empty_filters_and_award_removal_keep_callback_outputs_valid():
    import json
    from plotly.utils import PlotlyJSONEncoder
    output = refresh_dashboard("Tools", ["missing-tool"], "no-match", "projects")
    assert len(output) == 15
    rendered = json.dumps(output, cls=PlotlyJSONEncoder).lower()
    assert "scholarship" not in rendered
    assert "sandler" not in rendered
    assert "colab" not in rendered
    assert "awards" not in rendered
    callback = next(iter(app.callback_map.values()))
    assert len(callback["output"]) == len(output)

