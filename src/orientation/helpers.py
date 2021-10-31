def generate_whole_adj_list(graph):
    adj_dict = {}
    for node, neighbors in graph.adjacency():
        n = {}
        for neighbor in neighbors:
            o = {}
            for i in neighbors[neighbor]:
                o[i] = 'u'
            n[neighbor] = o
        adj_dict[node] = n
    return adj_dict
