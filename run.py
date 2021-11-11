import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
from src.orientation.orientation import *
from src.testing.testing import *


def main():
    graph = nx.MultiGraph()
    # graph.add_nodes_from([1, 2, 3, 4, 5])
    # graph.add_edges_from([(1, 2), (2, 3), (2, 5), (3, 4), (3, 5)])
    graph = nx.MultiGraph()
    graph.add_nodes_from([2,3,4,5,1])
    graph.add_edges_from([(2, 5, 0), (2, 1, 0), (3, 4, 0), (4, 5, 0), (2, 3, 0), (4, 1, 0), (1, 3, 0), (5, 1, 0), (2, 4, 0)])
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
    ref = {}
    if number_of_edges > 3 * number_of_nodes - 6:
        print('NOT PLANAR')
        sys.exit()
    else:
        print('PLANAR')

    orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth)
    print('nesting depth:', nesting_depth)
    print(parent_edge)

    test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref)


if __name__ == "__main__":
    main()