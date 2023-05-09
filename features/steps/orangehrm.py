# from behave import *
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# site = "https://opensource-demo.orangehrmlive.com"
# drivers_loc = "/home/mnoworyta/lazelab/nauka/behave/geckodriver"
#
# @given('launch Firefox')
# def launchBrowser(context):
#     context.driver = webdriver.Firefox(executable_path=drivers_loc)
#
# @when('open orange hmr homepage')
# def openHomePage(context):
#     context.driver.get(site)
#
#
#
# @then('verify that the logo present on page')
# def verifyLogo(context):
#     context.driver.implicitly_wait(5)
#     status=context.driver.find_element_by_class_name("orangehrm-login-branding").is_displayed()
#
#     assert status is True
#
# @then('close browser')
# def closeBrowser(context):
#     context.driver.close()