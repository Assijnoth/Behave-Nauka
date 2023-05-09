Feature: Site login
  Scenario Outline: Testing sign in
     Given Launch browser
      When open site
      Then go to login section
       And enter username <login> and password <password>
       And check login is success
       And close browser



 Examples: Users
   | login                 | password             |
   | noworyta@outlook.com  | SdH3swhLbD6P6w@!@#   |
   | error@gmail.com       | SdH3swh              |
   | error                 | SdH3swhLbD           |
