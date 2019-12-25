from py2neo import Graph, Node, NodeMatcher
#载入instance
def load_instance_and_relation(file_obj, graph):
    matcher = NodeMatcher(graph)
    str = file_obj.readline().rstrip("\n")
    while str != "":
        instance_node = matcher.match("RDunit", name = str).first()
        if instance_node == None:
            instance_node = Node("RDunit", name = str)
            graph.create(instance_node)
        str = file_obj.readline().rstrip("\n")


def main():
    # 连接neo4j
    graph = Graph("http://localhost:7474", username="neo4j", password="li19970701")
    # 打开指定文件
    with open('D:\military\military\data\RDunit\RDunit_list.txt', 'r', encoding='utf-8') as file_obj:
        #载入概念及关系
        load_instance_and_relation(file_obj, graph)

if __name__ == "__main__":
    main()


