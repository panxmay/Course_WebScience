from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time

def craw_link(text, category_index):
    html = etree.HTML(text,etree.HTMLParser())
    result = html.xpath('//div[@class="search-item"]/a/@href')
    country = html.xpath('//div[@class="search-item-country"]/span/text()')
    with open(' ', 'a', encoding='utf-8') as file_obj:
        for index in range(len(result)):
            file_obj.write(result[index] + '@' + country[index])
            file_obj.write('\n')
            print(result[index] + '@' + country[index])
    file_obj.close()


def main():
    #浏览器打开
    # chromeOptions = Options()
    # chromeOptions.add_argument('C:/Users/92898/AppData/Local/Google/Chrome/User Data/Default/extension')
    # browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://wikipedia.hk.wjbk.site/baike-Category:%E8%BB%8D%E4%BA%8B%E4%BA%BA%E7%89%A9')
    wait = WebDriverWait(browser, 10)
    #类目遍历
    browser.f

if __name__ == "__main__":
    main()
