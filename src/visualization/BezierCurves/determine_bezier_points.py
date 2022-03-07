import networkx as nx
from src.visualization.BezierCurves.bezier_point_for_no_relevant_nodes import *
from src.visualization.BezierCurves.helpers import *


def determine_bezier_points(graph, back_edge, relevant_nodes, parent_edge, final_adj_list, sorted_tree_edges, height,
                            side, leaf):

    position = nx.get_node_attributes(graph, 'pos')

    height_diff = height[back_edge[0]] - height[back_edge[1]]
    hdc1 = height_diff / 1.3
    hdc2 = height_diff / 1.8
    hdc3 = height_diff / 4
    # print('hdc', hdc)

    bezier_coords = [[], []]
    bezier_coords[0].append(position[back_edge[0]][0])
    bezier_coords[1].append(position[back_edge[0]][1])

    if not relevant_nodes:
        # wenn es gar keinen relevant node gibt, braucht man aber trotzdem eine kleine
        # Verschiebung der Rückkante, sodass Rückkante nicht auf DFS Kanten liegt
        # hdc am geringsten gewertet, da diese Backedeges sich meistens weiter innen befinden
        bezier_point_for_no_relevant_nodes(bezier_coords, back_edge[0], back_edge[1], position, side, hdc3)
    else:
        if not leaf:
            # wenn man nicht bei einem Blatt beginnt, dann Bogen von Start der Backedge zum ersten relevant node
            # side*-1 weil Ausrichtung des Normalenvektor genau entgegengesetzt zu Normalenvektor bei Backedges
            bezier_point_for_no_relevant_nodes(bezier_coords, back_edge[0], relevant_nodes[0], position, side*-1, hdc1)

            # doppelter Code, da für Backedges die bei keinem Blatt beginnen, andere Parameter gelten sollen
            # da diese Backedges noch eher um andere herum verlaufen müssen, werden height_diff und counter mehr
            # gewertet
            counter = 6
            for rn in relevant_nodes:
                p = position[parent_edge[rn][0]]
                q = position[rn]
                xcoord = (q[0] - p[0]) * hdc1 * (counter / 2) + p[0]
                ycoord = (q[1] - p[1]) * hdc1 * (counter / 2) + p[1]

                bezier_coords[0].append(xcoord)
                bezier_coords[1].append(ycoord)
                counter = counter + 2.5

        else:
            counter = 5
            for rn in relevant_nodes:
                p = position[parent_edge[rn][0]]
                q = position[rn]
                xcoord = (q[0] - p[0]) * hdc2 * (counter / 2) + p[0]
                ycoord = (q[1] - p[1]) * hdc2 * (counter / 2) + p[1]

                bezier_coords[0].append(xcoord)
                bezier_coords[1].append(ycoord)
                counter = counter + 1

        # für alle Backedges Bogen vom letzten relevant node zum Endpunkt der Backedge
        bezier_point_for_no_relevant_nodes(bezier_coords, relevant_nodes[-1], back_edge[1], position, side, hdc1)

    bezier_coords[0].append(position[back_edge[1]][0])
    bezier_coords[1].append(position[back_edge[1]][1])

    return bezier_coords
