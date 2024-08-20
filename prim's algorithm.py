# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 00:33:13 2023

@author: kiran
"""


INF = 9999999

V = 5

G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]S

selected = [0, 0, 0, 0, 0]

no_edge = 0

selected[0] = True

print("Edge : Weight\n")
while (no_edge < V - 1):

    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):

                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1

"""
#Test case 1

G = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

Test case 2

G = [
    [0, 1, 3, 0,4],
    [1, 0, 3, 4,5],
    [3, 2, 0, 1,7],
    [0, 5, 4, 0,9],
    [0, 8, 7, 9, 0]
]



"""