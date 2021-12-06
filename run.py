import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
import tkinter as tk
from PIL import Image, ImageTk
from src.orientation.orientation import *
from src.testing.testing import *
from src.embedding.embedding import *


def run(graph):

#def main():
    #graph = nx.MultiGraph()

    #graph.add_nodes_from([1,2,3,4,5,6])
    #graph.add_edges_from([(1,2,0), (2,3,0), (3,4,0), (4,5,0), (5,6,0), (6,1,0), (6,3,0), (5,2,0)])

    #graph.add_nodes_from([1,2,3,4,5])
    #graph.add_edges_from([(1,2,0), (2,3,0), (3,4,0), (4,5,0), (5,1,0), (5,2,0), (4,1,0), (4,2,0), (3,1,0)])

    #graph.add_nodes_from([1,2,3,4,5,6])
    #graph.add_edges_from([(1,2,0), (1,4,0), (1,6,0), (2,3,0), (2,5,0), (3,4,0), (3,6,0), (4,5,0), (5,6,0)])

    #nx.draw(graph, with_labels=True)
    #plt.show()
    print('graph', graph)
    print('graph edges:', graph.edges)
    number_of_nodes = graph.number_of_nodes()
    number_of_edges = graph.number_of_edges()
    height = dict.fromkeys(graph.nodes, math.inf)
    roots = []
    parent_edge = dict.fromkeys(graph.nodes, (math.nan, math.nan, math.nan))
    low_pt = {}
    low_pt_2 = {}
    nesting_depth = {}
    left_ref = {}
    right_ref = {}
    planar = True

    if number_of_nodes >= 3 and number_of_edges > 3 * number_of_nodes - 6:
        planar = False
    else:
        orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth)

        ref = dict.fromkeys(nesting_depth, (math.nan, math.nan, math.nan))
        side = dict.fromkeys(nesting_depth, 1)

        planar = test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref, side) # planar = # planar,
        print('ref', ref)

        final_adj_list = embed(graph, roots, nesting_depth, parent_edge, ref, side, left_ref, right_ref)
        print('left_ref', left_ref)
        print('right_ref', right_ref)
        print('final_adj_list', final_adj_list)
    return planar

#if __name__ == "__main__":
#    main()
