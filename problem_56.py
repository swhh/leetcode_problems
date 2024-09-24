"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input."""
intervals_one = [[1,3],[2,6],[5,10],[15,18]]
intervals_two = [[1, 2], [3,4],[4,5]]
intervals_three = [[1, 3], [2, 6], [4, 9], [10, 12]]
intervals_four = [[1, 2]]


def overlap(a, b):
    return a[1] >= b[0]

def merge_intervals(a, b):
    return [a[0], b[1]]

def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals_sorted = sorted(intervals, key=lambda x: (x[0], x[1]))
    final_intervals = []
    current_interval = intervals_sorted[0]

    for i in range(len(intervals)):
        if overlap(current_interval, intervals_sorted[i]):
            current_interval = merge_intervals(current_interval, intervals_sorted[i])
        else:
            final_intervals.append(current_interval)
            current_interval = intervals_sorted[i]
    final_intervals.append(current_interval)
    
    return final_intervals


print(merge(intervals_one))




