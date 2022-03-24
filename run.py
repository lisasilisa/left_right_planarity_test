from src.orientation.orientation import *
from src.testing.testing import *
from src.embedding.embedding import *
from src.visualization.visualization import *


def run(graph):

    print(graph)
    print(graph.edges)
    print(graph.nodes)
    number_of_nodes = graph.number_of_nodes()
    number_of_edges = graph.number_of_edges()
    height = dict.fromkeys(graph.nodes, math.inf)
    roots = []
    parent_edge = dict.fromkeys(graph.nodes, (math.nan, math.nan))  # , math.nan
    low_pt = {}
    low_pt_2 = {}
    nesting_depth = {}
    planar = True

    if number_of_nodes >= 3 and number_of_edges > 3 * number_of_nodes - 6:
        planar = False
    else:
        orientate(graph, height, roots, parent_edge, low_pt, low_pt_2, nesting_depth)
        print('parent_edge', parent_edge)
        print('height', height)
        print('lowpoint', low_pt)
        print('lowpoint2', low_pt_2)
        print('nesting depth', nesting_depth)
        ref = dict.fromkeys(nesting_depth, (math.nan, math.nan))  # , math.nan
        side = dict.fromkeys(nesting_depth, 1)

        planar = test(graph, roots, nesting_depth, parent_edge, low_pt, low_pt_2, height, ref, side)
        print("side", side)
        print("ref", ref)

    if planar:
        # planar graph drawing
        final_adj_list = embed(graph, roots, nesting_depth, parent_edge, ref, side)
        print('final_adj_list', final_adj_list)
        return planar, [final_adj_list, parent_edge, height, side]

    return planar, []

# if __name__ == "__main__":
#    main()
