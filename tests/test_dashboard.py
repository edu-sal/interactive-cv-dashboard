from datetime import datetime

from app import app, filter_projects, flatten_skills, make_timeline_figure, refresh_dashboard, split_experience_sections
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
    sql = next(row for row in flatten_skills('Statistics and coursework') if row['skill'] == 'SQL')
    assert 'coursework' in sql['context'].lower()
    assert not flatten_skills('Missing category')


def test_callback_and_dash_endpoints_render_without_scores():
    for view in ['overview', 'experience', 'projects', 'skills']:
        output = refresh_dashboard('All', [], '', view)
        assert len(output) == 16
        assert sum(style['display'] == 'block' for style in output[-4:]) == 1
    client = app.server.test_client()
    assert client.get('/').status_code == 200
    layout = client.get('/_dash-layout')
    assert layout.status_code == 200
    assert 'skill-min' not in layout.get_data(as_text=True)
