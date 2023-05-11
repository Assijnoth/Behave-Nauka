# from settings import *
#
#
# @given('Check if homepage is 404')
# def get_status(context):
#     SITE_STATUS = requests.get(SITE, timeout=5)
#     MARK_AS_FAILED = False
#     if SITE_STATUS.status_code == 404:
#         logging.error("  Scenario: Is homepage 404                      |   SITE IS 404: " + SITE)
#         assert MARK_AS_FAILED is True
#     else:
#         pass
#
#
