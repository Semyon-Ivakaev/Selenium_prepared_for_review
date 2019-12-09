from .base_page import BasePage
import time
import pytest
from selenium import webdriver
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.login_link), "Login form not found"
        
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.registr_link), "Registr form not found"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        email_input.send_keys(email)
        password1_input.send_keys(password)
        password2_input.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.BUTTON_SUBMIT).click()
        
