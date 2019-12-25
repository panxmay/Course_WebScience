import scrapy
import os
from military.items import WeaponItem
from military.items import WeaponItem_2

class WeaponSpider(scrapy.Spider):
    name = 'weapon'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.WeaponPipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/weapon.txt', 'r', encoding='utf-8') as file_obj:
        comp_url = file_obj.readline()
        while 1:
            compound = comp_url.split('@', 1)
            start_urls.insert(0, compound[0])
            dict[str(compound[0])] = compound[1].replace('\n', '')
            comp_url = file_obj.readline()
            if comp_url == '':
                break
    file_obj.close()


    def parse(self, response):
        #entity
        print(response.url)
        weapon_item = WeaponItem()
        #country
        country = self.dict.get(str(response.url).replace("https", "http"))
        #提取
        pic = response.xpath('//div[@class="article-photo"]/a/img/@src')
        description = response.xpath('//div[@class="article-content"]/p/text()')
        name_addition = response.xpath('//h1[@class="article-title"]/text()')
        alias =response.xpath('//div[@class="article-alias"]/text()')
        category = response.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
        name = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="名称"]]/p/text()')

        manufacturer = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="制造商"]]/p/text()')
        product_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="生产年限"]]/p/text()')
        war_participation = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="参战情况"]]/p/text()')
        caliber = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="口径"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="全枪长"]]/p/text()')
        weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="全枪重"]]/p/text()')
        capacity =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹匣容弹量"]]/p/text()')
        shoot_range = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="有效射程"]]/p/text()')
        shoot_speed = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="战斗射速"]]/p/text()')
        performance = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="发射性能"]]/p/text()')

        #验证
        weapon_item['country'] = country
        if len(pic) != 0:
            weapon_item['pic'] = pic[0].extract()
        else:
            weapon_item['pic'] = 'unknown'
        if len(description) != 0:
            weapon_item['description'] = description[0].extract()
        else:
            weapon_item['description'] = 'unknown'
        if len(alias) != 0:
            weapon_item['alias'] = alias[0].extract()
        else:
            weapon_item['alias'] = 'unknown'
        if len(category) != 0:
            weapon_item['category'] = category[0].extract()
        else:
            weapon_item['category'] = 'unknown'
        if len(name) != 0:
            weapon_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            weapon_item['name'] = name_addition[0].extract()
        else:
            weapon_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            weapon_item['manufacturer'] = manufacturer[0].extract()
        else:
            weapon_item['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            weapon_item['product_time'] = product_time[0].extract()
        else:
            weapon_item['product_time'] = 'unknown'
        if len(war_participation) != 0:
            weapon_item['war_participation'] = war_participation[0].extract()
        else:
            weapon_item['war_participation'] = 'unknown'
        if len(caliber) != 0:
            ca_str = ''
            for index in range(len(caliber)):
                ca_str = ca_str + caliber[index].extract() + ";"
            weapon_item['caliber'] = ca_str
        else:
            weapon_item['caliber'] = 'unknown'
        if len(length) != 0:
            weapon_item['length'] = length[0].extract()
        else:
            weapon_item['length'] = 'unknown'
        if len(weight) != 0:
            weapon_item['weight'] = weight[0].extract()
        else:
            weapon_item['weight'] = 'unknown'
        if len(capacity) != 0:
            weapon_item['capacity'] = capacity[0].extract()
        else:
            weapon_item['capacity'] = 'unknown'
        if len(shoot_range) != 0:
            weapon_item['shoot_range'] = shoot_range[0].extract()
        else:
            weapon_item['shoot_range'] = 'unknown'
        if len(shoot_speed) != 0:
            weapon_item['shoot_speed'] = shoot_speed[0].extract()
        else:
            weapon_item['shoot_speed'] = 'unknown'
        if len(performance) != 0:
            weapon_item['performance'] = performance[0].extract()
        else:
            weapon_item['performance'] = 'unknown'

        yield weapon_item

class WeaponSpider_2(scrapy.Spider):


    name = 'weapon_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.WeaponPipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/guns.txt', 'r', encoding='utf-8') as file_obj:
        comp_url = file_obj.readline()
        while 1:
            compound = comp_url.split('@', 1)
            start_urls.insert(0, compound[0])
            dict[str(compound[0])] = compound[1].replace('\n', '')
            comp_url = file_obj.readline()
            if comp_url == '':
                break
    file_obj.close()


    def parse(self, response):
        #entity
        print(response.url)
        weapon_item_2 = WeaponItem_2()
        #fundamental elements
        # picture
        pic = response.xpath('//div[@class="maxPic"]/img/@src')
        print(len(pic))
        if len(pic) != 0:
            name = response.xpath('//div[@class="maxPic"]/span[@class="name"]/text()')
            country = response.xpath('//div[@class="maxPic"]/span[@class="country"]/b/a/text()')
        else:
            #pic
            pic = response.xpath('//div[@class="dataInfo"]/img/@src')
            # name
            name = response.xpath('//div[@class="maxNoPic"]/span[@class="name"]/text()')
            # country
            country = response.xpath('//div[@class="maxNoPic"]/span[@class="country"]/b/a/text()')
        #description
        description = response.xpath('//div[@class="intron"]/div/p/text()')
        if len(description) == 0:
            description = response.xpath('//div[@class="intron"]/div/text()')
            if len(description) == 0:
                description = response.xpath('//div[@class="intron"]/div/span/text()')
                if len(description) == 0:
                    description = response.xpath('//div[@class="module"]/span/p/text()')
        #category and serve_period
        info = self.dict.get(str(response.url).replace("https", "http"))
        category = info.split('|',1)[0].strip()
        serve_period = info.split('|',1)[1].strip()
        full_name = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="名称："]]/text()')

        manufacturer = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="制造商："]]/text()')
        product_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="生产年限："]]/text()')
        caliber_1 = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="口径："]]/text()')
        caliber_2 = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="口径："]]/b/text()')
        war_participation = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="参战情况："]]/text()')
        performance = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="发射性能："]]/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="全枪长："]]/b/text()')
        weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="全枪重："]]/b/text()')
        capacity = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹匣容弹量："]]/b/text()')
        shoot_range = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="有效射程："]]/b/text()')
        shoot_speed = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="战斗射速："]]/b/text()')


        # #验证
        weapon_item_2['category'] = category
        weapon_item_2['serve_period'] = serve_period
        if len(description) != 0:
            weapon_item_2['description'] = description[0].extract().strip()
        else:
            weapon_item_2['description'] = 'unknown'
        if len(pic) != 0:
            weapon_item_2['pic'] = pic[0].extract()
        else:
            weapon_item_2['pic'] = 'unknown'
        if len(country) != 0:
            weapon_item_2['country'] = country[0].extract()
        else:
            weapon_item_2['country'] = 'unknown'
        if len(name) != 0:
            weapon_item_2['name'] = name[0].extract()
        else:
            weapon_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            weapon_item_2['full_name'] = full_name[0].extract()
        else:
            weapon_item_2['full_name'] = 'unknown'


        if len(manufacturer) != 0:
            weapon_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            weapon_item_2['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            weapon_item_2['product_time'] = product_time[0].extract()
        else:
            weapon_item_2['product_time'] = 'unknown'

        weapon_item_2['caliber'] = ''
        if len(caliber_1) != 0:
            weapon_item_2['caliber'] = caliber_1[0].extract()
        if len(caliber_2) != 0:
            if weapon_item_2['caliber'] == '':
                weapon_item_2['caliber'] = caliber_2[0].extract()
            else:
                weapon_item_2['caliber'] = weapon_item_2['caliber'] + ';' + caliber_2[0].extract()
        if len(caliber_1) == 0 & len(caliber_2) == 0:
            weapon_item_2['caliber'] = 'unknown'

        if len(war_participation) != 0:
            weapon_item_2['war_participation'] = war_participation[0].extract()
        else:
            weapon_item_2['war_participation'] = 'unknown'
        if len(performance) != 0:
            weapon_item_2['performance'] = performance[0].extract()
        else:
            weapon_item_2['performance'] = 'unknown'
        if len(length) != 0:
            weapon_item_2['length'] = length[0].extract()
        else:
            weapon_item_2['length'] = 'unknown'
        if len(weight) != 0:
            weapon_item_2['weight'] = weight[0].extract()
        else:
            weapon_item_2['weight'] = 'unknown'
        if len(capacity) != 0:
            weapon_item_2['capacity'] = capacity[0].extract()
        else:
            weapon_item_2['capacity'] = 'unknown'
        if len(shoot_range) != 0:
            weapon_item_2['shoot_range'] = shoot_range[0].extract()
        else:
            weapon_item_2['shoot_range'] = 'unknown'
        if len(shoot_speed) != 0:
            weapon_item_2['shoot_speed'] = shoot_speed[0].extract()
        else:
            weapon_item_2['shoot_speed'] = 'unknown'

        yield weapon_item_2