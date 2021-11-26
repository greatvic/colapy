from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://gomedia.asia/zh/free_tarot/
    page.goto("https://gomedia.asia/zh/free_tarot/")

    # Select 財運
    page.select_option("select[name=\"category\"]", "財運")

    # Click input:has-text("洗牌")
    page.click("input:has-text(\"洗牌\")")

    # Press - with modifiers
    page.press("text=Skip to content MENU 愛情占卜 運勢占卜 免費塔羅牌占卜 免費生命靈數占卜 免費易經圖解占卜 免費星座愛情占卜 最新消息 影音分享 溫柔畫字", "Meta+-")

    # Press - with modifiers
    page.press("text=Skip to content MENU 愛情占卜 運勢占卜 免費塔羅牌占卜 免費生命靈數占卜 免費易經圖解占卜 免費星座愛情占卜 最新消息 影音分享 溫柔畫字", "Meta+-")

    # Click #cardProto81
    page.click("#cardProto81")

    # Click #cardProto80
    page.click("#cardProto80")

    # Click #cardProto79
    page.click("#cardProto79")

    # Click #cardProto78
    page.click("#cardProto78")

    # Click #cardProto77
    page.click("#cardProto77")

    # Click input:has-text("翻牌")
    page.click("input:has-text(\"翻牌\")")

    # Click input:has-text("解牌")
    page.click("input:has-text(\"解牌\")")
    time.sleep(10)
    print(page.content())
    # assert page.url == "https://gomedia.asia/zh/%E7%84%A1%E7%89%8C%E9%99%A3%E5%A1%94%E7%BE%85%E5%8D%A0%E5%8D%9C%E8%A7%A3%E7%89%8C/?card=16,18,7,43,61,&category=5&subitem=0"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
