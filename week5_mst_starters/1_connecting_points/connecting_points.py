#Uses python3
import sys
import math
import networkx as nx
import  numpy as np

def minimum_distance(x, y):
    result = 0.
    #write your code here


    num_vertices = len(x)
    G = nx.Graph()
    for vertice in range(num_vertices):
        for next_vertice in range(vertice+1, num_vertices):
            G.add_edge(vertice, next_vertice,
                       weight=np.sqrt((x[vertice] - x[next_vertice])**2 + (y[vertice]-y[next_vertice])**2))

    T = nx.minimum_spanning_tree(G)

    return T.size(weight="weight")


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
