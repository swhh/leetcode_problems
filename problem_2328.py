from collections import defaultdict
from functools import cache
from itertools import chain
"""You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells."""

"""Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3."""

test_grid1 = [[1, 1], [3, 4]]
test_grid2 = [[1], [2]]
test_grid3 = [
    [12469, 18741, 68716, 30594, 65029, 44019, 92944, 84784, 92781, 5655, 43120, 81333, 54113, 88220, 23446, 6129, 2904,
     48677, 20506, 79604, 82841, 3938, 46511, 60870, 10825, 31759, 78612, 19776, 43160, 86915, 74498, 38366, 28228,
     23687, 40729, 42613, 61154, 22726, 51028, 45603, 53586, 44657, 97573, 61067, 27187, 4619, 6135, 24668, 69634,
     24564, 30255, 51939, 67573, 87012, 4106, 76312, 28737, 7704, 35798]]


def grid_to_graph(grid):
    graph = defaultdict(dict)
    for i, row in enumerate(grid):
        for j, num in enumerate(row):
            node = len(row) * i + j
            if j:
                behind = row[j - 1]
                if behind > num:
                    graph[node][node - 1] = 1
                if behind < num:
                    graph[node - 1][node] = 1
            if i:
                above = grid[i - 1][j]
                if above > num:
                    graph[node][node - len(row)] = 1
                if above < num:
                    graph[node - len(row)][node] = 1
    return graph


def graph_to_immutable_map(graph, grid):
    return tuple(tuple(graph[i].keys()) for i in range(sum(1 for _ in chain.from_iterable(grid))))


@cache
def dfs(immutable_map, source):
    neighbors = immutable_map[source]
    if not neighbors:
        return 1
    return sum(dfs(immutable_map, neighbor) for neighbor in neighbors) + 1


def count_paths(grid):
    graph = grid_to_graph(grid)
    immutable_map = graph_to_immutable_map(graph, grid)
    paths = 0
    for s in range(len(grid) * (len(grid[0]))):
        paths += dfs(immutable_map, s)
    return paths


