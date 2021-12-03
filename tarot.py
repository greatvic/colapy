from playwright.sync_api import Playwright, sync_playwright
import time, random
from bs4 import BeautifulSoup
import pandas

def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    allcomb = []
    for i in range(3):
        for c in range(1,3):
            for s in range(0,2):
                ary = []
                for num in random.sample(range(1,79), 5):
                    ary.append(str(num))
                p = ','.join(ary)

                # Go to https://gomedia.asia/zh/free_tarot/
                page.goto("https://gomedia.asia/zh/%E7%84%A1%E7%89%8C%E9%99%A3%E5%A1%94%E7%BE%85%E5%8D%A0%E5%8D%9C%E8%A7%A3%E7%89%8C/?card={},&category={}&subitem={}".format(p, c, s))

                time.sleep(1)
                soup = BeautifulSoup(page.content(), 'lxml')
                result = soup.select_one('.text-inner.text-left > h4').text
                dic = {'cards':p, 'category': c,'subitem':s,'result':result}
                print(dic)
                allcomb.append(dic)
    df = pandas.DataFrame(allcomb)
    df.to_excel('tarot.xlsx')
    # assert page.url == "https://gomedia.asia/zh/%E7%84%A1%E7%89%8C%E9%99%A3%E5%A1%94%E7%BE%85%E5%8D%A0%E5%8D%9C%E8%A7%A3%E7%89%8C/?card=16,18,7,43,61,&category=5&subitem=0"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
