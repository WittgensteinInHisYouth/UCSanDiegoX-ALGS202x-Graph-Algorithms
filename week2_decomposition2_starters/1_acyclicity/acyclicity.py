#Uses python3

import sys
import networkx as nx
def acyclic(adj):
    G = nx.DiGraph()
    for vertice in range(len(adj)):
        for next_vertice in adj[vertice]:
            G.add_edge(vertice, next_vertice)

    try:
        nx.find_cycle(G)
        return 1
    except nx.exception.NetworkXNoCycle:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
