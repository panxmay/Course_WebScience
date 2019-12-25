#简单做并集
def fusion_weapon_schema():
    list_1 = []
    list_2 = []
    with open('D:\military\military\data\weapon\schema_zhonghuawuqiku.txt', 'r', encoding='utf-8') as file_obj_1:
        str_1 = file_obj_1.readline()
        while str_1 != "":
            list_1.append(str_1)
            str_1 = file_obj_1.readline()
        file_obj_1.close()

    with open('D:\military\military\data\weapon\schema_huanqiujunshi.txt', 'r', encoding='utf-8') as file_obj_2:
        str_2 = file_obj_2.readline()
        while str_2 != "":
            list_2.append(str_2)
            str_2 = file_obj_2.readline()
        file_obj_2.close()

    # 以中华武器库为基准，将环球军事网的内容作为补充
    with open('D:\military\military\data\weapon\schema.txt', 'a', encoding='utf-8') as file_obj:
        first = 0
        for s2 in list_2:
            flag = 0
            for s1 in list_1:
                if first == 0:
                    file_obj.write(s1)
                if s1 == s2:
                    flag = 1
            first = 1
            if flag == 0:
                file_obj.write(s2)
        file_obj.close()

def main():
    fusion_weapon_schema()

if __name__ == "__main__":
    main()


