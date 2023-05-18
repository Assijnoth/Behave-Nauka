import logging


# ENTER CLIENT NAME

CLIENT = "lamania.test"

# ENTER DRIVER PATH


DRIVERS = "/home/mnoworyta/Nauka/Nauka/Behave-Nauka/geckodriver"

SITE = "https://" + CLIENT + "-ecompwa.com/"


# LOG SETTINGS

LOG_DIR = "log"
LOG_FILENAME = "failed_scenarios.log"

logging.basicConfig(
    filename=LOG_DIR + "/" + LOG_FILENAME,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",)