from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import random
import string
import time


def randomizer(size):
    random_string = ''.join([random.choice(string.ascii_lowercase)
        for n in range(size)])
    return random_string


login = "noworyta@outlook.com"
password = "SdH3swhLbD6P6w@!@#"
random_name = randomizer(5)
random_subname = randomizer(5)
random_email = randomizer(5)
random_address = randomizer(5)
random_postal = random.randint(10000,30000)
random_city = randomizer(5)
random_phone = randomizer(5)



@given('running webdrivers')
def running_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)


@when('visit homepage')
def visit_homepage(context):
    try:
        context.driver.get(SITE)
    except:
        logging.error("  Scenario: Adding/editing address to my account |" + "   SITE NOT FOUND")
        context.driver.close()



@then('go to login panel')
def go_to_login_panel(context):
    my_account = context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h")
    cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs")
    try:
        my_account.click()
        cookies_confirm.click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   NOT FOUND LOGIN MODULE")
        context.driver.close()

# EMAIL, PASSWORD.send_keys and zaloguj.click


@then('enter account informations')
def enter_account_informations(context):
    email_input = context.driver.find_element_by_xpath("//input[@placeholder='E-mail']")
    password_input = context.driver.find_element_by_xpath("//input[@placeholder='Hasło']")
    login_button = context.driver.find_element(By.CSS_SELECTOR, "button.btn-primary:nth-child(5) > span:nth-child(1)")
    try:
        email_input.clear()
        email_input.send_keys(login)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   NOT FOUND PASSWORD MODULE")
        context.driver.close()

# Check if LOGOUT is available


@then('check if login is correct')
def check_if_login_is_correct(context):
    try:
        logout_button = context.driver.find_element(By.CSS_SELECTOR, "div.menu-select-btn:nth-child(3)").is_displayed()
        assert logout_button is True
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   INVALID LOGIN/PASSWORD")
        context.driver.close()

# Moje dane.click


@then('go to my data')
def go_to_mydata(context):
    my_data = context.driver.find_element(By.CSS_SELECTOR, ".menu-select-btn:nth-child(3) p")
    try:
        time.sleep(2)
        my_data.click()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   NO MY DATA MODULE IN MY ACCOUNT MENU")
        context.driver.close()

# imię, nazwisko.fill  płeć.click


@then('fill user data')
def fill_user_data(context):
    user_name = context.driver.find_element_by_xpath("//input[@placeholder='Imię']")
    user_subname = context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    try:
        user_name.clear()
        user_name.send_keys(random_name)
        user_subname.clear()
        user_subname.send_keys(random_subname)
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   CANNOT FILL USER DATA")
        context.driver.close()


# aktualizuj dane.click -> refresh -> moje dane.click -> porównaj pola imię i nazwisko ze zmiennymi name i subname

@then('save it and compare')
def save_it_and_compare(context):
    user_name = context.driver.find_element_by_xpath("//input[@placeholder='Imię']")
    user_subname = context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    try:
        user_name_value = user_name.get_attribute('value')
        user_subname_value = user_subname.get_attribute('value')
        if user_name_value == random_name and user_subname_value == random_subname:
            pass
        else:
            logging.error("  Scenario: Adding/editing adress to my account  |   USER DATA WAS NOT SAVED CORRECTLY - " +
                          " ENTERED NAME WAS: " + random_name + " AND SAVED VALUE IS: " + user_name_value +
                          " ENTERED SUBNAME WAS: " + random_subname + " AND SAVED VALUE IS: " + user_subname_value)
            context.driver.close()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   CANNOT SAVE USER DATA")
        context.driver.close()


@then('fill delivery data')
def fill_delivery_data(context):
    delivery_email = context.driver.find_element_by_xpath("//input[@placeholder='Email']")
    delivery_name = context.driver.find_element_by_xpath("//input[@name='input-199']")
    delivery_subname = context.driver.find_element_by_xpath("//input[@name='input-862']")
    delivery_address = context.driver.find_element_by_xpath("//input[@placeholder='Adres']")
    delivery_phone = context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']")
    try:
        delivery_email.clear()
        delivery_email.send_keys(random_email)
        delivery_name.clear(random_name)
        delivery_name.send_keys(random_name)
        delivery_subname.clear(random_name)
        delivery_subname.send_keys(random_name)
        delivery_address.clear(random_address)
        delivery_address.send_keys(random_address)
        delivery_phone.clear()
        delivery_phone.send_keys(random_phone)
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   NOT FOUND PASSWORD MODULE")
        context.driver.close()


@then('save it and compare too')
def save_it_and_compare_too(context):
    try:
        logout_button = context.driver.find_element(By.CSS_SELECTOR, "div.menu-select-btn:nth-child(3)").is_displayed()
        assert logout_button is True
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   INVALID LOGIN/PASSWORD")
        context.driver.close()


@then('end that test')
def end_that_test(context):
    pass
