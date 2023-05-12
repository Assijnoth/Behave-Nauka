# from settings import DRIVERS, SITE
# import logging
# from selenium import webdriver
# from behave import *
# from selenium.webdriver.common.by import By
#
# @given('launch browser')
# def launchBrowser(context):
#     context.driver = webdriver.Firefox(executable_path=DRIVERS)
#
# @when('open homepage')
# def openHomePage(context):
#     context.driver.get(SITE)
#
# @then('go to login section')
# def goToLogin(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h").click()
#     except:
#         logging.error("  Scenario: Signin with various logins           |   NOT FOUND LOGIN MODULE")
#         context.driver.close()
#
# @then('enter username {login} and password {password}')
# def enterUserdata(context, login, password):
#     try:
#         context.driver.implicitly_wait(3    )
#         context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").clear()
#         context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").send_keys(login)
#         context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
#         context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys(password)
#         context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(5)").click()
#     except:
#         logging.error("  Scenario: Signin with various logins           |   NOT FOUND PASSWORD MODULE")
#         context.driver.close()
#
#
# #Check if LOGOUT is available
#
# @then('check login {login} is success')
# def loginSuccespageVerify(context, login):
#     context.driver.implicitly_wait(2)
#     try:
#         status = context.driver.find_element(By.CSS_SELECTOR, "div.link:nth-child(4)").is_displayed()
#         assert status is True
#     except:
#         logging.error("  Scenario: Signin with various logins           |   INVALID LOGIN/PASSWORD FOR USER " + login)
#         context.driver.close()
#
# @then('close browser')
# def closeBrowser(context):
#     context.driver.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
