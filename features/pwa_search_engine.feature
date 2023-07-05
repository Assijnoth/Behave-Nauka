Feature: Search engine

 Background: common steps
       Given open webdrivers
        When get homepage
        Then go to search engine

  Scenario: Search for existing item

       And type a name of existing item
       And check if search engine return that item
       And shutdown webdrivers


   Scenario: Search for non existing item
       And type a random string
       And check if search engine return something
       And close webdrivers
