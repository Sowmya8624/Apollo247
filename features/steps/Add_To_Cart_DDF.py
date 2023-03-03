from behave import *
from hamcrest import *
from features.pages.CartPageClass import CartPageClass
from features.pages.LandingPageClass import LandingPageClass
from datafiles import ExcelUtils
from features.utility.ConfigClass import ConfigClass

@given(u'Chrome is opened and the apollo 247 app is opened')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))
    context.driver.implicitly_wait(10)

@when(u'User clicks onto later button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    laterbutton = LandingPageClass(context.driver)
    laterbutton.click_later_Button()
    context.driver.implicitly_wait(10)

@when(u'User clicks onto cart icon')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Carticon = LandingPageClass(context.driver)
    Carticon.click_cart_button()
    context.driver.implicitly_wait(10)

@then(u'It navigates to cart page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    textwritten = CartPageClass(context.driver)
    expectedText = "YOUR CART IS EMPTY"
    actualText = textwritten.Text_Capture()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))
    context.driver.implicitly_wait(10)

@when(u'User clicks onto  search test and packages textbox')
def step_impl(context):
    context.driver.implicitly_wait(10)
    SearchBar = CartPageClass(context.driver)
    SearchBar.click_SearchBar_Button()
    context.driver.implicitly_wait(10)

@when(u'user enter {validdata1} for the first data')
def step_impl(context,validdata1):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    validdata1 = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1",2,1)
    SearchBar = CartPageClass(context.driver)
    SearchBar.enter_data(validdata1)
    context.driver.implicitly_wait(10)


@when(u'user enter {invaliddata1} for the first invalid data')
def step_impl(context,invaliddata1):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet2")
    invaliddata1 = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet2", 2, 1)
    SearchBar = CartPageClass(context.driver)
    SearchBar.enter_data(invaliddata1)
    context.driver.implicitly_wait(10)

@when(u'user enter {validdata2} for the second data')
def step_impl(context,validdata2):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    validdata2 = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 3, 1)
    SearchBar = CartPageClass(context.driver)
    SearchBar.enter_data(validdata2)
    context.driver.implicitly_wait(10)

@when(u'user enter {invaliddata2} for the second invalid data')
def step_impl(context,invaliddata2):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet2")
    invaliddata2 = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet2", 3, 1)
    SearchBar = CartPageClass(context.driver)
    SearchBar.enter_data(invaliddata2)
    context.driver.implicitly_wait(10)

@then(u'It shows results for the given validdata')
def step_impl(context):
    context.driver.implicitly_wait(10)
    liver_kidney = CartPageClass(context.driver)
    expectedText = "VIEW ALL RESULTS"
    actualText = liver_kidney.valid_test()
    print(actualText)
    try:
        if (expectedText== actualText):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 3, 2, "Passed")

        else:

            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 2, 2, "Failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet1", 3, 2, "Failed")
            assert False
    finally:
        print("results are shown")

    context.driver.implicitly_wait(10)

@then(u'It shows error message')
def step_impl(context):
    context.driver.implicitly_wait(10)
    liver_kidney = CartPageClass(context.driver)
    expectedText = "Sorry, we couldn’t find what you are looking for. Please check the recommendations below"
    actualText = liver_kidney.invalid_test()
    print(actualText)
    try:
        if (expectedText == actualText):
            assert True
            print("Test is passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet2", 2, 2, "Passed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet2", 3, 2, "Passed")

        else:
            print("Test is failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet2", 2, 2, "Failed")
            ExcelUtils.write_data(ConfigClass.dataFilePath, "Sheet2", 3, 2, "Failed")
            assert False

    finally:
        print("results are shown")

    context.driver.implicitly_wait(10)

