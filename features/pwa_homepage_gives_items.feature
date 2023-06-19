Feature: Homepage return items
  Scenario: does enabled category return items?
     Given run selenium
      When go to homepage
      Then check if homepage return items
       And end of test