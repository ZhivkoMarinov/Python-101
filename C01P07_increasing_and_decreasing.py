from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    incr = 0
    decr = 0

    for i in range(len(ns) - 1):
        if ns[i] < ns[i+1]:
            incr += 1
        elif ns[i] > ns[i+1]:
            decr += 1

    if incr == len(ns) - 1:
        return Monotonicity.INCREASING
    elif decr == len(ns) - 1:
        return Monotonicity.DECREASING

    return Monotonicity.NONE
