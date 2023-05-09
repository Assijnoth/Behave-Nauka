# from behave import given, when, then
#
# @given ('user is on Poczta Onet website')
# def step_start_page (context):
# context.driver.get('https://poczta.onet.pl/')
#
#
# @when('user fills in the Sign In form and submits it')
# def step_set_login_in(context):
# context.driver.find_element_by_id('email').send_keys('behavetest@buziaczek.pl')
# context.driver.find_element_by_id('password').send_keys('XVUhjtHmM3BdPPm')
# context.driver.find_element_by_css_selector('button').click()
#
#
#
# @then('User can see email list')
# def step_valid_login(context):
# context.driver.save_screenshot("screenshot-login.png")
# assert context.driver.find_element_by_id('mailList-list-items')