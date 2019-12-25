import scrapy
import os
from military.items import CraftItem
from military.items import CraftItem_2

class CraftSpider(scrapy.Spider):
    name = 'craft'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.CraftPipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/craft.txt', 'r', encoding='utf-8') as file_obj:
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
        craft_item = CraftItem()
        #country
        country = self.dict.get(str(response.url).replace("https", "http"))
        #提取
        description = response.xpath('//div[@class="article-content"]/p/text()')
        pic = response.xpath('//div[@class="article-photo"]/a/img/@src')
        name_addition = response.xpath('//h1[@class="article-title"]/text()')
        alias =response.xpath('//div[@class="article-alias"]/text()')
        category = response.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
        name = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="名称"]]/p/text()')
        start_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="首飞时间"]]/p/text()')
        end_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="退役时间"]]/p/text()')
        RD_unit = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="研发单位"]]/p/text()')
        aerodynamic_layout = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="气动布局"]]/p/text()')
        crew = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="乘员"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="机长"]]/p/text()')
        wingspan =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="翼展"]]/p/text()')
        height = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="机高"]]/p/text()')
        weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="空重"]]/p/text()')
        velocity = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="飞行速度"]]/p/text()')
        engine = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="发动机"]]/p/text()')
        engine_num = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="发动机数量"]]/p/text()')
        max_flight_weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大起飞重量"]]/p/text()')
        max_flight_velocity = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大飞行速度"]]/p/text()')
        max_flight_distance = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大航程"]]/p/text()')

        #验证
        craft_item['country'] = country
        if len(pic) != 0:
            craft_item['pic'] = pic[0].extract()
        else:
            craft_item['pic'] = 'unknown'
        if len(description) != 0:
            craft_item['description'] = description[0].extract()
        else:
            craft_item['description'] = 'unknown'
        if len(alias) != 0:
            craft_item['alias'] = alias[0].extract()
        else:
            craft_item['alias'] = 'unknown'
        if len(category) != 0:
            craft_item['category'] = category[0].extract()
        else:
            craft_item['category'] = 'unknown'

        if len(name) != 0:
            craft_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            craft_item['name'] = name_addition[0].extract()
        else:
            craft_item['name'] = 'unknown'

        if len(start_time) != 0:
            craft_item['start_time'] = start_time[0].extract()
        else:
            craft_item['start_time'] = 'unknown'
        if len(end_time) != 0:
            craft_item['end_time'] = end_time[0].extract()
        else:
            craft_item['end_time'] = 'unknown'
        if len(RD_unit) != 0:
            craft_item['RD_unit'] = RD_unit[0].extract()
        else:
            craft_item['RD_unit'] = 'unknown'
        if len(aerodynamic_layout) != 0:
            craft_item['aerodynamic_layout'] = aerodynamic_layout[0].extract()
        else:
            craft_item['aerodynamic_layout'] = 'unknown'
        if len(crew) != 0:
            craft_item['crew'] = crew[0].extract()
        else:
            craft_item['crew'] = 'unknown'
        if len(length) != 0:
            craft_item['length'] = length[0].extract()
        else:
            craft_item['length'] = 'unknown'
        if len(wingspan) != 0:
            craft_item['wingspan'] = wingspan[0].extract()
        else:
            craft_item['wingspan'] = 'unknown'
        if len(height) != 0:
            craft_item['height'] = height[0].extract()
        else:
            craft_item['height'] = 'unknown'
        if len(weight) != 0:
            craft_item['weight'] = weight[0].extract()
        else:
            craft_item['weight'] = 'unknown'
        if len(velocity) != 0:
            craft_item['velocity'] = velocity[0].extract()
        else:
            craft_item['velocity'] = 'unknown'
        if len(engine) != 0:
            craft_item['engine'] = engine[0].extract()
        else:
            craft_item['engine'] = 'unknown'
        if len(engine_num) != 0:
            craft_item['engine_num'] = engine_num[0].extract()
        else:
            craft_item['engine_num'] = 'unknown'
        if len(max_flight_weight) != 0:
            craft_item['max_flight_weight'] = max_flight_weight[0].extract()
        else:
            craft_item['max_flight_weight'] = 'unknown'
        if len(max_flight_velocity) != 0:
            craft_item['max_flight_velocity'] = max_flight_velocity[0].extract()
        else:
            craft_item['max_flight_velocity'] = 'unknown'
        if len(max_flight_distance) != 0:
            craft_item['max_flight_distance'] = max_flight_distance[0].extract()
        else:
            craft_item['max_flight_distance'] = 'unknown'
        yield craft_item

class CraftSpider_2(scrapy.Spider):
    name = 'craft_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.CraftPipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/aircraft.txt', 'r', encoding='utf-8') as file_obj:
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
        craft_item_2 = CraftItem_2()
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
        #category and serve_period
        info = self.dict.get(str(response.url).replace("https", "http"))
        category = info.split('|',1)[0].strip()
        serve_period = info.split('|',1)[1].strip()
        full_name = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="名称："]]/text()')

        start_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="首飞时间："]]/text()')
        serve_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="服役时间："]]/text()')
        RD_unit = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研发单位："]]/text()')
        aerodynamic_layout = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="气动布局："]]/text()')
        engine_num = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="发动机数量："]]/text()')
        speed = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="飞行速度："]]/text()')
        weaponry = response.xpath('//div[@class="dataInfo"]/ul[@class="multiList"]/li/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="机长："]]/b/text()')
        height = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="机高："]]/b/text()')
        wingspan = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="翼展："]]/b/text()')
        wings_diameter = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="翼旋直径："]]/b/text()')
        empty_weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="空重："]]/b/text()')
        passenger = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="乘员："]]/text()')
        engine = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="发动机："]]/b/text()')
        max_flight_weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大起飞重量："]]/b/text()')
        max_flight_velocity = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大飞行速度："]]/b/text()')
        max_flight_distance = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大航程："]]/b/text()')

        # #验证
        craft_item_2['category'] = category
        craft_item_2['serve_period'] = serve_period
        if len(description) != 0:
            craft_item_2['description'] = description[0].extract().strip()
        else:
            craft_item_2['description'] = 'unknown'
        if len(pic) != 0:
            craft_item_2['pic'] = pic[0].extract()
        else:
            craft_item_2['pic'] = 'unknown'
        if len(country) != 0:
            craft_item_2['country'] = country[0].extract()
        else:
            craft_item_2['country'] = 'unknown'
        if len(name) != 0:
            craft_item_2['name'] = name[0].extract()
        else:
            craft_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            craft_item_2['full_name'] = full_name[0].extract()
        else:
            craft_item_2['full_name'] = 'unknown'

        if len(start_time) != 0:
            craft_item_2['start_time'] = start_time[0].extract()
        else:
            craft_item_2['start_time'] = 'unknown'
        if len(serve_time) != 0:
            craft_item_2['serve_time'] = serve_time[0].extract()
        else:
            craft_item_2['serve_time'] = 'unknown'
        if len(RD_unit) != 0:
            craft_item_2['RD_unit'] = RD_unit[0].extract()
        else:
            craft_item_2['RD_unit'] = 'unknown'
        if len(aerodynamic_layout) != 0:
            craft_item_2['aerodynamic_layout'] = aerodynamic_layout[0].extract()
        else:
            craft_item_2['aerodynamic_layout'] = 'unknown'
        if len(engine_num) != 0:
            craft_item_2['engine_num'] = engine_num[0].extract()
        else:
            craft_item_2['engine_num'] = 'unknown'
        if len(speed) != 0:
            craft_item_2['speed'] = speed[0].extract()
        else:
            craft_item_2['speed'] = 'unknown'
        if len(weaponry) != 0:
            str_weaponry = ''
            for we in weaponry:
                str_weaponry = str_weaponry + we.extract() + '@'
            craft_item_2['weaponry'] = str_weaponry
        else:
            craft_item_2['weaponry'] = 'unknown'
        if len(length) != 0:
            craft_item_2['length'] = length[0].extract()
        else:
            craft_item_2['length'] = 'unknown'
        if len(height) != 0:
            craft_item_2['height'] = height[0].extract()
        else:
            craft_item_2['height'] = 'unknown'
        if len(wingspan) != 0:
            craft_item_2['wingspan'] = wingspan[0].extract()
        else:
            craft_item_2['wingspan'] = 'unknown'
        if len(wings_diameter) != 0:
            craft_item_2['wings_diameter'] = wings_diameter[0].extract()
        else:
            craft_item_2['wings_diameter'] = 'unknown'
        if len(empty_weight) != 0:
            craft_item_2['empty_weight'] = empty_weight[0].extract()
        else:
            craft_item_2['empty_weight'] = 'unknown'
        if len(passenger) != 0:
            craft_item_2['passenger'] = passenger[0].extract()
        else:
            craft_item_2['passenger'] = 'unknown'
        if len(engine) != 0:
            craft_item_2['engine'] = engine[0].extract()
        else:
            craft_item_2['engine'] = 'unknown'
        if len(max_flight_weight) != 0:
            craft_item_2['max_flight_weight'] = max_flight_weight[0].extract()
        else:
            craft_item_2['max_flight_weight'] = 'unknown'
        if len(max_flight_velocity) != 0:
            craft_item_2['max_flight_velocity'] = max_flight_velocity[0].extract()
        else:
            craft_item_2['max_flight_velocity'] = 'unknown'
        if len(max_flight_distance) != 0:
            craft_item_2['max_flight_distance'] = max_flight_distance[0].extract()
        else:
            craft_item_2['max_flight_distance'] = 'unknown'
        yield craft_item_2
