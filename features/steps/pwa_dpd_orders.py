from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time



# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA ODWIEDZIC KATEGORIĘ PACZKI BASIC

SITE_TEMP = SITE + "p/test-przemke"


@given('browser running')
def browser_running(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])


@when('ordered item site')
def ordered_item_site(context):
    context.driver.implicitly_wait(3)
    try:
        context.driver.get(SITE_TEMP)
    except:
        logging.error("  Scenario: DPD order                            |" + "   SITE NOT FOUND")
        context.driver.close()

# PRÓBUJE KLIKNĄĆ W BUTTON "DODAJ DO KOSZYKA"

@then('adding item to cart')
def adding_item_to_cart(context):
    try:
        context.driver.implicitly_wait(3)
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
        context.driver.implicitly_wait(5)
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
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element_by_xpath("//input[@placeholder='Email']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Email']").send_keys("lazelab@test.com")
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Imię']").send_keys("Tester")
        context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']").clear()
        context.driver.find_element_by_xpath("//input[@placeholder='Nazwisko']").send_keys("Testowicz")
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
            logging.error("  Scenario: DPD order                            |"
                + "   CAN'T CONFIRM FORMS AND SITE IS: " + str(site_response))

    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T FILL CHECKOUT FORMS AND SITE IS: " + str(site_response))
        context.driver.close()


# WYBIERA DPD I "PRZECHODZI DO PŁATNOŚCI"


@then('mark DPD shipment')
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element(By.CSS_SELECTOR, ".shipping-method-tile:nth-child(4)").click()
        try:
            time.sleep(2)
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
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element(By.CSS_SELECTOR, "div.payment-method-tile:nth-child(7) > div:nth-child(1)").click()
        try:
            time.sleep(2)
            context.driver.find_element(By.CSS_SELECTOR, ".mt-sm > span:nth-child(1)").click()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Scenario: DPD order                            |"
                          + "   CAN'T PROCEED AFTER CHOOSING PAYU FAST PAYMENT " + str(site_response))
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CHOOSE PAYU FAST PAYMENT " + str(site_response))
        context.driver.close()


# ZAZNACZA WYMAGANE ZGODY

@then('complete checkboxes')
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(1) > div:nth-child(1)").click()
        context.driver.find_element(By.CSS_SELECTOR, "label.pointer:nth-child(2) > div:nth-child(1)").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T CONFIRM CHECKBOXES " + str(site_response))
        context.driver.close()

# PRZECHODZI DO PAYU SANDBOX

@then('confirm checkout')
def step_impl(context):
    try:
        context.driver.implicitly_wait(2)
        context.driver.find_element(By.CSS_SELECTOR, ".button-basic").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()


# POTWIERDZA PŁATNOŚĆ W SANDBOX

@then(u'confirm payment')
def step_impl(context):
    try:
        context.driver.implicitly_wait(5)
        context.driver.find_element(By.CSS_SELECTOR, "div.button-like").click()
        context.driver.find_element(By.CSS_SELECTOR, ".formSubmit").click()   TO DOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Scenario: DPD order                            |"
                      + "   CAN'T COMPLETE CHECKOUT" + str(site_response))
        context.driver.close()



# SPRAWDZA CZY WYŚWIETLA SIĘ NAPIS Z POTWIERDZENIEM ZAMÓWIENIA

@then('check if successpage appear')
def step_impl(context):
    pass


@then(u'close test')
def step_impl(context):
    pass


@then(u'mark PayU Card payment')
def step_impl(context):
    pass


@then(u'complete card informations')
def step_impl(context):
    pass


@then(u'confirm card')
def step_impl(context):
    pass


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



