"""A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""
from collections import defaultdict
from itertools import combinations

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def one_letter_dif(a, b):
    return sum(1 for c, d in zip(a, b) if c != d) == 1

def convert_to_graph(begin, word_list):
    graph = defaultdict(list)
    for a, b in combinations([begin] + word_list, 2):
        if one_letter_dif(a, b):
            graph[a].append(b)
            graph[b].append(a)
    return graph

def bfs(root, graph):
    visited = {word: False for word in graph.keys()}
    distances = {word: float('inf') for word in graph.keys()}
    distances[root] = 0
    queue = [root]
    while queue:
        word = queue.pop(0)
        for neighbor in graph[word]:
            if not visited[neighbor]:
                distances[neighbor] = distances[word] + 1
                visited[neighbor] = True
                queue.append(neighbor)
        visited[word] = True
    return distances

def ladder_length(begin, end, word_list):
    """Return length of shorted transformation sequence from begin to end using words in word_list"""
    if begin in word_list or end not in word_list:
        return 0
    graph = convert_to_graph(begin, word_list)
    distances = bfs(begin, graph)
    return distances[end] + 1 if distances[end] != float('inf') else 0

print(ladder_length(beginWord, endWord, wordList))



    