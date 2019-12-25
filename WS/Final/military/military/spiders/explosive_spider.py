import scrapy
import os
from military.items import ExplosiveItem
from military.items import ExplosiveItem_2

class ExplosiveSpider(scrapy.Spider):
    name = 'explosive'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.ExplosivePipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons/explosive.txt', 'r', encoding='utf-8') as file_obj:
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
        explosive_item = ExplosiveItem()
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
        develop_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="研制时间"]]/p/text()')
        guidance_system = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="制导系统"]]/p/text()')
        charge_type = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="装药类型"]]/p/text()')
        weight = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="全重"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹长"]]/p/text()')
        path =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="弹径"]]/p/text()')
        max_speed = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="最大速度"]]/p/text()')
        power_device = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="动力装置"]]/p/text()')
        fuse_device = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="引信装置"]]/p/text()')
        tail_device = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="尾翼装置"]]/p/text()')

        #验证
        explosive_item['country'] = country
        if len(pic) != 0:
            explosive_item['pic'] = pic[0].extract()
        else:
            explosive_item['pic'] = 'unknown'
        if len(description) != 0:
            explosive_item['description'] = description[0].extract()
        else:
            explosive_item['description'] = 'unknown'
        if len(alias) != 0:
            explosive_item['alias'] = alias[0].extract()
        else:
            explosive_item['alias'] = 'unknown'
        if len(category) != 0:
            explosive_item['category'] = category[0].extract()
        else:
            explosive_item['category'] = 'unknown'
        if len(name) != 0:
            explosive_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            explosive_item['name'] = name_addition[0].extract()
        else:
            explosive_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            explosive_item['manufacturer'] = manufacturer[0].extract()
        else:
            explosive_item['manufacturer'] = 'unknown'
        if len(develop_time) != 0:
            explosive_item['develop_time'] = develop_time[0].extract()
        else:
            explosive_item['develop_time'] = 'unknown'
        if len(guidance_system) != 0:
            explosive_item['guidance_system'] = guidance_system[0].extract()
        else:
            explosive_item['guidance_system'] = 'unknown'
        if len(charge_type) != 0:
            explosive_item['charge_type'] = charge_type[0].extract()
        else:
            explosive_item['charge_type'] = 'unknown'
        if len(weight) != 0:
            explosive_item['weight'] = weight[0].extract()
        else:
            explosive_item['weight'] = 'unknown'
        if len(length) != 0:
            explosive_item['length'] = length[0].extract()
        else:
            explosive_item['length'] = 'unknown'
        if len(path) != 0:
            explosive_item['path'] = path[0].extract()
        else:
            explosive_item['path'] = 'unknown'
        if len(max_speed) != 0:
            explosive_item['max_speed'] = max_speed[0].extract()
        else:
            explosive_item['max_speed'] = 'unknown'
        if len(power_device) != 0:
            explosive_item['power_device'] = power_device[0].extract()
        else:
            explosive_item['power_device'] = 'unknown'
        if len(fuse_device) != 0:
            explosive_item['fuse_device'] = fuse_device[0].extract()
        else:
            explosive_item['fuse_device'] = 'unknown'
        if len(tail_device) != 0:
            explosive_item['tail_device'] = tail_device[0].extract()
        else:
            explosive_item['tail_device'] = 'unknown'

        yield explosive_item

class ExplosiveSpider_2(scrapy.Spider):

    name = 'explosive_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.ExplosivePipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/explosive.txt', 'r', encoding='utf-8') as file_obj:
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
        explosive_item_2 = ExplosiveItem_2()
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

        RD_unit = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研发单位："]]/text()')
        develop_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研制时间："]]/text()')
        charge_type = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="装药类型："]]/text()')
        weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="全重："]]/text()')
        path = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹径："]]/b/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="弹长："]]/b/text()')
        guidance_system = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="制导系统："]]/text()')
        tail_device = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="尾翼装置："]]/text()')
        fuse_device = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="引信装置："]]/text()')
        power_device = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="动力装置："]]/text()')
        max_speed = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大速度："]]/b/text()')


        # #验证
        explosive_item_2['category'] = category
        explosive_item_2['serve_period'] = serve_period
        if len(description) != 0:
            explosive_item_2['description'] = description[0].extract().strip()
        else:
            explosive_item_2['description'] = 'unknown'
        if len(pic) != 0:
            explosive_item_2['pic'] = pic[0].extract()
        else:
            explosive_item_2['pic'] = 'unknown'
        if len(country) != 0:
            explosive_item_2['country'] = country[0].extract()
        else:
            explosive_item_2['country'] = 'unknown'
        if len(name) != 0:
            explosive_item_2['name'] = name[0].extract()
        else:
            explosive_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            explosive_item_2['full_name'] = full_name[0].extract()
        else:
            explosive_item_2['full_name'] = 'unknown'


        if len(develop_time) != 0:
            explosive_item_2['develop_time'] = develop_time[0].extract()
        else:
            explosive_item_2['develop_time'] = 'unknown'
        if len(RD_unit) != 0:
            explosive_item_2['RD_unit'] = RD_unit[0].extract()
        else:
            explosive_item_2['RD_unit'] = 'unknown'
        if len(charge_type) != 0:
            explosive_item_2['charge_type'] = charge_type[0].extract()
        else:
            explosive_item_2['charge_type'] = 'unknown'
        if len(weight) != 0:
            explosive_item_2['weight'] = weight[0].extract()
        else:
            explosive_item_2['weight'] = 'unknown'
        if len(path) != 0:
            explosive_item_2['path'] = path[0].extract()
        else:
            explosive_item_2['path'] = 'unknown'
        if len(length) != 0:
            explosive_item_2['length'] = length[0].extract()
        else:
            explosive_item_2['length'] = 'unknown'
        if len(tail_device) != 0:
            explosive_item_2['tail_device'] = tail_device[0].extract()
        else:
            explosive_item_2['tail_device'] = 'unknown'
        if len(fuse_device) != 0:
            explosive_item_2['fuse_device'] = fuse_device[0].extract()
        else:
            explosive_item_2['fuse_device'] = 'unknown'
        if len(max_speed) != 0:
            explosive_item_2['max_speed'] = max_speed[0].extract()
        else:
            explosive_item_2['max_speed'] = 'unknown'
        if len(guidance_system) != 0:
            explosive_item_2['guidance_system'] = guidance_system[0].extract()
        else:
            explosive_item_2['guidance_system'] = 'unknown'
        if len(power_device) != 0:
            explosive_item_2['power_device'] = power_device[0].extract()
        else:
            explosive_item_2['power_device'] = 'unknown'

        yield explosive_item_2
