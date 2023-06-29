#Feature: Inpost orders
#
# Background: common steps
#      Given browser run
#       When go to ordered item productsite
#       Then moving item to cart
#        And move to cart and confirm
#        And complete checkout forms then confirm
#        And mark INPOST shipment
#        And fill INPOST delivery forms
#        And proceed to picking payment methods
#
#  Scenario: Making order with Inpost and PayU Fast Payment
#
#       And choose PayU Fast payment
#       And confirm marketing consents
#       And end checkout
#       And complete payment on payu
#       And see if successpage appear
#       And test is done
#
#
#  Scenario: Making order with Inpost and PayU Card Payment
#       And choose PayU Card payment
#       And fill card informations
#       And fill marketing consents
#       And checkout finish
#       And see if successpage is displayed
#       And test is end
#
#
#    Scenario: Making order with Inpost and COD payment
#       And choose COD payment
#       And complete marketing consents
#       And complete checkout
#       And check if successpage is displayed
#       And test is over