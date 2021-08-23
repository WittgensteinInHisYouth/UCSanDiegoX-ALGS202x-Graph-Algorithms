#Uses python3

import sys

def reach(adj, x, y):
    #write your code here

    def explore(vertice):
        visited_marker[vertice] = True

        for adj_node in adj[vertice]:
            if not visited_marker[adj_node]:
                explore(adj_node)

    num_nodes = len(adj)
    visited_marker = [False for _ in range(num_nodes)]
    explore(x)
    return int(visited_marker[y])




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, x, y))
