Feature: Products sorting

  Background: common steps
     Given start test
      When run category site
      Then check if sorting button is active

    Scenario: sort from lowest price
       And sort from lowest price
       And confirm and check results
       And finish this test

    Scenario: sort from highest price
       And sort from highest price
       And apply and verify result
       And end this test



