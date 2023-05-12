# from settings import SITE
# import logging
# import requests
# from behave import *
#
# @given('Check homepage status')
# def get_homepage_status(context):
#     site_response = requests.get(SITE, timeout=5)
#     mark_as_failed = False
#     if site_response.status_code == 200:
#         pass
#     else:
#         logging.error("  Scenario: Is homepage 200?                     |" + "   SITE STATUS IS: " + str(site_response))
#         assert mark_as_failed is True
#
#
