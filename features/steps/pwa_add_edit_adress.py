from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



@given('running webdrivers')
def running_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)

@when('visit homepage')
def visit_homepage(context):
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: Adding/editing adress to my account  |" + "   SITE NOT FOUND")
        context.driver.close()


# MOJE KONTO.click


@then('go to login panel')
def go_to_login_panel(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h").click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   NOT FOUND LOGIN MODULE")
        context.driver.close()

# EMAIL, PASSWORD.send_keys and zaloguj.click

@then('enter account informations')
def enter_account_informations(context):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").send_keys("noworyta@outlook.com")
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys("SdH3swhLbD6P6w@!@#")
        context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(5)").click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   NOT FOUND PASSWORD MODULE")
        context.driver.close()

# Check if LOGOUT is available

@then('check if login is correct')
def check_if_login_is_correct(context):
    try:
        status = context.driver.find_element(By.CSS_SELECTOR, "div.menu-select-btn:nth-child(3)").is_displayed()
        assert status is True
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   INVALID LOGIN/PASSWORD")
        context.driver.close()


@then('go to my data')
def go_to_mydata(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".menu-select-btn:nth-child(3) p").click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   NO MY DATA IN MY ACCOUNT MENU")
        context.driver.close()

@then('fill user data')
def fill_user_data(context):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").send_keys()
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys(password)
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   NOT FOUND PASSWORD MODULE")
        context.driver.close()

@then('save it and compare')
def save_it_and_compare(context):
    pass


@then('fill delivery data')
def fill_delivery_data(context):
    pass


@then('save it and compare too')
def save_it_and_compare_too(context):
    pass

@then('end that test')
def end_that_test(context):
    pass
