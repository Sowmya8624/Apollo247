from behave import *
from hamcrest import *



from features.pages.LandingPageClass import LandingPageClass
from features.pages.CartPageClass import CartPageClass
from features.pages.LabTestsPageClass  import LabTestsPageClass

@given(u'Chrome is opened and the apollo app is opened')
def step_impl(context):
    context.driver.implicitly_wait(10)
    expectedTitle = "Apollo 247 - Online Doctor Consultation & Book Lab Tests at Home"
    actualTitle = context.driver.title
    print("Page title is " + actualTitle)
    assert_that(expectedTitle, equal_to(actualTitle))


@when(u'User clicks on later button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    laterbutton = LandingPageClass(context.driver)
    laterbutton.click_later_Button()

@when(u'User clicks on cart icon')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Carticon= LandingPageClass(context.driver)
    Carticon.click_cart_button()


@then(u'It shows cart page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    textwritten=CartPageClass(context.driver)
    expectedText = "YOUR CART IS EMPTY"
    actualText = textwritten.Text_Capture()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


@step(u'User clicks on Book Lab tests button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    BookLabTestsButton= CartPageClass(context.driver)
    BookLabTestsButton.click_BookLabTests_Button()

@then(u'It shows Book Lab Tests at Home from Apollo Diagnostics, Pathology Labs near me page')
def step_impl(context):
    context.driver.implicitly_wait(10)
    booking_a_test = LabTestsPageClass(context.driver)
    expectedText = "WHY BOOK WITH US?"
    actualText = booking_a_test.WHY_BOOK()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))

@when(u'User clicks on  search test and packages textbox')
def step_impl(context):
    context.driver.implicitly_wait(10)
    SearchBar= CartPageClass(context.driver)
    SearchBar.click_SearchBar_Button()

@step(u'User clicks on add icon')
def step_impl(context):
    context.driver.implicitly_wait(10)
    clickplus= CartPageClass(context.driver)
    clickplus.click_img_Element()

@then(u'Test is able to add to cart')
def step_impl(context):
    context.driver.implicitly_wait(10)
    booking_a_test = LabTestsPageClass(context.driver)
    expectedText = "WHY BOOK WITH US?"
    actualText = booking_a_test.WHY_BOOK()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))

@when(u'User clicks on  Book Lab tests button')
def step_impl(context):
    context.driver.implicitly_wait(10)
    BookLabTestsButton= CartPageClass(context.driver)
    BookLabTestsButton.click_BookLabTests_Button()






@when(u'User enters {Data}')
def step_impl(context,Data):
    context.driver.implicitly_wait(10)
    SearchBar=CartPageClass(context.driver)
    SearchBar.enter_data(Data)

@then(u'It shows results for the given data')
def step_impl(context):
    context.driver.implicitly_wait(10)
    liver_kidney = CartPageClass(context.driver)
    expectedText = "VIEW ALL RESULTS"
    actualText = liver_kidney.valid_test()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


@then(u'It shows Sorry, we couldn’t find what you are looking for. Please check the recommendations below error')
def step_impl(context):
    context.driver.implicitly_wait(10)
    Error_Msg = CartPageClass(context.driver)
    expectedText = "Sorry, we couldn’t find what you are looking for. Please check the recommendations below"
    actualText = Error_Msg.error_msg()
    print(actualText)
    assert_that(expectedText, equal_to(actualText))


