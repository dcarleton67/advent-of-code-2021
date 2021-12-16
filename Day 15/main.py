with open('Day 15/input.txt') as f:
    risk_levels = [[int(risk) for risk in list(line.strip())] for line in f.readlines()]

class Node:
    def __init__(self, position, weight, distance):
        self.position = position
        self.weight = weight
        self.distance = distance
        self.neighbors = []

    def __lt__(self, other):
        return self.distance < other.distance

    def add_neighbors(self, other):
        self.neighbors = other.neighbors

def create_graph(risk_levels):
    graph = []

    for i in range(len(risk_levels)):
        for j in range(len(risk_levels[0])):
            if i == 0 and j == 0:
                graph.append(Node((i, j), risk_levels[i][j], 0))
            else:
                # the furthest away a Node could possibly be is 9 * 100 * 100 (probably lower?)
                graph.append(Node((i, j), risk_levels[i][j], 9 * 100 * 100))

    for node_idx, node in enumerate(graph):
        # above is node_idx - len(risk_levels)
        if node_idx - len(risk_levels) >= 0: node.neighbors.append(graph[node_idx - len(risk_levels)])
        # left is node_idx - 1
        if node_idx % len(risk_levels): node.neighbors.append(graph[node_idx - 1])
        # right is node_idx + 1
        if (node_idx + 1) % len(risk_levels): node.neighbors.append(graph[node_idx + 1])
        # below is node_idx + len(risk_levels)
        if (node_idx + len(risk_levels)) < (len(risk_levels) * len(risk_levels[0])): node.neighbors.append(graph[node_idx + len(risk_levels)])
        # why did I do it like this

    return graph

def heappop(heap):
    val = heap[0]
    # put largest element on top then sift it down
    largest = heap.pop()
    size = len(heap)
    if size == 0: return val # only one value

    heap[0] = largest
    idx = 0
    while True:
        child_1 = 2 * idx + 1
        child_2 = 2 * idx + 2
        if child_1 >= size: return val # children are past the end of the array - they don't exist

        smallest_child = child_2 if child_2 < size and heap[child_2].distance < heap[child_1].distance else child_1
        if heap[idx].distance <= heap[smallest_child].distance: return val # we are in the right order
        # otherwise we have to swap
        heap[smallest_child], heap[idx] = heap[idx], heap[smallest_child]
        idx = smallest_child

def heappush(heap, ele):
    idx = len(heap)
    heap.append(ele)
    while True:
        if idx == 0: return # we've pushed onto an empty heap or we are the largest element
        parent = (idx - 1) // 2

        if heap[idx].distance >= heap[parent].distance: return # we are in the right order
        # otherwise we have to swap
        heap[parent], heap[idx] = heap[idx], heap[parent]
        idx = parent


def dijkstra(graph, dim):
    searched = set()
    min_dist = [graph[0]]
    while len(min_dist):
        cur_node = heappop(min_dist)
        if cur_node.position in searched:
            continue 
    
        searched.add(cur_node.position)
    
        if cur_node.position == (dim - 1, dim - 1):
            return cur_node.distance

        for neighbor_node in cur_node.neighbors:
            if cur_node.distance + neighbor_node.weight < neighbor_node.distance:
                new_node = Node(neighbor_node.position, neighbor_node.weight, cur_node.distance + neighbor_node.weight)
                new_node.add_neighbors(neighbor_node)
                heappush(min_dist, new_node)

graph = create_graph(risk_levels)
print(dijkstra(graph, len(risk_levels)))

bigger_risk_levels = []
for i in range(5):
    for row in risk_levels:
        bigger_row = []
        for j in range(5):
            for risk in row:
                bigger_val = risk + i + j
                bigger_val = bigger_val - 9 if bigger_val > 9 else bigger_val
                bigger_row.append(bigger_val)
        bigger_risk_levels.append(bigger_row)

bigger_graph = create_graph(bigger_risk_levels)
print(dijkstra(bigger_graph, 5 * len(risk_levels)))