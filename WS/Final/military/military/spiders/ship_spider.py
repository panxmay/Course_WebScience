import scrapy
import os
from military.items import ShipItem
from military.items import ShipItem_2

class ShipSpider(scrapy.Spider):
    name = 'ship'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.ShipPipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/ship.txt', 'r', encoding='utf-8') as file_obj:
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
        ship_item = ShipItem()
        #country
        country = self.dict.get(str(response.url).replace("https", "http"))
        #提取
        pic = response.xpath('//div[@class="article-photo"]/a/img/@src')
        description = response.xpath('//div[@class="article-content"]/p/text()')
        name_addition = response.xpath('//h1[@class="article-title"]/text()')
        alias =response.xpath('//div[@class="article-alias"]/text()')
        category = response.xpath('//div[@id="chan_breadcrumbs"]/a[@class="cur"]/text()')
        name = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="名称"]]/p/text()')

        construct_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="建造时间"]]/p/text()')
        launch_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="下水时间"]]/p/text()')
        service_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="服役时间"]]/p/text()')
        current_situation = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="现状"]]/p/text()')
        homo_type = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="同型"]]/p/text()')
        former_type = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="前型"]]/p/text()')
        sub_type =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="次型"]]/p/text()')
        manufacturer = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="制造厂"]]/p/text()')
        tonnage = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="满排吨位"]]/p/text()')
        formation = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="编制"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="舰长"]]/p/text()')
        width = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="型宽"]]/p/text()')
        displacement = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="满载排水量"]]/p/text()')
        endurance_distance = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="续航距离"]]/p/text()')
        velocity = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="航速"]]/p/text()')
        activity_scope = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="活动范围"]]/p/text()')
        submerge_depth = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="潜航深度"]]/p/text()')
        hold = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="自持力"]]/p/text()')

        #验证
        ship_item['country'] = country
        if len(pic) != 0:
            ship_item['pic'] = pic[0].extract()
        else:
            ship_item['pic'] = 'unknown'
        if len(description) != 0:
            ship_item['description'] = description[0].extract()
        else:
            ship_item['description'] = 'unknown'
        if len(alias) != 0:
            ship_item['alias'] = alias[0].extract()
        else:
            ship_item['alias'] = 'unknown'
        if len(category) != 0:
            ship_item['category'] = category[0].extract()
        else:
            ship_item['category'] = 'unknown'
        if len(name) != 0:
            ship_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            ship_item['name'] = name_addition[0].extract()
        else:
            ship_item['name'] = 'unknown'

        if len(construct_time) != 0:
            ship_item['construct_time'] = construct_time[0].extract()
        else:
            ship_item['construct_time'] = 'unknown'
        if len(launch_time) != 0:
            ship_item['launch_time'] = launch_time[0].extract()
        else:
            ship_item['launch_time'] = 'unknown'
        if len(service_time) != 0:
            ship_item['service_time'] = service_time[0].extract()
        else:
            ship_item['service_time'] = 'unknown'
        if len(current_situation) != 0:
            ship_item['current_situation'] = current_situation[0].extract()
        else:
            ship_item['current_situation'] = 'unknown'
        if len(homo_type) != 0:
            ship_item['homo_type'] = homo_type[0].extract()
        else:
            ship_item['homo_type'] = 'unknown'
        if len(former_type) != 0:
            ship_item['former_type'] = former_type[0].extract()
        else:
            ship_item['former_type'] = 'unknown'
        if len(sub_type) != 0:
            ship_item['sub_type'] = sub_type[0].extract()
        else:
            ship_item['sub_type'] = 'unknown'
        if len(manufacturer) != 0:
            ship_item['manufacturer'] = manufacturer[0].extract()
        else:
            ship_item['manufacturer'] = 'unknown'
        if len(tonnage) != 0:
            ship_item['tonnage'] = tonnage[0].extract()
        else:
            ship_item['tonnage'] = 'unknown'
        if len(formation) != 0:
            ship_item['formation'] = formation[0].extract()
        else:
            ship_item['formation'] = 'unknown'
        if len(length) != 0:
            ship_item['length'] = length[0].extract()
        else:
            ship_item['length'] = 'unknown'
        if len(width) != 0:
            ship_item['width'] = width[0].extract()
        else:
            ship_item['width'] = 'unknown'
        if len(displacement) != 0:
            ship_item['displacement'] = displacement[0].extract()
        else:
            ship_item['displacement'] = 'unknown'
        if len(endurance_distance) != 0:
            ship_item['endurance_distance'] = endurance_distance[0].extract()
        else:
            ship_item['endurance_distance'] = 'unknown'
        if len(velocity) != 0:
            ship_item['velocity'] = velocity[0].extract()
        else:
            ship_item['velocity'] = 'unknown'
        if len(activity_scope) != 0:
            ship_item['activity_scope'] = activity_scope[0].extract()
        else:
            ship_item['activity_scope'] = 'unknown'
        if len(submerge_depth) != 0:
            ship_item['submerge_depth'] = submerge_depth[0].extract()
        else:
            ship_item['submerge_depth'] = 'unknown'
        if len(hold) != 0:
            ship_item['hold'] = hold[0].extract()
        else:
            ship_item['hold'] = 'unknown'
        yield ship_item

class ShipSpider_2(scrapy.Spider):
    name = 'ship_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.ShipPipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/warship.txt', 'r', encoding='utf-8') as file_obj:
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
        ship_item_2 = ShipItem_2()
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

        construct_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="建造时间："]]/text()')
        launch_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="下水时间："]]/text()')
        service_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="服役时间："]]/text()')
        current_situation = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="现状："]]/text()')
        former_type = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="前型："]]/text()')
        manufacturer = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="制造厂："]]/text()')
        tonnage = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="满排吨位："]]/text()')
        length = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="舰长："]]/b/text()')
        width = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="型宽："]]/b/text()')
        formation = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="编制："]]/text()')
        displacement = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="满载排水量："]]/b/text()')
        endurance_distance = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="续航距离："]]/text()')
        velocity = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="航速："]]/b/text()')
        weapon = response.xpath('//div[@class="dataInfo"]/ul[@class="multiList"]/li/text()')


        # #验证
        ship_item_2['category'] = category
        ship_item_2['serve_period'] = serve_period
        if len(description) != 0:
            ship_item_2['description'] = description[0].extract().strip()
        else:
            ship_item_2['description'] = 'unknown'
        if len(pic) != 0:
            ship_item_2['pic'] = pic[0].extract()
        else:
            ship_item_2['pic'] = 'unknown'
        if len(country) != 0:
            ship_item_2['country'] = country[0].extract()
        else:
            ship_item_2['country'] = 'unknown'
        if len(name) != 0:
            ship_item_2['name'] = name[0].extract()
        else:
            ship_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            ship_item_2['full_name'] = full_name[0].extract()
        else:
            ship_item_2['full_name'] = 'unknown'

        if len(construct_time) != 0:
            ship_item_2['construct_time'] = construct_time[0].extract()
        else:
            ship_item_2['construct_time'] = 'unknown'
        if len(launch_time) != 0:
            ship_item_2['launch_time'] = launch_time[0].extract()
        else:
            ship_item_2['launch_time'] = 'unknown'
        if len(service_time) != 0:
            ship_item_2['service_time'] = service_time[0].extract()
        else:
            ship_item_2['service_time'] = 'unknown'
        if len(current_situation) != 0:
            ship_item_2['current_situation'] = current_situation[0].extract()
        else:
            ship_item_2['current_situation'] = 'unknown'
        if len(former_type) != 0:
            ship_item_2['former_type'] = former_type[0].extract()
        else:
            ship_item_2['former_type'] = 'unknown'
        if len(manufacturer) != 0:
            ship_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            ship_item_2['manufacturer'] = 'unknown'
        if len(tonnage) != 0:
            ship_item_2['tonnage'] = tonnage[0].extract()
        else:
            ship_item_2['tonnage'] = 'unknown'
        if len(length) != 0:
            ship_item_2['length'] = length[0].extract()
        else:
            ship_item_2['length'] = 'unknown'
        if len(width) != 0:
            ship_item_2['width'] = width[0].extract()
        else:
            ship_item_2['width'] = 'unknown'
        if len(formation) != 0:
            ship_item_2['formation'] = formation[0].extract()
        else:
            ship_item_2['formation'] = 'unknown'
        if len(displacement) != 0:
            ship_item_2['displacement'] = displacement[0].extract()
        else:
            ship_item_2['displacement'] = 'unknown'
        if len(endurance_distance) != 0:
            ship_item_2['endurance_distance'] = endurance_distance[0].extract()
        else:
            ship_item_2['endurance_distance'] = 'unknown'
        if len(velocity) != 0:
            ship_item_2['velocity'] = velocity[0].extract()
        else:
            ship_item_2['velocity'] = 'unknown'
        if len(weapon) != 0:
            str_weapon = ''
            for we in weapon:
                str_weapon = str_weapon + we.extract() + '@'
            ship_item_2['weapon'] = str_weapon
        else:
            ship_item_2['weapon'] = 'unknown'

        yield ship_item_2