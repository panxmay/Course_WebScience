from py2neo import Graph, Node, Relationship, NodeMatcher
#载入instance和relation
def load_instance_and_relation(file_obj, graph):
    matcher = NodeMatcher(graph)
    str = file_obj.readline()
    while str != "":
        dict = eval(str)
        name = dict.pop("名称")
        dict["name"] = name
        instance_node = Node("country", **dict)
        graph.create(instance_node)
        category = dict.get("所属洲", "未知")
        if category != "未知":
            concept_node = matcher.match("concept", name=category).first()
            if concept_node == None:
                print("subclass error")
            else:
                re_subclass = Relationship(concept_node, "subclass", instance_node)
                graph.create(re_subclass)
        str = file_obj.readline()


def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开指定文件
    with open('D:\military\military\data\country\\baidubaike_instance_property.txt', 'r', encoding='utf-8') as file_obj:
        #载入概念及关系
        load_instance_and_relation(file_obj, graph)

if __name__ == "__main__":
    main()

