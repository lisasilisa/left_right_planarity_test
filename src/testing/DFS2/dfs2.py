from src.testing.DFS2.add_constraints import *
from src.testing.DFS2.trim_back_edges import *


def dfs2(v, sorted_adj_list, parent_edge, stack_bottom, stack, low_pt_edge, low_pt, low_pt_2, height, ref, side):
    e = parent_edge[v]
    for e_i in sorted_adj_list[v]:
        stack_bottom[e_i] = stack.top()
        if e_i == parent_edge[e_i[1]]:
            planar = dfs2(e_i[1], sorted_adj_list, parent_edge, stack_bottom,
                          stack, low_pt_edge, low_pt, low_pt_2, height, ref, side)
            if not planar:
                return False
        else:
            low_pt_edge[e_i] = e_i
            stack.push([[(math.nan, math.nan), (math.nan, math.nan)], [e_i, e_i]])
        if low_pt[e_i] < height[v]:
            if e_i == sorted_adj_list[v][0]:
                low_pt_edge[e] = low_pt_edge[e_i]
            else:
                planar = add_constraints(e_i, e, stack, stack_bottom, low_pt, low_pt_edge, ref)
                if not planar:
                    return False

    if not check_for_nan_tuple(e):
        u = e[0]
        trim_back_edges(u, stack, height, low_pt, ref, side)

        # side of e is side of a highest return edge
        if low_pt[e] < height[u]:
            h_L = stack.top()[0][1]
            h_R = stack.top()[1][1]
            if not check_for_nan_tuple(h_L) and (check_for_nan_tuple(h_R) or low_pt[h_L] > low_pt[h_R]):
                ref[e] = h_L
            else:
                ref[e] = h_R

    return True
