from selene import browser, have


def set_cookie_from_api_and_open_cart(cookie):
    browser.open('/')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.open('/cart')


def cart_should_have_product_with_quantity(product_name, quantity):
    browser.element('.cart-item-row').should(have.text(product_name))
    browser.element('.qty-input').should(have.value(str(quantity)))


def cart_should_have_products(product_name_1, product_name_2):
    browser.element('.cart').should(have.text(product_name_1))
    browser.element('.cart').should(have.text(product_name_2))


def cart_should_be_empty():
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def remove_product_from_cart(product_name):
    row = browser.element('.cart-item-row').should(have.text(product_name))
    row.element('.remove-from-cart input').click()
    browser.element('input[name="updatecart"]').click()
