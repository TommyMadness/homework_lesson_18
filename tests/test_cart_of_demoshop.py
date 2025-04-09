from allure_commons._allure import step
from api import cart_api
from ui import cart_methods

def test_remove_product_after_adding(browser_setup):
    '''Add product then remove it (API + UI)'''
    with step('Add product'):
        result = cart_api.add_product(product_id=45, quantity=1)

    with step('Get cookie from API'):
        cookie = cart_api.get_cookie_from_api(result)

    with step('Set cookie and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Remove product from Cart via UI'):
        cart_methods.remove_product_from_cart('Fiction')

    with step('Check cart is empty'):
        cart_methods.cart_should_be_empty()


def test_add_product_with_large_quantity(browser_setup):
    '''Add large quantity of a product (API)'''
    with step('Add product'):
        result = cart_api.add_product(product_id=43, quantity=100)

    with step('Get cookie from API'):
        cookie = cart_api.get_cookie_from_api(result)

    with step('Set cookie and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check product is in cart with quantity'):
        cart_methods.cart_should_have_product_with_quantity('Smartphone', quantity=100)


def test_adding_product_multiple_times(browser_setup):
    '''Add same product twice (API)'''
    with step('Add product 1st time'):
        result = cart_api.add_product(product_id=22, quantity=1)

    with step('Get cookie from API'):
        cookie = cart_api.get_cookie_from_api(result)

    with step('Add same product again'):
        cart_api.add_product_with_cookie(product_id=22, quantity=2, cookie=cookie)

    with step('Set cookie and open Cart'):
        cart_methods.set_cookie_from_api_and_open_cart(cookie)

    with step('Check total quantity is sum'):
        cart_methods.cart_should_have_product_with_quantity('Health Book', quantity=3)

