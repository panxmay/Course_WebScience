from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time

def get_country_list():
    list = []
    with open('D:\military\military\data\country\country_list.txt', 'r', encoding='utf-8') as file_obj:
        str = file_obj.readline()
        while str != "":
            list.append(str.rstrip('\n'))
            str = file_obj.readline()
    file_obj.close()
    return list

def craw_infobox_and_store(browser, country):
    dt = browser.find_elements_by_xpath("//div[@class='main-content']/div[@class='basic-info cmn-clearfix']/dl/dt")
    dd = browser.find_elements_by_xpath("//div[@class='main-content']/div[@class='basic-info cmn-clearfix']/dl/dd")
    store_as_rdf(country, dt, dd)
    store_as_property(country, dt, dd)

def store_as_rdf(country, dt, dd):
    with open('D:\military\military\data\country\\baidubaike_instance_rdf.txt', 'a', encoding='utf-8') as file_obj:
        subject = country
        for index in range(len(dt)):
            predicate = dt[index].text.replace(' ', '')
            object = dd[index].text.rstrip(' [1] ').rstrip(' [2] ').rstrip(' [3] ').rstrip(' [4] ').rstrip(' [5] ')
            file_obj.write(subject + '||' + predicate + '||' + object + '\n')
    file_obj.close()
def store_as_property(country, dt, dd):
    with open('D:\military\military\data\country\\baidubaike_instance_property.txt', 'a', encoding='utf-8') as file_obj:
        dict = {}
        dict["名称"] = country
        for index in range(len(dt)):
            predicate = dt[index].text.replace(' ', '')
            object = dd[index].text.rstrip(' [1] ').rstrip(' [2] ').rstrip(' [3] ').rstrip(' [4] ').rstrip(' [5] ')
            dict[predicate] = object
        file_obj.write(str(dict) + '\n')
    file_obj.close()
def main():
    #浏览器打开
    # chromeOptions = Options()
    # chromeOptions.add_argument('C:/Users/92898/AppData/Local/Google/Chrome/User Data/Default/extension')
    # browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://baike.baidu.com/')
    wait = WebDriverWait(browser, 10)
    list = get_country_list()
    for country in list:
        browser.find_element_by_id("query").send_keys(country)
        browser.find_element_by_id("search").click()
        time.sleep(1)
        craw_infobox_and_store(browser, country)
        time.sleep(1)
        browser.find_element_by_id("query").clear()
    extra_country = "苏联"
    browser.find_element_by_id("query").send_keys(extra_country)
    browser.find_element_by_id("search").click()
    time.sleep(1)
    craw_infobox_and_store(browser, extra_country)
    time.sleep(1)



if __name__ == "__main__":
    main()
