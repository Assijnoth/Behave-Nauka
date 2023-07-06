Feature: Products filtering
  Scenario: filtering returns right items
     Given webdrivers startup
      When go to category site
      Then check if filter button is active
       And apply price filter
       And apply size filter
       And apply color filter
       And confirm filter and check results
       And finalize the test



