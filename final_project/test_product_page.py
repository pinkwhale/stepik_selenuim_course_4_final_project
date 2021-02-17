
from .pages.product_page import ProductPage
import pytest
import time

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

promo_urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail(reason="promo does'nt work")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

@pytest.mark.parametrize('link', promo_urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(10)
    page.should_match_product_name()
    page.should_match_product_price()

@pytest.mark.xfail(reason="expected failed")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link)
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="expected failed")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappeared()

