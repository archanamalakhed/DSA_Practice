from playwright.sync_api import Page,expect
from orangehrm_home_page import HomePage
from orangehrm_login_page import LoginPage

def test_example(self,page:Page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    login_page.login("Admin","admin123")
    expect(home_page.is_upgrade_button_visible()).to_be_true()
    home_page.click_performance()
    home_page.click_dashboard()
    


