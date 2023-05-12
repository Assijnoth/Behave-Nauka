from settings import SITE
import logging
import requests
from behave import *



# SITE_TEMP = SITE + "c/wyl-kategoria"
SITE_TEMP = "https://www.morele.net/qwe/"


@given('Check off category status')
def get_status(context):
    site_response = requests.get(SITE_TEMP, timeout=3)
    mark_as_failed = False
    if site_response.status_code == 404:
        pass
    else:
        logging.error("  Scenario: Is off category 404?           |" + "   SITE STATUS IS: " + str(site_response))
        assert mark_as_failed is True


