from src.visualization.BezierCurves.helpers import is_tree_edge_in_adj_list
from src.visualization.BezierCurves.helpers import add_subtree_leafes


def find_relevant_nodes(edge, sorted_tree_edges, target_node, parent_edge, final_adj_list, relevant_nodes, side):
    if edge[0] == target_node:
        return

    adj_list = final_adj_list[edge[0]]

    if side == 1:
        for e in adj_list[adj_list.index(edge)+1:]:
            if is_tree_edge_in_adj_list(e, sorted_tree_edges, edge[0]):
                add_subtree_leafes(e[1], sorted_tree_edges, relevant_nodes, side)

        find_relevant_nodes(parent_edge[edge[0]], sorted_tree_edges, target_node, parent_edge, final_adj_list, relevant_nodes, side)

    elif side == -1:
        for e in adj_list[:adj_list.index(edge)][::-1]:
            if is_tree_edge_in_adj_list(e, sorted_tree_edges, edge[0]):
                add_subtree_leafes(e[1], sorted_tree_edges, relevant_nodes, side)
        find_relevant_nodes(parent_edge[edge[0]], sorted_tree_edges, target_node, parent_edge, final_adj_list, relevant_nodes, side)
