from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    basket_button = (By.CSS_SELECTOR, "span a.btn.btn-default")
    
class LoginPageLocators():
    login_link = (By.CSS_SELECTOR, "#login_form")
    registr_link = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.ID, "id_registration-email")
    PASSWORD1 = (By.ID, "id_registration-password1")
    PASSWORD2 = (By.ID, "id_registration-password2")
    BUTTON_SUBMIT = (By.NAME, "registration_submit")

class ButtonAddLocators():
    button = (By.CSS_SELECTOR, "#add_to_basket_form button")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    FIND_TAG = (By.TAG_NAME, "h1")
    NEW_TEXT = (By.CSS_SELECTOR, "div#messages div.alertinner > strong:nth-child(1)")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
    ALERT = (By.CSS_SELECTOR, "div#content_inner p")
