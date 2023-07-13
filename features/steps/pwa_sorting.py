import time
from settings import SITE, BROWSERS, BROWSER_NAME
import logging
import requests
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# docoelowo będziemy poszukiwać w konkretnej kategorii po konkretny produkt spełniający konkretne kryteria sortowania

SITE_TEMP = SITE + "c/kurtki-i-plaszcze"


@given('start test')
def start_test(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(6)


@when('run category site')
def run_category_site(context):
    try:
        context.driver.get(SITE_TEMP)
        try:
            time.sleep(5)
            _cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs").click()
            _page_not_found = context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Sorting returns right items          |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            pass
    except:
        logging.error("  Scenario: Sorting returns right items          |" + "   SITE NOT FOUND")
        context.driver.close()


@then('check if sorting button is active')
def check_for_sorting_button(context):
    filter_button = context.driver.find_element(By.CSS_SELECTOR, ".small > span:nth-child(2)")
    try:
        filter_button.is_displayed()
        filter_button.click()
    except NoSuchElementException:
        try:
            context.driver.implicitly_wait(3)
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Sorting returns right items          |" + "   CATEGORY SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: Sorting returns right items          |"
                          + "   NO ITEMS AND CATEGORY SITE HAVE STATUS: " + str(site_response))
            context.driver.close()


@then('sort from lowest price')
def sort_from_lowest_price(context):
    pass


@then('confirm and check results')
def confirm_and_check_results(context):
    pass


@then('finish this test')
def finish_this_test(context):
    pass


@then('sort from highest price')
def sort_from_highest_price(context):
    pass


@then('apply and verify result')
def apply_and_verify_result(context):
    pass

@then('end this test')
def end_this_test(context):
    pass