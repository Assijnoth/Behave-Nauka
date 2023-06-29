from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time


# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA OBSŁUGIWAĆ ITEM Z DUŻYM STOCKIEM Z PACZKI BASIC

SITE_TEMP = SITE + "p/year-beige-grey-one-size"


@given('browser running')
def browser_running(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(5)


@when('ordered item site')
def ordered_item_site(context):
    try:
        context.driver.get(SITE_TEMP)
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: DPD order                            |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            pass
    except:
        logging.error("  Scenario: DPD order                            |" + "   SITE NOT FOUND")
        context.driver.close()


@then('adding item to cart')
def adding_item_to_cart(context):
    add_to_cart = context.driver.find_element(By.CSS_SELECTOR, ".f-grow > .btn-text")
    try:
        add_to_cart.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T ADD ITEM TO CART " + str(site_response))
        context.driver.close()


@then('go to cart and confirm')
def go_to_cart_and_confirm(context):
    cart_confirm_box = context.driver.find_element(By.CSS_SELECTOR, ".messages-container")
    cart = context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile")
    cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs")
    try:
        cart_confirm_box.click()
        time.sleep(0.5)
        cart.click()
        time.sleep(0.5)
        cookies_confirm.click()
        time.sleep(0.5)
        context.driver.find_element(By.CSS_SELECTOR, ".small").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T PROCEED TO CHECKOUT " + str(site_response))
        context.driver.close()


@then('complete checkout forms and confirm')
def complete_checkout_and_confirm(context):
    email_input = context.driver.find_element_by_xpath("//input[@placeholder='Email']")
    name_input = context.driver.find_element_by_xpath("//input[@placeholder='Imię']")
    subname_input = context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']")
    address_input = context.driver.find_element_by_xpath("//input[@placeholder='Adres']")
    postal_code_input = context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']")
    city_input = context.driver.find_element_by_xpath("//input[@placeholder='Miasto']")
    phone_input = context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']")
    try:
        email_input.clear()
        email_input.send_keys("lazelab@test.com")
        name_input.clear()
        name_input.send_keys("Tester")
        subname_input.clear()
        subname_input.send_keys("DPD")
        address_input.clear()
        address_input.send_keys("Sezamkowa")
        postal_code_input.clear()
        postal_code_input.send_keys("47-400")
        city_input.clear()
        city_input.send_keys("Kraków")
        phone_input.clear()
        phone_input.send_keys("123234345")
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".btn-text").click()
        except:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |" +
                          "   CAN'T CONFIRM FORMS AND SITE IS: " + str(site_response))
            context.driver.close()
    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T FILL CHECKOUT FORMS AND SITE IS: " + str(site_response))
        context.driver.close()

# Wybiera DPD i przechodzi do wyboru płatności

@then('mark DPD shipment')
def mark_dpd_shipment(context):
    dpd = context.driver.find_element(By.CSS_SELECTOR, ".shipping-method-tile:nth-child(4)")
    try:
        dpd.click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                          + "   CAN'T PROCEED AFTER CHOOSING DPD SHIPMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T CHOOSE DPD SHIPMENT " + str(site_response))
        context.driver.close()

# Wybiera PAYU i przechodzi do wyboru płatności

@then('mark PayU Fast payment')
def mark_payu_fast_payment(context):
    payu_method = context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(7) > div:nth-child(1)")
    try:
        payu_method.click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU FAST PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


# ZAZNACZA DWA PIERWSZE CHECKBOXY

@then('complete checkboxes')
def complete_checkboxes(context):
    statute_consent = context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)")
    personal_data_consent = context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > "
                                                                         "div:nth-child(1)")
    try:
        statute_consent.click()
        personal_data_consent.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()

# PRZECHODZI DO PAYU SANDBOX

@then('confirm checkout')
def confirm_checkout(context):
    confirm_and_pay = context.driver.find_element(By.CSS_SELECTOR, ".button-basic")
    try:
        confirm_and_pay.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()

# blik - > potwierdź -> logout / nie radzi sobie z lokalizacją w zmiennej

@then('confirm payment on payu')
def confirm_payment_payu(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.button-like").click()
        context.driver.find_element(By.CSS_SELECTOR, "#formSubmit").click()
        context.driver.find_element(By.CSS_SELECTOR, "#btnLogout").click()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T CONFIRM PAYMENT ON PAYU SITE")
        context.driver.close()


# SPRAWDZA CZY WYŚWIETLA SIĘ NAPIS Z POTWIERDZENIEM ZAMÓWIENIA
@then('check if successpage appear')
def check_successpage(context):
    thanks_for_order = context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm")
    try:
        thanks_for_order.is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('close test')
def close_test(context):
    context.driver.close()


@then('mark PayU Card payment')
def mark_payu_card(context):
    payu_card_method = context.driver.find_element(By.CSS_SELECTOR, ".mt-xsm > span:nth-child(1)")
    try:
        payu_card_method.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (BY CARD)                  |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


@then('complete card informations')
def complete_card_informations(context):
    try:
        context.driver.switch_to.frame(2)
        context.driver.find_element(By.ID, "card-number").send_keys("4444333322221111")
        context.driver.switch_to.parent_frame()
        context.driver.switch_to.frame(3)
        context.driver.find_element(By.NAME, "expDate").send_keys("12/23")
        context.driver.switch_to.parent_frame()
        context.driver.switch_to.frame(4)
        context.driver.find_element(By.NAME, "cvv").send_keys("123")
        context.driver.switch_to.parent_frame()
        context.driver.find_element(By.CSS_SELECTOR, ".button-basic:nth-child(2)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order (BY CARD)                  |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU CARD PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (BY CARD)                  |"
                      + "   CAN'T COMPLETE CARD FORMS " + str(site_response))
        context.driver.close()


@then('fill checkboxes')
def fill_checkboxes(context):
    statute_consent = context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)")
    personal_data_consent = context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > "
                                                                         "div:nth-child(1)")
    try:
        statute_consent.click()
        personal_data_consent.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (BY CARD)                  |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()


@then('finish checkout')
def finish_checkout(context):
    confirm_and_pay = context.driver.find_element(By.CSS_SELECTOR, ".button-basic")
    try:
        confirm_and_pay.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


@then('check successpage status')
def check_successpage_status(context):
    thanks_for_order = context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm")
    try:
        thanks_for_order.is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order (BY CARD)                  |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('finish test')
def finish_test(context):
    context.driver.close()
