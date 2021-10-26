import networkx as nx
import matplotlib.pyplot as plt
import sys
import math
from src.orientation.orientation import *


def main():
    graph = nx.Graph()
    graph.add_nodes_from([1, 2, 3, 4, 5])
    graph.add_edges_from([(1, 2), (2, 3), (2, 5), (3, 4), (3, 5)])
    nx.draw(graph, with_labels=True)
    plt.show()

    # TODO: git anlegen

    number_of_nodes = graph.number_of_nodes()
    number_of_edges = graph.number_of_edges()
    height = dict.fromkeys(graph.nodes, math.inf)
    roots = []
    parent_edge = dict.fromkeys(graph.nodes, (math.nan, math.nan))
    low_pt = {}
    low_pt_2 = {}
    nesting_depth = {}
    if number_of_edges > 3 * number_of_nodes - 6:
        print('NOT PLANAR')
        sys.exit()
    else:
        print('PLANAR')

    orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth)
    print('nesting depth:', nesting_depth)


if __name__ == "__main__":
    main()


    """
    list_of_edges = list(graph.edges)
    list_of_nodes = list(graph.nodes)
    a = nx.dfs_edges(graph, list_of_nodes[0])
    """