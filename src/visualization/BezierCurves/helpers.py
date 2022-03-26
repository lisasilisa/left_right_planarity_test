def is_tree_edge_in_adj_list(edge, sorted_tree_edges, node):
    if edge in sorted_tree_edges[node]:
        return True
    else:
        return False


def add_subtree_leafes(node, sorted_tree_edges, relevant_nodes, side):
    # wenn Liste leer, dann Blattknoten zu relevant_nodes hinzufügen
    if not sorted_tree_edges[node]:
        relevant_nodes.append(node)

    if side == 1:
        for edge in sorted_tree_edges[node]:
            add_subtree_leafes(edge[1], sorted_tree_edges, relevant_nodes, side)

    elif side == -1:
        for edge in sorted_tree_edges[node][::-1]:
            add_subtree_leafes(edge[1], sorted_tree_edges, relevant_nodes, side)


def is_leaf(node, sorted_tree_edges):
    if not sorted_tree_edges[node]: #leere Liste, also keine Folgeknoten
        return True
    else:
        return False


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def get_next_tree_edges(back_edge, adj_list, sorted_tree_edges):
    adj_sublist = []
    for idx, edge in enumerate(adj_list):
        if edge == back_edge:
            adj_sublist = adj_list[idx + 1:]
    next_tree_edges = intersection(adj_sublist, sorted_tree_edges[back_edge[0]])
    return next_tree_edges
