import logging
from selenium import webdriver


# ENTER CLIENT NAME
CLIENT = "lamania.test"

# ENTER DRIVER PATH
DRIVERS_PATH = "/home/mnoworyta/Nauka/Nauka/Behave-Nauka/drivers/geckodriver"


# ENTER BROWSER NAME (example: "Firefox", "Chrome")  - TO DO  tutaj settings local
BROWSER_NAME = "Firefox"


BROWSERS = {
    "Firefox": {"class": webdriver.Firefox, "exec_path": "/home/mnoworyta/Nauka/Nauka/Behave-Nauka/drivers/geckodriver"},
    "Safaro": {"class": webdriver.Safari, "exec_path": ""},
    "Chrome": {"class": webdriver.Chrome, "exec_path": ""}
}


SITE = "https://" + CLIENT + "-ecompwa.com/"


# LOG SETTINGS
LOG_DIR = "log"
LOG_FILENAME = "failed_scenarios.log"

logging.basicConfig(
    filename=LOG_DIR + "/" + LOG_FILENAME,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",)