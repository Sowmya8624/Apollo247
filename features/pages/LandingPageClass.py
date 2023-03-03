from selenium.webdriver.common.by import By


class LandingPageClass:


    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.laterButtonElement = "//*[@id='wzrk-cancel']"
        self.cartButtonElement = "//span[@class='icon-ic_cart']"


    # Creating Element Methods
    def click_later_Button(self):
        laterButton = self.driver.find_element(By.XPATH, self.laterButtonElement)
        laterButton.click()

    def click_cart_button(self):
        cartButton = self.driver.find_element(By.XPATH, self.cartButtonElement)
        cartButton.click()














