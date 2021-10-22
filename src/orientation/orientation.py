import math
from src.orientation.DFS1.dfs1 import *
from src.orientation.helpers import *


def orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth):
    adj_list = generate_whole_adj_list(graph)
    # print(adj_list)
    for v in graph.nodes:
        if height[v] == math.inf:
            height[v] = 0
            # print(height)
            roots.append(v)
            dfs1(graph, v, height, parent_edge, adj_list, low_pt, low_pt_2, nesting_depth)
