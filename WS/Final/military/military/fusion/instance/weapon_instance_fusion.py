#简单做并集
def get_subject(str):
    list = str.rstrip("\n").split('||')
    return list[0]
def get_predicate(str):
    list = str.rstrip("\n").split('||')
    return list[1]
def get_object(str):
    list = str.rstrip("\n").split('||')
    return list[2]

def union_property(d_1, d_2, list):
    index = list.index(d_1)
    for key_2 in d_2.keys():
        flag = 0
        for key_1 in d_1.keys():
            # 已出现
            if key_1 == key_2:
                flag = 1
                break
        # 未出现
        if flag == 0:
            (list[index])[key_2] = d_2.get(key_2)


def fusion_weapon_instance():
    list_1 = []
    list_2 = []
    with open('D:\military\military\data\weapon\instance_zhonghuawuqiku.txt', 'r', encoding='utf-8') as file_obj_1:
        str_1 = file_obj_1.readline()
        dict = {}
        dict[get_predicate(str_1)] = get_object(str_1)
        while str_1 != "":
            #rdf 有误
            if len(str_1.rstrip("\n").split('||')) != 3:
                print("error:" + str_1)
            #同一主语
            else:
                if dict["名称"] == get_subject(str_1):
                    dict[get_predicate(str_1)] = get_object(str_1)
                #主语不同
                else:
                    list_1.append(dict)
                    dict = {}
                    dict[get_predicate(str_1)] = get_object(str_1)
            str_1 = file_obj_1.readline()
        list_1.append(dict)
        file_obj_1.close()

    with open('D:\military\military\data\weapon\instance_huanqiujunshi.txt', 'r', encoding='utf-8') as file_obj_2:
        str_2 = file_obj_2.readline()
        dict = {}
        dict[get_predicate(str_2)] = get_object(str_2)
        while str_2 != "":
            # rdf 有误
            if len(str_2.rstrip("\n").split('||')) != 3:
                print("rdf error")
            #rdf 无误
            else:
                # 同一主语
                if dict["名称"] == get_subject(str_2):
                    dict[get_predicate(str_2)] = get_object(str_2)
                # 主语不同
                else:
                    list_2.append(dict)
                    dict = {}
                    dict[get_predicate(str_2)] = get_object(str_2)
            str_2 = file_obj_2.readline()
        list_2.append(dict)
        file_obj_2.close()

    # 以中华武器库为基准，将环球军事网的内容作为补充
    fusion_list = list_1.copy()
    for d_2 in list_2:
        for d_1 in list_1:
            # 主语相同
            if (d_2.get("名称","error_2") == d_1.get("名称","error_1")) | (d_2.get("名称","error_2") == d_1.get("别名","error_1")):
                # 取并集 并更新
                union_property(d_1, d_2, fusion_list)
                break
    #name property形式存储
    with open('D:\military\military\data\weapon\instance_property.txt', 'a', encoding='utf-8') as file_obj_property:
        for d in fusion_list:
            file_obj_property.write(str(d) + '\n')
    file_obj_property.close()

    #rdf形式存储
    with open('D:\military\military\data\weapon\instance_rdf.txt', 'a', encoding='utf-8') as file_obj_rdf:
        for d in fusion_list:
            subject = d["名称"]
            for key in d.keys():
                if key == "名称":
                    continue
                else:
                    file_obj_rdf.write(subject + "||" + key + "||" + d[key] + "\n")
    file_obj_rdf.close()


def main():
    fusion_weapon_instance()

if __name__ == "__main__":
    main()


