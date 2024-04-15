import csv
from py2neo import Graph, Node, Relationship


class KnowledgeGraph:
    def __init__(self):
        self.graph = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")

    def build_HLM_knowledge_graph(self):
        self.graph.run("match (n) detach delete n")
        self.graph = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")
        with open('HLM.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for item in reader:
                if reader.line_num == 1:
                    continue
                print("当前行数：", reader.line_num, "当前内容：", item)
                start_node = Node("Person", name=item[0])
                end_node = Node("Person", name=item[1])
                relation = Relationship(start_node, item[2], end_node)
                self.graph.merge(start_node, "Person", "name")
                self.graph.merge(end_node, "Person", "name")
                self.graph.merge(relation, "Person", "name")
        # self.graph.run("MATCH (p:Person {name: '贾宝玉'})-[r]-(other) RETURN p, r, other")
        # self.graph.run("match (n) detach delete n")

    def build_paper_knowledge_graph(self):
        self.graph.run("match (n) detach delete n")
        self.graph = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")
        with open('paper.csv', 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for item in reader:

                if reader.line_num == 1:
                    continue
                print("当前行数：", reader.line_num, "当前内容：", item)
                start_node = Node("Paper", name=item[1])
                end_node = Node("Paper", name=item[3])
                relation = Relationship(start_node, item[4], end_node)
                self.graph.merge(start_node, "Paper", "name")
                self.graph.merge(end_node, "Paper", "name")
                self.graph.merge(relation, "Paper", "name")

    # def run(self):
    #     self.build_HLM_knowledge_graph()
    #     self.build_paper_knowledge_graph()
