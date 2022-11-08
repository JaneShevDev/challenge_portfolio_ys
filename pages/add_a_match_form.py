from pages.base_page import BasePage


class Dashboard(BasePage):
    Email_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input"
    Phone_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    Name_field_xpath = "//*[@id=/__next/]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    Surname_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    Weight_field_xpath = "//*[@id=/__next/]/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    Height_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/div/div/input"
    Select_leg_field_xpath = "//*[@id='mui-component-select-leg']"
    Club_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    Level_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    Main_position_field_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    pass