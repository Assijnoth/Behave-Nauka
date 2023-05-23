from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


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
        logging.error("  Can I add and then remove item from cart?      |" + "   SITE NOT FOUND")
        context.driver.close()

# PRÓBUJE KLIKNĄĆ W BUTTON "DODAJ DO KOSZYKA"

@then('adding item to cart')
def adding_item_to_cart(context):
    try:
        context.driver.implicitly_wait(3)
        context.driver.find_element(By.CSS_SELECTOR, ".f-grow > .btn-text").click()
    except NoSuchElementException:
        try:
            context.driver.implicitly_wait(3)
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Can I add and then remove item from cart?      |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Can I add and then remove item from cart?      |"
                          + "   CAN'T ADD ITEM TO CART " + str(site_response))
            context.driver.close()


# KLIKA W BOXA Z POTWIERDZENIEM DODANIA DO KOSZYKA, A NASTĘPNIE OTWIERA KOSZYK I PRZECHODZI DO CHECKOUT

@then('go to cart and confirm')
def go_to_cart_and_confirm(context):
    try:
        context.driver.implicitly_wait(3)
        context.driver.find_element(By.CSS_SELECTOR, ".messages-container").click()
        context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile").click()
        context.driver.find_element(By.CSS_SELECTOR, ".ch2-btn-text-xs").click()
        context.driver.find_element(By.CSS_SELECTOR, ".small").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CAN'T PROCEED TO CHECKOUT " + str(site_response))
        context.driver.close()


@then('complete checkout forms')
def step_impl(context):
    try:
        context.driver.implicitly_wait(3)
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
    except:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CAN'T FILL CHECKOUT FORMS AND SITE IS: " + str(site_response))
        context.driver.close()

@then(u'mark DPD shipment')
def step_impl(context):
    pass


@then(u'mark PayU Fast payment')
def step_impl(context):
    pass


@then(u'complete checkboxes')
def step_impl(context):
    pass


@then(u'confirm checkout')
def step_impl(context):
    pass


@then(u'confirm payment')
def step_impl(context):
    pass


@then(u'check if successpage appear')
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



