#Uses python3

import sys


# Python3 program for the above approach

# Structure to represent a weighted
# edge in graph
class Edge:
    def __init__(self):
        self.src = 0
        self.dest = 0
        self.weight = 0


# Structure to represent a directed
# and weighted graph
class Graph:

    def __init__(self):
        # V. Number of vertices, E.
        # Number of edges
        self.V = 0
        self.E = 0

        # Graph is represented as
        # an array of edges.
        self.edge = []


# Creates a new graph with V vertices
# and E edges
def createGraph(V, E):
    graph = Graph();
    graph.V = V;
    graph.E = E;
    graph.edge = [Edge() for i in range(graph.E)]
    return graph;


# Function runs Bellman-Ford algorithm
# and prints negative cycle(if present)
def NegCycleBellmanFord(graph, src):
    V = graph.V;
    E = graph.E;
    dist = [1000000 for i in range(V)]
    parent = [-1 for i in range(V)]
    dist[src] = 0;

    # Relax all edges |V| - 1 times.
    for i in range(1, V):
        for j in range(E):

            u = graph.edge[j].src;
            v = graph.edge[j].dest;
            weight = graph.edge[j].weight;

            if (dist[u] != 1000000 and
                    dist[u] + weight < dist[v]):
                dist[v] = dist[u] + weight;
                parent[v] = u;

    # Check for negative-weight cycles
    C = -1;
    for i in range(E):
        u = graph.edge[i].src;
        v = graph.edge[i].dest;
        weight = graph.edge[i].weight;

        if (dist[u] != 1000000 and
                dist[u] + weight < dist[v]):
            # Store one of the vertex of
            # the negative weight cycle
            C = v;
            break;

    if (C != -1):
        for i in range(V):
            C = parent[C];

        # To store the cycle vertex
        cycle = []
        v = C

        while (True):
            cycle.append(v)
            if (v == C and len(cycle) > 1):
                break;
            v = parent[v]

        # Reverse cycle[]
        cycle.reverse()

        # Printing the negative cycle
        #for v in cycle:
            # print(v, end=" ");
        # print()
        return 1
    else:
        return 0


# Driver Code



# This code is contributed by Pratham76


def negative_cycle(graph):
    #write your code here

    return NegCycleBellmanFord(graph, 0)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    graph = createGraph(n, m)
    for ix, ((a, b), w) in enumerate(edges):
        graph.edge[ix].src=a-1
        graph.edge[ix].dest=b-1
        graph.edge[ix].weight=w
    print(negative_cycle(graph))
