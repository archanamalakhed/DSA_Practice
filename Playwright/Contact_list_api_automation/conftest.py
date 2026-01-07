import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL,HEADERS

@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        context = p.request.new_context(
            base_url=BASE_URL,
            extra_http_headers=HEADERS
        )
        yield context
        context.dispose()
@pytest.fixture(scope='session')
def auth_token(api_context):
    response = api_context.post("/users/login",data={
        "email":"archanamalakhed@gmail.co",
        "password":"admin123"
    })
    assert response.status == 200,"LOGIN FAILED"
    token = response.json()["token"]
    return token

   

