from py2neo import Graph, Node, Relationship, NodeMatcher

def get_subject(str):
    list = str.rstrip("\n").split('||')
    return list[0]
def get_predicate(str):
    list = str.rstrip("\n").split('||')
    return list[1]
def get_object(str):
    list = str.rstrip("\n").split('||')
    return list[2]

def establish_relation(graph, file_obj):
    rdf = file_obj.readline()
    matcher = NodeMatcher(graph)
    while rdf != "":
        if len(rdf.rstrip("\n").split('||')) == 3:
            if get_predicate(rdf) == "国籍":
                node_person = matcher.match("person", name=get_subject(rdf)).first()
                if node_person== None:
                    print("error! "+ get_subject(rdf)+ " not exist!")
                else:
                    if get_object(rdf) == "中华人民共和国":
                        node_country = matcher.match("country", name="中国").first()
                    else:
                        node_country = matcher.match("country", name=get_object(rdf)).first()
                    if node_country != None:
                        create_relationship = Relationship(node_person, "come_from", node_country)
                        graph.create(create_relationship)
                    else:
                        print(get_object(rdf) + "不存在")
        rdf = file_obj.readline()

def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开文件
    with open("D:\military\military\data\person\\baidubaike_instance_rdf.txt", 'r', encoding='utf-8') as file_obj:
        establish_relation(graph, file_obj)
    file_obj.close()

if __name__ == "__main__":
    main()