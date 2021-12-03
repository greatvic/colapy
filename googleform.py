from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://docs.google.com/forms/d/1wZ3yPWQywTN88m2H3Rs-vVcKQQVkmrQgzc9YYsWKsps/viewform?ts=60f392ce(wink)&edit_requested=true
    page.goto("https://docs.google.com/forms/d/1wZ3yPWQywTN88m2H3Rs-vVcKQQVkmrQgzc9YYsWKsps/viewform?ts=60f392ce(wink)&edit_requested=true")



    # Click input[type="text"]
    page.click("input[type=\"text\"]")

    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "吳")
    page.wait_for_timeout(3000)

    # Click text=幼兒姓名您的回答 >> input[type="text"]
    page.click("text=幼兒姓名您的回答 >> input[type=\"text\"]")

    # Fill text=幼兒姓名您的回答 >> input[type="text"]
    page.fill("text=幼兒姓名您的回答 >> input[type=\"text\"]", "蔡")
    page.wait_for_timeout(3000)

    # Click [aria-label="無"]
    page.click("[aria-label=\"無\"]")

    # Click [aria-label="皆無症狀"]
    page.click("[aria-label=\"皆無症狀\"]")

    # Click text=無醫院、診所就醫出入機場出入賣場/市集曾參與公眾集會(宗教/政治/學術/藝文活動宗教/政治/學術/藝文活動/開學/畢業典禮、婚喪喜慶、運動賽事等聚眾活動野生動物 >> [aria-label="無"]
    page.click("text=無醫院、診所就醫出入機場出入賣場/市集曾參與公眾集會(宗教/政治/學術/藝文活動宗教/政治/學術/藝文活動/開學/畢業典禮、婚喪喜慶、運動賽事等聚眾活動野生動物 >> [aria-label=\"無\"]")

    # Click text=無同住家人正在(居家隔離/居家檢疫/自主健康管理)家人也有發燒或呼吸道症狀朋友也有發燒或呼吸道症狀同事也有發燒或呼吸道症狀 >> [aria-label="無"]
    page.click("text=無同住家人正在(居家隔離/居家檢疫/自主健康管理)家人也有發燒或呼吸道症狀朋友也有發燒或呼吸道症狀同事也有發燒或呼吸道症狀 >> [aria-label=\"無\"]")
    page.wait_for_timeout(3000)
    # Click div[role="button"]:has-text("提交")
    # with page.expect_navigation(url="https://docs.google.com/forms/d/e/1FAIpQLScjdoxlfiguCnMNJ4_hndwPsSLxYh40kYv8Trz2D9gOqhH8EA/formResponse"):
    with page.expect_navigation():
        page.click("div[role=\"button\"]:has-text(\"提交\")")
    page.wait_for_timeout(3000)
    # assert page.url == "https://docs.google.com/forms/d/e/1FAIpQLScjdoxlfiguCnMNJ4_hndwPsSLxYh40kYv8Trz2D9gOqhH8EA/formResponse"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
