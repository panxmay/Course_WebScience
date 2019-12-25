from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time

categories = ['飞行器', '舰船舰艇', '枪械与单兵', '坦克装甲车辆', '火炮', '导弹武器', '太空装备', '爆炸物']
linkText = ['aircraft', 'warship', 'guns', 'tank', 'artillery', 'missile', 'spaceship', 'explosive']
sumPages = [111, 100, 81, 46, 45, 39, 31, 39]
def craw_link(text, category_index):
    html = etree.HTML(text,etree.HTMLParser())
    result = html.xpath('//div[@class="picList"]/ul/li/span[@class="pic"]/a/@href')
    #category and serve_period
    info = html.xpath('//div[@class="picList"]/ul/li/span[@class="category"]/text()')
    if len(result) != len(info):
        with open('../data/weapons_2/' + linkText[category_index] + '.txt', 'a', encoding='utf-8') as file_obj:
            for index in range(len(result)):
                file_obj.write('http://weapon.huanqiu.com' + result[index] + '@' + 'unknown' + '@' + 'unknown')
                file_obj.write('\n')
                print(result[index])
        file_obj.close()
    else:
        with open('../data/weapons_2/' + linkText[category_index] + '.txt', 'a', encoding='utf-8') as file_obj:
            for index in range(len(result)):
                file_obj.write('http://weapon.huanqiu.com' + result[index] + '@' + info[index])
                file_obj.write('\n')
                print(result[index])
        file_obj.close()

def main():
    #浏览器打开
    # chromeOptions = Options()
    # chromeOptions.add_argument('C:/Users/92898/AppData/Local/Google/Chrome/User Data/Default/extension')
    # browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('http://weapon.huanqiu.com/weaponlist')
    wait = WebDriverWait(browser, 10)
    #类目遍历
    for index in range(len(categories)):
        current_page = 1
        while current_page <= sumPages[index]:
            # 爬取当前页面链接
            browser.get('http://weapon.huanqiu.com/weaponlist/'+linkText[index]+'/list_0_0_0_0_'+str(current_page))
            text = browser.page_source
            craw_link(text, index)
            current_page = current_page + 1



if __name__ == "__main__":
    main()
