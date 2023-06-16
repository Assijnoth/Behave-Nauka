from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time


# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA OBSŁUGIWAĆ ITEM Z DUŻYM STOCKIEM Z PACZKI BASIC

SITE_TEMP = SITE + "p/test-przemke"


@given('browser running')
def browser_running(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(5)


@when('ordered item site')
def ordered_item_site(context):
    try:
        context.driver.get(SITE_TEMP)
    except:
        logging.error("  Scenario: DPD order                            |" + "   SITE NOT FOUND")
        context.driver.close()

# PRÓBUJE KLIKNĄĆ W BUTTON "DODAJ DO KOSZYKA"


@then('adding item to cart')
def adding_item_to_cart(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".f-grow > .btn-text").click()
    except NoSuchElementException:
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Scenario: DPD order                            |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T ADD ITEM TO CART " + str(site_response))
            context.driver.close()


# KLIKA W BOXA Z POTWIERDZENIEM DODANIA DO KOSZYKA, A NASTĘPNIE OTWIERA KOSZYK I PRZECHODZI DO CHECKOUT

@then('go to cart and confirm')
def go_to_cart_and_confirm(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".messages-container").click()
        time.sleep(0.5)
        context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile").click()
        time.sleep(0.5)
        context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs").click()
        time.sleep(0.5)
        context.driver.find_element(By.CSS_SELECTOR, ".small").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T PROCEED TO CHECKOUT " + str(site_response))
        context.driver.close()

# UZUPEŁNIA FORMULARZE I WCISKA "PRZEJDZ DO DOSTAWY"

@then('complete checkout forms and confirm')
def complete_checkout_and_confirm(context):
    try:
        context.driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("lazelab@test.com")
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").send_keys("Tester")
        context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']").send_keys("DPD")
        context.driver.find_element_by_xpath("//input[@placeholder='Adres']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Adres']").send_keys("Sezamkowa")
        context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Kod pocztowy']").send_keys("47-400")
        context.driver.find_element_by_xpath("//input[@placeholder='Miasto']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Miasto']").send_keys("Kraków")
        context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Numer telefonu']").send_keys("123234345")
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".btn-text").click()
        except:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |" + "   CAN'T CONFIRM FORMS AND SITE IS: "
                          + str(site_response))
            context.driver.close()

    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T FILL CHECKOUT FORMS AND SITE IS: " + str(site_response))
        context.driver.close()


# WYBIERA DPD I "PRZECHODZI DO PŁATNOŚCI"


@then('mark DPD shipment')
def mark_dpd_shipment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".shipping-method-tile:nth-child(4)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T PROCEED AFTER CHOOSING DPD SHIPMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CHOOSE DPD SHIPMENT " + str(site_response))
        context.driver.close()

# WYBIERA PAYU I "PRZECHODZI DO POTWIERDZENIA"


@then('mark PayU Fast payment')
def mark_payu_fast_payment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(7) > div:nth-child(1)").click()
        try:
            time.sleep(1.5)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU FAST PAYMENT " + str(site_response))
            context.driver.close()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


# ZAZNACZA DWA PIERWSZE CHECKBOXY

@then('complete checkboxes')
def complete_checkboxes(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()

# PRZECHODZI DO PAYU SANDBOX


@then('confirm checkout')
def confirm_checkout(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".button-basic").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


# WYBIERA PŁATNOŚC BLIK -> POTWIERDZA -> LOGOUT

@then(u'confirm payment')
def confirm_payment(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.button-like").click()
        context.driver.find_element(By.CSS_SELECTOR, "#formSubmit").click()
        context.driver.find_element(By.CSS_SELECTOR, "#btnLogout").click()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CONFIRM PAYMENT ON PAYU SITE")
        context.driver.close()


# SPRAWDZA CZY WYŚWIETLA SIĘ NAPIS Z POTWIERDZENIEM ZAMÓWIENIA
@then('check if successpage appear')
def check_successpage(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "h2.mb-sm").is_displayed()
    except NoSuchElementException:
        logging.error("  Scenario: DPD order                            |"
                      + "   THERE'S NO SUCCESSPAGE AFTER PAYMENT")
        context.driver.close()


@then('close test')
def close_test(context):
    context.driver.close()


@then(u'mark PayU Card payment')
def mark_payu_card(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".mt-xsm > span:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


@then(u'complete card informations')
def step_impl(context):
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
            logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU CARD PAYMENT " + str(site_response))
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T COMPLETE CARD FORMS " + str(site_response))



@then(u'fill checkboxes')
def step_impl(context):
    pass


@then(u'confirm order')
def step_impl(context):
    pass


@then(u'check if successpage status')
def step_impl(context):
    pass


@then(u'finish test')
def step_impl(context):
    pass



