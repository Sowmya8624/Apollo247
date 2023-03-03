
from selenium.webdriver.common.by import By

class LabTestsPageClass:
    def __init__(self, driver):
        self.driver = driver
        self.whybook = "// *[contains(text(), 'WHY BOOK WITH US?')]"

    def WHY_BOOK(self):
        whybookus=self.driver.find_element(By.XPATH,self.whybook).text
        return whybookus












