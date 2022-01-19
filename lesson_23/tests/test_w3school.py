from time import sleep


def test_check_title_after_click_on_search_result(dashboard_page):
    csharp_cource_page = dashboard_page.select_c_sharp_cource()

    assert "C#" in csharp_cource_page.get_title()
    sleep(5)
