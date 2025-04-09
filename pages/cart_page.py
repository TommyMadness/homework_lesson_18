from selene import browser, have

class CartPage:
    def open(self):
        browser.open('/cart')
        return self

    def should_have_product(self, product_name):
        browser.element('.cart').should(have.text(product_name))
        return self
