
def generate_whole_adj_list(graph):
    adj_dict = {}
    for node, neighbors in graph.adjacency():
        oriented = {}
        for neighbor in neighbors.keys():
            oriented[neighbor] = 'u'
        adj_dict[node] = oriented
    return adj_dict

