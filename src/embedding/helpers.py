import math


def check_for_nan_tuple(t):
    return t[0] != t[0] and t[1] != t[1]  # and t[2] != t[2] muss raus


def sign(e, ref, side):
    if not check_for_nan_tuple(ref[e]):
        side[e] *= sign(ref[e], ref, side)
        ref[e] = (math.nan, math.nan)  # math.nan muss raus
    return side[e]


def get_sorted_edges_from_same_v(nesting_depth, n):
    """

    for v, w, i in nesting_depth:
        if n == v:
            v_dict[(v, w, i)] = nesting_depth[(v, w, i)]
    v_dict_sorted = {k: v for k, v in sorted(v_dict.items(), key=lambda item: item[1])} # sort v_dict by keys
    return list(v_dict_sorted.keys())
    """
    v_dict = {}
    for v, w in nesting_depth:
        if n == v:
            v_dict[(v, w)] = nesting_depth[(v, w)]
    v_dict_sorted = {k: v for k, v in sorted(v_dict.items(), key=lambda item: item[1])}  # sort v_dict by keys
    return list(v_dict_sorted.keys())


def sort_adj_lists(graph, nesting_depth):
    sorted_adj = {}
    for n in graph.nodes:
        sorted_adj[n] = get_sorted_edges_from_same_v(nesting_depth, n)
    return sorted_adj
