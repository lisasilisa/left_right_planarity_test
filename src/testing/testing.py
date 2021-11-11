from src.testing.helpers import *
from src.testing.DFS2.dfs2 import *
from src.testing.stack import Stack


def test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref):
    sorted_adj_lists = sort_adj_lists(graph, nesting_depth)
    stack_bottom = {}
    stack = Stack()
    low_pt_edge = {}
    for s in roots:
        dfs2(s, sorted_adj_lists, parent_edge, stack_bottom, stack, low_pt_edge, low_pt, low_pt_2, height, ref)
