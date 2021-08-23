#Uses python3

import sys
import queue
import networkx as nx
from networkx.algorithms import bipartite as bi


def bipartite(adj):
    #write your code here
    G = nx.Graph()
    for vertice in range(len(adj)):
        for next_vertice in adj[vertice]:
            G.add_edge(vertice, next_vertice)

    return int(bi.is_bipartite(G))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
