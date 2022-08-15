from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//*[@id='__next']/div[1]/header/div/h6"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//span[text()='Polski']"
    sign_out_button_xpath = "//span[text()='Sign out']"
    dev_team_contact_field_xpath = "//a[@href='https://app.slack.com/client/T3X4CAKNU/C3XTEGXB6']"
    test_name_test_surname_hyperlink_xpath = "//a[@href='/en/players/62f0389d2d2b7461da157b11/edit']"
    tester_tester_button_xpath = "//a[@href='/en/players/6079e8746629f1037f4e302a/edit']/child::button"
    test_testowy_link_xpath = "//a[@href='/en/players/6026b48956c79737b3f3c624/reports/605a2740d6f567200510a7d6/edit']"
    events_count_subheader_xpath = "//*[text()='Events count']"
    pass