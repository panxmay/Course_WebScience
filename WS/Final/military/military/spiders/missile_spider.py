import scrapy
import os
from military.items import MissileItem
from military.items import MissileItem_2

class MissileSpider(scrapy.Spider):
    name = 'missile'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.MissilePipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/missile.txt', 'r', encoding='utf-8') as file_obj:
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
        missile_item = MissileItem()
        #country
        country = self.dict.get(str(response.url).replace("https", "http"))
        #提取
        pic = response.xpath('//div[@class="article-photo"]/a/img/@src')
        description = response.xpath('//div[@class="article-content"]/p/text()')
        name_addition = response.xpath('//h1[@class="article-title"]/text()')
        alias =response.xpath('//div[@class="article-alias"]/text()')
        category = response.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
        name = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="名称"]]/p/text()')
        manufacturer = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="研发单位"]]/p/text()')
        product_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="研发时间"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹长"]]/p/text()')
        path = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹径"]]/p/text()')
        weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹重"]]/p/text()')
        wingspan = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="翼展"]]/p/text()')
        range =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="射程"]]/p/text()')
        max_speed = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大速度"]]/p/text()')
        fuse = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="引信"]]/p/text()')
        guidance_system = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="制导系统"]]/p/text()')

        #验证
        missile_item['country'] = country
        if len(pic) != 0:
            missile_item['pic'] = pic[0].extract()
        else:
            missile_item['pic'] = 'unknown'
        if len(description) != 0:
            missile_item['description'] = description[0].extract()
        else:
            missile_item['description'] = 'unknown'
        if len(alias) != 0:
            missile_item['alias'] = alias[0].extract()
        else:
            missile_item['alias'] = 'unknown'
        if len(category) != 0:
            missile_item['category'] = category[0].extract()
        else:
            missile_item['category'] = 'unknown'

        if len(name) != 0:
            missile_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            missile_item['name'] = name_addition[0].extract()
        else:
            missile_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            missile_item['manufacturer'] = manufacturer[0].extract()
        else:
            missile_item['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            missile_item['product_time'] = product_time[0].extract()
        else:
            missile_item['product_time'] = 'unknown'
        if len(length) != 0:
            missile_item['length'] = length[0].extract()
        else:
            missile_item['length'] = 'unknown'
        if len(path) != 0:
            missile_item['path'] = path[0].extract()
        else:
            missile_item['path'] = 'unknown'
        if len(weight) != 0:
            missile_item['weight'] = weight[0].extract()
        else:
            missile_item['weight'] = 'unknown'
        if len(wingspan) != 0:
            missile_item['wingspan'] = wingspan[0].extract()
        else:
            missile_item['wingspan'] = 'unknown'
        if len(range) != 0:
            missile_item['range'] = range[0].extract()
        else:
            missile_item['range'] = 'unknown'
        if len(max_speed) != 0:
            missile_item['max_speed'] = max_speed[0].extract()
        else:
            missile_item['max_speed'] = 'unknown'
        if len(fuse) != 0:
            missile_item['fuse'] = fuse[0].extract()
        else:
            missile_item['fuse'] = 'unknown'
        if len(guidance_system) != 0:
            missile_item['guidance_system'] = guidance_system[0].extract()
        else:
            missile_item['guidance_system'] = 'unknown'
        yield missile_item

class MissileSpider_2(scrapy.Spider):

    name = 'missile_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.MissilePipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/missile.txt', 'r', encoding='utf-8') as file_obj:
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
        missile_item_2 = MissileItem_2()
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

        manufacturer = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研发单位："]]/text()')
        product_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研制时间："]]/text()')
        range = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="射程："]]/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹长："]]/b/text()')
        path = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹径："]]/b/text()')
        wingspan = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="翼展："]]/b/text()')
        weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹重："]]/b/text()')
        fuse = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="引信："]]/text()')
        guidance_system = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="制导系统："]]/text()')
        max_speed = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大速度："]]/b/text()')


        # #验证
        missile_item_2['category'] = category
        missile_item_2['serve_period'] = serve_period
        if len(description) != 0:
            missile_item_2['description'] = description[0].extract().strip()
        else:
            missile_item_2['description'] = 'unknown'
        if len(pic) != 0:
            missile_item_2['pic'] = pic[0].extract()
        else:
            missile_item_2['pic'] = 'unknown'
        if len(country) != 0:
            missile_item_2['country'] = country[0].extract()
        else:
            missile_item_2['country'] = 'unknown'
        if len(name) != 0:
            missile_item_2['name'] = name[0].extract()
        else:
            missile_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            missile_item_2['full_name'] = full_name[0].extract()
        else:
            missile_item_2['full_name'] = 'unknown'


        if len(manufacturer) != 0:
            missile_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            missile_item_2['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            missile_item_2['product_time'] = product_time[0].extract()
        else:
            missile_item_2['product_time'] = 'unknown'
        if len(range) != 0:
            missile_item_2['range'] = range[0].extract()
        else:
            missile_item_2['range'] = 'unknown'
        if len(length) != 0:
            missile_item_2['length'] = length[0].extract()
        else:
            missile_item_2['length'] = 'unknown'
        if len(path) != 0:
            missile_item_2['path'] = path[0].extract()
        else:
            missile_item_2['path'] = 'unknown'
        if len(wingspan) != 0:
            missile_item_2['wingspan'] = wingspan[0].extract()
        else:
            missile_item_2['wingspan'] = 'unknown'
        if len(weight) != 0:
            missile_item_2['weight'] = weight[0].extract()
        else:
            missile_item_2['weight'] = 'unknown'
        if len(fuse) != 0:
            missile_item_2['fuse'] = fuse[0].extract()
        else:
            missile_item_2['fuse'] = 'unknown'
        if len(guidance_system) != 0:
            missile_item_2['guidance_system'] = guidance_system[0].extract()
        else:
            missile_item_2['guidance_system'] = 'unknown'
        if len(max_speed) != 0:
            missile_item_2['max_speed'] = max_speed[0].extract()
        else:
            missile_item_2['max_speed'] = 'unknown'

        yield missile_item_2
