from pages.looks_like_a_button import LooksButton


def test_button_exist_2(driver):
    button_page_2 = LooksButton(driver)
    button_page_2.open()
    assert button_page_2.button_exist
