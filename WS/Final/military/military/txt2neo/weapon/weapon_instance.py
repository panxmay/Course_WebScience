from py2neo import Graph, Node, Relationship, NodeMatcher
#载入instance和relation
def load_instance_and_relation(file_obj, graph):
    matcher = NodeMatcher(graph)
    str = file_obj.readline()
    while str != "":
        dict = eval(str)
        name = dict.pop("名称")
        dict["name"] = name
        instance_node = Node("weapon", **dict)
        graph.create(instance_node)
        category = dict["类型"]
        concept_node = matcher.match("concept", name=category).first()
        if concept_node == None:
            print("subclass error")
        else:
            re_subclass = Relationship(concept_node,"subclass", instance_node)
            graph.create(re_subclass)
        str = file_obj.readline()

        # if node_1 == None:
        #     node_1 = Node("concept", name=get_subject(str))
        #     graph.create(node_1)
        # #concept to subconcept
        # node_2 = matcher.match("concept", name=get_object(str)).first()
        # if node_2 == None:
        #     node_2 = Node("concept", name=get_object(str))
        # re_subclass = Relationship(node_1, "subclass", node_2)
        # graph.create(re_subclass)
        # str = file_obj.readline()

def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开指定文件
    with open('D:\military\military\data\weapon\instance_property.txt', 'r', encoding='utf-8') as file_obj:
        #载入概念及关系
        load_instance_and_relation(file_obj, graph)

if __name__ == "__main__":
    main()


