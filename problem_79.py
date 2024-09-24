from collections import defaultdict
from itertools import chain

"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters."""

test_board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word1 = "ABCCED"

test_board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word2 = "SEE"

test_board3 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
test_word3 = "ABCB"


def dfs(graph, word, board):
    def dfs_visit(v, visited, word=word):
        if not word:
            return True
        if board[v] != word[0]:
            return False
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs_visit(neighbor, visited, word=word[1:]):
                    return True
        return False

    for node in graph.keys():
        visited = defaultdict(lambda: False)
        if dfs_visit(node, visited, word):
            return True

    return False


def convert_to_graph(board):
    graph = defaultdict(list)
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            node = len(row) * i + j
            if j:
                graph[node].append(node - 1)
                graph[node - 1].append(node)
            if i:
                graph[node].append(node - len(row))
                graph[node - len(row)].append(node)
    return graph


def exist(board, word):
    graph = convert_to_graph(board)
    board = list(chain.from_iterable(board))
    return dfs(graph, word, board)


def test():
    test_cases = zip((test_board1, test_board2, test_board3), (test_word1, test_word2, test_word3), (True, True, False))
    for board, word, case in test_cases:
        assert exist(board, word) is case


if __name__ == '__main__':
    test()
    
