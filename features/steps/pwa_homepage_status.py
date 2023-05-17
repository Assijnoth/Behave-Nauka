# from settings import DRIVERS, SITE
# import logging
# from selenium import webdriver
# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# import requests
#
#
# @given('launch browser')
# def launch_browser(context):
#     context.driver = webdriver.Firefox(executable_path=DRIVERS)
#
#
# @when('open homepage')
# def open_homepage(context):
#     context.driver.implicitly_wait(3)
#     try:
#         context.driver.get(SITE)
#     except:
#         logging.error("  Scenario: Is homepage 200?                     |" + "   SITE NOT FOUND")
#         context.driver.close()
#
#
# @then('check if 404 error will appear')
# def check_if_homepage_is_404(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
#     except NoSuchElementException:
#         site_response = requests.get(SITE, timeout=5)
#         if site_response.status_code == 200:
#             pass
#         else:
#             logging.error("  Scenario: Is homepage 200?                     |"
#                           + "   PWA HAS NOT 404 ELEMENT, AND SITE STATUS IS " + str(site_response))
#         return True
#     logging.error("  Scenario: Is homepage 200?                     |" + "   PWA HOMEPAGE IS 404")
#     context.driver.close()
#
#
# @then('close browser')
# def close_browser(context):
#     context.driver.close()
