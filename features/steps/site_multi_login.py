from behave import *
from selenium import webdriver


#ENTER CLIENT NAME
CLIENT = "lamania.test"

#ENTER DRIVER PATH
DRIVERS = "/home/mnoworyta/lazelab/nauka/behave/geckodriver"

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
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/header/nav/div[2]/button[2]/span[2]").click()

@then('enter username {login} and password {password}')
def enterUserdata(context, login, password):
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/input").clear()
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[1]/div/input").send_keys(login)
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/input").clear()
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[2]/div[2]/div/input").send_keys(password)
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div/div[2]/button[1]/span").click()

@then('check login is success')
def loginSuccespageVerify(context):
    context.driver.implicitly_wait(5)
    status = context.driver.find_element_by_xpath("/html/body/section/div/div[1]/div[2]/button[1]").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()













