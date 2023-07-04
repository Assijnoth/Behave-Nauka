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
                             for _n in range(size)])
    return random_string


login = "noworyta@outlook.com"
password = "SdH3swhLbD6P6w@!@#"
random_name = randomizer(5)
random_subname = randomizer(5)
random_email = randomizer(5) + "@gmail.com"
random_address = randomizer(5)
random_postal = "47-" + str(random.randint(100, 300))
random_city = randomizer(5)
random_phone = random.randint(100000000, 300000000)


@given('running webdrivers')
def running_webdrivers(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)


@when('visit homepage')
def visit_homepage(context):
    try:
        context.driver.get(SITE)
    except Exception:
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


@then('fill user data')
def fill_user_data(context):
    user_name = context.driver.find_elements_by_xpath("//input[@placeholder='Imię']")
    user_subname = context.driver.find_elements_by_xpath("//input[@placeholder='Nazwisko']")
    delivery_email = context.driver.find_element_by_xpath("//input[@placeholder='Email']")
    delivery_address = context.driver.find_element_by_xpath("//input[@placeholder='Adres']")
    delivery_phone = context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']")
    delivery_postal = context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']")
    delivery_city = context.driver.find_element_by_xpath("//input[@placeholder='Miasto']")
    time.sleep(1)
    try:
        user_name[0].clear()
        user_name[0].send_keys(random_name)
        user_subname[0].clear()
        user_subname[0].send_keys(random_subname)
        delivery_email.clear()
        delivery_email.send_keys(random_email)
        user_name[1].clear()
        user_name[1].send_keys(random_name)
        user_subname[1].clear()
        user_subname[1].send_keys(random_subname)
        delivery_address.clear()
        delivery_address.send_keys(random_address)
        delivery_postal.clear()
        delivery_postal.send_keys(random_postal)
        delivery_phone.clear()
        delivery_phone.send_keys(random_phone)
        delivery_city.clear()
        delivery_city.send_keys(random_address)
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing address to my account |   CANNOT FILL USER DATA")
        context.driver.close()


# aktualizuj dane.click -> refresh -> moje dane.click -> porównaj pola imię i nazwisko ze zmiennymi name i subname

@then('save it and compare')
def save_it_and_compare(context):
    try:
        _save_button_user_data = context.driver.find_element(By.CSS_SELECTOR,
                                                             "button.button-basic:nth-child(6)").click()
        _save_button_delivery_data = context.driver.find_element(By.CSS_SELECTOR,
                                                                 "button.button-basic:nth-child(11) > "
                                                                 "span:nth-child(1)").click()
        time.sleep(1)
        context.driver.refresh()
        time.sleep(1)
        _my_data = context.driver.find_element(By.CSS_SELECTOR, "div.menu-select-btn:nth-child(3) > div:nth-child(1) > "
                                                                "p:nth-child(1)").click()
        try:
            user_name = context.driver.find_elements_by_xpath("//input[@placeholder='Imię']")
            user_subname = context.driver.find_elements_by_xpath("//input[@placeholder='Nazwisko']")
            user_name_value = user_name[0].get_attribute('value')
            user_subname_value = user_subname[0].get_attribute('value')
            if user_name_value == random_name and user_subname_value == random_subname:
                pass
            else:
                logging.error("  Scenario: Adding/editing adress to my account  |   "
                              "USER DATA WAS NOT SAVED CORRECTLY (INPUT / ENTERED / SAVED): " +
                              "   NAME / " + random_name + " / " + user_name_value +
                              " ; SUBNAME / " + random_subname + " / " + user_subname_value)
                context.driver.close()
        except NoSuchElementException:
            logging.error("  Scenario: Adding/editing adress to my account  |   CAN'T GET VALUES FROM INPUTS")
            context.driver.close()
    except NoSuchElementException:
        logging.error("  Scenario: Adding/editing adress to my account  |   CANNOT SAVE USER DATA")
        context.driver.close()


@then('compare delivery data')
def compare_delivery_data(context):
    try:
        delivery_email = context.driver.find_element_by_xpath("//input[@placeholder='Email']")
        delivery_name = context.driver.find_elements_by_xpath("//input[@placeholder='Imię']")
        delivery_subname = context.driver.find_elements_by_xpath("//input[@placeholder='Nazwisko']")
        delivery_address = context.driver.find_element_by_xpath("//input[@placeholder='Adres']")
        delivery_phone = context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']")
        delivery_postal = context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']")
        delivery_city = context.driver.find_element_by_xpath("//input[@placeholder='Miasto']")
        delivery_email_value = delivery_email.get_attribute('value')
        delivery_name_value = delivery_name[1].get_attribute('value')
        delivery_subname_value = delivery_subname[1].get_attribute('value')
        delivery_address_value = delivery_address.get_attribute('value')
        delivery_phone_value = delivery_phone.get_attribute('value')
        delivery_postal_value = delivery_postal.get_attribute('value')
        delivery_city_value = delivery_city.get_attribute('value')
        if delivery_email_value == random_email and delivery_name_value == random_name \
                and delivery_subname_value == random_subname and delivery_address_value == random_address \
                and str(delivery_phone_value) == str(random_phone) and str(delivery_postal_value) == str(
            random_postal) \
                and delivery_city_value == random_address:
            pass
        else:
            logging.error("  Scenario: Adding/editing adress to my account  |   "
                          "USER DELIVERY DATA WAS NOT SAVED CORRECTLY (INPUT / ENTERED / SAVED): " +
                          "   NAME / " + random_name + " / " + delivery_name_value +
                          " ; SUBNAME / " + random_subname + " / " + delivery_subname_value +
                          " ; EMAIL / " + random_email + " / " + delivery_email_value +
                          " ; ADDRESS / " + random_address + " / " + delivery_address_value +
                          " ; PHONE / " + str(random_phone) + " / " + str(delivery_phone_value) +
                          " ; POSTAL / " + str(random_postal) + " / " + str(delivery_postal_value) +
                          " ; CITY / " + str(random_address) + " / " + str(delivery_city_value))
            context.driver.close()
    except Exception:
        context.driver.close()




@then('end that test')
def end_that_test(context):
    context.driver.close()
