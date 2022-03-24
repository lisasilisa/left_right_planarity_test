from src.testing.helpers import *
from src.testing.DFS2.dfs2 import *
from src.testing.stack import Stack


def test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref, side):
    sorted_adj_list = sort_adj_list(graph, nesting_depth)
    stack_bottom = {}
    stack = Stack()
    low_pt_edge = {}
    for s in roots:
        planar = dfs2(s, sorted_adj_list, parent_edge, stack_bottom, stack, low_pt_edge, low_pt, low_pt_2, height, ref, side)
        print("sorted_adj_list testing", sorted_adj_list)
        if not planar:
            return False
        print('low_pt_edge', low_pt_edge)
        print('stack_bottom', stack_bottom)
    return True
