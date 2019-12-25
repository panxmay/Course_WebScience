# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
class CraftPipeline(object):

    collection = 'craft'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '首飞时间':item['start_time'],
            '退役时间':item['end_time'],
            '研发单位':item['RD_unit'],
            '气动布局':item['aerodynamic_layout'],
            '乘员':item['crew'],
            '机长':item['length'],
            '翼展':item['wingspan'],
            '机高':item['height'],
            '空重':item['weight'],
            '飞行速度':item['velocity'],
            '发动机':item['engine'],
            '发动机数量':item['engine_num'],
            '最大起飞重量':item['max_flight_weight'],
            '最大飞行速度':item['max_flight_velocity'],
            '最大航程':item['max_flight_distance']
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class ShipPipeline(object):

    collection = 'ship'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '建造时间':item['construct_time'],
            '下水时间':item['launch_time'],
            '服役时间':item['service_time'],
            '现状':item['current_situation'],
            '同型':item['homo_type'],
            '前型':item['former_type'],
            '次型':item['sub_type'],
            '制造厂':item['manufacturer'],
            '满排吨位':item['tonnage'],
            '编制':item['formation'],
            '舰长':item['length'],
            '型宽':item['width'],
            '满载排水量':item['displacement'],
            '续航距离':item['endurance_distance'],
            '航速':item['velocity'],
            '活动范围': item['activity_scope'],
            '潜航深度': item['submerge_depth'],
            '自持力': item['hold']
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class WeaponPipeline(object):

    collection = 'weapon'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '制造商':item['manufacturer'],
            '生产年限':item['product_time'],
            '参战情况':item['war_participation'],
            '口径':item['caliber'],
            '全枪长':item['length'],
            '全枪重':item['weight'],
            '弹匣容弹量':item['capacity'],
            '有效射程':item['shoot_range'],
            '战斗射速':item['shoot_speed'],
            '发射性能':item['performance'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class TankPipeline(object):

    collection = 'tank'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '研发厂商':item['manufacturer'],
            '诞生时间':item['product_time'],
            '底盘类型':item['chassis_type'],
            '轮胎负重轮数量':item['num_tire_loaders'],
            '车长':item['length'],
            '宽度':item['width'],
            '高度':item['height'],
            '乘员与载员':item['crew'],
            '战斗全重':item['weight'],
            '最大速度':item['max_speed'],
            '最大行程':item['max_distance'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class CannonPipeline(object):

    collection = 'cannon'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '研发厂商':item['manufacturer'],
            '诞生时间':item['product_time'],
            '底盘类型':item['chassis_type'],
            '轮胎负重轮数量':item['num_tire_loaders'],
            '车长':item['length'],
            '宽度':item['width'],
            '高度':item['height'],
            '乘员与载员':item['crew'],
            '战斗全重':item['weight'],
            '最大速度':item['max_speed'],
            '最大行程':item['max_distance'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class MissilePipeline(object):

    collection = 'missile'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '研发单位':item['manufacturer'],
            '研发时间':item['product_time'],
            '弹长':item['length'],
            '弹径':item['path'],
            '弹重':item['weight'],
            '翼展':item['wingspan'],
            '射程':item['range'],
            '最大速度':item['max_speed'],
            '引信':item['fuse'],
            '制导系统':item['guidance_system'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class SpacePipeline(object):

    collection = 'space'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '制造商':item['manufacturer'],
            '发射日期':item['launch_time'],
            '发射地点':item['launch_site'],
            '长度':item['length'],
            '中心直径':item['center_diameter'],
            '轨道':item['track'],
            '运载火箭':item['carrier_rocket'],
            '纬度':item['latitude'],
            '经度':item['longitude'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class ExplosivePipeline(object):

    collection = 'explosive'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '别名':item['alias'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片': item['pic'],
            '研发单位':item['manufacturer'],
            '研制时间':item['develop_time'],
            '制导系统':item['guidance_system'],
            '装药类型':item['charge_type'],
            '全重':item['weight'],
            '弹长':item['length'],
            '弹径':item['path'],
            '最大速度':item['max_speed'],
            '动力装置':item['power_device'],
            '引信装置': item['fuse_device'],
            '尾翼装置': item['tail_device'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class CraftPipeline_2(object):

    collection = 'craft_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '首飞时间':item['start_time'],
            '服役时间(开始)':item['serve_time'],
            '研发单位':item['RD_unit'],
            '气动布局':item['aerodynamic_layout'],
            '发动机数量':item['engine_num'],
            '飞行速度':item['speed'],
            '武器装备':item['weaponry'],
            '机长':item['length'],
            '机高':item['height'],
            '翼展':item['wingspan'],
            '空重':item['empty_weight'],
            '乘员': item['passenger'],
            '发动机': item['engine'],
            '最大起飞重量': item['max_flight_weight'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class ShipPipeline_2(object):

    collection = 'ship_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '建造时间':item['construct_time'],
            '下水时间':item['launch_time'],
            '服役时间':item['service_time'],
            '现状':item['current_situation'],
            '前型':item['former_type'],
            '制造厂':item['manufacturer'],
            '满排吨位':item['tonnage'],
            '舰长':item['length'],
            '型宽':item['width'],
            '编制':item['formation'],
            '满载排水量':item['displacement'],
            '续航距离': item['endurance_distance'],
            '航速': item['velocity'],
            '武器装备': item['weapon'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class CannonPipeline_2(object):

    collection = 'cannon_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '研发单位':item['manufacturer'],
            '研发时间':item['product_time'],
            '口径':item['caliber'],
            '总重':item['cannon_weight'],
            '全长':item['cannon_length'],
            '最大射程':item['max_range'],
            '炮管长度':item['barrel_length'],
            '炮口初速':item['muzzle_velocity'],
            '型号':item['model'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class ExplosivePipeline_2(object):

    collection = 'explosive_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '研发单位':item['RD_unit'],
            '研制时间':item['develop_time'],
            '装药类型':item['charge_type'],
            '全重':item['weight'],
            '弹径':item['path'],
            '弹长':item['length'],
            '尾翼装置':item['tail_device'],
            '引信装置':item['fuse_device'],
            '制导系统':item['guidance_system'],
            '动力装置': item['power_device'],
            '最大速度': item['max_speed'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class TankPipeline_2(object):

    collection = 'tank_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '研发厂商':item['manufacturer'],
            '诞生时间':item['product_time'],
            '底盘类型':item['chassis_type'],
            '轮胎负重轮数量':item['num_tire_loaders'],
            '乘员与载员':item['crew'],
            '车长':item['length'],
            '宽度':item['width'],
            '高度':item['height'],
            '战斗全重':item['weight'],
            '最大速度': item['max_speed'],
            '最大行程': item['max_distance'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class MissilePipeline_2(object):

    collection = 'missile_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '研发单位':item['manufacturer'],
            '研发时间':item['product_time'],
            '射程':item['range'],
            '弹长':item['length'],
            '弹径':item['path'],
            '翼展':item['wingspan'],
            '弹重':item['weight'],
            '引信':item['fuse'],
            '制导系统':item['guidance_system'],
            '最大速度': item['max_speed'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class WeaponPipeline_2(object):

    collection = 'weapon_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全名': item['full_name'],
            '制造商':item['manufacturer'],
            '生产年限':item['product_time'],
            '参战情况':item['war_participation'],
            '口径':item['caliber'],
            '全枪长':item['length'],
            '全枪重':item['weight'],
            '弹匣容弹量':item['capacity'],
            '有效射程':item['shoot_range'],
            '战斗射速':item['shoot_speed'],
            '发射性能':item['performance'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item

class SpacePipeline_2(object):

    collection = 'space_2'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        data = {
            '名称': item['name'],
            '描述':item['description'],
            '国家':item['country'],
            '类型':item['category'],
            '图片':item['pic'],
            '服役时间段': item['serve_period'],
            '全称': item['full_name'],
            '制造商':item['manufacturer'],
            '发射日期':item['launch_time'],
            '发射地点':item['launch_site'],
            '轨道':item['track'],
            '运载火箭':item['carrier_rocket'],
        }
        table = self.db[self.collection]
        table.insert_one(data)
        return item