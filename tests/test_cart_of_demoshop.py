from allure import step
from services import cart_api
from ui import cart_methods


def test_post_product_and_remove_via_ui(browser_setup):
    with step('POST /addproducttocart - add item to cart'):
        result = cart_api.post_product_to_cart(product_id=45, quantity=1)

    with step('Extract Nop.customer cookie from API session'):
        cookie = cart_api.extract_customer_cookie(result)

    with step('Open /cart with a cookie from API'):
        cart_methods.open_cart_with_cookie_from_api(cookie)

    with step('Remove product via UI'):
        cart_methods.remove_product_from_cart('Fiction')

    with step('Verify cart is empty'):
        cart_methods.cart_should_be_empty()


def test_post_product_with_large_quantity(browser_setup):
    with step('POST /addproducttocart - add item with quantity 100'):
        result = cart_api.post_product_to_cart(product_id=43, quantity=100)

    with step('Extract Nop.customer cookie from API session'):
        cookie = cart_api.extract_customer_cookie(result)

    with step('Open /cart with a cookie from API'):
        cart_methods.open_cart_with_cookie_from_api(cookie)

    with step('Verify product is in cart with quantity = 100'):
        cart_methods.check_cart_have_product_with_quantity('Smartphone', quantity=100)


def test_post_same_product_twice(browser_setup):
    with step('POST /addproducttocart - first time'):
        result = cart_api.post_product_to_cart(product_id=22, quantity=1)

    with step('Extract Nop.customer cookie from API session'):
        cookie = cart_api.extract_customer_cookie(result)

    with step('POST /addproducttocart - second time (with cookie)'):
        cart_api.post_product_to_cart_with_cookie(product_id=22, quantity=2, cookie=cookie)

    with step('Open /cart with a cookie from API'):
        cart_methods.open_cart_with_cookie_from_api(cookie)

    with step('Verify total quantity = 3'):
        cart_methods.check_cart_have_product_with_quantity('Health Book', quantity=3)


def test_post_two_products_and_check_cart(browser_setup):
    with step('POST /addproducttocart - add first product'):
        result_1 = cart_api.post_product_to_cart(product_id=31, quantity=1)

    with step('Extract Nop.customer cookie'):
        cookie = cart_api.extract_customer_cookie(result_1)

    with step('POST /addproducttocart - add second product (with same cookie)'):
        cart_api.post_product_to_cart_with_cookie(product_id=45, quantity=1, cookie=cookie)

    with step('Set cookie and open /cart'):
        cart_methods.open_cart_with_cookie_from_api(cookie)

    with step('Check both products are in cart'):
        cart_methods.check_exact_products_in_cart('Health Book', 'Fiction')

