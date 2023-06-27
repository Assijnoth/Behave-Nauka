from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA ODWIEDZIC KATEGORIĘ PACZKI BASIC

SITE_TEMP = SITE + "p/test-przemke"


@given('running browser')
def browser_run(context):
    context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
    context.driver.implicitly_wait(3)

@when('open item site')
def open_item_site(context):
    try:
        context.driver.get(SITE_TEMP)
    except:
        logging.error("  Can I add and then remove item from cart?      |" + "   SITE NOT FOUND")
        context.driver.close()

# PRÓBUJE KLIKNĄĆ W BUTTON "DODAJ DO KOSZYKA"


@then('add item to cart')
def add_item_to_cart(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "button.f-grow").click()
    except NoSuchElementException:
        try:
            context.driver.find_element(By.CSS_SELECTOR, ".error-txt").is_displayed()
            logging.error("  Can I add and then remove item from cart?      |" + "   SITE IS 404")
            context.driver.close()
        except NoSuchElementException:
            site_response = requests.get(SITE, timeout=5)
            logging.error("  Can I add and then remove item from cart?      |"
                          + "   CAN'T ADD ITEM TO CART " + str(site_response))
            context.driver.close()


# KLIKA W BOXA Z POTWIERDZENIEM DODANIA DO KOSZYKA, A NASTĘPNIE OTWIERA KOSZYK
@then('open cart')
def open_cart(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".messages-container").click()
        context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile").click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CAN'T OPEN CART " + str(site_response))
        context.driver.close()

# SPRAWDZA, CZY KAFELEK Z ITEMEM POJAWIŁ SIĘ W KOSZU


@then('check if item is in cart')
def check_item_in_cart(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".product-tile-name").is_displayed()
    except NoSuchElementException:
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   ITEM IS NOT IN CART")
        context.driver.close()


# SZUKA BUTTONA "..." A NASTĘPNIE BUTTONA "USUŃ"
@then('remove item from cart')
def remove_item(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, ".ellipsis").click()
    except NoSuchElementException:
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CANT REMOVE ITEM FROM CART")
        context.driver.close()
    context.driver.find_element(By.CSS_SELECTOR, "div.basic-link:nth-child(2)").click()


# SZUKA ELEMENTU "PRZENIEŚ DO ULUBIONYCH"
@then('check if item was removed from cart')
def remove_item_check(context):
    try:
        context.driver.find_element(By.CSS_SELECTOR, "div.basic-link:nth-child(1)").is_displayed()
        context.driver.close()
        logging.error("  Can I add and then remove item from cart?      |")
    except:
        pass


@then('browser shutdown')
def browser_shutdown(context):
    context.driver.close()
