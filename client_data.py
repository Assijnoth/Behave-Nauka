from behave import *
import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

#ENTER CLIENT NAME

CLIENT = "lamania.test"

#ENTER DRIVER PATH
DRIVERS = "/home/mnoworyta/Nauka/Nauka/Behave-Nauka/geckodriver"



SITE = "https://" + CLIENT + "-ecompwa.com/"

#FOR TESTING
# SITE = "https://www.morele.net/p/we/"


LOG_DIR = "log"
LOG_FILENAME = "failed_scenarios.log"


logging.basicConfig(
    filename=LOG_DIR + "/" + LOG_FILENAME,
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)