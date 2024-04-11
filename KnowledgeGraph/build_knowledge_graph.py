import csv
from py2neo import Graph, Node, Relationship, NodeMatcher
import py2neo  # py2neo是Python代码操作neo4j的库，类似于jdbc


class KnowledgeGraph:
    def __init__(self):
        self.graph = None

    def build_HLM_knowledge_graph(self):
        # self.graph.run("match (n) detach delete n")
        self.graph = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")
        with open('HLM.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for item in reader:
                if reader.line_num == 1:
                    continue
                print("当前行数：", reader.line_num, "当前内容：", item)
                start_node = Node("Person", name=item[0])
                end_node = Node("Person", name=item[1])
                relation = Relationship(start_node, item[3], end_node)
                self.graph.merge(start_node, "Person", "name")
                self.graph.merge(end_node, "Person", "name")
                self.graph.merge(relation, "Person", "name")

    def build_paper_knowledge_graph(self):
        pass
