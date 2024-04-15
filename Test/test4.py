import csv
from py2neo import Graph, Node, Relationship

# graph.run("match (n) detach delete n")
graph = Graph('http://localhost:7474', user='neo4j', password='20040304', name="neo4j")
with open('hlm.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for item in reader:
        print("当前行数：", reader.line_num, "当前内容：", item)
        start_node = Node("Person", name=item[0])
        end_node = Node("Person", name=item[1])
        relation = Relationship(start_node, item[2], end_node)
        graph.merge(start_node, "Person", "name")
        graph.merge(end_node, "Person", "name")
        graph.merge(relation, "Person", "name")
