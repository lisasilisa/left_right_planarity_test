def get_dfs_tree_edges(final_adj_list, parent_edge):
    sorted_tree_edges = {}
    for node in final_adj_list:
        sorted_tree_edges[node] = []
        for edge in final_adj_list[node]:
            if edge[0] == node and edge == parent_edge[edge[1]]:
                sorted_tree_edges[node].append(edge)

    return sorted_tree_edges
