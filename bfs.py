from graph import Graph
import queue

infinite = 999999


# v has to be in the graph
def bfs(graph, v):
    vertices = graph.get_vertices();
    vertices_status = {}
    q = queue.Queue()
    distance = {}
    parent = {}
    for vertex in vertices:
        vertices_status[vertex] = 0
        if vertex != v:
            distance[vertex] = infinite
            parent[vertex] = 'nil'
        else:
            distance[vertex] = 0
            parent[vertex] = vertex
            vertices_status[vertex] = 1
    q.put(v)
    while not q.empty():
        u = q.get()
        for v in graph.get_neighbours(u):
            if vertices_status[v] == 0:
                vertices_status[v] = 1
                distance[v] = distance[u] + 1
                parent[v] = u
                q.put(v)
        vertices_status[u] = 1

    return [parent, distance]


def shortest_path(graph, s, v):
    structure = bfs(graph, s)
    vertex = v
    times = structure[1][v] + 1
    output = []
    for i in range(times):
        output.insert(0, vertex)
        vertex = structure[0][vertex]
    print (output)
    print ("The distance from " + s + " to " + v + " is " + str((times - 1)))
    return output
