from settings import DRIVERS, SITE
import logging
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



@given('launch browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox(executable_path=DRIVERS)

@when('open homepage')
def openHomepage(context):
    context.driver.implicitly_wait(5)
    context.driver.get(SITE)

@then('check if 404 error will appear')
def checkIfHomepageIs404(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
    except NoSuchElementException:
        return True
    logging.error("  Scenario: Is homepage 404?                     |" + "   HOMEPAGE IS 404")
    context.driver.close()



@then('close browser')
def closeBrowser(context):
    context.driver.close()











