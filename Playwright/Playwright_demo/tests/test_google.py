import re
from playwright.sync_api import expect
def test_google_search(page):
    page.wait_for_timeout(3000)
    page.goto("https://www.google.com/ncr")
    try:
        page.get_by_role("button",name = "Accept all").click(timeout=3000)
    except:
        print("NO POPUP")
    page.get_by_role("combobox",name="Search").fill("Playwright")
    page.wait_for_timeout(4000)   # waits 2 seconds
    page.keyboard.press("Enter")
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))
    
