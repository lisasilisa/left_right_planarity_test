import networkx as nx
from src.visualization.BezierCurves.bezier_point_for_no_relevant_nodes import *
from src.visualization.BezierCurves.helpers import *


def determine_bezier_points(graph, back_edge, relevant_nodes, parent_edge, final_adj_list, sorted_tree_edges, height,
                            side, leaf):
    position = nx.get_node_attributes(graph, 'pos')

    height_diff = height[back_edge[0]] - height[back_edge[1]]
    hdc = height_diff / 1.8
    # print('hdc', hdc)

    bezier_coords = [[], []]
    bezier_coords[0].append(position[back_edge[0]][0])
    bezier_coords[1].append(position[back_edge[0]][1])

    if not relevant_nodes:  # wenn es gar keinen relevant node gibt, braucht man aber trotzdem eine kleine
        # Verschiebung der Rückkante, sodass Rückkante nicht auf DFS Kanten liegt
        bezier_point_for_no_relevant_nodes(bezier_coords, back_edge[0], back_edge[1], position, side, hdc)
    else:
        if not leaf:  # wenn die Rükkante nicht bei einem Blattknoten startet, muss man nachfolgende Knoten betrachten
            next_tree_edges = get_next_tree_edges(back_edge, final_adj_list[back_edge[0]], sorted_tree_edges)

            # nur dann eine zur Seite rücken, wenn nachfolgende tree_nodes auch relevant_nodes sind
            if next_tree_edges and (next_tree_edges[0][1] in relevant_nodes):
                # side*-1 weil Ausrichtung des Normalenvektor genau entgegengesetzt zu Normalenvektor bei Rückkanten
                # ohne relevant_nodes
                bezier_point_for_no_relevant_nodes(bezier_coords, back_edge[0], next_tree_edges[0][1], position,
                                                   side * -1, hdc)

        counter = 6
        for rn in relevant_nodes:
            p = position[parent_edge[rn][0]]
            q = position[rn]
            xcoord = (q[0] - p[0]) * hdc * (counter / 2) + p[0]
            ycoord = (q[1] - p[1]) * hdc * (counter / 2) + p[1]

            bezier_coords[0].append(xcoord)
            bezier_coords[1].append(ycoord)
            counter = counter + 2.5

    bezier_coords[0].append(position[back_edge[1]][0])
    bezier_coords[1].append(position[back_edge[1]][1])

    print('bezier_coords', bezier_coords)
    return bezier_coords
