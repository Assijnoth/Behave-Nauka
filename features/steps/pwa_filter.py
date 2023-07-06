import time
from settings import SITE, BROWSERS, BROWSER_NAME
import logging
import requests
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# docoelowo będziemy poszukiwać w konkretnej kategorii po konkretny produkt spełniający konkretne kryteria filtrowania

SITE_TEMP = SITE + "c/kurtki-i-plaszcze"


@given('webdrivers startup')
def webdrivers_startup(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(6)


@when('go to category site')
def go_to_category_site(context):
    try:
        context.driver.get(SITE_TEMP)
        try:
            time.sleep(5)
            _cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs").click()
            _page_not_found = context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Filtering returns right items        |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            pass
    except:
        logging.error("  Scenario: Filtering returns right items        |" + "   SITE NOT FOUND")
        context.driver.close()


@then('check if filter button is active')
def check_for_filter_button(context):
    filter_button = context.driver.find_element(By.CSS_SELECTOR, ".small > span:nth-child(2)")
    try:
        filter_button.is_displayed()
        filter_button.click()
    except NoSuchElementException:
        try:
            context.driver.implicitly_wait(3)
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Filtering returns right items        |" + "   CATEGORY SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: Filtering returns right items        |"
                          + "   NO ITEMS AND CATEGORY SITE HAVE STATUS: " + str(site_response))
            context.driver.close()


@then('apply price filter')
def apply_price_filter(context):
    _price_filter_button = context.driver.find_element(By.CSS_SELECTOR, "div.accordion:nth-child(2) > div:nth-child(1)"
                                                                        " > div:nth-child(1)").click()
    try:
        price_from_input = context.driver.find_element(By.CSS_SELECTOR, "div.range-input-wrapper:nth-child(1) "
                                                                        "> input:nth-child(1)")
        price_to_input = context.driver.find_element(By.CSS_SELECTOR, "div.range-input-wrapper:nth-child(2) "
                                                                      "> input:nth-child(1)")
        price_to_input.clear()
        price_to_input.send_keys(1050)
        price_from_input.send_keys(1000)
    except NoSuchElementException:
        logging.error("  Scenario: Filtering returns right items        |"
                      + "   CAN'T FILL PRICE FILTER INPUT'S")
        context.driver.close()


@then('apply size filter')
def apply_size_filter(context):
    try:
        size_filter_button = context.driver.find_element(By.CSS_SELECTOR,
                                                         "div.accordion:nth-child(3) > div:nth-child(1) >"
                                                         " div:nth-child(1) > div:nth-child(1) > p:nth-child(1)")
        size_filter_button.click()
        try:
            choose_size = context.driver.find_element(By.CSS_SELECTOR,
                                                      "div.single-simple-text-sample:nth-child(6)")
            choose_size.click()
        except NoSuchElementException:
            logging.error("  Scenario: Filtering returns right items        |"
                          + "   CAN'T PICK SIZE FILTER")
            context.driver.close()
    except NoSuchElementException:
        logging.error("  Scenario: Filtering returns right items        |"
                      + "   CAN'T CHOOSE SIZE")
        context.driver.close()


@then('apply color filter')
def step_impl(context):
    try:
        color_filter_button = context.driver.find_element(By.CSS_SELECTOR,
                                                          "div.accordion:nth-child(4) > div:nth-child(1) > "
                                                          "div:nth-child(1) > div:nth-child(1) > p:nth-child(1)")
        color_filter_button.click()
        try:
            choose_color = context.driver.find_element(By.CSS_SELECTOR,
                                                       "div.swatch-sample:nth-child(8) > div:nth-child(1) >"
                                                       " span:nth-child(1)")
            choose_color.click()
        except NoSuchElementException:
            logging.error("  Scenario: Filtering returns right items        |"
                          + "   CAN'T PICK COLOR FILTER")
            context.driver.close()
    except NoSuchElementException:
        logging.error("  Scenario: Filtering returns right items        |"
                      + "   CAN'T CHOOSE COLOR")
        context.driver.close()


@then('confirm filter and check results')
def step_impl(context):
    try:
        confirm_button = context.driver.find_element(By.CSS_SELECTOR,
                                                     "button.btn-primary:nth-child(1) > span:nth-child(1)")
        confirm_button.click()
        try:

        except NoSuchElementException:
            logging.error("  Scenario: Filtering returns right items        |"
                          + "   CAN'T PICK COLOR FILTER")
            context.driver.close()
    except NoSuchElementException:
        logging.error("  Scenario: Filtering returns right items        |"
                      + "   CAN'T CHOOSE COLOR")
        context.driver.close()


@then('finalize the test')
def end_test(context):
    context.driver.close()
