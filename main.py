from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto("https://services.aun.edu.eg/results/public/ar/exam-result", wait_until="networkidle")

    print("========== SELECT ==========")
    for s in page.locator("select").all():
        print(s)

    print("========== INPUT ==========")
    for i in page.locator("input").all():
        print(i)

    input("اضغط Enter للإغلاق...")

    browser.close()