import math


def set_coordinates(graph, sorted_tree_edges, node, coord, wedge, angle):
    for edge in sorted_tree_edges[node]:
        w = edge[1]
        p = coord[node]
        newx = p[0] + math.cos(math.radians(angle[w] + (wedge[w] / 2)))
        newy = p[1] + math.sin(math.radians(angle[w] + (wedge[w] / 2)))
        coord[w] = (newx, newy)

        graph.add_node(w, pos=coord[w], label=w)
        graph.add_edge(node, w)

        set_coordinates(graph, sorted_tree_edges, w, coord, wedge, angle)
