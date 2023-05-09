# from behave import *
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# site = "https://opensource-demo.orangehrmlive.com"
# drivers_loc = "/home/mnoworyta/lazelab/nauka/behave/geckodriver"
#
# @given('I launch Firefox')
# def launchBrowser(context):
#     context.driver = webdriver.Firefox(executable_path=drivers_loc)
#
#
# @when('I open OrangeHRM homepade')
# def openHomePage(context):
#      context.driver.get(site)
#
#
# @when('Enter username "{user}" and password "{pwd}"')
# def login(context, user, pwd):
#     context.driver.implicitly_wait(5)
#     context.driver.find_element_by_name("username").send_keys(user)
#     context.driver.find_element_by_name("password").send_keys(pwd)
#
#
# @when('Click on login button')
# def step_impl(context):
#     context.driver.implicitly_wait(5)
#     context.driver.find_element_by_type("submit").click()
#
#
# @then('User must succesfully login to dashboard')
# def step_impl(context):
#     pass
#
