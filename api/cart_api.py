import requests
import allure
from typing import Optional
from utils.allure_helper import log_request_response

BASE_URL = "https://demowebshop.tricentis.com"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


@allure.step("Add product to cart via API (no auth)")
def add_product_to_cart(product_id: int, quantity: int = 1) -> requests.Response:
    session = requests.Session()
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    url = f"{BASE_URL}/addproducttocart/details/{product_id}/1"

    response = session.post(url, headers=HEADERS, data=payload)
    response.session = session

    log_request_response(response)
    return response


@allure.step("Add product to cart via API using cookie")
def add_product_to_cart_with_cookie(product_id: int, quantity: int, cookie: str) -> requests.Response:
    session = requests.Session()
    session.cookies.set("Nop.customer", cookie)
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    url = f"{BASE_URL}/addproducttocart/details/{product_id}/1"

    response = session.post(url, headers=HEADERS, data=payload)
    response.session = session

    log_request_response(response)
    return response


@allure.step("Extract 'Nop.customer' cookie from API response")
def get_cookie_from_api(response: requests.Response) -> Optional[str]:
    return response.session.cookies.get_dict().get("Nop.customer")
