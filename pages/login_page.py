from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage

class LoginPage(BasePage):
    scouts_panel_header_xpath = "//*[text()='Scouts Panel']"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    language_button_xpath = "//*[@id='__next']/form/div/div[2]/div/div"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]"

    expected_title = "Scouts panel - sign in"
    login_url = "https://scouts-test.futbolkolektyw.pl/en"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_the_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
