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
    tds = browser.find_elements_by_xpath("//div[@id='datamodule']/div[@class='module zoom']/table/tbody/tr/td")
    store_as_rdf(country, tds)
    store_as_property(country, tds)

def store_as_rdf(country, tds):
    with open('D:\military\military\data\country\hudongbaike_instance_rdf.txt', 'a', encoding='utf-8') as file_obj:
        subject = country
        for index in range(len(tds)):
            list = tds[index].text.split('\n')
            if len(list) == 2 :
                predicate = list[0].rstrip('：')
                object = list[1]
                file_obj.write(subject + '||' + predicate + '||' + object + '\n')
    file_obj.close()
def store_as_property(country, tds):
    with open('D:\military\military\data\country\hudongbaike_instance_property.txt', 'a', encoding='utf-8') as file_obj:
        dict = {}
        dict["名称"] = country
        for index in range(len(tds)):
            list = tds[index].text.split('\n')
            if len(list) == 2:
                predicate = list[0].rstrip("：")
                object = list[1]
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
    browser.get('http://www.baike.com/')
    wait = WebDriverWait(browser, 10)
    list = get_country_list()
    for country in list:
        browser.find_element_by_class_name("ac_input").send_keys(country)
        browser.find_element_by_class_name("entry-button").click()
        time.sleep(1)
        craw_infobox_and_store(browser, country)
        browser.back()
        time.sleep(1)
        browser.find_element_by_class_name("ac_input").clear()




if __name__ == "__main__":
    main()
