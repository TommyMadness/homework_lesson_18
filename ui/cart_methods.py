from selene import browser, have


def open_cart_with_cookie_from_api(cookie):
    browser.open('/')
    browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie})
    browser.open('/cart')


def check_cart_have_product_with_quantity(product_name, quantity):
    browser.element('.cart-item-row').should(have.text(product_name))
    browser.element('.qty-input').should(have.value(str(quantity)))


def check_exact_products_in_cart(product_1, product_2):
    rows = browser.all('.cart-item-row')

    rows.element_by(have.text(product_1))
    rows.element_by(have.text(product_2))


def cart_should_be_empty():
    browser.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


def remove_product_from_cart(product_name):
    row = browser.element('.cart-item-row').should(have.text(product_name))
    row.element('.remove-from-cart input').click()
    browser.element('input[name="updatecart"]').click()
