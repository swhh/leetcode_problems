import heapq

"""The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
        """
test_input1 = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
test_input2 = [[], [1], [2], [], [3], []]


class MedianFinder(object):
    """Track median in integer data stream by maintaining two heaps that contain half the integers each"""
    def __init__(self):
        self.heap_high = []
        self.heap_low = []

    def add_num(self, num):
        """"Add number to one of heap_high or heap_low in a way that keeps the two equal sized or high one bigger"""
        if not self.heap_high:
            self.heap_high.append(num)
        else:
            if self.heap_high[0] <= num:
                heapq.heappush(self.heap_high, num)
            else:
                heapq.heappush(self.heap_low, -num)
            diff = len(self.heap_high) - len(self.heap_low)
            if diff > 1:
                elem = heapq.heappop(self.heap_high)
                heapq.heappush(self.heap_low, -elem)
            elif diff <= -1:
                elem = heapq.heappop(self.heap_low)
                heapq.heappush(self.heap_high, -elem)

    def find_median(self):
        """Return median"""
        if len(self.heap_high) == len(self.heap_low):
            return (-self.heap_low[0] + self.heap_high[0]) / 2
        return self.heap_high[0]


def test():
    median_tracker = MedianFinder()
    for i, j in zip(test_input1[1:], test_input2[1:]):
        if i == 'addNum':
            for k in j:
                median_tracker.add_num(k)
        else:
            print(median_tracker.find_median())


if __name__ == '__main__':
    test()
