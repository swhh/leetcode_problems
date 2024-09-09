"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it."""

lists = [[1,4,5],[1,3,4],[2,6]]
edge_1 = [[]]
edge_2 = []

def merge_k_lists(lists):
    merged = []
    k = len(lists)
    remaining = set(range(k))
    places = {
        i: 0 for i in range(k)
    }
    sizes = {
        i: len(lists[i]) for i in range(k)
    }
    while any(places[i] < sizes[i] for i in range(k)):
        i = min(remaining, key=lambda x: lists[x][places[x]])
        merged.append(lists[i][places[i]])
        places[i] += 1
        if places[i] == sizes[i]:
            remaining.remove(i)
    return merged



print(merge_k_lists(lists))