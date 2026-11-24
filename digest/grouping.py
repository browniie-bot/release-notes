"""Group commit subjects by the area they name, as `api: fix paging` names `api`."""


def by_area(subjects: list[str]) -> dict[str, list[str]]:
    """Group subjects by the word before the first colon; the rest go under `other`."""
    groups: dict[str, list[str]] = {}
    for subject in subjects:
        area, mark, rest = subject.partition(":")
        key = area.strip().lower() if mark and " " not in area.strip() else "other"
        groups.setdefault(key, []).append(rest.strip() if key != "other" else subject.strip())
    return groups
