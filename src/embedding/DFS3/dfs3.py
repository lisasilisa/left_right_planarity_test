import copy


def dfs3(v, sorted_adj_list, final_adj_list, parent_edge, left_ref, right_ref, side):
    for e_i in sorted_adj_list[v]:
        w = e_i[1]
        if e_i == parent_edge[w]:
            final_adj_list[w].insert(0, e_i)
            left_ref[v] = e_i
            right_ref[v] = e_i
            dfs3(w, sorted_adj_list, final_adj_list,
                 parent_edge, left_ref, right_ref, side)
        else:
            tmp_list = copy.deepcopy(final_adj_list[w])
            if side[e_i] == 1:
                for idx, s in enumerate(tmp_list):
                    if s == right_ref[w]:
                        final_adj_list[w].insert(idx+1, e_i)
            else:
                for idx, s in enumerate(tmp_list):
                    if s == left_ref[w]:
                        final_adj_list[w].insert(idx, e_i)
                left_ref[w] = e_i

