"""We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X."""

from bisect import bisect_left
from functools import cache
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
startTime_2 = [1,2,3,3]
endTime_2 = [3,4,5,6]
profit_2 = [50,10,40,70]
startTime3 = [1,1,1]
endTime3 = [2,3,4]
profit3 = [5,6,4]
startTime4 =[5,2,1] 
endTime4 =[7,4,4] 
profit4 =[40,10,30]


def overlapping(start_times, end_time):
    """Return index of earliest overlapping intervals in start_times with binary search"""
    return bisect_left(start_times, end_time)
    

def job_scheduling(start_times, end_times, profit):
    sorted_job_intervals = sorted(zip(start_times, end_times)) # sort job_intervals in case not sorted
    new_start_times, new_end_times = zip(*sorted_job_intervals) # sorted start and end times
    profits_dict = {(start_times[i], end_times[i]): profit[i] for i in range(len(profit))}

    @cache
    def recursive_job_scheduling(start_times, end_times):
        if not start_times:
            return 0
        index = overlapping(start_times, end_times[0]) # find overlapping intervals
        end_points = [index] + [overlapping(start_times, end_times[i]) for i in range(1, index)] # find overlaps for overlapping intervals
        profits = [profits_dict[(start_times[i], end_times[i])] for i in (range(index))] # get profits for overlapping intervals
        profits = [profit + recursive_job_scheduling(start_times[i:], end_times[i:]) for profit, i in zip(profits, end_points)] # choose max profit for all overlapping intervals
        return max(profits)
    
    return recursive_job_scheduling(tuple(new_start_times), tuple(new_end_times))

print(job_scheduling(startTime4, endTime4, profit4))






    

        
