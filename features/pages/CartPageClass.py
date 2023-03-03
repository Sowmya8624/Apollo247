
from selenium.webdriver.common.by import By

class CartPageClass:
    def __init__(self, driver):
        self.driver = driver
        self.BookLabTestsButtonElement = "//*[contains(text(),'BOOK LAB TESTS')]"
        self.SearchBarElement = "// input[ @ placeholder = 'Search test and packages']"
        self.imageElement="//img[@alt='add'][1]"
        self.validtest="//*[contains(text(),'VIEW ALL RESULTS')]"
        self.showerror="//*[@id='fixedSearchCT']/div[2]/div/div[1]/p"
        self.EmptyTextElement = "//*[contains(text(),'YOUR CART IS EMPTY')]"

    def click_BookLabTests_Button(self):
        BookLabTestsButton = self.driver.find_element(By.XPATH, self.BookLabTestsButtonElement)
        BookLabTestsButton.click()

    def click_SearchBar_Button(self):
        SearchBarButton = self.driver.find_element(By.XPATH, self.SearchBarElement)
        SearchBarButton.click()

    def click_img_Element(self):
        imgclick=self.driver.find_element(By.XPATH, self.imageElement)
        imgclick.click()

    def enter_data(self,text):
        enterdata=self.driver.find_element(By.XPATH,self.SearchBarElement)
        enterdata.send_keys(text)

    def valid_test(self):
        valid_test_result=self.driver.find_element(By.XPATH,self.validtest).text
        return valid_test_result

    def error_msg(self):
        err_msg = self.driver.find_element(By.XPATH, self.showerror).text
        return err_msg

    def Text_Capture(self):
        TextElement = self.driver.find_element(By.XPATH, self.EmptyTextElement).text
        return TextElement


    def invalid_test(self):
        invalid_test_result=self.driver.find_element(By.XPATH,self.showerror).text
        return invalid_test_result


