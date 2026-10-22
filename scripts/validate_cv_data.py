from __future__ import annotations

from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from cv_data import EDUCATION, EXPERIENCE, PROFILE, PROJECTS, SKILLS


def _is_http_url(value) -> bool:
    return isinstance(value, str) and value.startswith(("http://", "https://"))


def _is_text_list(value) -> bool:
    return isinstance(value, list) and bool(value) and all(isinstance(item, str) and item.strip() for item in value)


def validate() -> list[str]:
    errors = []
    for key in ("name", "headline", "location", "email", "phone", "summary"):
        if not isinstance(PROFILE.get(key), str) or not PROFILE[key].strip():
            errors.append(f"PROFILE.{key} must be non-empty text")
    if not isinstance(PROFILE.get("links"), dict) or not PROFILE["links"]:
        errors.append("PROFILE.links must be a non-empty dict")
    elif any(not label or not _is_http_url(url) for label, url in PROFILE["links"].items()):
        errors.append("PROFILE.links must contain labeled HTTP URLs")

    if not isinstance(EXPERIENCE, list) or not EXPERIENCE:
        errors.append("EXPERIENCE must be a non-empty list")
    for idx, row in enumerate(EXPERIENCE):
        for key in ("role", "company", "location", "date_range"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"EXPERIENCE[{idx}].{key} must be non-empty text")
        if row.get("section") not in {"work", "project"}:
            errors.append(f"EXPERIENCE[{idx}].section must be work or project")
        try:
            start = datetime.strptime(row.get("start_month", ""), "%Y-%m")
            end = datetime.strptime(row.get("end_month", ""), "%Y-%m")
            if start > end or start.year != row.get("start_year") or end.year != row.get("end_year"):
                errors.append(f"EXPERIENCE[{idx}] has inconsistent dates")
        except (TypeError, ValueError):
            errors.append(f"EXPERIENCE[{idx}] must have valid month dates")
        for key in ("highlights", "tech"):
            if not _is_text_list(row.get(key)):
                errors.append(f"EXPERIENCE[{idx}].{key} must be a non-empty text list")

    if not isinstance(PROJECTS, list) or not PROJECTS:
        errors.append("PROJECTS must be a non-empty list")
    for idx, row in enumerate(PROJECTS):
        for key in ("name", "description", "details"):
            if not isinstance(row.get(key), str) or not row[key].strip():
                errors.append(f"PROJECTS[{idx}].{key} must be non-empty text")
        if not _is_text_list(row.get("tech")):
            errors.append(f"PROJECTS[{idx}].tech must be a non-empty text list")
        if "link" in row and not _is_http_url(row["link"]):
            errors.append(f"PROJECTS[{idx}].link must be an HTTP URL when supplied")
        if {"score", "impact", "rating"}.intersection(row):
            errors.append(f"PROJECTS[{idx}] must use descriptions without ratings or impact fields")

    if not isinstance(SKILLS, dict) or not SKILLS:
        errors.append("SKILLS must be a non-empty dict")
    else:
        for category, items in SKILLS.items():
            if not category or not _is_text_list(items):
                errors.append(f"SKILLS[{category!r}] must be a non-empty text list")

    if not isinstance(EDUCATION, list) or not EDUCATION:
        errors.append("EDUCATION must be a non-empty list")
    for idx, item in enumerate(EDUCATION):
        for key in ("degree", "school", "graduation", "gpa", "coursework"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                errors.append(f"EDUCATION[{idx}].{key} must be non-empty text")
        if not isinstance(item.get("year"), int):
            errors.append(f"EDUCATION[{idx}].year must be an integer")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("CV data validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("CV data validation passed")
    print(f"Experience entries: {len(EXPERIENCE)}")
    print(f"Project entries: {len(PROJECTS)}")
    print(f"Skill categories: {len(SKILLS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
