@functionaltests
Feature: Apollo Addtocart
Background:
    Given Chrome is opened and the apollo app is opened
    When User clicks on later button

  Scenario: To validate Add to cart page is opened

    When User clicks on cart icon
    Then It shows cart page



  Scenario: To validate BOOK LAB TESTS button

    When User clicks on cart icon
    Then It shows cart page
    And User clicks on Book Lab tests button
    Then It shows Book Lab Tests at Home from Apollo Diagnostics, Pathology Labs near me page



  Scenario:Validate test is added into cart by using "search test and packages"option

    When User clicks on cart icon
    Then It shows cart page
    When User clicks on  search test and packages textbox
    And User clicks on add icon
    Then Test is able to add to cart


  Scenario Outline:  Validate showing results when enters valid data

    When User clicks on cart icon
    Then It shows cart page
    When User clicks on  search test and packages textbox
    And User enters <valid data>
    Then It shows results for the given data
    Examples:
    |valid data|
    |liver |
    |kidney |


  Scenario Outline:  Validate error message is shown when invalid data is entered in search test and packages textbox

    When User clicks on cart icon
    Then It shows cart page
    When User clicks on  search test and packages textbox
    And User enters <invalid data>
    Then It shows Sorry, we couldn’t find what you are looking for. Please check the recommendations below error
    Examples:
    |invalid data|
    |193028259 |
    |rwwtwaeta |



