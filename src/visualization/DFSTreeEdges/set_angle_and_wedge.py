

def set_angle_and_wedge(sorted_tree_edges, node, wedge, angle):
    amount_of_child_nodes = len(sorted_tree_edges[node])
    ang = angle[node]
    for edge in sorted_tree_edges[node][::-1]:
        w = edge[1]
        wedge[w] = wedge[node] / amount_of_child_nodes
        angle[w] = ang
        ang = ang + wedge[w]
        set_angle_and_wedge(sorted_tree_edges, w, wedge, angle)