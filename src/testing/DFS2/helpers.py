def check_for_nan_tuple(t):
    return t[0] != t[0] and t[1] != t[1]


def check_for_nan_stack_side(t):
    nan_side = True
    for i in range(len(t)):
        nan_side = nan_side and check_for_nan_tuple(t[i])
    return nan_side


def check_for_nan_stack(st):
    return check_for_nan_stack_side(st[0]) and check_for_nan_stack_side(st[1])


def conflicting(I, b, low_pt):
    return not check_for_nan_stack_side(I) and low_pt[I[1]] > low_pt[b]


def lowest(P, low_pt):
    if check_for_nan_stack_side(P[0]):
        return low_pt[P[1][0]]
    if check_for_nan_stack_side(P[1]):
        return low_pt[P[0][0]]
    return min(low_pt[P[0][0]], low_pt[P[1][0]])
