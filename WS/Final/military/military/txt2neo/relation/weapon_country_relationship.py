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
        if get_predicate(rdf) == "国家":
            node_weapon = matcher.match("weapon", name=get_subject(rdf)).first()
            if node_weapon == None:
                print("error! "+ get_subject(rdf)+ " not exist!")
            else:
                if get_object(rdf) == "苏/俄":
                    node_country = matcher.match("country", name="苏联").first()
                else:
                    node_country = matcher.match("country", name=get_object(rdf)).first()
                if node_country != None:
                    create_relationship = Relationship(node_weapon, "create_from", node_country)
                    graph.create(create_relationship)
                else:
                    print(get_object(rdf) + "不存在")
        rdf = file_obj.readline()

def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开文件
    with open("D:\military\military\data\weapon\instance_rdf.txt", 'r', encoding='utf-8') as file_obj:
        establish_relation(graph, file_obj)
    file_obj.close()

if __name__ == "__main__":
    main()