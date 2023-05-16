from settings import SITE, DRIVERS
import logging
import requests
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


SITE_TEMP = SITE + "c/akcesoria"

@given('run webdrivers')
def step_impl(context):
    context.driver = webdriver.Firefox(executable_path=DRIVERS)


@when('open active category site')
def openActiveCat(context):
    context.driver.implicitly_wait(5)
    try:
        context.driver.get(SITE_TEMP)
    except:
        logging.error("  Scenario: Is homepage 200?                     |" + "   SITE NOT FOUND")
        context.driver.close()


@then('check if enabled category return items')
def checkIfItemsAppear(context):
    try:
        context.driver.implicitly_wait(3)
        context.driver.find_element(By.CSS_SELECTOR, ".small > span:nth-child(2)").is_displayed()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        try:
            context.driver.implicitly_wait(3)
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: Does enabled category return items?  |" + "   CATEGORY SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: Does enabled category return items?  |" + "   NO ITEMS AND CATEGORY SITE HAVE STATUS: " + str(site_response))
            context.driver.close()


@then('end test')
def endTest(context):
    context.driver.close()