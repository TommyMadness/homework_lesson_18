import requests
import allure
from typing import Optional

BASE_URL = "https://demowebshop.tricentis.com"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


@allure.step("Add product to cart via API (no auth)")
def add_product(product_id: int, quantity: int = 1) -> requests.Response:
    session = requests.Session()
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    response = session.post(
        f"{BASE_URL}/addproducttocart/details/{product_id}/1",
        headers=HEADERS,
        data=payload
    )
    response.session = session
    return response


@allure.step("Extract Nop.customer cookie from API response")
def get_cookie_from_api(response: requests.Response) -> Optional[str]:
    return response.session.cookies.get_dict().get("Nop.customer")


@allure.step("Add product to cart via API using cookie")
def add_product_with_cookie(product_id: int, quantity: int, cookie: str) -> requests.Response:
    session = requests.Session()
    session.cookies.set("Nop.customer", cookie)
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    response = session.post(
        f"{BASE_URL}/addproducttocart/details/{product_id}/1",
        headers=HEADERS,
        data=payload
    )
    response.session = session
    return response
