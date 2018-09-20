## script implementing naive O(mn) Dijkstra's algorithm

def load_graph():
    with open('downloads/dijkstra.txt') as f:
        data = f.readlines()
    graph = {}
    for row in data:
        row = row.split()
        graph[int(row[0])] = [tuple(map(int, x.split(','))) for x in row[1:]]
    return graph

G = load_graph()

def compute_min(A, G):
    min_node = None
    min_score = int(1e6)
    for node in A:
        for destination in G[node]:
            key, length = destination[0], destination[1]
            if key not in A:
                score = A[node] + length
                if score < min_score:
                    min_score = score
                    min_node = key
    return min_node, min_score

def dijkstra(G, s):
    ''' compute shortest paths from s to every other vertex in G '''

    # X = {s: True} # initialize X to include only s
    A = {s: 0} # initialize path length for s to s to be 0

    V = {} # let V be the set of vertices not processed yet
    for v in list(G.keys()): # initialize V to be everything except s
        if v != s:
            V[v] = True

    while V:
        min_node, min_score = compute_min(A,G)

        if min_node is None:
            break

        # min_node, min_score contains w*, and edge (v*, w*) through exhaustive searching
        A[min_node] = min_score
        del V[min_node]

    return A

A = dijkstra(G, 1)
for dest in [7,37,59,82,99,115,133,165,188,197]:
    print(A[dest])
# first try beauty!
