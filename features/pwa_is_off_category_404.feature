Feature: Category status
  Scenario: Is off category 404?
     Given run browser
      When open off category site
      Then check if 404 error will show up
       And shutdown browser