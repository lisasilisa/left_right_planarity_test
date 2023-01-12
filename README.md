# 1. Project Summary
This project implements the left-right planarity test based on the pseudocode of the article "The Left-Right Planarity Test" by Ulrik Brandes (2011).
Briefly, it tests whether a simple graph is planar, where a simple graph is an unweighted, undirected graph that has no loops and no multiple edges.

# 2. Requirements
The project was implemented with the following library versions, which I recommend to install along with Python 3.9
* Tkinter 8.6.11
* numpy 1.21.2
* matplotlib 3.4.3
* pillow 8.4.0
* networkx 2.6.3

# 3. Modular Structure
The project was implemented by setting up the code in a modular way.

## 3.1 orientation
The orientation package contains the DFS1 package and the corresponding dfs1.py, the first 'depth first search'. The purpose of this first phase is to orient the graph, to determine the lowpoints
and the nesting order of the edges.

## 3.2 testing
The testing package contains the DFS2 package and the corresponding dfs2.py, the second 'depth first search'. The goal of the second phase 
is to determine if the graph has a consistent LR partition. Consistent means that all back edges of a tree edge ending at its low point 
belong to the same orientation. The challenge is that so-called pairwise constraints have to be dealt with: either two back edges are 
constrained to be on the same (same constraint) or on different sides (different constraint). Therefor the package keeps track of the 
constrains through the add_constraints.py.

## 3.3 embedding
The embedding package contains the DFS3 package and the corresponding dfs3.py, the third 'depth first search'.
After the test phase has been completed, one has either found a consistent LR partition or the graph has been found to be non-planar. 
If the graph is planar, the goal of the third phase is to find a planar embedding for the graph.

## 3.4 visualization
The visualization package contains of the coordinating visualization.py file. It initiates the drawing of the planar graph, which is broken down into two steps:
the depth-first search tree and the left- or right-oriented back edges. For the former is the package DSFTreeEdges responsible, for the latter the package
BezierCurves

# 4. Usage 
The project can be started by running the run.py. This calls the user interface, which is implemented in the file app.py. Here the user can either import
the adjacency matrix as a csv-file or enter the matrix itself by hand.

# 5. Further description
For further description and more details about the implementation please look at my report: 'Abschlussbericht Studienprojekt".
