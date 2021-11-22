import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
from src.orientation.orientation import *
from src.testing.testing import *
from src.embedding.embedding import *


def main():
    graph = nx.MultiGraph()

    graph.add_nodes_from([1,2,3,4,5,6])
    graph.add_edges_from([(1,2,0), (2,3,0), (3,4,0), (4,5,0), (5,6,0), (6,1,0), (6,3,0), (5,2,0)])

    nx.draw(graph, with_labels=True)
    plt.show()

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
    final_adj_list = {}

    if number_of_edges > 3 * number_of_nodes - 6:
        print('NOT PLANAR')
        sys.exit()
    else:
        print('PLANAR')

    orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth)

    ref = dict.fromkeys(nesting_depth, (math.nan, math.nan, math.nan))
    side = dict.fromkeys(nesting_depth, 1)

    test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref, side)

    embed(graph, roots, nesting_depth, parent_edge, ref, side, left_ref, right_ref, final_adj_list)

    print('left_ref', left_ref)
    print('right_ref', right_ref)

if __name__ == "__main__":
    main()