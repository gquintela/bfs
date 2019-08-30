from bfs import *

# create dummy graph & driver test
my_graph = Graph()
my_graph.add_directed_edge('r', 's')
my_graph.add_directed_edge('t', 'u')
my_graph.add_directed_edge('w', 'x')
my_graph.add_directed_edge('x', 'y')
my_graph.add_directed_edge('r', 'v')
my_graph.add_directed_edge('s', 'w')
my_graph.add_directed_edge('t', 'x')
my_graph.add_directed_edge('u', 'y')
my_graph.add_directed_edge('t', 'w')
my_graph.add_directed_edge('u', 'x')

bfs_result = bfs(my_graph,'s')
print ("List of parents")
print(bfs_result[0])
print ("")

print ("List of distance from " + 's')
print(bfs_result[1])
print ("")

shortest_path(my_graph, 's', 'y')
