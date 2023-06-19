from settings import SITE, BROWSERS, BROWSER_NAME
import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import requests
import time

@given(u'browser run')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given browser run')


@when(u'go to ordered item productsite')
def step_impl(context):
    raise NotImplementedError(u'STEP: When go to ordered item productsite')


@then(u'moving item to cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then moving item to cart')


@then(u'move to cart and confirm')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then move to cart and confirm')


@then(u'complete checkout forms then confirm')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then complete checkout forms then confirm')


@then(u'mark INPOST shipment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then mark INPOST shipment')


@then(u'choose PayU Fast payment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then choose PayU Fast payment')


@then(u'confirm marketing consents')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then confirm marketing consents')


@then(u'end checkout')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then end checkout')


@then(u'complete payment on payu')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then complete payment on payu')


@then(u'see if successpage appear')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then see if successpage appear')


@then(u'test is done')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then test is done')


@then(u'choose PayU Card payment')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then choose PayU Card payment')


@then(u'fill card informations')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then fill card informations')


@then(u'fill marketing consents')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then fill marketing consents')


@then(u'checkout finish')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then checkout finish')


@then(u'see if successpage is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then see if successpage is displayed')


@then(u'test is end')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then test is end')

