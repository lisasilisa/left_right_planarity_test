def check_for_nan_tuple(t):
    return t[0] != t[0] and t[1] != t[1] and t[2] != t[2]


def check_for_nan_side(t):
    nan_side = True
    for i in range(len(t)):
        nan_side = nan_side and check_for_nan_tuple(t[i])
    return nan_side


def conflicting(I, b, low_pt):
    return not check_for_nan_side(I) and low_pt[I[1]] > low_pt[b]


