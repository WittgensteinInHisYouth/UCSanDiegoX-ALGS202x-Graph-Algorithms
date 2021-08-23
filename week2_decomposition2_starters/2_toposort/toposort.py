#Uses python3

import sys
import networkx as nx

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    #write your code here

    G = nx.DiGraph()
    for vertice in range(len(adj)):
        for next_vertice in adj[vertice]:
            G.add_edge(vertice, next_vertice)


    return list(nx.topological_sort(G))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

