Feature: Adding/editing adress to my account
  Scenario: I can add/edit adress to my account
     Given running webdrivers
      When visit homepage
      Then go to login panel
       And enter account informations
       And check if login is correct
       And go to my data
       And fill user data
       And save it and compare
       And fill delivery data
       And save it and compare too
       And end that test


