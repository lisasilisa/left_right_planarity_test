import math
import sys
from src.testing.DFS2.helpers import *


def add_constraints(e_i, e, stack, stack_bottom, low_pt, low_pt_edge, ref): # planar,
    P = [[(math.nan, math.nan, math.nan), (math.nan, math.nan, math.nan)], [(math.nan, math.nan, math.nan), (math.nan,
                                                                                                         math.nan,
                                                                                                             math.nan)]]
    while True:
        Q = stack.pop()
        if not check_for_nan_stack_side(Q[0]):
            Q[0], Q[1] = Q[1], Q[0]
        if not check_for_nan_stack_side(Q[0]):
            #planar = False
            #return planar
            return False
            #print('NOT PLANAR')
            #sys.exit()
        else:
            if low_pt[Q[1][0]] > low_pt[e]:
                if check_for_nan_stack_side(P[1]):
                    P[1][1] = Q[1][1]
                else:
                    ref[P[1][0]] = Q[1][1]
                P[1][0] = Q[1][0]
            else:
                # print('make consistent')
                ref[Q[1][0]] = low_pt_edge[e]
                # print(Q[1][0])

        if stack.top() == stack_bottom[e_i]:
            break

    while conflicting(stack.top()[0], e_i, low_pt) or conflicting(stack.top()[1], e_i, low_pt):
        Q = stack.pop()
        if conflicting(Q[1], e_i, low_pt):
            Q[0], Q[1] = Q[1], Q[0]
        if conflicting(Q[1], e_i, low_pt):
            return False
            #return planar
            #print('NOT PLANAR')
            #sys.exit()
        else:
            ref[P[1][0]] = Q[1][1]
            if not check_for_nan_tuple(Q[1][0]):
                P[1][0] = Q[1][0]
        if check_for_nan_stack_side(P[0]):
            P[0][1] = Q[0][1]
        else:
            ref[P[0][0]] = Q[0][1]
        P[0][0] = Q[0][0]

    if not check_for_nan_stack(P):
        stack.push(P)

    return True

