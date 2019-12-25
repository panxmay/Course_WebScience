from py2neo import Graph, Node, Relationship, NodeMatcher
def get_subject(str):
    list = str.rstrip("\n").split(' ')
    return list[0]
def get_predicate(str):
    list = str.rstrip("\n").split(' ')
    return list[1]
def get_object(str):
    list = str.rstrip("\n").split(' ')
    return list[2]
#载入concept和relation
def load_concept_and_relation(file_obj, graph):
    matcher = NodeMatcher(graph)
    str = file_obj.readline()
    while str != "":
        node_1 = matcher.match("concept", name=get_subject(str)).first()
        if node_1 == None:
            node_1 = Node("concept", name=get_subject(str))
            graph.create(node_1)
        #concept to subconcept
        node_2 = matcher.match("concept", name=get_object(str)).first()
        if node_2 == None:
            node_2 = Node("concept", name=get_object(str))
        re_subclass = Relationship(node_1, "subclass", node_2)
        graph.create(re_subclass)
        str = file_obj.readline()

def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开指定文件
    with open('D:\military\military\data\\top_schema.txt', 'r', encoding='utf-8') as file_obj:
        #载入概念及关系
        load_concept_and_relation(file_obj, graph)

if __name__ == "__main__":
    main()


