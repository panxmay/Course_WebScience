import scrapy
import os
from military.items import TankItem
from military.items import TankItem_2

class TankSpider(scrapy.Spider):
    name = 'tank'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.TankPipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/tank.txt', 'r', encoding='utf-8') as file_obj:
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
        tank_item = TankItem()
        #country
        country = self.dict.get(str(response.url).replace("https", "http"))
        #提取
        pic = response.xpath('//div[@class="article-photo"]/a/img/@src')
        description = response.xpath('//div[@class="article-content"]/p/text()')
        name_addition = response.xpath('//h1[@class="article-title"]/text()')
        alias =response.xpath('//div[@class="article-alias"]/text()')
        category = response.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
        name = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="名称"]]/p/text()')

        manufacturer = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="研发厂商"]]/p/text()')
        product_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="诞生时间"]]/p/text()')
        chassis_type = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="底盘类型"]]/p/text()')
        num_tire_loaders = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="轮胎负重轮数量"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="车长"]]/p/text()')
        width = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="宽度"]]/p/text()')
        height =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="高度"]]/p/text()')
        crew = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="乘员与载员"]]/p/text()')
        weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="战斗全重"]]/p/text()')
        max_speed = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大速度"]]/p/text()')
        max_distance = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大行程"]]/p/text()')

        #验证
        tank_item['country'] = country
        if len(pic) != 0:
            tank_item['pic'] = pic[0].extract()
        else:
            tank_item['pic'] = 'unknown'
        if len(description) != 0:
            tank_item['description'] = description[0].extract()
        else:
            tank_item['description'] = 'unknown'
        if len(alias) != 0:
            tank_item['alias'] = alias[0].extract()
        else:
            tank_item['alias'] = 'unknown'
        if len(category) != 0:
            tank_item['category'] = category[0].extract()
        else:
            tank_item['category'] = 'unknown'
        if len(name) != 0:
            tank_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            tank_item['name'] = name_addition[0].extract()
        else:
            tank_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            tank_item['manufacturer'] = manufacturer[0].extract()
        else:
            tank_item['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            tank_item['product_time'] = product_time[0].extract()
        else:
            tank_item['product_time'] = 'unknown'
        if len(chassis_type) != 0:
            tank_item['chassis_type'] = chassis_type[0].extract()
        else:
            tank_item['chassis_type'] = 'unknown'
        if len(num_tire_loaders) != 0:
            tank_item['num_tire_loaders'] = num_tire_loaders[0].extract()
        else:
            tank_item['num_tire_loaders'] = 'unknown'
        if len(length) != 0:
            tank_item['length'] = length[0].extract()
        else:
            tank_item['length'] = 'unknown'
        if len(width) != 0:
            tank_item['width'] = width[0].extract()
        else:
            tank_item['width'] = 'unknown'
        if len(height) != 0:
            tank_item['height'] = height[0].extract()
        else:
            tank_item['height'] = 'unknown'
        if len(crew) != 0:
            tank_item['crew'] = crew[0].extract()
        else:
            tank_item['crew'] = 'unknown'
        if len(weight) != 0:
            tank_item['weight'] = weight[0].extract()
        else:
            tank_item['weight'] = 'unknown'
        if len(max_speed) != 0:
            tank_item['max_speed'] = max_speed[0].extract()
        else:
            tank_item['max_speed'] = 'unknown'
        if len(max_distance) != 0:
            tank_item['max_distance'] = max_distance[0].extract()
        else:
            tank_item['max_distance'] = 'unknown'

        yield tank_item

class TankSpider_2(scrapy.Spider):
    name = 'tank_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.TankPipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/tank.txt', 'r', encoding='utf-8') as file_obj:
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
        tank_item_2 = TankItem_2()
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

        manufacturer = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研发厂商："]]/text()')
        product_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="诞生时间："]]/text()')
        chassis_type = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="底盘类型："]]/text()')
        num_tire_loaders = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="轮胎负重轮数量："]]/text()')
        crew = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="乘员与载员："]]/b/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="车长："]]/b/text()')
        width = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="宽度："]]/b/text()')
        height = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="高度："]]/b/text()')
        weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="战斗全重："]]/b/text()')
        max_speed = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大速度："]]/b/text()')
        max_distance = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大行程："]]/b/text()')


        # #验证
        tank_item_2['category'] = category
        tank_item_2['serve_period'] = serve_period
        if len(description) != 0:
            tank_item_2['description'] = description[0].extract().strip()
        else:
            tank_item_2['description'] = 'unknown'
        if len(pic) != 0:
            tank_item_2['pic'] = pic[0].extract()
        else:
            tank_item_2['pic'] = 'unknown'
        if len(country) != 0:
            tank_item_2['country'] = country[0].extract()
        else:
            tank_item_2['country'] = 'unknown'
        if len(name) != 0:
            tank_item_2['name'] = name[0].extract()
        else:
            tank_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            tank_item_2['full_name'] = full_name[0].extract()
        else:
            tank_item_2['full_name'] = 'unknown'

        if len(manufacturer) != 0:
            tank_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            tank_item_2['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            tank_item_2['product_time'] = product_time[0].extract()
        else:
            tank_item_2['product_time'] = 'unknown'
        if len(chassis_type) != 0:
            tank_item_2['chassis_type'] = chassis_type[0].extract()
        else:
            tank_item_2['chassis_type'] = 'unknown'
        if len(num_tire_loaders) != 0:
            tank_item_2['num_tire_loaders'] = num_tire_loaders[0].extract()
        else:
            tank_item_2['num_tire_loaders'] = 'unknown'
        if len(crew) != 0:
            tank_item_2['crew'] = crew[0].extract()
        else:
            tank_item_2['crew'] = 'unknown'
        if len(length) != 0:
            tank_item_2['length'] = length[0].extract()
        else:
            tank_item_2['length'] = 'unknown'
        if len(width) != 0:
            tank_item_2['width'] = width[0].extract()
        else:
            tank_item_2['width'] = 'unknown'
        if len(height) != 0:
            tank_item_2['height'] = height[0].extract()
        else:
            tank_item_2['height'] = 'unknown'
        if len(weight) != 0:
            tank_item_2['weight'] = weight[0].extract()
        else:
            tank_item_2['weight'] = 'unknown'
        if len(max_speed) != 0:
            tank_item_2['max_speed'] = max_speed[0].extract()
        else:
            tank_item_2['max_speed'] = 'unknown'
        if len(max_distance) != 0:
            tank_item_2['max_distance'] = max_distance[0].extract()
        else:
            tank_item_2['max_distance'] = 'unknown'
        yield tank_item_2
