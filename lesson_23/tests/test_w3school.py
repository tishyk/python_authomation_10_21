def test_check_title_after_click_on_search_result(dashboard_page):
    c_sharp_course_page = dashboard_page.select_c_sharp_course()

    assert "C#" in c_sharp_course_page.get_title()
