import networkx as nx
import math
from src.orientation.DFS1.helpers import *


def dfs1(graph, v, height, parent_edge, adj_list, low_pt, low_pt_2, nesting_depth):
    e = parent_edge[v]
    for w, ori in adj_list[v].items():
        if ori == 'o':
            continue
        if ori == 'u':
            adj_list[v][w] = 'o'
            adj_list[w][v] = 'o'

        low_pt[(v, w)] = height[v]
        low_pt_2[(v, w)] = height[v]

        if height[w] == math.inf:
            parent_edge[w] = (v, w)
            height[w] = height[v] + 1
            dfs1(graph, w, height, parent_edge, adj_list, low_pt, low_pt_2, nesting_depth)
        else:
            low_pt[(v, w)] = height[w]

        nesting_depth[(v, w)] = 2 * low_pt[(v,w)]
        if low_pt_2[(v, w)] < height[v]:
            nesting_depth[(v, w)] = nesting_depth[(v, w)] + 1

        if not check_for_nan_tuple(e):
            if low_pt[(v, w)] < low_pt[e]:
                low_pt_2[e] = min(low_pt[e], low_pt_2[v, w])
                low_pt[e] = low_pt[(v, w)]
            elif low_pt[(v, w)] > low_pt[e]:
                low_pt_2[e] = min(low_pt_2[e], low_pt[(v, w)])
            else:
                low_pt_2[e] = min(low_pt_2[e], low_pt_2[(v, w)])


    # TODO: Wie orientiere ich eine edge? Idee: mit list_of_edges aus run.py abgleichen
