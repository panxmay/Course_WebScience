import pymongo

#载入instance,relation和property
def load_instance(table):
    with open('D:\military\military\data\weapon\instance_zhonghuawuqiku.txt', 'a', encoding='utf-8') as file_obj:
        for row in table.find():
            #创建instance
            name = row["名称"]
            if name == "unknown":
                continue
            for item in row.items():
                if (item[0] == '_id') | (item[0] == 'name') :
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
    # 数据源_1
    category = ['craft', 'ship', 'weapon', 'tank', 'cannon', 'missile', 'space', 'explosive']
    # # 载入实例及其属性及其层级
    for ca in category:
        load_instance(db[ca])

if __name__ == "__main__":
    main()



