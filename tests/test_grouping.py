from digest.grouping import by_area


def test_subjects_group_by_the_area_before_the_colon():
    assert by_area(["api: fix paging", "API: add search", "docs: typo"]) == {
        "api": ["fix paging", "add search"], "docs": ["typo"]}


def test_a_subject_with_no_area_goes_under_other():
    assert by_area(["Merge branch main", "fix the thing: now"]) == {
        "other": ["Merge branch main", "fix the thing: now"]}
