import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import ctypes

#bezier = ctypes.cdll.LoadLibrary(
#    r"C:\Users\lisas\anaconda3\envs\Studienprojekt\Lib\site-packages\bezier\extra-dll\bezier-2a44d276.dll")
import bezier

from src.visualization.BezierCurves.find_relevant_nodes import *
from src.visualization.BezierCurves.determine_bezier_points import *
from src.visualization.BezierCurves.helpers import *


def draw_bezier_curves(graph, ax, final_adj_list,
                       sorted_tree_edges, parent_edge, height, side):

    position = nx.get_node_attributes(graph, 'pos')
    nodes = nx.draw_networkx_nodes(graph, position, node_size=200,
                                   node_color='lightgray', ax=ax)
    labels = nx.draw_networkx_labels(graph, position,
                                     labels={n: n for n in graph}, ax=ax)
    edges = nx.draw_networkx_edges(graph, position, ax=ax)
    nodes.set_zorder(20)
    for label in labels:
        labels[label].set_zorder(25)

    for node in list(graph.nodes):
        for back_edge in final_adj_list[node]:
            if back_edge not in sorted_tree_edges[back_edge[0]] and back_edge[0] == node:
                target_node = back_edge[1]
                relevant_nodes = []
                find_relevant_nodes(back_edge, sorted_tree_edges, target_node, parent_edge, final_adj_list,
                                    relevant_nodes,
                                    side[back_edge])

                # wenn Rückkante von einem Blatt startet: Flag leaf = True
                if is_leaf(back_edge[0], sorted_tree_edges):
                    bezier_coords = determine_bezier_points(graph, back_edge, relevant_nodes, parent_edge, height, side[back_edge], True)

                # wenn Rückkante von keinem Blatt startet: Flag leaf = False
                else:
                    bezier_coords = determine_bezier_points(graph, back_edge, relevant_nodes, parent_edge, height, side[back_edge], False)

                nodes = np.asfortranarray(bezier_coords)
                curve = bezier.Curve(nodes, degree=len(bezier_coords[0]) - 1)
                if side[back_edge] == 1:
                    curve.plot(num_pts=1000, ax=ax, color='red')
                elif side[back_edge] == -1:
                    curve.plot(num_pts=1000, ax=ax, color='blue')

