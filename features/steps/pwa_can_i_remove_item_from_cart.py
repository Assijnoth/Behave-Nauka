# from settings import DRIVERS, SITE
# import logging
# from selenium import webdriver
# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import requests
#
#
# # AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA ODWIEDZIC KATEGORIĘ PACZKI BASIC
#
# SITE_TEMP = SITE + "p/test-przemke"
#
#
# @given(u'browser run')
# def browser_run(context):
#     context.driver = webdriver.Firefox(executable_path=DRIVERS)
#
#
# @when(u'open category site')
# def open_category_site(context):
#     context.driver.implicitly_wait(3)
#     try:
#         context.driver.get(SITE_TEMP)
#     except:
#         logging.error("  Scenario: Can I add item to cart?              |" + "   SITE NOT FOUND")
#         context.driver.close()
#
#
# @then(u'add item to cart')
# def add_item_to_cart(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, "button.f-grow").click()
#     except NoSuchElementException:
#         try:
#             context.driver.implicitly_wait(3)
#             context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
#             logging.error("  Scenario: Can I add item to cart?              |" + "   SITE IS 404")
#             context.driver.close()
#         except NoSuchElementException:
#             site_response = requests.get(SITE, timeout=5)
#             logging.error("  Scenario: Can I add item to cart?              |"
#                           + "   CAN'T ADD ITEM TO CART " + str(site_response))
#             context.driver.close()
#
#
# @then(u'open cart')
# def open_cart(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, ".messages-container").click()
#         context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile").click()
#     except NoSuchElementException:
#         site_response = requests.get(SITE, timeout=5)
#         logging.error("  Scenario: Can I add item to cart?              |"
#                       + "   CAN'T OPEN CART " + str(site_response))
#         context.driver.close()
#
#
# @then(u'check if item is in cart')
# def check_item_in_cart(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, ".product-tile-name").is_displayed()
#     except NoSuchElementException:
#         logging.error("  Scenario: Does enabled category return items?  |"
#                       + "   ITEM IS NOT IN CART")
#         context.driver.close()
#
#
# @then(u'browser shutdown')
# def browser_shutdown(context):
#     context.driver.close()
