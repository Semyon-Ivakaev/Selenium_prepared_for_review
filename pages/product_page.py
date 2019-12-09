from .locators import ButtonAddLocators
from .locators import ProductPageLocators
from .base_page import BasePage
from selenium import webdriver
import pytest

class PageObject(BasePage):
    def click_button_add(self):
        button_add = self.browser.find_element(*ButtonAddLocators.button).click()

    def should_be_alert(self):
        assert self.browser.switch_to.alert, "Alert window not found"
        
    def should_be_book_name(self):
        find_tag = self.browser.find_element(*ProductPageLocators.FIND_TAG).text
        new_text = self.browser.find_element(*ProductPageLocators.NEW_TEXT).text
        assert find_tag == new_text, "baaag"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should be"

        
