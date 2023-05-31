Feature: DPD orders

 Background: common steps
      Given browser running
       When ordered item site
       Then adding item to cart
        And go to cart and confirm
        And complete checkout forms and confirm
        And mark DPD shipment

  Scenario: Making order with DPD and PayU Fast Payment

       And mark PayU Fast payment
       And complete checkboxes
       And confirm checkout
       And confirm payment
       And check if successpage appear
       And close test


  Scenario: Making order with DPD and PayU Card Payment
       And mark PayU Card payment
       And complete card informations
       And confirm card
       And fill checkboxes
       And confirm order
       And check if successpage status
       And finish test

