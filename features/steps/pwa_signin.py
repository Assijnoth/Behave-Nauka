# from settings import SITE, BROWSERS, BROWSER_NAME
# import logging
# from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
#
# @given('open browser')
# def open_browser(context):
#     context.driver = BROWSERS[BROWSER_NAME]["class"](executable_path=BROWSERS[BROWSER_NAME]["exec_path"])
#
#
# @when('open site homepage')
# def open_site_homepage(context):
#     context.driver.implicitly_wait(3)
#     try:
#         context.driver.get(SITE)
#     except:
#         logging.error("  Scenario: Signin with various logins           |" + "   SITE NOT FOUND")
#         context.driver.close()
#
#
# # OTWIERA ELEMENT MOJE KONTO
#
#
# @then('go to login section')
# def go_to_login(context):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element(By.CSS_SELECTOR, ".btn-icons-h").click()
#     except NoSuchElementException:
#         logging.error("  Scenario: Signin with various logins           |   NOT FOUND LOGIN MODULE")
#         context.driver.close()
#
#
# @then('enter username {login} and password {password}')
# def enter_userdata(context, login, password):
#     try:
#         context.driver.implicitly_wait(3)
#         context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").clear()
#         context.driver.find_element_by_xpath("//input[@placeholder='E-mail']").send_keys(login)
#         context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").clear()
#         context.driver.find_element_by_xpath("//input[@placeholder='Hasło']").send_keys(password)
#         context.driver.find_element(By.CSS_SELECTOR, "button.button-basic:nth-child(5)").click()
#     except NoSuchElementException:
#         logging.error("  Scenario: Signin with various logins           |   NOT FOUND PASSWORD MODULE")
#         context.driver.close()
#
# # Check if LOGOUT is available
#
#
# @then('check login {login} is success')
# def login_succespage_verify(context, login):
#     context.driver.implicitly_wait(2)
#     try:
#         status = context.driver.find_element(By.CSS_SELECTOR, "div.link:nth-child(4)").is_displayed()
#         assert status is True
#     except NoSuchElementException:
#         logging.error("  Scenario: Signin with various logins           |   INVALID LOGIN/PASSWORD FOR USER " + login)
#         context.driver.close()
#
#
# @then('close browser window')
# def close_browser_window(context):
#     context.driver.close()
