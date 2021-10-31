import networkx as nx
import math
from src.orientation.DFS1.helpers import *


def dfs1(graph, v, height, parent_edge, adj_list, low_pt, low_pt_2, nesting_depth):
    e = parent_edge[v]
    for w, ori in adj_list[v].items():
        for i in ori:
            if ori[i] == 'o':
                continue
            if ori[i] == 'u':
                adj_list[v][w][i] = 'o'
                adj_list[w][v][i] = 'o'

            low_pt[(v, w, i)] = height[v]
            low_pt_2[(v, w, i)] = height[v]

            if height[w] == math.inf:
                parent_edge[w] = (v, w, i)
                height[w] = height[v] + 1
                dfs1(graph, w, height, parent_edge, adj_list, low_pt, low_pt_2, nesting_depth)
            else:
                low_pt[(v, w, i)] = height[w]

            nesting_depth[(v, w, i)] = 2 * low_pt[(v, w, i)]
            if low_pt_2[(v, w, i)] < height[v]:
                nesting_depth[(v, w, i)] = nesting_depth[(v, w, i)] + 1

            if not check_for_nan_tuple(e):
                if low_pt[(v, w, i)] < low_pt[e]:
                    low_pt_2[e] = min(low_pt[e], low_pt_2[(v, w, i)])
                    low_pt[e] = low_pt[(v, w, i)]
                elif low_pt[(v, w, i)] > low_pt[e]:
                    low_pt_2[e] = min(low_pt_2[e], low_pt[(v, w, i)])
                else:
                    low_pt_2[e] = min(low_pt_2[e], low_pt_2[(v, w, i)])
