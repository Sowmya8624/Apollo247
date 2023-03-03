Feature: Add_To_Cart_DDF
Background:
    Given Chrome is opened and the apollo 247 app is opened
    When User clicks onto later button
    When User clicks onto cart icon
    Then It navigates to cart page


Scenario:  Validate valid results are showing when enters valid data
    When User clicks onto  search test and packages textbox
    And user enter validdata  for the first data
    Then It shows results for the given validdata


Scenario:  Validate valid results are showing when enters valid data
    When User clicks onto  search test and packages textbox
    And user enter validdata for the second data
    Then It shows results for the given validdata




Scenario:  Validate error showing when invalid data is entered
    When User clicks onto  search test and packages textbox
    And user enter invaliddata for the first invalid data
    Then It shows error message




Scenario:  Validate error showing when invalid data is entered
    When User clicks onto  search test and packages textbox
    And user enter invaliddata for the second invalid data
    Then It shows error message







