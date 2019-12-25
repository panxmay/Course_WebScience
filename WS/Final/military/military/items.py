import scrapy

class CraftItem(scrapy.Item):
    #名称
    name = scrapy.Field()
    #别名
    alias = scrapy.Field()
    #国家
    country = scrapy.Field()
    #描述
    description = scrapy.Field()
    #类型
    category = scrapy.Field()
    #图片
    pic = scrapy.Field()
    #首飞时间
    start_time = scrapy.Field()
    #退役时间
    end_time = scrapy.Field()
    #研发单位
    RD_unit = scrapy.Field()
    #气动布局
    aerodynamic_layout = scrapy.Field()
    #乘员
    crew = scrapy.Field()
    #机长
    length = scrapy.Field()
    #翼展
    wingspan = scrapy.Field()
    #机高
    height = scrapy.Field()
    #空重
    weight = scrapy.Field()
    #飞行速度
    velocity = scrapy.Field()
    #发动机
    engine = scrapy.Field()
    #发动机数量
    engine_num = scrapy.Field()
    #最大起飞重量
    max_flight_weight = scrapy.Field()
    #最大飞行速度
    max_flight_velocity = scrapy.Field()
    #最大航程
    max_flight_distance = scrapy.Field()

class ShipItem(scrapy.Item):
    #名称
    name = scrapy.Field()
    #别名
    alias = scrapy.Field()
    #国家
    country = scrapy.Field()
    #描述
    description = scrapy.Field()
    #类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    #建造时间
    construct_time = scrapy.Field()
    #下水时间
    launch_time = scrapy.Field()
    #服役时间
    service_time = scrapy.Field()
    #现状
    current_situation = scrapy.Field()
    #同型
    homo_type = scrapy.Field()
    #前型
    former_type = scrapy.Field()
    #次型
    sub_type = scrapy.Field()
    #制造厂
    manufacturer = scrapy.Field()
    #满排吨位
    tonnage = scrapy.Field()
    #编制
    formation = scrapy.Field()
    #舰长
    length = scrapy.Field()
    #型宽
    width = scrapy.Field()
    #满载排水量
    displacement = scrapy.Field()
    #续航距离
    endurance_distance = scrapy.Field()
    #航速
    velocity = scrapy.Field()
    #活动范围
    activity_scope = scrapy.Field()
    #潜航深度
    submerge_depth = scrapy.Field()
    #自持力
    hold = scrapy.Field()

class WeaponItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 制造商
    manufacturer = scrapy.Field()
    # 生产年限
    product_time = scrapy.Field()
    # 参战情况
    war_participation = scrapy.Field()
    # 口径
    caliber = scrapy.Field()
    # 全枪长
    length = scrapy.Field()
    # 全枪重
    weight = scrapy.Field()
    # 弹匣容弹量
    capacity = scrapy.Field()
    # 有效射程
    shoot_range = scrapy.Field()
    # 战斗射速
    shoot_speed = scrapy.Field()
    # 发射性能
    performance = scrapy.Field()

class TankItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 研发厂商
    manufacturer = scrapy.Field()
    # 诞生时间
    product_time = scrapy.Field()
    # 底盘类型
    chassis_type = scrapy.Field()
    # 轮胎负重轮数量
    num_tire_loaders = scrapy.Field()
    # 车长
    length = scrapy.Field()
    # 宽度
    width = scrapy.Field()
    # 高度
    height = scrapy.Field()
    # 乘员与载员
    crew = scrapy.Field()
    # 战斗全重
    weight = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()
    #最大行程
    max_distance = scrapy.Field()

class CannonItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 研发厂商
    manufacturer = scrapy.Field()
    # 诞生时间
    product_time = scrapy.Field()
    # 底盘类型
    chassis_type = scrapy.Field()
    # 轮胎负重轮数量
    num_tire_loaders = scrapy.Field()
    # 车长
    length = scrapy.Field()
    # 宽度
    width = scrapy.Field()
    # 高度
    height = scrapy.Field()
    # 乘员与载员
    crew = scrapy.Field()
    # 战斗全重
    weight = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()
    # 最大行程
    max_distance = scrapy.Field()

class MissileItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 研发单位
    manufacturer = scrapy.Field()
    # 研发时间
    product_time = scrapy.Field()
    # 弹长
    length = scrapy.Field()
    # 弹径
    path = scrapy.Field()
    # 弹重
    weight = scrapy.Field()
    # 翼展
    wingspan = scrapy.Field()
    # 射程
    range = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()
    # 引信
    fuse = scrapy.Field()
    # 制导系统
    guidance_system = scrapy.Field()

class SpaceItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 制造商
    manufacturer = scrapy.Field()
    # 发射日期
    launch_time = scrapy.Field()
    # 发射地点
    launch_site = scrapy.Field()
    # 长度
    length = scrapy.Field()
    # 中心直径
    center_diameter = scrapy.Field()
    # 轨道
    track = scrapy.Field()
    # 运载火箭
    carrier_rocket = scrapy.Field()
    # 纬度
    latitude = scrapy.Field()
    # 经度
    longitude = scrapy.Field()

class ExplosiveItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 别名
    alias = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 研发单位
    manufacturer = scrapy.Field()
    # 研制时间
    develop_time = scrapy.Field()
    # 制导系统
    guidance_system = scrapy.Field()
    # 装药类型
    charge_type = scrapy.Field()
    # 全重
    weight = scrapy.Field()
    # 弹长
    length = scrapy.Field()
    # 弹径
    path = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()
    # 动力装置
    power_device = scrapy.Field()
    #引信装置
    fuse_device = scrapy.Field()
    #尾翼装置
    tail_device = scrapy.Field()

class CraftItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    #图片
    pic = scrapy.Field()
    #服役时间（时间段）
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    # 首飞时间
    start_time = scrapy.Field()
    # 服役时间（开始）
    serve_time = scrapy.Field()
    # 研发单位
    RD_unit = scrapy.Field()
    # 气动布局
    aerodynamic_layout = scrapy.Field()
    # 发动机数量
    engine_num = scrapy.Field()
    # 飞行速度
    speed = scrapy.Field()
    # 武器装备
    weaponry = scrapy.Field()
    # 机长
    length = scrapy.Field()
    # 机高
    height = scrapy.Field()
    # 翼展
    wingspan = scrapy.Field()
    # 旋翼直径
    wings_diameter = scrapy.Field()
    # 空重
    empty_weight = scrapy.Field()
    # 乘员
    passenger = scrapy.Field()
    #发动机
    engine = scrapy.Field()
    #最大起飞重量
    max_flight_weight = scrapy.Field()
    # 最大飞行速度
    max_flight_velocity = scrapy.Field()
    # 最大航程
    max_flight_distance = scrapy.Field()

class ShipItem_2(scrapy.Item):
    #名称
    name = scrapy.Field()
    #国家
    country = scrapy.Field()
    #描述
    description = scrapy.Field()
    #类型
    category = scrapy.Field()
    #图片
    pic = scrapy.Field()
    #服役时间（时间段）
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    #建造时间
    construct_time = scrapy.Field()
    #下水时间
    launch_time = scrapy.Field()
    #服役时间
    service_time = scrapy.Field()
    #现状
    current_situation = scrapy.Field()
    #前型
    former_type = scrapy.Field()
    #制造厂
    manufacturer = scrapy.Field()
    #满排吨位
    tonnage = scrapy.Field()
    #舰长
    length = scrapy.Field()
    #型宽
    width = scrapy.Field()
    # 编制
    formation = scrapy.Field()
    #满载排水量
    displacement = scrapy.Field()
    #续航距离
    endurance_distance = scrapy.Field()
    #航速
    velocity = scrapy.Field()
    #武器装备
    weapon = scrapy.Field()

class WeaponItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 服役时间（段）
    serve_period = scrapy.Field()
    # 全名
    full_name = scrapy.Field()

    # 制造商
    manufacturer = scrapy.Field()
    # 生产年限
    product_time = scrapy.Field()
    # 参战情况
    war_participation = scrapy.Field()
    # 口径
    caliber = scrapy.Field()
    # 发射性能
    performance = scrapy.Field()
    # 全枪长
    length = scrapy.Field()
    # 全枪重
    weight = scrapy.Field()
    # 弹匣容弹量
    capacity = scrapy.Field()
    # 有效射程
    shoot_range = scrapy.Field()
    # 战斗射速
    shoot_speed = scrapy.Field()

class TankItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 服役时间（段）
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    # 研发厂商
    manufacturer = scrapy.Field()
    # 诞生时间
    product_time = scrapy.Field()
    # 底盘类型
    chassis_type = scrapy.Field()
    # 轮胎负重轮数量
    num_tire_loaders = scrapy.Field()
    # 乘员与载员
    crew = scrapy.Field()
    # 车长
    length = scrapy.Field()
    # 宽度
    width = scrapy.Field()
    # 高度
    height = scrapy.Field()
    # 战斗全重
    weight = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()
    # 最大行程
    max_distance = scrapy.Field()

class CannonItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    #图片
    pic = scrapy.Field()
    #服役时间
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    # 研发单位
    manufacturer = scrapy.Field()
    # 研发时间
    product_time = scrapy.Field()
    # 口径
    caliber = scrapy.Field()
    # 总重
    cannon_weight = scrapy.Field()
    # 全长
    cannon_length = scrapy.Field()
    # 最大射程
    max_range = scrapy.Field()
    # 炮管长度
    barrel_length = scrapy.Field()
    # 炮口初速
    muzzle_velocity = scrapy.Field()
    # 型号
    model = scrapy.Field()

class MissileItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 服役时间（段）
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    # 研发单位
    manufacturer = scrapy.Field()
    # 研发时间
    product_time = scrapy.Field()
    # 射程
    range = scrapy.Field()
    # 弹长
    length = scrapy.Field()
    # 弹径
    path = scrapy.Field()
    # 翼展
    wingspan = scrapy.Field()
    # 弹重
    weight = scrapy.Field()
    # 引信
    fuse = scrapy.Field()
    # 制导系统
    guidance_system = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()

class SpaceItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 图片
    pic = scrapy.Field()
    # 服役时间（段）
    serve_period = scrapy.Field()
    # 全称
    full_name = scrapy.Field()

    # 制造商
    manufacturer = scrapy.Field()
    # 发射日期
    launch_time = scrapy.Field()
    # 发射地点
    launch_site = scrapy.Field()
    # 轨道
    track = scrapy.Field()
    # 运载火箭
    carrier_rocket = scrapy.Field()

class ExplosiveItem_2(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 国家
    country = scrapy.Field()
    # 描述
    description = scrapy.Field()
    # 类型
    category = scrapy.Field()
    #图片
    pic = scrapy.Field()
    #服役时间
    serve_period = scrapy.Field()
    # 全称
    full_name =scrapy.Field()

    # 研发单位
    RD_unit = scrapy.Field()
    # 研制时间
    develop_time = scrapy.Field()
    # 装药类型
    charge_type = scrapy.Field()
    # 全重
    weight = scrapy.Field()
    # 弹径
    path = scrapy.Field()
    # 弹长
    length = scrapy.Field()
    #尾翼装置
    tail_device = scrapy.Field()
    #引信装置
    fuse_device = scrapy.Field()
    # 制导系统
    guidance_system = scrapy.Field()
    # 动力装置
    power_device = scrapy.Field()
    # 最大速度
    max_speed = scrapy.Field()

