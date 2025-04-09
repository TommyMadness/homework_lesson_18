import requests
import json
import allure


def log_request_response(response: requests.Response):
    request = response.request
    cookies = response.cookies.get_dict()
    content_type = response.headers.get("Content-Type", "")
    is_json = "application/json" in content_type

    if is_json:
        try:
            parsed = json.loads(response.text)
            formatted_response = json.dumps(parsed, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            formatted_response = "<invalid JSON>"
    else:
        formatted_response = response.text

    with allure.step("API Request"):
        allure.attach(
            name="Request URL",
            body=f"{request.method} {request.url}",
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            name="Request Payload",
            body=str(request.body or "<empty>"),
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            name="Response Status",
            body=str(response.status_code),
            attachment_type=allure.attachment_type.TEXT
        )

        allure.attach(
            name="Response Body",
            body=formatted_response,
            attachment_type=allure.attachment_type.JSON if is_json else allure.attachment_type.TEXT
        )

        allure.attach(
            name="Cookies",
            body=json.dumps(cookies, indent=2),
            attachment_type=allure.attachment_type.JSON
        )
