from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time


# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA OBSŁUGIWAĆ ITEM Z DUŻYM STOCKIEM Z PACZKI BASIC


SITE_TEMP = SITE + "p/year-beige-grey-one-size"
@given('browser run')
def browser_run(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(5)


@when('go to ordered item productsite')
def go_to_productsite(context):
    try:
        context.driver.get(SITE_TEMP)
    except:
        logging.error("  Scenario: INPOST order                         |" + "   SITE NOT FOUND")
        context.driver.close()

# KLIKA W BUTTON "DODAJ DO KOSZYKA"

@then(u'moving item to cart')
def moving_item_to_cart(context):
    cart = context.driver.find_element(By.CSS_SELECTOR, ".f-grow > .btn-text")
    try:
        cart.click()
    except NoSuchElementException:
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: INPOST order                         |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: INPOST order                         |"
                          + "   CAN'T ADD ITEM TO CART " + str(site_response))
            context.driver.close()

# KLIKA W BOXA Z POTWIERDZENIEM DODANIA DO KOSZYKA, A NASTĘPNIE OTWIERA KOSZYK I PRZECHODZI DO CHECKOUT

@then('move to cart and confirm')
def move_to_cart_and_confirm(context):
    add_to_cart_confirm = context.driver.find_element(By.CSS_SELECTOR, ".messages-container")
    cart = context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile")
    cookies_confirm = context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs")
    try:
        add_to_cart_confirm.click()
        time.sleep(0.5)
        cart.click()
        time.sleep(0.5)
        cookies_confirm.click()
        time.sleep(0.5)
        context.driver.find_element(By.CSS_SELECTOR, ".small").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order                         |"
                      + "   CAN'T PROCEED TO CHECKOUT " + str(site_response))
        context.driver.close()


@then('complete checkout forms then confirm')
def complete_checkout_forms_then_confirm(context):
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
            logging.error("  Scenario: INPOST order                         |" + "   CAN'T CONFIRM FORMS AND SITE IS: "
                          + str(site_response))
            context.driver.close()
    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order                         |"
                      + "   CAN'T FILL CHECKOUT FORMS AND SITE IS: " + str(site_response))
        context.driver.close()


# WYBIERA INPOST I KLIKA W "WYBIERZ PACZKOMAT"


@then('mark INPOST shipment')
def mark_dpd_shipment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.shipping-method-tile:nth-child(5)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-xsm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: INPOST order                         |"
                          + "   CAN'T PROCEED TO PICKING INPOST DELIVERY SPOT" + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order                         |"
                      + "   CAN'T CHOOSE INPOST SHIPMENT " + str(site_response))
        context.driver.close()

# WPISUJE KOD POCZTOWY, SZUKA PACZKOMATU, WYBIERA GO I ZAPISUJE WPROWADZONE DANE

@then('fill INPOST delivery forms')
def fill_inpost_delivery_forms(context):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']").send_keys("47-400")
        try:
            context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(4) > span:nth-child(1)").click()
            try:
                context.driver.find_element(By.CSS_SELECTOR, ".arrow-wrapper").click()
                context.driver.find_element(By.CSS_SELECTOR, "li.pointer:nth-child(1) > span:nth-child(1)").click()
                context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(5) > span:nth-child(1)").click()
            except NoSuchElementException:
                site_response = requests.get(SITE, timeout=5)
                logging.error("  Scenario: INPOST order                         |"
                              + "   CAN'T PICK PARCEL LOCKER " + str(site_response))
                context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: INPOST order                         |"
                          + "   CAN'T SEARCH FOR PARCEL LOCKER " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order                         |"
                      + "   CAN'T FILL ZIP CODE IN INPOST MODULE " + str(site_response))
        context.driver.close()


# KLIKA W PRZEJDŹ DO PŁATNOŚCI

@then('proceed to picking payment methods')
def proceed_to_picking_payment_methods(context):
    try:
        time.sleep(1.5)
        context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order                         |"
                      + "   CAN'T PROCEED AFTER CHOOSING INPOST SHIPMENT " + str(site_response))
        context.driver.close()

# WYBIERA PAYU I "PRZECHODZI DO POTWIERDZENIA"


@then('choose PayU Fast payment')
def choose_payu_fast_payment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(7) > div:nth-child(1)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU FAST PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


@then('confirm marketing consents')
def confirm_marketing_consents(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()


@then('end checkout')
def end_checkout(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".btn-primary > span:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


@then('complete payment on payu')
def complete_payment_on_payu(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.button-like").click()
        context.driver.find_element(By.CSS_SELECTOR, "#formSubmit").click()
        context.driver.find_element(By.CSS_SELECTOR, "#btnLogout").click()
    except NoSuchElementException:
        logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                      + "   CAN'T CONFIRM PAYMENT ON PAYU SITE")
        context.driver.close()


# SPRAWDZA CZY WYŚWIETLA SIĘ NAPIS Z POTWIERDZENIEM ZAMÓWIENIA

@then('see if successpage appear')
def see_if_successpage_appear(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm").is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('test is done')
def test_is_done(context):
    context.driver.close()


@then('choose PayU Card payment')
def choose_payu_card(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(9) > div:nth-child(2)"
                                                     " > button:nth-child(1) > span:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY CARD)               |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


@then('fill card informations')
def fill_card_informations(context):
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
            logging.error("  Scenario: INPOST order (BY CARD)               |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU CARD PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY CARD)               |"
                      + "   CAN'T COMPLETE CARD FORMS " + str(site_response))
        context.driver.close()


@then('fill marketing consents')
def fill_marketing_consents(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY CARD)               |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()


@then('checkout finish')
def checkout_finish(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY CARD)               |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


@then('see if successpage is displayed')
def step_impl(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm").is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order (FAST PAYMENT)             |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('test is end')
def test_is_end(context):
    context.driver.close()


@then('choose COD payment')
def choose_cod_payment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(8)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: INPOST order (FAST PAYMENT)          |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU FAST PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY COD)                |"
                      + "   CAN'T CHOOSE COD " + str(site_response))
        context.driver.close()


@then('complete marketing consents')
def complete_marketing_consents(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY COD)                |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()


@then('complete checkout')
def checkout_finish(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: INPOST order (BY COD)                |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


@then('check if successpage is displayed')
def check_if_successpage_is_displayed(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm").is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: INPOST order (BY COD)                |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('test is over')
def test_is_over(context):
    context.driver.close()