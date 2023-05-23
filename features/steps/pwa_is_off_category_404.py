# from settings import SITE, BROWSERS, BROWSER_NAME
# import logging
# from behave import given, when, then
# from selenium.webdriver.common.by import By
# import requests
# from selenium.common.exceptions import NoSuchElementException
#
# SITE_TEMP = SITE + "c/kurtki-i-plaszcze"
#
#
# @given('run browser')
# def run_browser(context):
#     context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
#
#
# @when('open off category site')
# def open_of_category_page(context):
#     context.driver.implicitly_wait(15)
#     try:
#         context.driver.get(SITE_TEMP)
#     except:
#         logging.error("  Scenario: Is off category 404?                 |" + "   SITE NOT FOUND")
#         context.driver.close()
#
#
# # SZUKA NAPISU 404
#
#
# @then('check if 404 error will show up')
# def check_if_category_is_404(context):
#     try:
#         status = context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
#         assert status is True
#     except NoSuchElementException:
#         site_response = requests.get(SITE_TEMP, timeout=15)
#         logging.error("  Scenario: Is off category 404?                 |"
#                       + "   CATEGORY IS NOT 404 - SITE STATUS IS: " + str(site_response))
#         context.driver.close()
#
#
# @then('shutdown browser')
# def shutdown_browser(context):
#     context.driver.close()
