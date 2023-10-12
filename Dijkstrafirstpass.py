# define a linked list
class LinkedList:
    # declared within a class and used to initialise the attributes of an object as soon as it is formed
    def __init__(self):
        self.head = None
        # currently there are no nodes, so the head of the list points to NULL

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    def sizeofLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0

    def returnValueatIndex(self, index):
        tempi = 0
        current_node = self.head
        while current_node:
            if tempi == index:
                return current_node.data
            else:
                tempi += 1
                current_node = current_node.next

    def findWeight(self, item):
        current_node = self.head
        while current_node:
            if current_node.data[0] == item:
                return current_node.data[1]
            else:
                current_node = current_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# USER INPUT - TESTING
# create an adjacency list for the graph. first, input the number of vertices
number_vertices = int(input("Number of vertices?"))
adjacency_list = []
for i in range(0, number_vertices):  # for each vertex, create the corresponding linked list
    adjacency_list.append(LinkedList())
    print("Now filling list for vertex {}".format(i+1))
    number_connectors = int(input("How many neighbours from this vertex?"))
    print("Inserting neighbours:")
    for j in range(0, number_connectors):
        neighbour_vertex = int(input("Neighbouring Vertex:"))
        weight = int(input("Weight:"))
        adjacency_list[i].insertAtEnd([neighbour_vertex, weight])

print("Adjacency list created. Confirm?")
for i in range(0, number_vertices):
    print("for vertex {}:".format(i+1), end=" ")
    adjacency_list[i].printLL()
# Graph has been created


# METHOD/FUNCTION DEFINITIONS FOR A MINIMISING HEAP (from an arbitrary array; for a priority queue)
def build_a_min_heap(arr):
    i = int(len(arr)/2) - 1
    while i >= 0:
        min_heapify(arr, i)
        i -= 1


def insertion_heap(arr, i):
    i = int((i+1)/2) - 1
    while i >= 0:
        min_heapify(arr, i)
        i = int((i+1)/2) - 1


def min_heapify(arr, i):  # or fix heap
    l = (2*(i+1)) - 1  # left child
    r = (2*(i+1))  # right child
    if l >= len(arr) or r >= len(arr):  # if we are at the leaves, return immediately
        return

    if arr[l][1] < arr[r][1]:
        smallest = l
    else:
        smallest = r

    if arr[smallest][1] < arr[i][1]:
        temp = arr[i]
        arr[i] = arr[smallest]
        arr[smallest] = temp
        min_heapify(arr, smallest)


def extract_min(arr):
    min = arr[0][0]
    arr[0] = arr[len(arr) - 1]
    arr.pop(len(arr)-1)  # delete element at that index.
    min_heapify(arr, 0)
    return min


def return_distance(dist, v):
    for i in range(0, len(dist)):
        if dist[i][0] == v:
            return dist[i][1]


def return_index(dist, v):
    for i in range(0, len(dist)):
        if dist[i][0] == v:
            return i


# DIJKSTRA'S ALGORITHM
def dijkstra(num_vertices, source, destination, adjacency_list):
    dist = []
    prev = []  # or parent pointer
    S = []  # for exploration
    limit_bound = 999999999
    for i in range(0, num_vertices):
        dist[i] = [i+1, limit_bound]
        prev[i] = None

    dist[source - 1][1] = 0
    build_a_min_heap(dist)
    while num_vertices - len(S) > 0:
        u = extract_min(dist)
        S.append(u)
        if u == destination:
            break
        dist_u = return_distance(dist, u)
        for i in range(0, adjacency_list[u-1].sizeofLL()):
            v = adjacency_list[u-1].returnValueatIndex(i)
            v_index = S.index(u) if u in S else -1  # exception handling

            v_dist_index = return_index(dist, v)
            weight_u_v = adjacency_list[v-1].findWeight(v)
            if v_index == -1 and dist_u + weight_u_v < dist[v_dist_index][1]:
                dist[v_dist_index][1] = dist_u + weight_u_v
                prev[v-1] = u
                insertion_heap(dist, v_dist_index)
    print("distance from {} to {}: ".format(source, destination) + return_distance(dist, destination))
    print("Shortest path:")
    k = destination
    while k != source:
        print("{} -> ".format(prev[k]), end="")
        k = prev[k]


# ================MAIN==================
dijkstra(number_vertices, 1, 3, adjacency_list)
