import heapq
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt

adjList = {}
vertices = []

class GraphB:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = [[] for i in range(vertices)]

    def add_edge(self, first_node, second_node, weight):
        self.adjList[first_node].append([second_node, weight])
        self.adjList[second_node].append([first_node, weight])

    def generate_random_graph_edges_per_vertex(self, num_edges_per_vertex):
        for v in range(self.V):
            for i in range(1, num_edges_per_vertex+1):
                u = random.randint(0, self.V-1)
                while u==v:
                    u = random.randint(0, self.V-1)
                weight = random.randint(0, self.V-1)
                self.add_edge(v, u, weight)
    
    def generate_random_graph_total_edges(self, total_edges):
        edges = []
        while len(edges) < total_edges:
            u = random.randint(0, self.V-1)
            v = random.randint(0, self.V-1)
            if u!=v and [u, v] not in edges and [v, u] not in edges:
                weight = random.randint(0, self.V-1)
                self.add_edge(u, v, weight)
                edges.append([u, v])

    def Dijkstra(self, source):
        # S denotes if vertex has been visited
        S = [0 for i in range(self.V)]

        # d denotes the shortest distance from source
        d = [float('inf') for i in range(self.V)]
        d[source] = 0

        # pi denotes the predecessors for each vertex
        pi = [None for i in range(self.V)]
        
        minheap_pqueue = [[0, source]]

        while minheap_pqueue:
            distance, node = heapq.heappop(minheap_pqueue)

            if S[node] != 1:
                S[node] = 1

                for neighbours in self.adjList[node]:
                    neighbour_node = neighbours[0]
                    neighbour_weight = neighbours[1]
                    if S[neighbour_node] != 1:
                        new_dist = d[node] + neighbour_weight
                        if new_dist < d[neighbour_node]:
                            d[neighbour_node] = new_dist
                            pi[neighbour_node] = node
                            heapq.heappush(minheap_pqueue, [new_dist, neighbour_node])

        # print("Shortest distances from source node:")
        # vertex = 0
        # for distance in d:
        #     print(f"Vertex {vertex}: {distance}")
        #     vertex += 1
        return d
    
    

def time_wrt_edges():
    num_of_vertices = 500
    edges_per_vertex = []
    for x in range (300):
        edges_per_vertex.append(x+1)
    execution_time = []

    for i in edges_per_vertex:
        print("measure time taken for graph with edges " + str(i))
        graph = GraphB(num_of_vertices)
        graph.generate_random_graph_edges_per_vertex(i)
        start_time = timer()
        graph.Dijkstra(0)
        end_time = timer()
        execution_time.append(end_time-start_time)

    plt.plot(edges_per_vertex, execution_time, label='constanct |V| = 500')
    plt.title("time taken with respect to number of edges")
    plt.xlabel("Number of edges per vertex")
    plt.ylabel("Time taken")
    plt.show()


def time_wrt_vertices():
    num_of_vertices = []
    for x in range(2, 500+3):
        num_of_vertices.append(x)
    execution_time = []

    for i in num_of_vertices:
        print("measure time taken for graph with vertices " + str(i))
        graph = GraphB(300)
        graph.generate_random_graph_total_edges((i*(i-1))/2)
        start_time = timer()
        graph.Dijkstra(0)
        end_time = timer()
        execution_time.append(end_time-start_time)

    plt.plot(num_of_vertices, execution_time, label='constanct |E| = n(n-1)/2')
    plt.title("time taken with respect to number of vertices")
    plt.xlabel("Number of vertices")
    plt.ylabel("Time taken")
    plt.show()
