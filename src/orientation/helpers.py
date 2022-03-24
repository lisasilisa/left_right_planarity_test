def generate_whole_adj_list(graph):
    adj_dict = {}
    for node, neighbors in graph.adjacency():
        n = {}
        for neigh in neighbors:
            n[neigh] = 'u'
        adj_dict[node] = n
    return adj_dict

