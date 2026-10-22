from __future__ import annotations

from datetime import datetime, timedelta

from dash import Dash, Input, Output, dcc, html
import plotly.graph_objects as go

from cv_data import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS

ACCENT_COLORS = ["#0ea5a4", "#ff7a59", "#ffd166", "#3aa8ff", "#6b9ac4", "#f29e4c"]


def flatten_skills(category: str) -> list[dict]:
    return [
        {"category": cat_name, "skill": skill}
        for cat_name, items in SKILLS.items()
        if category == "All" or cat_name == category
        for skill in items
    ]


def filter_projects(tech_filter: list[str], query: str) -> list[dict]:
    tech_filter = tech_filter or []
    query = (query or "").strip().lower()
    filtered = []

    for project in PROJECTS:
        stack = {tech.lower() for tech in project["tech"]}
        if tech_filter and not stack.intersection({t.lower() for t in tech_filter}):
            continue
        if query:
            searchable = " ".join(
                [project["name"], project["description"], project["details"], " ".join(project["tech"])]
            ).lower()
            if query not in searchable:
                continue
        filtered.append(project)

    return filtered


def filter_experience(tech_filter: list[str]) -> list[dict]:
    tech_filter = tech_filter or []
    if not tech_filter:
        return EXPERIENCE

    filtered = []
    lowered = {tech.lower() for tech in tech_filter}
    for role in EXPERIENCE:
        if lowered.intersection({tech.lower() for tech in role["tech"]}):
            filtered.append(role)
    return filtered


def classify_experience_section(role: dict) -> str:
    section = str(role.get("section", "")).strip().lower()
    if section in {"work", "professional"}:
        return "work"
    if section in {"leadership", "competition", "hackathon", "project", "research"}:
        return "leadership"

    company_text = f"{role.get('company', '')} {role.get('role', '')}".lower()
    if "hackathon" in company_text or "competition" in company_text:
        return "leadership"
    return "work"


def split_experience_sections(roles: list[dict]) -> tuple[list[dict], list[dict]]:
    work_roles = []
    leadership_roles = []
    for role in roles:
        if classify_experience_section(role) == "leadership":
            leadership_roles.append(role)
        else:
            work_roles.append(role)
    return work_roles, leadership_roles


def card(title: str, value: str, subtitle: str) -> html.Div:
    return html.Div(
        className="kpi-card",
        children=[
            html.Div(title, className="kpi-title"),
            html.Div(value, className="kpi-value"),
            html.Div(subtitle, className="kpi-subtitle"),
        ],
    )


def empty_figure(title: str, message: str) -> go.Figure:
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=14, color="#35495e"),
    )
    fig.update_layout(
        title=title,
        margin=dict(l=24, r=24, t=60, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        font=dict(family="'Space Grotesk', sans-serif", color="#16212f"),
    )
    return fig


def style_figure(fig: go.Figure, title: str) -> go.Figure:
    fig.update_layout(
        title=dict(text=title, x=0.01, xanchor="left"),
        margin=dict(l=24, r=24, t=60, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="'Space Grotesk', sans-serif", color="#16212f"),
    )
    fig.update_xaxes(gridcolor="rgba(22,33,47,0.12)", zeroline=False)
    fig.update_yaxes(gridcolor="rgba(22,33,47,0.12)", zeroline=False)
    return fig


def make_timeline_figure(roles: list[dict]) -> go.Figure:
    if not roles:
        return empty_figure("Experience dates", "No experience matches this filter.")

    fig = go.Figure()
    for idx, role in enumerate(sorted(roles, key=lambda r: r["start_month"])):
        start = datetime.strptime(role["start_month"], "%Y-%m")
        end_month = datetime.strptime(role["end_month"], "%Y-%m")
        end = (end_month.replace(day=28) + timedelta(days=4)).replace(day=1)
        label = role.get("timeline_label", role["role"])
        fig.add_trace(go.Bar(
            x=[(end - start).total_seconds() * 1000], y=[label], base=[start],
            orientation="h", marker=dict(color=ACCENT_COLORS[idx % len(ACCENT_COLORS)]),
            customdata=[[role["date_range"], role["company"], role["location"]]],
            hovertemplate="<b>%{y}</b><br>%{customdata[1]}<br>%{customdata[0]}<br>%{customdata[2]}<extra></extra>",
        ))
    fig.update_layout(showlegend=False, bargap=0.45, height=360)
    fig.update_xaxes(type="date", tickformat="%b %Y", title="Month", automargin=True)
    fig.update_yaxes(automargin=True)
    return style_figure(fig, "Experience dates")


def make_skill_category_figure(skill_rows: list[dict]) -> go.Figure:
    if not skill_rows:
        return empty_figure("Tools and topics", "No skills match this filter.")
    categories = list(dict.fromkeys(row["category"] for row in skill_rows))
    counts = [sum(row["category"] == category for row in skill_rows) for category in categories]
    fig = go.Figure(go.Bar(
        x=counts, y=categories, orientation="h", marker_color="#0ea5a4",
        hovertemplate="%{y}<br>%{x} listed tools or topics<extra></extra>",
    ))
    fig.update_xaxes(title="Number listed", dtick=1)
    fig.update_yaxes(automargin=True)
    return style_figure(fig, "Tools and topics by category")


def make_skill_bubble_figure(skill_rows: list[dict]) -> go.Figure:
    if not skill_rows:
        return empty_figure("Tools and topics", "Choose a category to see its tools and topics.")
    fig = go.Figure(go.Scatter(
        x=[row["category"] for row in skill_rows],
        y=[row["skill"] for row in skill_rows], mode="markers",
        marker=dict(size=13, color="#0ea5a4"),
        text=[row["category"] for row in skill_rows],
        hovertemplate="<b>%{y}</b><br>%{text}<extra></extra>",
    ))
    fig.update_layout(height=max(360, len(skill_rows) * 26))
    fig.update_yaxes(automargin=True)
    return style_figure(fig, "Tools and methods")


def make_project_technology_figure(projects: list[dict]) -> go.Figure:
    if not projects:
        return empty_figure("Project tools", "No projects match this filter.")
    points = [(project["name"], tech) for project in projects for tech in project["tech"]]
    fig = go.Figure(go.Scatter(
        x=[tech for _, tech in points], y=[name for name, _ in points],
        mode="markers", marker=dict(size=12, color="#ff7a59"),
        hovertemplate="<b>%{y}</b><br>%{x}<extra></extra>",
    ))
    fig.update_yaxes(automargin=True)
    fig.update_xaxes(tickangle=-35, automargin=True)
    return style_figure(fig, "Tools listed for each project")


def make_project_cards(projects: list[dict]) -> list[html.Div]:
    if not projects:
        return [html.Div("No projects match your filters.", className="empty-state")]

    cards = []
    for project in projects:
        children = []
        if project.get("badge"):
            children.append(html.Div(project["badge"], className="feature-badge"))
        children.extend([
            html.Div(project["name"], className="card-title"),
            html.Div(project["description"], className="card-description"),
            html.Div(project["details"], className="card-description"),
            html.Div([html.Span(tag, className="tag") for tag in project["tech"]], className="tag-row"),
        ])
        if project.get("link"):
            children.append(html.A("View Project", href=project["link"], target="_blank", className="card-link"))
        cards.append(html.Div(
            className="project-card featured" if project.get("badge") else "project-card",
            children=children,
        ))
    return cards


def make_experience_cards(roles: list[dict], empty_message: str) -> list[html.Div]:
    if not roles:
        return [html.Div(empty_message, className="empty-state")]

    cards = []
    for role in sorted(roles, key=lambda r: r["start_year"], reverse=True):
        cards.append(
            html.Div(
                className="experience-card",
                children=[
                    html.Div(f"{role['role']} @ {role['company']}", className="card-title"),
                    html.Div(f"{role['date_range']} | {role['location']}", className="card-meta"),
                    html.Ul([html.Li(item) for item in role["highlights"]], className="bullet-list"),
                    html.Div([html.Span(tag, className="tag") for tag in role["tech"]], className="tag-row"),
                ],
            )
        )
    return cards


def make_education_cards() -> list[html.Div]:
    cards = []
    for item in EDUCATION:
        cards.append(
            html.Div(
                className="education-card",
                children=[
                    html.Div(item["degree"], className="card-title"),
                    html.Div(item["school"], className="card-description"),
                    html.Div(item.get("graduation", str(item["year"])), className="card-meta"),
                    html.Div("GPA: " + item["gpa"], className="card-meta"),
                    html.P("Coursework: " + item.get("coursework", ""), className="card-description"),
                ],
            )
        )
    return cards




def make_skill_chips(skill_rows: list[dict]) -> list[html.Span]:
    if not skill_rows:
        return [html.Span("No skills selected", className="tag")]
    return [html.Span(row["skill"], className="tag") for row in skill_rows]


def panel_visibility(selected_view: str) -> tuple[dict, dict, dict, dict]:
    hidden = {"display": "none"}
    visible = {"display": "block"}

    if selected_view == "overview":
        return visible, hidden, hidden, hidden
    if selected_view == "experience":
        return hidden, visible, hidden, hidden
    if selected_view == "projects":
        return hidden, hidden, visible, hidden
    return hidden, hidden, hidden, visible


all_tech = sorted({tech for project in PROJECTS for tech in project["tech"]} | {tech for role in EXPERIENCE for tech in role["tech"]})
all_categories = ["All"] + sorted(SKILLS.keys())

app = Dash(__name__)
app.title = "Interactive CV Dashboard"

app.layout = html.Div(
    id="app-shell",
    children=[
        html.Div(className="bg-grid"),
        html.Div(className="orb orb-1"),
        html.Div(className="orb orb-2"),
        html.Div(className="orb orb-3"),
        html.Div(
            className="page",
            children=[
                html.Header(
                    className="hero",
                    children=[
                        html.Div("Interactive CV", className="eyebrow"),
                        html.H1(PROFILE["name"], className="name"),
                        html.Div(PROFILE["headline"], className="headline"),
                        html.P(PROFILE["summary"], className="summary"),
                        html.Div(
                            className="contact-row",
                            children=[
                                html.Span(PROFILE["location"]),
                                html.Span(PROFILE["email"]),
                                html.Span(PROFILE["phone"]),
                            ],
                        ),
                        html.Div(
                            className="link-row",
                            children=[
                                html.A(label, href=url, target="_blank", className="pill-link")
                                for label, url in PROFILE["links"].items()
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="dashboard-grid",
                    children=[
                        html.Aside(
                            className="control-panel",
                            children=[
                                html.H3("Explore"),
                                html.Label("View"),
                                dcc.RadioItems(
                                    id="view-mode",
                                    options=[
                                        {"label": "Overview", "value": "overview"},
                                        {"label": "Experience", "value": "experience"},
                                        {"label": "Projects", "value": "projects"},
                                        {"label": "Skills", "value": "skills"},
                                    ],
                                    value="overview",
                                    className="view-pills",
                                    labelClassName="view-pill",
                                ),
                                html.Label("Skill Category"),
                                dcc.Dropdown(
                                    id="skill-category",
                                    options=[{"label": item, "value": item} for item in all_categories],
                                    value="All",
                                    clearable=False,
                                ),
                                html.Label("Filter by Tool or Topic"),
                                dcc.Dropdown(
                                    id="tech-filter",
                                    options=[{"label": item, "value": item} for item in all_tech],
                                    multi=True,
                                    placeholder="Select one or more",
                                ),
                                html.Label("Search Projects"),
                                dcc.Input(
                                    id="project-search",
                                    type="text",
                                    placeholder="e.g. Costos, MovieLens, Excel",
                                    debounce=True,
                                ),
                            ],
                        ),
                        html.Main(
                            className="main-panel",
                            children=[
                                html.Div(id="view-badge", className="view-badge"),
                                html.Div(id="kpi-row", className="kpi-row"),
                                html.Div(
                                    id="overview-panel",
                                    className="panel",
                                    children=[
                                        dcc.Graph(id="timeline-graph", config={"displayModeBar": False}),
                                        html.Div(
                                            className="split-grid",
                                            children=[
                                                dcc.Graph(id="project-tools", config={"displayModeBar": False}),
                                                dcc.Graph(id="skill-categories", config={"displayModeBar": False}),
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    id="experience-panel",
                                    className="panel",
                                    children=[
                                        html.H3("Work Experience"),
                                        html.Div(id="work-experience-grid", className="card-grid"),
                                        html.H3("Research & Student Projects"),
                                        html.Div(id="leadership-experience-grid", className="card-grid"),
                                        html.H3("Education"),
                                        html.Div(id="education-grid", className="education-grid"),
                                    ],
                                ),
                                html.Div(
                                    id="projects-panel",
                                    className="panel",
                                    children=[
                                        html.H3("Selected Projects"),
                                        html.Div(id="project-grid", className="card-grid"),
                                    ],
                                ),
                                html.Div(
                                    id="skills-panel",
                                    className="panel",
                                    children=[
                                        dcc.Graph(id="skill-bubbles", config={"displayModeBar": False}),
                                        html.H3("Skill Tags"),
                                        html.Div(id="skill-chips", className="tag-row"),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)


@app.callback(
    Output("view-badge", "children"),
    Output("kpi-row", "children"),
    Output("timeline-graph", "figure"),
    Output("skill-categories", "figure"),
    Output("skill-bubbles", "figure"),
    Output("project-tools", "figure"),
    Output("project-grid", "children"),
    Output("work-experience-grid", "children"),
    Output("leadership-experience-grid", "children"),
    Output("education-grid", "children"),
    Output("skill-chips", "children"),
    Output("overview-panel", "style"),
    Output("experience-panel", "style"),
    Output("projects-panel", "style"),
    Output("skills-panel", "style"),
    Input("skill-category", "value"),
    Input("tech-filter", "value"),
    Input("project-search", "value"),
    Input("view-mode", "value"),
)
def refresh_dashboard(category: str, tech_filter: list[str], search: str, view_mode: str):
    skill_rows = flatten_skills(category)
    projects = filter_projects(tech_filter, search)
    roles = filter_experience(tech_filter)
    work_roles, leadership_roles = split_experience_sections(roles)

    min_start = min(item["start_year"] for item in EXPERIENCE)
    max_end = max(item["end_year"] for item in EXPERIENCE)

    kpis = [
        card("Experience dates", f"{min_start}-{max_end}", "Internships and student projects"),
        card("Visible Projects", str(len(projects)), "Based on filters"),
        card("Visible Skills", str(len(skill_rows)), "In selected category"),
        card("Roles", str(len(roles)), "Matching tech filter"),
    ]

    view_title = {
        "overview": "Overview Mode",
        "experience": "Experience Mode",
        "projects": "Projects Mode",
        "skills": "Skills Mode",
    }.get(view_mode, "Overview Mode")

    overview_style, experience_style, projects_style, skills_style = panel_visibility(view_mode)

    return (
        view_title,
        kpis,
        make_timeline_figure(roles),
        make_skill_category_figure(skill_rows),
        make_skill_bubble_figure(skill_rows),
        make_project_technology_figure(projects),
        make_project_cards(projects),
        make_experience_cards(work_roles, "No work-experience roles match this tech filter."),
        make_experience_cards(leadership_roles, "No research or student projects match this tech filter."),
        make_education_cards(),
        make_skill_chips(skill_rows),
        overview_style,
        experience_style,
        projects_style,
        skills_style,
    )


if __name__ == "__main__":
    app.run(debug=True)


