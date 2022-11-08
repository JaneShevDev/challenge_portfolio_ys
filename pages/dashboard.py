from pages.base_page import BasePage


class Dashboard(BasePage):
    Players_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    Language_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    Main_page_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    Add_player_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    Add_language_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[15]/button/span[1]"
    Add_link_to_Youtube_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[19]/button/span[1]"
    Clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    Submit_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[1]/span[1]"
    Reset_button_xpath = "/html/body/div[2]/div[3]/div/div[1]/div[1]/button/span[1]"
    Search_field_xpath = "//*[@id='__next']/div[1]/header/div/div[1]/div[2]/input"
    pass