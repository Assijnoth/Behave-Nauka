from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


@given('launch browser')
def launch_browser(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)


@when('open homepage')
def open_homepage(context):
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: Is homepage 200?                     |" + "   SITE NOT FOUND")
        context.driver.close()

# SZUKA NAPISU 404


@then('check if 404 error will appear')
def check_if_homepage_is_404(context):
    try:
        page_not_found = context.driver.find_element(By.CSS_SELECTOR, ".error-txt")
        page_not_found.is_displayed()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        if site_response.status_code == 200:
            pass
        else:
            logging.error("  Scenario: Is homepage 200?                     |"
                          + "   PWA HAS NOT 404 ELEMENT, AND SITE STATUS IS " + str(site_response))
        return True
    logging.error("  Scenario: Is homepage 200?                     |" + "   PWA HOMEPAGE IS 404")
    context.driver.close()


@then('close browser')
def close_browser(context):
    context.driver.close()
