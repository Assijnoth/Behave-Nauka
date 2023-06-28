Feature: Creating new user
  Scenario: I can create new user
     Given launch webdrivers
      When run homepage
       And dismiss cache
       And open login section
       And choose create account
       And fill account details
       And confirm consents
       And confirm creating account
       And check if creating account succesbox appear
      Then test ending
