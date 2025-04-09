import requests
from typing import Optional
from services.allure_helper import log_request_response

BASE_URL = "https://demowebshop.tricentis.com"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded"}


def post_product_to_cart(product_id: int, quantity: int = 1) -> requests.Response:
    session = requests.Session()
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    url = f"{BASE_URL}/addproducttocart/details/{product_id}/1"

    response = session.post(url, headers=HEADERS, data=payload)
    response.session = session

    log_request_response(response)
    return response


def post_product_to_cart_with_cookie(product_id: int, quantity: int, cookie: str) -> requests.Response:
    session = requests.Session()
    session.cookies.set("Nop.customer", cookie)
    payload = {f"addtocart_{product_id}.EnteredQuantity": quantity}
    url = f"{BASE_URL}/addproducttocart/details/{product_id}/1"

    response = session.post(url, headers=HEADERS, data=payload)
    response.session = session

    log_request_response(response)
    return response


def extract_customer_cookie(response: requests.Response) -> Optional[str]:
    return response.session.cookies.get_dict().get("Nop.customer")
