from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@given('open browser')
def open_browser(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)

@when('open site homepage')
def open_site_homepage(context):
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: Signin with various logins           |" + "   SITE NOT FOUND")
        context.driver.close()


# OTWIERA ELEMENT MOJE KONTO


@then('go to login section')
def go_to_login(context):
    my_account = context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h")
    try:
        my_account.click()
    except NoSuchElementException:
        logging.error("  Scenario: Signin with various logins           |   NOT FOUND LOGIN MODULE")
        context.driver.close()


@then('enter username {login} and password {password}')
def enter_userdata(context, login, password):
    email_input = context.driver.find_element_by_xpath("//input[@placeholder='E-mail']")
    password_input =  context.driver.find_element_by_xpath("//input[@placeholder='Hasło']")
    signin = context.driver.find_element(By.CSS_SELECTOR, "button.btn-primary:nth-child(5) > span:nth-child(1)")
    try:
        email_input.clear()
        email_input.send_keys(login)
        password_input.clear()
        password_input.send_keys(password)
        signin.click()
    except NoSuchElementException:
        logging.error("  Scenario: Signin with various logins           |   NOT FOUND PASSWORD MODULE")
        context.driver.close()

# Check if LOGOUT is available


@then('check login {login} is success')
def login_succespage_verify(context, login):
    try:
        logout_button = context.driver.find_element(By.CSS_SELECTOR, "div.link:nth-child(4)").is_displayed()
        assert logout_button is True
    except NoSuchElementException:
        logging.error("  Scenario: Signin with various logins           |   INVALID LOGIN/PASSWORD FOR USER " + login)
        context.driver.close()


@then('close browser window')
def close_browser_window(context):
    context.driver.close()
