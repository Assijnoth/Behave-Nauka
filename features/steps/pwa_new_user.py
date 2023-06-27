from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import time
import requests
import random
import string


randomizer = random.randint(15000,30000)
email = "avs" + str(randomizer) + "@gmail.com"
password = "@sA" + str(randomizer)



@given('launch webdrivers')
def launch_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(5)

@when('run homepage')
def run_homepage(context):
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: I can create new user                |" + "   SITE NOT FOUND")
        context.driver.close()
@when('dismiss cache')
def run_homepage(context):
    time.sleep(1)
    try:
        context.driver.find_element(By.CSS_SELECTOR, "button.ch2-allow-all-btn:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND CACHE PANEL " + str(site_response))
        context.driver.close()

# "MOJE KONTO".click
@when('open login section')
def open_login_section(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND LOGIN MODULE " + str(site_response))
        context.driver.close()

# WYBIERA OPCJĘ "UTWÓRZ KONTO"
@when('choose create account')
def choose_create_account(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(11)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND CREATE USER BUTTON " + str(site_response))
        context.driver.close()

# EMAIL I HASŁO.fill

@when('fill account details')
def fill_account_details(context):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").send_keys(email)
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys(password)
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   CANNOT FILL NEW USER INFORMATIONS" + str(site_response))
        context.driver.close()


# OBOWIĄZKOWE REGULAMINY.fill

@when('confirm consents')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.newsletter-checkbox:nth-child(9) > label:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, ".login-body > div:nth-child(10) > label:nth-child(1) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()

# ZAŁÓŻ KONTO.click

@when('confirm creating account')
def confirm_creating_account(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR,
                                    "button.button-basic:nth-child(12) > span:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |"
                      + "   CAN'T CONFIRM SIGNIN " + str(site_response))
        context.driver.close()

# DZIĘKUJEMY ZA ZAŁOŻENIE KONTA.is_displayed

@when('check if creating account succesbox appear')
def check_if_creating_acc_is_success(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".messages-container > p:nth-child(1)").is_displayed()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error(
            "  Scenario: I can create new user                |   NOT FOUND CONFIRM BOX - ACCOUNT WAS NOT CREATED " + str(site_response))
        context.driver.close()

# .messages-container
@then('test ending')
def test_ending(context):
    context.driver.close()