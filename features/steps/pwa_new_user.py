from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import requests
import random

randomizer = random.randint(15000, 30000)
email = "usr" + str(randomizer) + "@gmail.com"
password = "P@s$" + str(randomizer)


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
    cache_accept = context.driver.find_element(By.CSS_SELECTOR, "button.ch2-allow-all-btn:nth-child(1)")
    try:
        cache_accept.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND CACHE PANEL "
                      + str(site_response))
        context.driver.close()


@when('open login section')
def open_login_section(context):
    my_account = context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h")
    try:
        my_account.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND LOGIN MODULE "
                      + str(site_response))
        context.driver.close()


@when('choose create account')
def choose_create_account(context):
    create_account = context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(11)")
    try:
        create_account.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   NOT FOUND CREATE USER BUTTON "
                      + str(site_response))
        context.driver.close()


@when('fill account details')
def fill_account_details(context):
    email_input = context.driver.find_element_by_xpath("//input[@placeholder='E-mail']")
    password_input = context.driver.find_element_by_xpath("//input[@placeholder='Hasło']")
    try:
        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |   CANNOT FILL NEW USER INFORMATIONS"
                      + str(site_response))
        context.driver.close()


@when('confirm consents')
def step_impl(context):
    statute_consent = context.driver.find_element(By.CSS_SELECTOR, "div.newsletter-checkbox:nth-child(9) > "
                                                                   "label:nth-child(1) > div:nth-child(1)")
    personal_data_consent = context.driver.find_element(By.CSS_SELECTOR, ".login-body > div:nth-child(10) > "
                                                                         "label:nth-child(1) > div:nth-child(1)")
    try:
        statute_consent.click()
        personal_data_consent.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()


@when('confirm creating account')
def confirm_creating_account(context):
    create_account = context.driver.find_element(By.CSS_SELECTOR,
                                                 "button.button-basic:nth-child(12) > span:nth-child(1)")
    try:
        create_account.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: I can create new user                |"
                      + "   CAN'T CONFIRM SIGNIN " + str(site_response))
        context.driver.close()


@when('check if creating account succesbox appear')
def check_if_creating_acc_is_success(context):
    creation_confirm_box = context.driver.find_element(By.CSS_SELECTOR, ".messages-container > p:nth-child(1)")
    try:
        creation_confirm_box.is_displayed()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error(
            "  Scenario: I can create new user                |   NOT FOUND CONFIRM BOX - ACCOUNT WAS NOT CREATED " +
            str(site_response))
        context.driver.close()


# .messages-container

@then('test ending')
def test_ending(context):
    context.driver.close()
