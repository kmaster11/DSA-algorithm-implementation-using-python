# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:15:09 2023

@author: kiran
"""

import sys

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)

if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[5, 0, 9, 0, 0, 0, 0, 0, 0],  
               [0, 0, 1, 2, 0, 0, 0, 0, 0],
               [9, 1, 0, 0, 4, 0, 0, 0, 0],
               [0, 2, 0, 0, 5, 0, 0, 0, 0],
               [0, 0, 4, 5, 0, 6, 7, 0, 0],
               [0, 0, 0, 0, 6, 0, 2, 0, 0],
               [0, 0, 0, 0, 7, 2, 0, 4, 0],
               [0, 0, 0, 0, 0, 0, 4, 0, 8],
               [0, 0, 0, 0, 0, 0, 0, 8, 0]]

    g.dijkstra(0)  # Starting vertex
if __name__ == "__main__":
    g = Graph(3)
    g.graph = [[2,2,4,5,6],  
               [0,0,10,5,0],
               [6,4,0,0,1],
               [8,5,4,9,0],
               [0,5,2,9,3]]
               
               
    g.dijkstra(0)  # Starting vertex
