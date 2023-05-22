Feature: Active category is visible in megamenu
  Scenario: Is active category visible?
     Given browser launch
      When homepage open
      Then open megamenu
      Then check if active category appear in megamenu
       And browser close