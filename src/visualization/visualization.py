import matplotlib
import networkx as nx
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#from matplotlib.figure import Figure

from src.visualization.DFSTreeEdges.get_dfs_tree_edges import *
from src.visualization.DFSTreeEdges.set_angle_and_wedge import *
from src.visualization.DFSTreeEdges.set_coordinates import *
from src.visualization.BezierCurves.draw_bezier_curves import *


def visualize(final_adj_list, parent_edge, height, side):
    graph = nx.DiGraph()
    fig, ax = plt.subplots()

    sorted_tree_edges = get_dfs_tree_edges(final_adj_list, parent_edge)
    wedge = {0: 180}
    angle = {0: 0}
    set_angle_and_wedge(sorted_tree_edges, 0, wedge, angle)

    coord = {0: (0, 0)}
    graph.add_node(0, pos=coord[0])
    set_coordinates(graph, sorted_tree_edges, 0, coord, wedge, angle)
    print('coord', coord)
    draw_bezier_curves(graph, ax, final_adj_list, sorted_tree_edges, parent_edge, height, side)
    plt.show()
