from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time

categories = ['飞行器', '舰船舰艇', '枪械与单兵', '坦克装甲车辆', '火炮', '导弹武器', '太空装备', '爆炸物']
linkText = ['aircraft', 'warship', 'guns', 'tank', 'artillery', 'missile', 'spaceship', 'explosive']

def craw_link(text, category_index):
    html = etree.HTML(text,etree.HTMLParser())
    result = html.xpath('//div[@class="search-item"]/a/@href')
    country = html.xpath('//div[@class="search-item-country"]/span/text()')
    if len(result) != len(country):
        with open('../data/weapons/' + linkText[category_index] + '.txt', 'a', encoding='utf-8') as file_obj:
            for index in range(len(result)):
                file_obj.write(result[index] + '@unknown')
                file_obj.write('\n')
                print(result[index] + '@unknown')
        file_obj.close()
    else:
        with open('../data/weapons/' + linkText[category_index] + '.txt', 'a', encoding='utf-8') as file_obj:
            for index in range(len(result)):
                file_obj.write(result[index] + '@' + country[index])
                file_obj.write('\n')
                print(result[index] + '@' + country[index])
        file_obj.close()



def next_page(browser):
    bt = browser.find_element_by_link_text('下一页')
    bt.click()

def switch_category(browser, current_category_index):
    if current_category_index != 0:
        bt = browser.find_element_by_link_text(categories[current_category_index])
        bt.click()
        time.sleep(1)
        bt2 = browser.find_element_by_link_text('筛选')
        bt2.click()

def main():
    #浏览器打开
    # chromeOptions = Options()
    # chromeOptions.add_argument('C:/Users/92898/AppData/Local/Google/Chrome/User Data/Default/extension')
    # browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://military.china.com/weapon/list.html')
    wait = WebDriverWait(browser, 10)
    #类目遍历
    for index in range(len(categories)):
        #类目转换
        switch_category(browser, index)
        # 获取总页数
        bt = browser.find_element_by_link_text('尾页')
        sum_page = bt.get_attribute('data-id')
        for i in range(int(sum_page)):
            # 爬取当前页面链接
            print(i)
            if i == 0:
                text = browser.page_source
                craw_link(text, index)
            # 翻页
            else:
                next_page(browser)
                text = browser.page_source
                craw_link(text, index)

if __name__ == "__main__":
    main()
