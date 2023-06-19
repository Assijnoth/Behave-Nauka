from settings import SITE, BROWSERS, BROWSER_NAME
import logging
import requests
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException




@given('run selenium')
def run_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])


@when('go to homepage')
def open_active_category(context):
    context.driver.implicitly_wait(5)
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: does enabled category return items?  |" + "   SITE NOT FOUND")
        context.driver.close()


# SPRAWDZA, CZY POJAWIA SIĘ ELEMENT FILTROWANIA

@then('check if homepage return items')
def check_if_item_appear(context):
    try:
        context.driver.implicitly_wait(3)
        context.driver.find_element(By.CSS_SELECTOR, ".small > span:nth-child(2)").is_displayed()
    except NoSuchElementException:

        try:
            context.driver.implicitly_wait(3)
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Does enabled category return items?  |" + "   CATEGORY SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: Does enabled category return items?  |"
                          + "   NO ITEMS AND CATEGORY SITE HAVE STATUS: " + str(site_response))
            context.driver.close()


@then('end of test')
def end_test(context):
    context.driver.close()
