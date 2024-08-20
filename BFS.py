# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:12:50 2023

@author: kiran
"""
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}


def bfs(node):
    visited = [False] * (len(graph))
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:

        v = queue.pop(0)
        print(v, end=" ")

        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


bfs('A')
"""graph1 = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['C'],
    'G': ['D']
}


bfs('A', graph1)
"""


"""graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

bfs('A', graph2)
"""