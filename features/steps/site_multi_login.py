from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


LOG_DIR = "log"
LOG_FILENAME = "failed_scenarios.log"

logging.basicConfig(
    filename=LOG_DIR + "/" + LOG_FILENAME,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


#ENTER CLIENT NAME
CLIENT = "lamania.test"

#ENTER DRIVER PATH
DRIVERS = "/home/mnoworyta/Nauka/Nauka/Behave-Nauka/geckodriver"

SITE = "https://" + CLIENT + "-ecompwa.com/"

@given('launch browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox(executable_path=DRIVERS)

@when('open site')
def openHomePage(context):
    context.driver.get(SITE)

@then('go to login section')
def goToLogin(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h").click()


@then('enter username {login} and password {password}')
def enterUserdata(context, login, password):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").clear()
    context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").send_keys(login)
    context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
    context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys(password)
    context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(5)").click()



#Check if LOGOUT is available

@then('check login {login} is success')
def loginSuccespageVerify(context, login):
    context.driver.implicitly_wait(2)
    try:
        status = context.driver.find_element(By.CSS_SELECTOR, "div.link:nth-child(4)").is_displayed()
        assert status is True
    except:
        logging.error("Scenario: Testing signin with various logins   |   INVALID LOGIN/PASSWORD FOR USER " + login)
        context.driver.close()

@then('close browser')
def closeBrowser(context):
    context.driver.close()













