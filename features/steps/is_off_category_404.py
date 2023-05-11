from settings import *


SITE_TEMP = SITE + "c/wyl-kategoria"


@given('Check if off category is 404')
def get_status(context):
    SITE_STATUS = requests.get(SITE_TEMP, timeout=5)
    MARK_AS_FAILED = False
    if SITE_STATUS.status_code == 404:
        logging.error("  Checking if off category is 404                |   CATEGORY SITE IS 404")
        assert MARK_AS_FAILED is True
    else:
        pass



