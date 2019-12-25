# import scrapy
# from lxml import etree
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get('http://military.china.com/weapon/aircraft/zdj/130002600/20190724/10371.html')
# wait = WebDriverWait(browser, 10)
# text = browser.page_source
# html = etree.HTML(text,etree.HTMLParser())
#
# description = html.xpath('//div[@class="article-content"]/p/text()')
# alias = html.xpath('//h1[@class="article-title"]/text()')
# category = html.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
# name = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="名称"]]/p/text()')
# start_time = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="首飞时间"]]/p/text()')
# end_time = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="退役时间"]]/p/text()')
# RD_unit = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="研发单位"]]/p/text()')
# aerodynamic_layout = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="气动布局"]]/p/text()')
# crew = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="乘员"]]/p/text()')
# length = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="机长"]]/p/text()')
# wingspan =html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="翼展"]]/p/text()')
# height = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="机高"]]/p/text()')
# weight = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="空重"]]/p/text()')
# velocity = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="飞行速度"]]/p/text()')
# engine = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="发动机"]]/p/text()')
# engine_num = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="发动机数量"]]/p/text()')
# max_flight_weight = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="最大起飞重量"]]/p/text()')
# max_flight_velocity = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="最大飞行速度"]]/p/text()')
# max_flight_distance = html.xpath('//table[@class="article-parameter-table"]/tbody/tr/td[em[text()="最大航程"]]/p/text()')
#
# print(str(name[0]))

dict={}
dict["http://military.china.com/weapon/aircraft/zdj/130002600/20190906/38591.html"] = "苏/俄"
print(dict.get("http://military.china.com/weapon/aircraft/zdj/130002600/20190906/38591.html"))

