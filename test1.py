import csv
from py2neo import Graph, Node, Relationship, NodeMatcher
import py2neo  # py2neo是Python代码操作neo4j的库，类似于jdbc

g = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")
with open('../Graph_Generator/KnowledgeGraph/HLM.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for item in reader:

        if reader.line_num == 1:
            continue
        print("当前行数：", reader.line_num, "当前内容：", item)
        start_node = Node("Person", name=item[0])
        end_node = Node("Person", name=item[1])
        relation = Relationship(start_node, item[3], end_node)
        g.merge(start_node, "Person", "name")
        g.merge(end_node, "Person", "name")
        g.merge(relation, "Person", "name")
# g.run("match (n) detach delete n")
