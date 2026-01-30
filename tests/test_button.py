from pages.button_page import ButtonPage


def test_button_exist(driver):
    button_page = ButtonPage(driver)
    button_page.open()
    assert button_page.button_is_displayed
