import pymongo

#载入instance,relation和property
def load_instance(table):
    with open('D:\military\military\data\weapon\instance_huanqiujunshi.txt', 'a', encoding='utf-8') as file_obj:
        for row in table.find():
            #创建instance
            name = row["名称"]
            if name == "unknown":
                continue
            for item in row.items():
                if (item[0] == '_id') | (item[0] == 'name') | (item[0] == '武器装备'):
                    continue
                if isinstance(item[1],str) & ((item[1] == "unknown") | (item[1] == "")):
                    continue
                file_obj.write(name + "||" + item[0] + "||" + item[1])
                file_obj.write('\n')
    file_obj.close()
def main():
    # 连接mongodb
    client = pymongo.MongoClient('localhost', 27017)
    db = client['military']
    # 创建category数组
    category = ['craft_2', 'ship_2', 'weapon_2', 'tank_2', 'cannon_2', 'missile_2', 'space_2', 'explosive_2']
    # # 载入实例及其属性及其层级
    for ca in category:
        load_instance(db[ca])

if __name__ == "__main__":
    main()



