from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_header_xpath = "//*[@id='__next']/form/div/div[1]/h5", "//*[text()='Scouts Panel']", "//h5[@class='MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom']"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a", "//*[text()='Remind password']", "//child::div/a"
    language_button_xpath = "//*[@id='__next']/form/div/div[2]/div/div", "//div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input']", "//*[text()='English']"
    sign_in_button_xpath = "//*[@id='__next']/form/div/div[2]/button/span[1]", "//*[text()='Sign in']", "//span[@class='MuiButton-label']"
    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
