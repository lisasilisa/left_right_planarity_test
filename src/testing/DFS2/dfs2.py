import math
from src.testing.DFS2.add_constraints import *


def dfs2(v, sorted_adj_list, parent_edge, stack_bottom, stack, low_pt_edge, low_pt, low_pt_2, height, ref):
    e = parent_edge[v]
    for e_i in sorted_adj_list[v]:
        stack_bottom[e_i] = stack.top()
        if e_i == parent_edge[e_i[1]]:
            dfs2(e_i[1], sorted_adj_list, parent_edge, stack_bottom, stack, low_pt_edge, low_pt, low_pt_2, height, ref)
        else:
            low_pt_edge[e_i] = e_i
            stack.push([[(math.nan, math.nan, math.nan), (math.nan, math.nan, math.nan)], [e_i, e_i]])

        if low_pt[e_i] < height[v]:
            if e_i == sorted_adj_list[v][0]:
                low_pt_edge[e] = low_pt_edge[e_i]
            else:
                add_constraints(e_i, e, stack, stack_bottom, low_pt, low_pt_edge, ref)

    if not check_for_nan_tuple(e):
        pass