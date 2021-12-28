import math
from src.testing.DFS2.helpers import *


def trim_back_edges(u, stack, height, low_pt, ref, side):
    while not stack.is_empty() and lowest(stack.top(), low_pt) == height[u]:
        P = stack.pop()
        if not check_for_nan_tuple(P[0][0]):
            side[P[0][0]] = -1

    if not stack.is_empty():
        P = stack.pop()

        # trim left interval
        while not check_for_nan_tuple(P[0][1]) and P[0][1][1] == u:
            P[0][1] = ref[P[0][1]]

        if check_for_nan_tuple(P[0][1]) and not check_for_nan_tuple(P[0][0]):
            ref[P[0][0]] = P[1][0]
            side[P[0][0]] = -1
            P[0][0] = (math.nan, math.nan)  # math.nan

        # trim right interval
        while not check_for_nan_tuple(P[1][1]) and P[1][1][1] == u:
            P[1][1] = ref[P[1][1]]

        if check_for_nan_tuple(P[1][1]) and not check_for_nan_tuple(P[1][0]):
            ref[P[1][0]] = P[0][0]  # P[0][0]
            side[P[1][0]] = -1
            P[1][0] = (math.nan, math.nan)  # math.nan muss raus

        stack.push(P)
