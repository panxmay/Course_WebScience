import scrapy
from military.items import SpaceItem
from military.items import SpaceItem_2

class SpaceSpider(scrapy.Spider):
    name = 'space'
    custom_settings = {
        'ITEM_PIPELINES': {'military.pipelines.SpacePipeline': 300}
    }
    allowed_domains = ['https://military.china.com']
    #打开文件
    start_urls = []
    compound = []
    dict={}
    with open('D:/military/military/data/uri/weapons/space.txt', 'r', encoding='utf-8') as file_obj:
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
        space_item = SpaceItem()
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
        launch_time = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="发射日期"]]/p/text()')
        launch_site = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="发射地点"]]/p/text()')
        length = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="长度"]]/p/text()')
        center_diameter = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="中心直径"]]/p/text()')
        track = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="轨道"]]/p/text()')
        carrier_rocket =response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="运载火箭"]]/p/text()')
        latitude = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="纬度"]]/p/text()')
        longitude = response.xpath('//table[@class="article-parameter-table"]/tr/td[em[text()="经度"]]/p/text()')

        #验证
        space_item['country'] = country
        if len(pic) != 0:
            space_item['pic'] = pic[0].extract()
        else:
            space_item['pic'] = 'unknown'
        if len(description) != 0:
            space_item['description'] = description[0].extract()
        else:
            space_item['description'] = 'unknown'
        if len(alias) != 0:
            space_item['alias'] = alias[0].extract()
        else:
            space_item['alias'] = 'unknown'
        if len(category) != 0:
            space_item['category'] = category[0].extract()
        else:
            space_item['category'] = 'unknown'
        if len(name) != 0:
            space_item['name'] = name[0].extract()
        elif len(name_addition) != 0:
            space_item['name'] = name_addition[0].extract()
        else:
            space_item['name'] = 'unknown'

        if len(manufacturer) != 0:
            space_item['manufacturer'] = manufacturer[0].extract()
        else:
            space_item['manufacturer'] = 'unknown'
        if len(launch_time) != 0:
            space_item['launch_time'] = launch_time[0].extract()
        else:
            space_item['launch_time'] = 'unknown'
        if len(launch_site) != 0:
            space_item['launch_site'] = launch_site[0].extract()
        else:
            space_item['launch_site'] = 'unknown'
        if len(length) != 0:
            space_item['length'] = length[0].extract()
        else:
            space_item['length'] = 'unknown'
        if len(center_diameter) != 0:
            space_item['center_diameter'] = center_diameter[0].extract()
        else:
            space_item['center_diameter'] = 'unknown'
        if len(track) != 0:
            space_item['track'] = track[0].extract()
        else:
            space_item['track'] = 'unknown'
        if len(carrier_rocket) != 0:
            space_item['carrier_rocket'] = carrier_rocket[0].extract()
        else:
            space_item['carrier_rocket'] = 'unknown'
        if len(latitude) != 0:
            space_item['latitude'] = latitude[0].extract()
        else:
            space_item['latitude'] = 'unknown'
        if len(longitude) != 0:
            space_item['longitude'] = longitude[0].extract()
        else:
            space_item['longitude'] = 'unknown'

        yield space_item

class SpaceSpider_2(scrapy.Spider):
    name = 'space_2'
    custom_settings = {
        'ITEM_PIPELINES':{'military.pipelines.SpacePipeline_2': 300}
    }
    allowed_domains = ['http://weapon.huanqiu.com']
    #打开文件
    start_urls = []
    compound = []
    dict = {}
    with open('D:/military/military/data/uri/weapons_2/spaceship.txt', 'r', encoding='utf-8') as file_obj:
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
        space_item_2 = SpaceItem_2()
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

        manufacturer = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="制造商："]]/text()')
        launch_time = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="发射日期："]]/text()')
        launch_site = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="发射地点："]]/text()')
        track = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="轨道："]]/text()')
        carrier_rocket = response.xpath('//div[@class="dataInfo"]/ul/li[span[text()="运载火箭："]]/text()')


        # #验证
        space_item_2['category'] = category
        space_item_2['serve_period'] = serve_period
        if len(description) != 0:
            space_item_2['description'] = description[0].extract().strip()
        else:
            space_item_2['description'] = 'unknown'
        if len(pic) != 0:
            space_item_2['pic'] = pic[0].extract()
        else:
            space_item_2['pic'] = 'unknown'
        if len(country) != 0:
            space_item_2['country'] = country[0].extract()
        else:
            space_item_2['country'] = 'unknown'
        if len(name) != 0:
            space_item_2['name'] = name[0].extract()
        else:
            space_item_2['name'] = 'unknown'
        if len(full_name) != 0:
            space_item_2['full_name'] = full_name[0].extract()
        else:
            space_item_2['full_name'] = 'unknown'

        if len(manufacturer) != 0:
            space_item_2['manufacturer'] = manufacturer[0].extract()
        else:
            space_item_2['manufacturer'] = 'unknown'
        if len(launch_time) != 0:
            space_item_2['launch_time'] = launch_time[0].extract()
        else:
            space_item_2['launch_time'] = 'unknown'
        if len(launch_site) != 0:
            space_item_2['launch_site'] = launch_site[0].extract()
        else:
            space_item_2['launch_site'] = 'unknown'
        if len(track) != 0:
            space_item_2['track'] = track[0].extract()
        else:
            space_item_2['track'] = 'unknown'
        if len(carrier_rocket) != 0:
            space_item_2['carrier_rocket'] = carrier_rocket[0].extract()
        else:
            space_item_2['carrier_rocket'] = 'unknown'

        yield space_item_2
