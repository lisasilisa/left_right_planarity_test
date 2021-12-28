import math
import copy
from src.embedding.helpers import *
from src.embedding.DFS3.dfs3 import *


def embed(graph, roots, nesting_depth, parent_edge, ref, side, left_ref, right_ref):
    for e in nesting_depth:
        nesting_depth[e] *= sign(e, ref, side)
    sorted_adj_list = sort_adj_lists(graph, nesting_depth)
    final_adj_list = copy.deepcopy(sorted_adj_list)
    for s in roots:
        dfs3(s, sorted_adj_list, final_adj_list, parent_edge, left_ref, right_ref, side)
    return final_adj_list
