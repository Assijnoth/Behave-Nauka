import time
from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import random
import string


def randomizer(size):
    random_string = ''.join([random.choice(string.ascii_lowercase)
                             for _n in range(size)])
    return random_string


random_item = randomizer(6)


@given('open webdrivers')
def open_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)


@when('get homepage')
def get_homepage(context):
    try:
        context.driver.get(SITE)
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Search engine                        |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            pass
    except:
        logging.error("  Scenario: Search engine                        |" + "   SITE NOT FOUND")
        context.driver.close()


@then('go to search engine')
def go_to_search(context):
    cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs")
    search = context.driver.find_element(By.CSS_SELECTOR, "button.square-nm:nth-child(3)")
    try:
        cookies_confirm.click()
        search.click()
    except NoSuchElementException:
        logging.error("  Scenario: Search engine                        |" + "   NO SEARCH BUTTON")
        context.driver.close()


# AKTUALNIE SCENARIUSZ SZUKA PRZEDMIOTU TESTOWEGO, DOCELOWO MA OBSŁUGIWAĆ ITEM Z DUŻYM STOCKIEM Z PACZKI BASIC

@then('type a name of existing item')
def type_existing_item(context):
    search_input = context.driver.find_element_by_xpath("//input[@placeholder='Szukaj produktu...']")
    try:
        search_input.clear()
        search_input.send_keys("Paradise Blue")
        time.sleep(15)
    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: Search engine                        |"
                      + "   CAN'T FILL SEARCH BAR AND SITE IS: " + str(site_response))
        context.driver.close()


@then('check if search engine return that item')
def check_if_search_return_item(context):
    try:
        product_tile = context.driver.find_element(By.CSS_SELECTOR, ".product-card:nth-child(1) > .basic-product-tile")
        product_tile.is_displayed()
    except:
        logging.error("  Scenario: Search engine                        |"
                      + "   SEARCH ENGINE DON'T RETURN ITEMS")
        context.driver.close()


@then('shutdown webdrivers')
def shutdown_webdrivers(context):
    context.driver.close()


@then('type a random string')
def type_random_string(context):
    search_input = context.driver.find_element_by_xpath("//input[@placeholder='Szukaj produktu...']")
    try:
        search_input.clear()
        search_input.send_keys(random_item)
        time.sleep(15)
    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: Search engine                        |"
                      + "   CAN'T FILL SEARCH BAR AND SITE IS: " + str(site_response))
        context.driver.close()


@then('check if search engine return something')
def check_if_search_return_something(context):
    try:
        product_tile = context.driver.find_element(By.CSS_SELECTOR, ".product-card:nth-child(1) > .basic-product-tile")
        product_tile.is_displayed()
        logging.error("  Scenario: Search engine                        |"
                      + "   SEARCH ENGINE RETURN ITEMS FOR: " + random_item)
        context.driver.close()
    except NoSuchElementException:
        pass


@then('close webdrivers')
def close_webdrivers(context):
    context.driver.close()
