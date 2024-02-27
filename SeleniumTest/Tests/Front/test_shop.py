import pytest

from selenium.webdriver.common.by import By

@pytest.mark.xfail(reason='Wait for fix bug')
def test_first(browser):
    """
    Тест проверка FAQ 
    """
    browser.get(url="https://testqastudio.me/")

    #menu-top [class*='menu-item-11088']
    element = browser.find_element(by=By.CSS_SELECTOR, value='#menu-top [class*="menu-item-11088"]')
    element.click()

    assert browser.current_url == 'https://testqastudio.me/faq/', 'Unexpected url'

    faq_menu_2 = browser.find_element(by=By.XPATH, value='//*[contains(text(), "Можно ли поставить доп.фурнитуру?")]')
    faq_menu_2.click()

    assert True, ''