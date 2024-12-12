"""You are given two jugs with capacities x liters and y liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach target using the following operations:
Fill either jug completely with water.
Completely empty either jug.
Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty."""
from functools import cache

@cache
def reachable_states(i, j, x, y):
    states = []
    if i and j:
        states.extend([(i, 0), (0, j)]) # empty a jug
    if i < x:
        states.append((x, j)) # fill a jug
        if j: # move water from one jug to another
            transfer = min(j, x - i)
            states.append((i + transfer, j - transfer))   
    if j < y:
        states.append((i, y)) # fill a jug
        if i: # move water from one jug to another
            transfer = min(i, y - j)
            states.append((i - transfer, j + transfer))
    return tuple(states)


def can_measure_water(x, y, target):
    """Use BFS for graph where nodes equal possible water distributions (i, j)
    and edge between nodes (i, j) and (k, l) if (k, l) in (i, j)'s reachable states"""
    root = (0, 0)
    queue = [root]
    visited = {(i, j): False for i in range(x + 1) for j in range(y + 1)}
    while queue:
        i, j = queue.pop(0)
        if i == target or j == target:
            return True
        for l, k in reachable_states(i, j, x, y):
            if not visited[(l, k)]:
                visited[(l, k)] = True
                queue.append((l, k))
        visited[(i, j)] = True
    return False

print(can_measure_water(3, 5, 4))
