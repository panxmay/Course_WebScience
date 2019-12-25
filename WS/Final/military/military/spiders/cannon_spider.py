import scrapy
import json
from military.items import CannonItem
from military.items import CannonItem_2

class CannonSpider(scrapy.Spider):
    name = 'cannon'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.CannonPipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/cannon.txt', 'r', encoding='utf-8') as file_obj:
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
        cannon_item = CannonItem()
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
        cannon_item['country'] = country
        if len(pic) != 0:
            cannon_item['pic'] = pic[0].extract()
        else:
            cannon_item['pic'] = 'unknown'
        if len(description) != 0:
            cannon_item['description'] = description[0].extract()
        else:
            cannon_item['description'] = 'unknown'
        if len(alias) != 0:
            cannon_item['alias'] = alias[0].extract()
        else:
            cannon_item['alias'] = 'unknown'
        if len(category) != 0:
            cannon_item['category'] = category[0].extract()
        else:
            cannon_item['category'] = 'unknown'
        if len(name) != 0:
            cannon_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            cannon_item['name'] = name_addition[0].extract()
        else:
            cannon_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            cannon_item['manufacturer'] = manufacturer[0].extract()
        else:
            cannon_item['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            cannon_item['product_time'] = product_time[0].extract()
        else:
            cannon_item['product_time'] = 'unknown'
        if len(chassis_type) != 0:
            cannon_item['chassis_type'] = chassis_type[0].extract()
        else:
            cannon_item['chassis_type'] = 'unknown'
        if len(num_tire_loaders) != 0:
            cannon_item['num_tire_loaders'] = num_tire_loaders[0].extract()
        else:
            cannon_item['num_tire_loaders'] = 'unknown'
        if len(length) != 0:
            cannon_item['length'] = length[0].extract()
        else:
            cannon_item['length'] = 'unknown'
        if len(width) != 0:
            cannon_item['width'] = width[0].extract()
        else:
            cannon_item['width'] = 'unknown'
        if len(height) != 0:
            cannon_item['height'] = height[0].extract()
        else:
            cannon_item['height'] = 'unknown'
        if len(crew) != 0:
            cannon_item['crew'] = crew[0].extract()
        else:
            cannon_item['crew'] = 'unknown'
        if len(weight) != 0:
            cannon_item['weight'] = weight[0].extract()
        else:
            cannon_item['weight'] = 'unknown'
        if len(max_speed) != 0:
            cannon_item['max_speed'] = max_speed[0].extract()
        else:
            cannon_item['max_speed'] = 'unknown'
        if len(max_distance) != 0:
            cannon_item['max_distance'] = max_distance[0].extract()
        else:
            cannon_item['max_distance'] = 'unknown'

        yield cannon_item

class CannonSpider_2(scrapy.Spider):

    name = 'cannon_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.CannonPipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/artillery.txt', 'r', encoding='utf-8') as file_obj:
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
        cannon_item_2 = CannonItem_2()
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
        product_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="研发时间："]]/text()')
        caliber_1 = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="口径："]]/text()')
        caliber_2 = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="口径："]]/b/text()')
        cannon_weight = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="总重："]]/b/text()')
        cannon_length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="全长："]]/text()')
        max_range = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="最大射程："]]/text()')
        barrel_length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="炮管长度："]]/b/text()')
        muzzle_velocity = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="炮口初速："]]/b/text()')
        model = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="型号："]]/text()')


        # #验证
        cannon_item_2['category'] = category
        cannon_item_2['serve_period'] = serve_period
        if len(description) != 0:
            cannon_item_2['description'] = description[0].extract().strip()
        else:
            cannon_item_2['description'] = 'unknown'
        if len(pic) != 0:
            cannon_item_2['pic'] = pic[0].extract()
        else:
            cannon_item_2['pic'] = 'unknown'
        if len(country) != 0:
            cannon_item_2['country'] = country[0].extract()
        else:
            cannon_item_2['country'] = 'unknown'
        if len(name) != 0:
            cannon_item_2['name'] = name[0].extract()
        else:
            cannon_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            cannon_item_2['full_name'] = full_name[0].extract()
        else:
            cannon_item_2['full_name'] = 'unknown'


        if len(manufacturer) != 0:
            cannon_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            cannon_item_2['manufacturer'] = 'unknown'
        if len(product_time) != 0:
            cannon_item_2['product_time'] = product_time[0].extract()
        else:
            cannon_item_2['product_time'] = 'unknown'

        cannon_item_2['caliber'] = ''
        if len(caliber_1) != 0:
            cannon_item_2['caliber'] = caliber_1[0].extract()
        if len(caliber_2) != 0:
            if cannon_item_2['caliber'] == '':
                cannon_item_2['caliber'] = caliber_2[0].extract()
            else:
                cannon_item_2['caliber'] = cannon_item_2['caliber'] + ';' + caliber_2[0].extract()
        if len(caliber_1) == 0 & len(caliber_2) == 0:
            cannon_item_2['caliber'] = 'unknown'

        if len(cannon_weight) != 0:
            cannon_item_2['cannon_weight'] = cannon_weight[0].extract()
        else:
            cannon_item_2['cannon_weight'] = 'unknown'
        if len(cannon_length) != 0:
            cannon_item_2['cannon_length'] = cannon_length[0].extract()
        else:
            cannon_item_2['cannon_length'] = 'unknown'
        if len(max_range) != 0:
            cannon_item_2['max_range'] = max_range[0].extract()
        else:
            cannon_item_2['max_range'] = 'unknown'
        if len(barrel_length) != 0:
            cannon_item_2['barrel_length'] = barrel_length[0].extract()
        else:
            cannon_item_2['barrel_length'] = 'unknown'
        if len(muzzle_velocity) != 0:
            cannon_item_2['muzzle_velocity'] = muzzle_velocity[0].extract()
        else:
            cannon_item_2['muzzle_velocity'] = 'unknown'
        if len(model) != 0:
            cannon_item_2['model'] = model[0].extract()
        else:
            cannon_item_2['model'] = 'unknown'

        yield cannon_item_2


