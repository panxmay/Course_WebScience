def get_subject(str):
    list = str.rstrip("\n").split('||')
    return list[0]
def get_predicate(str):
    list = str.rstrip("\n").split('||')
    return list[1]
def get_object(str):
    list = str.rstrip("\n").split('||')
    return list[2]

def load_fundamental_country_schema(components):
    with open('D:\military\military\data\country\\baidubaike_schema.txt', 'a', encoding='utf-8') as file_obj:
        for component in components:
            file_obj.write("国家 subclass " + component + '\n')
    file_obj.close()

# def load_advanced_country_schema():
#     with open('D:\military\military\data\country\\baidubaike_schema.txt', 'a', encoding='utf-8') as file_obj_1:
#         with open('D:\military\military\data\country\\baidubaike_instance_rdf.txt', 'r',
#                   encoding='utf-8') as file_obj_2:
#             rdf = file_obj_2.readline()
#             ##澳大利亚||所属洲||大洋洲
#             while (rdf != "") & (rdf != "\n"):
#                 if get_predicate(rdf) == "所属洲":
#                     file_obj_1.write(get_object(rdf) + " subclass " + get_subject(rdf) + '\n')
#                 rdf = file_obj_2.readline()
#         file_obj_2.close()
#     file_obj_1.close()



def main():
    components = ['亚洲', '非洲', '欧洲', '北美洲', '南美洲', '大洋洲', '南极洲']
    #写入最基本schema
    load_fundamental_country_schema(components)
    # load_advanced_country_schema()
    print()
if __name__ == "__main__":
    main()