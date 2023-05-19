Feature: Add item to cart
  Scenario: Can I add item to cart?
     Given running browser
      When open item site
      Then add item to cart
       And open cart
       And check if item is in cart
       And browser shutdown