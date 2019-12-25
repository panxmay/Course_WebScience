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
    with open('D:\military\military\data\weapon\schema.txt', 'r', encoding='utf-8') as file_obj:
        #载入概念及关系
        load_concept_and_relation(file_obj, graph)

if __name__ == "__main__":
    main()
#
#     import pymongo
#     from py2neo import Graph, Node, Relationship, NodeMatcher
#
#
#     # 载入concept和relation
#     def load_concept_and_relation(table, graph):
#         top_node = Node(label="weapon", name="兵器")
#         graph.create(top_node)
#         matcher = NodeMatcher(graph)
#         for row in table.find():
#             node_1 = matcher.match(label="weapon", name=row["name"])
#             if len(node_1) == 0:
#                 node_1 = Node(label="weapon", name=row["name"])
#                 graph.create(node_1)
#                 # top to class-1
#                 re_subclass = Relationship(top_node, "subclass", node_1)
#                 graph.create(re_subclass)
#             # class-1 to class-2
#             node_2 = Node(label="weapon", name=row["subclass"])
#             graph.create(node_2)
#             re_subclass_2 = Relationship(node_1, "subclass", node_2)
#             graph.create(re_subclass_2)
#
#
#     def main():
#         # 连接mongodb
#         client = pymongo.MongoClient('localhost', 27017)
#         db = client['military']
#         table_1 = db['schema']
#         table_2 = db['schema_2']
#         # 连接neo4j
#         graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
#
#         # 载入概念及关系
#         load_concept_and_relation(table_1, graph)
#
#
#     if __name__ == "__main__":
#         main()

