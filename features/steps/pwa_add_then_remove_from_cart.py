from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests


# AKTUALNIE SCENARIUSZ DODAJE DO KOSZYKA PRZEDMIOT TESTOWY, DOCELOWO MA ODWIEDZIC KATEGORIĘ PACZKI BASIC

SITE_TEMP = SITE + "p/gaja-white-36"


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
    add_to_cart = context.driver.find_element(By.CSS_SELECTOR, "button.f-grow")
    try:
        add_to_cart.click()
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
    cart_confirm_box = context.driver.find_element(By.CSS_SELECTOR, ".messages-container")
    cart = context.driver.find_element(By.CSS_SELECTOR, ".icon-cart-mobile")
    try:
        cart_confirm_box.click()
        cart.click()
    except NoSuchElementException:
        site_response = requests.get(SITE, timeout=5)
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CAN'T OPEN CART " + str(site_response))
        context.driver.close()


@then('check if item is in cart')
def check_item_in_cart(context):
    product_tile_in_cart = context.driver.find_element(By.CSS_SELECTOR, ".product-tile-name")
    try:
        product_tile_in_cart.is_displayed()
    except NoSuchElementException:
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   ITEM IS NOT IN CART")
        context.driver.close()


@then('remove item from cart')
def remove_item(context):
    three_dots = context.driver.find_element(By.CSS_SELECTOR, ".ellipsis")
    try:
        three_dots.click()
        remove_from_cart = context.driver.find_element(By.CSS_SELECTOR, "div.basic-link:nth-child(2)")
        remove_from_cart.click()
    except NoSuchElementException:
        logging.error("  Can I add and then remove item from cart?      |"
                      + "   CANT REMOVE ITEM FROM CART")
        context.driver.close()


@then('check if item was removed from cart')
def remove_item_check(context):
    try:
        three_dots = context.driver.find_element(By.CSS_SELECTOR, ".ellipsis")
        three_dots.is_displayed()
        context.driver.close()
        logging.error("  Can I add and then remove item from cart?      | CART IS NOT EMPTY")
    except NoSuchElementException:
        pass


@then('browser shutdown')
def browser_shutdown(context):
    context.driver.close()
