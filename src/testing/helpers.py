def get_sorted_edges_for_v(nesting_depth, n):
    v_dict = {}
    for v, w in nesting_depth:
        if n == v:
            v_dict[(v, w)] = nesting_depth[(v, w)]
    v_dict_sorted = {k: v for k, v in sorted(v_dict.items(),
                                             key=lambda item: item[1])} # sort v_dict by keys
    return list(v_dict_sorted.keys())


def sort_adj_list(graph, nesting_depth):
    sorted_adj = {}
    for n in graph.nodes:
        sorted_adj[n] = get_sorted_edges_for_v(nesting_depth, n)
    return sorted_adj
