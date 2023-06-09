from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


# AKTUALNIE SCENARIUSZ SZUKA KATEGORII SKARPETKI - DO ZMIANY, ABY WYSZUKIWAŁ KAT. Z PACZKI BASIC


@given('browser launch')
def browser_launch(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)


@when('homepage open')
def homepage_open(context):
    try:
        context.driver.get(SITE)
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Is active category visible?          |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            pass
    except:
        logging.error("  Scenario: Is active category visible?          |" + "   SITE NOT FOUND")
        context.driver.close()


@then('open megamenu')
def browser_close(context):
    megamenu = context.driver.find_element(By.CSS_SELECTOR, ".main-controller")
    try:
        megamenu.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: Is active category visible?          |"
                      + "   PWA HOMEPAGE HAS NO MEGAMENU, AND SITE STATUS IS " + str(site_response))
        context.driver.close()


@then('check if active category appear in megamenu')
def check_category_appear(context):
    category = context.driver.find_element(By.CSS_SELECTOR, "div.mb-md:nth-child(15) > div:nth-child(2) > "
                                                            "p:nth-child(1)")
    try:
        category.is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: Is active category visible?          |"
                      + "   NO ELEMENT IN MEGAMENU")
        context.driver.close()


@then('browser close')
def browser_close(context):
    context.driver.close()
